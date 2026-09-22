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

from _github import api_get, repo_of  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"
WORKERS = 6

# Rows pointing at this repository are its own runnable examples. Stamping them
# with this repo's own star count would be both meaningless and circular.
SELF = "kydlikebtc/awesome-jev"


def fetch(entry: dict) -> dict | None:
    """Current facts for one row, or None when the repo did not resolve."""
    repo = repo_of(entry)
    if not repo:
        return None
    data = api_get(f"/repos/{repo}")
    if not isinstance(data, dict) or "stargazers_count" not in data:
        return {"slug": entry["slug"], "repo": repo, "gone": True}

    spdx = ((data.get("license") or {}).get("spdx_id") or "").strip()
    # GitHub reports NOASSERTION for a LICENSE file it cannot identify, which
    # is different from having none at all — keep the distinction.
    if not spdx or spdx == "NOASSERTION" and not data.get("license"):
        spdx = "unknown"
    return {
        "slug": entry["slug"],
        "repo": repo,
        "gone": False,
        "stars": data["stargazers_count"],
        "repo_license": spdx or "unknown",
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

    unlicensed = fresh["repo_license"] in ("unknown", "NOASSERTION")
    if unlicensed and "no-license" not in flags and fresh["repo_license"] == "unknown":
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
    args = parser.parse_args()

    catalog = json.loads(CATALOG.read_text())
    rows = [e for e in catalog if repo_of(e) and repo_of(e) != SELF]
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


if __name__ == "__main__":
    sys.exit(main())
