#!/usr/bin/env python3
"""Re-read each platform's documentation and check compat.json still matches it.

compat.json is the source every other copy of a model string is linted against,
which makes it the one place a wrong string would propagate from. It records
thirteen surfaces the project does not control, each of which can rename a model
or retire an alias in an afternoon. verify_claims.py re-reads code call sites
weekly; this does the same for the platform matrix.

For every platform with a documentation URL, each model string compat.json
records for it must still appear on that page — or on `model_source`, when the
strings are documented somewhere other than the page readers are linked to. Three verdicts:

  ok            every recorded string is on the page
  string-gone   the page loaded but a recorded string is missing — a person
                needs to look; the platform may have renamed the model
  unreadable    the page refused a scripted request or renders client-side,
                so absence proves nothing. Reported, never failed on.

`as_of` in compat.json is deliberately not bumped by this script. It records
when a person last read the pages; a string match is weaker evidence than that,
and pretending otherwise would overstate what was checked.

Run: python3 scripts/verify_compat.py
"""

from __future__ import annotations

import html
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent.parent
TIMEOUT = 25
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
}


def expected_strings(platform: dict) -> list[str]:
    return [
        re.sub(r"\s*\(.*\)$", "", part.strip())
        for part in platform["model"].split("·")
        if part.strip() not in ("", "—")
    ]


def fetch(url: str) -> tuple[str | None, str]:
    request = urllib.request.Request(url, headers=HEADERS)
    for _attempt in range(2):  # one retry: a transient miss is not a verdict
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
                return response.read().decode("utf-8", "replace"), ""
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None, "HTTP 404 — the page itself is gone"
            reason = f"HTTP {exc.code}"
        except Exception as exc:  # noqa: BLE001 - one platform must not stop the sweep
            reason = exc.__class__.__name__
    return None, reason


def check(platform: dict) -> tuple[str, dict, list[str], str]:
    wanted = expected_strings(platform)
    # model_source, when set, is the page the strings are actually documented
    # on: the native API reference defers to a separate Models page, and a
    # GitHub tree URL renders client-side. Checking the linked page instead
    # would report a false `string-gone` every week.
    url = platform.get("model_source") or platform.get("url")
    if not url or not wanted:
        return "skipped", platform, [], "no URL or no model string recorded"
    page, reason = fetch(url)
    if page is None:
        verdict = "string-gone" if reason.startswith("HTTP 404") else "unreadable"
        return verdict, platform, wanted, reason
    text = html.unescape(page)
    missing = [s for s in wanted if s not in text]
    if not missing:
        return "ok", platform, [], ""
    # A page that mentions none of the recorded strings, and not even "jev",
    # is almost certainly rendered client-side. Absence there proves nothing.
    if "jev" not in text.lower():
        return (
            "unreadable",
            platform,
            missing,
            "page carries no server-rendered text about Jev",
        )
    return "string-gone", platform, missing, ""


def main() -> int:
    compat = json.loads((ROOT / "compat.json").read_text())
    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(check, compat["platforms"]))

    counts: dict[str, int] = {}
    for verdict, platform, missing, note in results:
        counts[verdict] = counts.get(verdict, 0) + 1
        detail = f"  missing {missing}" if missing else ""
        detail += f"  ({note})" if note else ""
        print(f"  {verdict:12} {platform['id']:24}{detail}")

    print()
    print(
        f"{counts.get('ok', 0)} ok, {counts.get('string-gone', 0)} string-gone, "
        f"{counts.get('unreadable', 0)} unreadable — compat.json as_of {compat['as_of']}"
    )
    if counts.get("string-gone"):
        print(
            "\nA recorded model string is no longer on its platform's page. Open the "
            "page, update compat.json, and run build_compat.py and lint_docs.py — "
            "every copy of the old string will then show up as an error."
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
