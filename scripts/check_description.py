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

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _stats  # noqa: E402
from _github import SELF, api_get, graphql, token  # noqa: E402


def main() -> int:
    stats = _stats.compute()
    expected = _stats.pitch(stats)

    if not token():
        print(f"skipped: no GITHUB_TOKEN. Catalogue holds {stats['entries']} entries.")
        return 0

    data = api_get(f"/repos/{SELF}")
    if not isinstance(data, dict):
        print(f"skipped: could not read the {SELF} description.")
        return 0

    report_social_preview()

    description = (data.get("description") or "").strip()
    if description == expected:
        print(f"description matches the catalogue: {stats['entries']} entries")
        return 0

    # The whole sentence is compared, not just its number. The same sentence is
    # the site's og:description (build_docs.py), so an exact match here is what
    # guarantees a link to the repo and a link to the site say the same thing.
    print("error: the published repository description has drifted.")
    print(f"  published: {description or '(empty)'}")
    print(f"  expected:  {expected}")
    print()
    print("Fix it with:")
    print(f'  gh repo edit --description "{expected}"')
    return 1


def report_social_preview() -> None:
    """Informational only. The social preview is the one image nothing can
    regenerate — GitHub has no upload API — so it is the durable card, whose
    only figure is a floor that growth can only understate. All CI can do is
    say whether it has been uploaded."""
    owner, name = SELF.split("/")
    data = graphql(
        f'{{ repository(owner: "{owner}", name: "{name}") {{ usesCustomOpenGraphImage }} }}'
    )
    uploaded = ((data or {}).get("repository") or {}).get("usesCustomOpenGraphImage")
    if uploaded is None:
        print("social preview: could not be read")
    elif uploaded:
        print("social preview: custom card uploaded (durable; its count is a floor)")
    else:
        print(
            "notice: no custom social preview is uploaded, so GitHub shows its generated "
            "card, which quotes the description checked below. To use the designed card, "
            "download https://kydlikebtc.github.io/awesome-jev/img/card.png and upload it "
            "at Settings → General → Social preview."
        )


if __name__ == "__main__":
    sys.exit(main())
