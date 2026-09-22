#!/usr/bin/env python3
"""Sweep every catalog URL and report which ones stopped resolving.

Read-only by default: it prints a report and exits non-zero when something is
dead, so a scheduled run opens a visible red build rather than silently
rewriting the catalog. Pass --write to stamp `checked` and `link_status` on the
rows that answered.

A dead link is never deleted by this script. Moving a row to retired.json is a
judgement call — the row needs a `notes` line saying why — so a person does it.

Usage:
  python3 scripts/check_links.py               # report only
  python3 scripts/check_links.py --write       # also update checked/link_status
  python3 scripts/check_links.py --only youtube.com
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"

TIMEOUT = 20
WORKERS = 8

# A plain urllib request gets 403'd by a lot of CDNs. Look like a browser.
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

# Hosts that answer HEAD with a lie. Ask for GET on these.
GET_ONLY = (
    "medium.com",
    "youtube.com",
    "youtu.be",
    "x.com",
    "twitter.com",
    "forbes.com",
)


def fetch_status(url: str) -> tuple[int, str]:
    """Return (status, note). Status 0 means the request never completed."""
    method = "GET" if any(host in url for host in GET_ONLY) else "HEAD"

    for attempt in (method, "GET"):
        request = urllib.request.Request(url, headers=HEADERS, method=attempt)
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
                return response.status, ""
        except urllib.error.HTTPError as exc:
            # 405 means the host dislikes HEAD, not that the page is gone.
            if attempt == "HEAD" and exc.code in (403, 405, 400, 501):
                continue
            return exc.code, exc.reason or ""
        except urllib.error.URLError as exc:
            if attempt == "HEAD":
                continue
            return 0, str(exc.reason)
        except Exception as exc:  # noqa: BLE001 - a sweep must not die on one row
            if attempt == "HEAD":
                continue
            return 0, exc.__class__.__name__
    return 0, "unreachable"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write", action="store_true", help="stamp checked/link_status on live rows"
    )
    parser.add_argument(
        "--only", default="", help="only check URLs containing this substring"
    )
    args = parser.parse_args()

    catalog = json.loads(CATALOG.read_text())
    targets = [entry for entry in catalog if args.only in entry["url"]]
    if not targets:
        print("nothing to check")
        return 0

    print(f"checking {len(targets)} url(s) with {WORKERS} workers\n")
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(lambda entry: fetch_status(entry["url"]), targets))

    today = dt.date.today().isoformat()
    dead: list[tuple[dict, int, str]] = []
    moved: list[tuple[dict, int]] = []
    blocked: list[tuple[dict, int, str]] = []

    for entry, (status, note) in zip(targets, results):
        alive = 200 <= status < 300
        redirected = 300 <= status < 400
        # 401/403/429 mean the host refused *us*, which is not evidence the page
        # is gone. Forbes, Medium and anything behind Cloudflare answer this way
        # to every scripted request. Retiring those rows would be factually
        # wrong, so they are reported separately for a human to eyeball.
        refused = status in (401, 403, 429)

        if alive:
            mark = "ok  "
        elif redirected:
            mark = "--> "
        elif refused:
            mark = "BLOK"
        else:
            mark = "DEAD"
        detail = f" {note}" if note else ""
        print(f"  {mark} {status or '---'}  {entry['slug']}{detail}")

        if alive:
            if args.write:
                entry["checked"] = today
                entry["link_status"] = status
        elif redirected:
            moved.append((entry, status))
        elif refused:
            blocked.append((entry, status, note))
        else:
            dead.append((entry, status, note))

    if args.write:
        CATALOG.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n")
        stamped = len(targets) - len(dead) - len(moved) - len(blocked)
        print(f"\nstamped checked={today} on {stamped} row(s)")

    if blocked:
        print(
            f"\n{len(blocked)} link(s) refused this checker but are probably fine. "
            "Open each in a browser; do NOT retire on a 403 alone:"
        )
        for entry, status, note in blocked:
            print(f"  {entry['slug']}  HTTP {status}  {entry['url']}  {note}")

    if moved:
        print(f"\n{len(moved)} redirect(s) — update `url` to the destination:")
        for entry, status in moved:
            print(f"  {entry['slug']}  HTTP {status}  {entry['url']}")

    if dead:
        print(
            f"\n{len(dead)} dead link(s). Move each to retired.json with a notes line saying why:"
        )
        for entry, status, note in dead:
            print(f"  {entry['slug']}  HTTP {status or '---'}  {entry['url']}  {note}")
        return 1

    print("\nall links resolved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
