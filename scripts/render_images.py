#!/usr/bin/env python3
"""Render every image that shows catalogue data, from the data, at deploy time.

The social card and the README screenshots were PNGs committed once and never
regenerated, so they said 148 entries long after the catalogue passed 800. This
renders them from the assembled site on every Pages deploy instead, and they
are served from Pages rather than committed — an image that is rebuilt from the
data it shows cannot drift from it, and git history does not collect a new
half-megabyte PNG every week.

  img/og.png           card.html?mode=live — the site's og:image, live figures
  img/card.png         card.html — the durable card for GitHub's social preview,
                       which has to be uploaded by hand and so carries no figure
                       that changes
  img/site-en.png      the site, English — the README hero image
  img/site-zh.png      the site, Chinese — the Chinese README hero image
  img/site-compat.png  the compatibility view — docs/compatibility.md

Each page is first loaded with --dump-dom and must have set data-ready="1" and
contain an expected string, or nothing is published: a screenshot of a page
whose fetch failed would otherwise go live looking like a real preview.

Stdlib plus a Chrome binary. GitHub's ubuntu runners ship Google Chrome, so CI
needs no install step; locally, set CHROME if it is not found.

Run: python3 scripts/render_images.py              # after copying data into site/
"""

from __future__ import annotations

import functools
import http.server
import json
import os
import pathlib
import platform
import shutil
import subprocess
import sys
import threading

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _stats  # noqa: E402

ROOT = _stats.ROOT
SITE = ROOT / "site"
OUT = SITE / "img"
BUDGET_MS = 15000

# (output name, page, viewport, a string the rendered DOM must contain)
TARGETS = (
    ("og.png", "card.html?mode=live", (1280, 640), "link-verified"),
    ("card.png", "card.html", (1280, 640), "One request, three answers"),
    ("site-en.png", "index.html?lang=en", (1200, 900), "Tool selection"),
    ("site-zh.png", "index.html?lang=zh", (1200, 900), "工具选择"),
    ("site-compat.png", "index.html?lang=en&view=compat", (1200, 900), "typesafe/jev"),
)

CANDIDATES = (
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
)


def find_chrome() -> str:
    for candidate in (
        [os.environ["CHROME"]] if os.environ.get("CHROME") else []
    ) + list(CANDIDATES):
        path = shutil.which(candidate) or (
            candidate if os.path.exists(candidate) else None
        )
        if path:
            return path
    raise SystemExit(
        "error: no Chrome found. Set CHROME to a Chrome or Chromium binary."
    )


class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args: object) -> None:  # one line per image is enough
        pass


def serve() -> tuple[http.server.ThreadingHTTPServer, int]:
    handler = functools.partial(_Quiet, directory=str(SITE))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, server.server_address[1]


def chrome(
    binary: str, size: tuple[int, int], *args: str
) -> subprocess.CompletedProcess:
    flags = [
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        f"--window-size={size[0]},{size[1]}",
        f"--virtual-time-budget={BUDGET_MS}",
    ]
    # The runner's container has no user namespace for Chrome's sandbox. These
    # are our own static pages, rendered once and thrown away.
    if platform.system() == "Linux":
        flags.append("--no-sandbox")
    return subprocess.run(
        [binary, *flags, *args], capture_output=True, text=True, timeout=120
    )


def main() -> int:
    for name in ("catalog.json", "patterns.json", "compat.json", "taxonomy.json"):
        if not (SITE / name).exists():
            raise SystemExit(f"error: site/{name} is missing; copy the data in first")

    # The card reads the same numbers the README badges use, rather than
    # recounting them in JavaScript with its own idea of "link-verified".
    (SITE / "stats.json").write_text(json.dumps(_stats.compute(), ensure_ascii=False))

    OUT.mkdir(exist_ok=True)
    binary = find_chrome()
    server, port = serve()
    failures = []
    try:
        for name, page, size, expect in TARGETS:
            url = f"http://127.0.0.1:{port}/{page}"
            target = OUT / name
            # Never leave a previous render in place: a stale image that
            # survives a failed render is exactly the bug this script removes.
            target.unlink(missing_ok=True)
            dom = chrome(binary, size, "--dump-dom", url).stdout
            if 'data-ready="1"' not in dom or expect not in dom:
                failures.append(f"{name}: {page} never finished rendering its data")
                continue
            chrome(binary, size, f"--screenshot={target}", url)
            if not target.exists() or target.stat().st_size < 10_000:
                failures.append(f"{name}: Chrome produced no usable screenshot")
                continue
            print(
                f"  rendered img/{name}  {size[0]}×{size[1]}  {target.stat().st_size // 1024} KB"
            )
    finally:
        server.shutdown()

    for failure in failures:
        print(f"error: {failure}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
