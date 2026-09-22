#!/usr/bin/env python3
"""Verify site/catalog.json matches the catalog at the repo root.

The Pages job copies catalog.json into site/ at build time. This guards against
publishing a site that reads a stale or truncated copy — the failure mode where
the README says 40 entries and the site quietly shows 12.

Run: python3 scripts/check_site_data.py
"""

from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ROOT / "catalog.json"
COPY = ROOT / "site" / "catalog.json"
COMPAT_SOURCE = ROOT / "compat.json"
COMPAT_COPY = ROOT / "site" / "compat.json"


def main() -> int:
    if not COPY.exists():
        print(
            "error: site/catalog.json is missing; the Pages job should copy it in",
            file=sys.stderr,
        )
        return 1

    source = json.loads(SOURCE.read_text())
    copy = json.loads(COPY.read_text())

    if source != copy:
        print(
            f"error: site/catalog.json differs from catalog.json "
            f"({len(copy)} vs {len(source)} entries)",
            file=sys.stderr,
        )
        return 1

    # The site renders these fields unconditionally; a missing one is a blank cell.
    required = ("slug", "title", "summary", "summary_zh", "url", "kind", "patterns")
    for entry in copy:
        missing = [field for field in required if field not in entry]
        if missing:
            print(
                f"error: entry {entry.get('slug', '?')!r} is missing {missing} "
                "which the site needs to render",
                file=sys.stderr,
            )
            return 1

    # The site's Compatibility view reads compat.json, so a stale copy there
    # would publish a matrix that disagrees with docs/compatibility.md — the
    # exact failure the generated-from-one-source design exists to prevent.
    if not COMPAT_COPY.exists():
        print("error: site/compat.json is missing; the Pages job should copy it in", file=sys.stderr)
        return 1
    if json.loads(COMPAT_SOURCE.read_text()) != json.loads(COMPAT_COPY.read_text()):
        print("error: site/compat.json differs from compat.json", file=sys.stderr)
        return 1

    print(f"site/catalog.json matches catalog.json ({len(copy)} entries)")
    print("site/compat.json matches compat.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
