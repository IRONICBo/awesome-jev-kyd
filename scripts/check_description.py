#!/usr/bin/env python3
"""Check that the published repository description still matches the catalogue.

The description is the single most-read sentence this project publishes — it is
what appears in GitHub search, in the social card and in every link preview —
and it was the one claim in the whole repository that nothing could check. It
lives in GitHub's database, not in git, so it sat at "148 verified examples"
while the catalogue grew to 805 and no build ever went red.

That is precisely the failure mode the catalogue exists to argue against, so it
gets the same treatment as everything else: a number that is asserted in public
has to be re-derivable from the data.

Read-only. A missing token or an unreachable API is reported as `skipped`, not
as a failure: a network hiccup must not turn the build red, because a build
that is red for reasons nobody can act on is a build everybody stops reading.

Usage:
  python3 scripts/check_description.py
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from _github import SELF, api_get, token  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"


def main() -> int:
    actual = len(json.loads(CATALOG.read_text()))

    if not token():
        print(f"skipped: no GITHUB_TOKEN. Catalogue holds {actual} entries.")
        return 0

    data = api_get(f"/repos/{SELF}")
    if not isinstance(data, dict):
        print(f"skipped: could not read {SELF} description.")
        return 0

    description = (data.get("description") or "").strip()
    if not description:
        print("error: the repository has no description at all.")
        return 1

    # The first run of digits, which is how the description opens: "805 verified
    # examples of Jev …". Deliberately not a search for any number anywhere —
    # "CC0-1.0" or a year later in the sentence must not be mistaken for a count.
    match = re.match(r"\s*([0-9][0-9,]*)\b", description)
    if not match:
        print("error: the description does not open with an entry count.")
        print(f"  description: {description}")
        print(f"  catalogue:   {actual} entries")
        return 1

    claimed = int(match.group(1).replace(",", ""))
    if claimed != actual:
        print("error: the published description is stale.")
        print(f"  it claims:  {claimed} entries")
        print(f"  catalogue:  {actual} entries")
        print()
        print("Fix it with:")
        print(f'  gh repo edit --description "{actual}{description[match.end() :]}"')
        return 1

    print(f"description matches the catalogue: {actual} entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
