#!/usr/bin/env python3
"""Refresh the repository facts in catalog.json from the GitHub API.

Star counts, licences and archive status go stale the moment they are written,
and a catalog full of six-month-old numbers is the failure mode every abandoned
awesome list shares. This script re-reads them.

It touches ONLY facts a machine can check:

  stars          <- stargazers_count
  repo_license   <- license.spdx_id, or "unknown" when none is declared
  archived flag  <- the repository's own archived field
  no-license flag<- whether a licence is declared

Summaries, notes, patterns and question_types are human judgements and are
never touched. `archived` follows GitHub's own flag rather than a
no-push-in-N-days heuristic, because the catalog's whole stance is to state
checkable facts rather than guesses — the cost is missing projects that are
quietly unmaintained without being formally archived.

Usage:
  python3 scripts/refresh_metadata.py            # report drift, change nothing
  python3 scripts/refresh_metadata.py --write    # apply it
  python3 scripts/refresh_metadata.py --json     # machine-readable report
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from _github import SELF, api_get, repo_of  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"
WORKERS = 6

# SELF is imported from _github: rows pointing at this repository are its own
# runnable examples, and stamping them with this repo's own star count would be
# both meaningless and circular.


def fetch(entry: dict) -> dict | None:
    """Current facts for one row, or None when the repo did not resolve."""
    repo = repo_of(entry)
    if not repo:
        return None
    data = api_get(f"/repos/{repo}")
    if not isinstance(data, dict) or "stargazers_count" not in data:
        return {"slug": entry["slug"], "repo": repo, "gone": True}

    # GitHub reports NOASSERTION for a LICENSE file it cannot identify — custom
    # or modified terms — which is different from having none at all, so it is
    # kept as-is. Only a repository with no licence file becomes "unknown".
    spdx = ((data.get("license") or {}).get("spdx_id") or "").strip() or "unknown"
    return {
        "slug": entry["slug"],
        "repo": repo,
        "gone": False,
        "stars": data["stargazers_count"],
        "repo_license": spdx,
        "archived": bool(data.get("archived")),
    }


def diff_for(entry: dict, fresh: dict) -> list[tuple[str, object, object]]:
    """Field-level changes this row would take. Empty means nothing moved."""
    changes: list[tuple[str, object, object]] = []

    if entry.get("stars") is not None and entry["stars"] != fresh["stars"]:
        changes.append(("stars", entry["stars"], fresh["stars"]))
    elif entry.get("stars") is None:
        changes.append(("stars", None, fresh["stars"]))

    if entry.get("repo_license") != fresh["repo_license"]:
        changes.append(
            ("repo_license", entry.get("repo_license"), fresh["repo_license"])
        )

    flags = set(entry.get("flags", []))
    # Both flags are two-way: a project that gets archived gains the flag, and
    # one that is un-archived or gains a licence loses it. A flag that only
    # ever accumulates would slowly stop meaning anything.
    if fresh["archived"] and "archived" not in flags:
        changes.append(("flags", "archived", "add"))
    if not fresh["archived"] and "archived" in flags:
        changes.append(("flags", "archived", "remove"))

    # `no-license` means no LICENSE file at all, which is exactly repo_license
    # "unknown" — the same definition lint.py enforces. This used to count
    # NOASSERTION as unlicensed too, so a row that correctly moved to NOASSERTION
    # kept telling readers there was no licence: 28 rows, vercel/ai among them.
    unlicensed = fresh["repo_license"] == "unknown"
    if unlicensed and "no-license" not in flags:
        changes.append(("flags", "no-license", "add"))
    if not unlicensed and "no-license" in flags:
        changes.append(("flags", "no-license", "remove"))

    return changes


def apply(entry: dict, fresh: dict, changes: list[tuple[str, object, object]]) -> None:
    for field, a, b in changes:
        if field == "stars":
            entry["stars"] = b
        elif field == "repo_license":
            entry["repo_license"] = b
        elif field == "flags":
            flags = entry.setdefault("flags", [])
            if b == "add" and a not in flags:
                flags.append(a)
            elif b == "remove" and a in flags:
                flags.remove(a)
            if not flags:
                entry.pop("flags", None)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="apply the changes")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument(
        "--only",
        default="",
        help="only refresh rows whose slug contains this substring",
    )
    parser.add_argument(
        "--digest",
        default="",
        help="also write a Markdown summary to this path, for an issue body",
    )
    args = parser.parse_args()

    catalog = json.loads(CATALOG.read_text())
    rows = [
        e
        for e in catalog
        if repo_of(e) and repo_of(e) != SELF and args.only in e["slug"]
    ]
    print(f"refreshing {len(rows)} row(s) with a GitHub repository\n", file=sys.stderr)

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(fetch, rows))

    report: list[dict] = []
    gone: list[str] = []
    for entry, fresh in zip(rows, results):
        if fresh is None:
            continue
        if fresh["gone"]:
            gone.append(f"{entry['slug']} ({fresh['repo']})")
            continue
        changes = diff_for(entry, fresh)
        if not changes:
            continue
        report.append(
            {
                "slug": entry["slug"],
                "repo": fresh["repo"],
                "changes": [{"field": f, "from": a, "to": b} for f, a, b in changes],
            }
        )
        if args.write:
            apply(entry, fresh, changes)

    if args.write and report:
        CATALOG.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n")

    if args.digest:
        pathlib.Path(args.digest).write_text(digest(report, gone, len(rows)))

    if args.json:
        print(
            json.dumps(
                {"changed": report, "unreachable": gone}, indent=2, ensure_ascii=False
            )
        )
        return 0

    for item in report:
        print(f"  {item['slug']}")
        for change in item["changes"]:
            if change["field"] == "flags":
                print(f"      flag {change['to']}: {change['from']}")
            else:
                print(f"      {change['field']}: {change['from']} -> {change['to']}")
    if gone:
        print(
            f"\n  {len(gone)} repository(ies) did not resolve — deleted, renamed or private:"
        )
        for item in gone:
            print(f"      {item}")
        print(
            "  These need a person: a rename is fixable, a deletion means retiring the row."
        )

    verb = "applied" if args.write else "would change"
    print(f"\n{verb} {len(report)} row(s) of {len(rows)}")
    if report and not args.write:
        print("Run with --write to apply.")
    return 0


def digest(report: list[dict], gone: list[str], checked: int) -> str:
    """What a person needs from a weekly refresh, in a form that fits an issue.

    Stars move on most rows every week; listing each one produced a report far
    past GitHub's 65,536-character issue body limit, so the notice for a
    refresh would have failed to post. Star-only changes are counted. Anything
    else — a licence changing, a project archived, a repository gone — is the
    reason a person reads this at all, and is listed in full.
    """
    stars_only = [r for r in report if {c["field"] for c in r["changes"]} == {"stars"}]
    notable = [r for r in report if r not in stars_only]
    lines = [
        f"Re-read {checked} repositories: {len(report)} rows changed, "
        f"{len(stars_only)} of them stars only.",
        "",
    ]
    if notable:
        lines += ["**Worth a look before merging:**", ""]
        for item in notable:
            parts = [
                f"{c['field']} {c['from']} → {c['to']}"
                if c["field"] != "flags"
                else f"flag `{c['from']}` {c['to']}"
                for c in item["changes"]
                if c["field"] != "stars"
            ]
            lines.append(f"- `{item['slug']}` ({item['repo']}): " + "; ".join(parts))
        lines.append("")
    if gone:
        lines += [
            f"**{len(gone)} repositories did not resolve** — deleted, renamed or "
            "private. A rename is fixable; a deletion means retiring the row with a "
            "notes line saying why.",
            "",
        ]
        lines += [f"- {item}" for item in gone]
        lines.append("")
    if not notable and not gone:
        lines += ["Nothing but star counts moved.", ""]
    return "\n".join(lines)


if __name__ == "__main__":
    sys.exit(main())
