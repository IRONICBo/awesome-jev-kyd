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

# Every file the site fetches at runtime. The Pages job copies each one in, so
# each one needs the same guard: a stale or missing copy publishes a site that
# disagrees with the repository it is built from. One list, so adding a fourth
# runtime file cannot forget its check — which is how compat.json once went
# unignored while catalog.json was.
RUNTIME_FILES = ("catalog.json", "compat.json", "patterns.json", "taxonomy.json")

# The site renders these fields unconditionally; a missing one is a blank cell.
REQUIRED = ("slug", "title", "summary", "summary_zh", "url", "kind", "patterns")


def main() -> int:
    for name in RUNTIME_FILES:
        copy = ROOT / "site" / name
        if not copy.exists():
            print(f"error: site/{name} is missing; the Pages job should copy it in", file=sys.stderr)
            return 1
        if json.loads((ROOT / name).read_text()) != json.loads(copy.read_text()):
            print(f"error: site/{name} differs from {name}", file=sys.stderr)
            return 1
        print(f"site/{name} matches {name}")

    for entry in json.loads((ROOT / "site" / "catalog.json").read_text()):
        missing = [field for field in REQUIRED if field not in entry]
        if missing:
            print(
                f"error: entry {entry.get('slug', '?')!r} is missing {missing} "
                "which the site needs to render",
                file=sys.stderr,
            )
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
