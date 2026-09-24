#!/usr/bin/env python3
"""Re-check that the primitive claims in catalog.json are still true upstream.

A row carrying `question_types` asserts which Jev primitives a project's code
actually calls. That assertion was true when a person read the call site, and
nothing stopped it going stale afterwards — an upstream refactor could remove
the integration entirely and this catalog would keep claiming it.

This script closes that gap. For every row with `evidence`, it fetches that file
from the repository's default branch and asserts every string in
`evidence.matched` still appears.

Deliberately not pinned to a commit. Pinning would verify a historical snapshot
forever and never notice a removal, which defeats the purpose. The cost is that
an upstream rename reports `path-gone`; that is a false positive a person
resolves, not a reason to check the wrong thing.

Exit code is 0 when every claim holds and 1 when any fails, so the scheduled
workflow can open an issue. It never edits the catalog.

Usage:
  python3 scripts/verify_claims.py              # check every row with evidence
  python3 scripts/verify_claims.py --only slug  # check one row
  python3 scripts/verify_claims.py --discover   # propose evidence for rows lacking it
  python3 scripts/verify_claims.py --json       # machine-readable report
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from concurrent.futures import ThreadPoolExecutor

from _github import api_get, default_branch, raw_get, repo_of

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"

# Signals that a file is a genuine Jev call site rather than a mention. The
# import and the endpoint are strong; a bare primitive name is not, because
# "choice" and "score" are ordinary English words.
STRONG = [
    "api.typesafe.ai",
    "typesafe_sdk",
    "@typesafe-ai/sdk",
    # The Vercel AI SDK provider: evaluate() calls, where noul is spelled boolean.
    "@ai-sdk/typesafe-ai",
    "typesafe-ai/jev",
    "typesafe/jev",
    "jev-latest",
    "jev-1.13",
    "/v1/systemone",
    "systemOne",
    "system_one",
    "langchain_typesafe",
    "TypeSafeClient",
    "AsyncTypeSafeClient",
]
# Only meaningful alongside a strong signal.
WEAK = ["noul", "Noul", "choice", "Choice", "score", "Score"]

CODE_EXT = (
    ".py", ".ts", ".tsx", ".js", ".mjs", ".jsx",
    ".go", ".rs", ".rb", ".java", ".kt", ".sql",
)

WORKERS = 6


def check(entry: dict) -> dict:
    slug = entry["slug"]
    evidence = entry["evidence"]
    repo = repo_of(entry)
    if not repo:
        return {
            "slug": slug,
            "status": "no-repo",
            "detail": "row has no GitHub repository",
        }

    branch = default_branch(repo)
    if not branch:
        return {
            "slug": slug,
            "status": "repo-gone",
            "detail": f"{repo} did not resolve",
        }

    body = raw_get(repo, branch, evidence["path"])
    if body is None:
        return {
            "slug": slug,
            "status": "path-gone",
            "detail": f"{repo}@{branch}:{evidence['path']} not found — renamed, moved or deleted",
        }

    missing = [needle for needle in evidence["matched"] if needle not in body]
    if missing:
        return {
            "slug": slug,
            "status": "claim-gone",
            "detail": f"{repo}@{branch}:{evidence['path']} no longer contains {missing}",
        }
    return {
        "slug": slug,
        "status": "ok",
        "detail": f"{repo}@{branch}:{evidence['path']}",
    }


def discover(entry: dict) -> dict:
    """Propose evidence for a row that has none, by reading the repository.

    Proposals are a starting point for a person, never written automatically —
    the whole point of this catalog is that a human read the call site.
    """
    slug = entry["slug"]
    repo = repo_of(entry)
    if not repo:
        return {"slug": slug, "status": "no-repo"}
    branch = default_branch(repo)
    if not branch:
        return {"slug": slug, "status": "repo-gone"}

    tree = api_get(f"/repos/{repo}/git/trees/{branch}?recursive=1")
    if not isinstance(tree, dict) or "tree" not in tree:
        return {"slug": slug, "status": "tree-unavailable"}

    # Prefer paths whose name already hints at the integration; it keeps the
    # candidate list short on repositories with thousands of files.
    paths = [
        node["path"]
        for node in tree["tree"]
        if node.get("type") == "blob" and node["path"].endswith(CODE_EXT)
    ]
    hinted = [p for p in paths if re.search(r"jev|typesafe", p, re.I)]
    candidates = (hinted or paths)[:40]

    best = None
    for path in candidates:
        body = raw_get(repo, branch, path)
        if not body:
            continue
        strong = [s for s in STRONG if s in body]
        if not strong:
            continue
        weak = [w for w in WEAK if re.search(rf"\b{re.escape(w)}\b", body)]
        score = len(strong) * 2 + len(weak)
        # A test file proves the integration exists, but the implementation is
        # the better witness: tests get deleted while features stay, and a
        # mocked string is weaker proof than a real call site.
        if re.search(r"(^|/)(tests?|spec|__tests__)/|\.(test|spec)\.[a-z]+$|_test\.[a-z]+$|test_[^/]*$", path, re.I):
            score -= 5
        # Config and fixture files mention endpoints without calling them.
        if re.search(r"(^|/)(fixtures?|config|constants|prefs)[./]", path, re.I):
            score -= 3
        if best is None or score > best["score"]:
            best = {
                "score": score,
                "path": path,
                "matched": (strong[:2] + weak[:2])[:4],
            }
    if not best:
        return {"slug": slug, "status": "no-call-site", "repo": repo}
    return {
        "slug": slug,
        "status": "proposed",
        "repo": repo,
        "path": best["path"],
        "matched": best["matched"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", default="", help="check a single slug")
    parser.add_argument(
        "--discover", action="store_true", help="propose evidence for rows lacking it"
    )
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args()

    catalog = json.loads(CATALOG.read_text())

    if args.discover:
        todo = [
            e
            for e in catalog
            if e.get("question_types")
            and "evidence" not in e
            and "evidence_none" not in e
            and repo_of(e)
            and (not args.only or e["slug"] == args.only)
        ]
        print(f"discovering evidence for {len(todo)} row(s)\n", file=sys.stderr)
        with ThreadPoolExecutor(max_workers=WORKERS) as pool:
            results = list(pool.map(discover, todo))
        if args.json:
            print(json.dumps(results, indent=2, ensure_ascii=False))
        else:
            for r in results:
                if r["status"] == "proposed":
                    print(
                        f"  {r['slug']}\n    path: {r['path']}\n    matched: {r['matched']}"
                    )
                else:
                    print(f"  {r['slug']}  [{r['status']}]")
        return 0

    todo = [
        e
        for e in catalog
        if "evidence" in e and (not args.only or e["slug"] == args.only)
    ]
    if not todo:
        print("no rows carry evidence yet")
        return 0

    print(f"re-checking {len(todo)} claim(s)\n", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(check, todo))

    failed = [r for r in results if r["status"] not in ("ok",)]
    if args.json:
        print(
            json.dumps(
                {"checked": len(results), "failed": failed},
                indent=2,
                ensure_ascii=False,
            )
        )
    else:
        for r in results:
            mark = "ok  " if r["status"] == "ok" else r["status"].upper()
            print(f"  {mark:<12} {r['slug']}  {r['detail']}")
        print(f"\n{len(results) - len(failed)}/{len(results)} claims still hold")
        if failed:
            print("\nFailures need a person: an upstream rename is a false positive,")
            print("a removed integration means the row's question_types is now wrong.")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
