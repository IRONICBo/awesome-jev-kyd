#!/usr/bin/env python3
"""Generate the tables in docs/compatibility.md from compat.json.

The platform matrix is the repo's most-cited original asset, so it follows the
same rule as the catalog: one machine-readable source, generated presentation.
The site reads the same compat.json, which means the doc and the site cannot
drift apart — the failure mode that would quietly make the matrix useless.

Only the regions between the markers below are rewritten; the prose around
them is hand-written and left alone.

Run: python3 scripts/build_compat.py
     python3 scripts/build_compat.py --check    # CI: fail if out of date
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
COMPAT = ROOT / "compat.json"
DOC = ROOT / "docs" / "compatibility.md"

# Each block is (marker-name, header row, row builder). A dash in the data
# means the surface does not expose that concept, and is printed as-is.
BLOCKS = {
    "models": (
        ["Surface", "Model string to send"],
        lambda p: [link(p), code_list(p["model"])],
    ),
    "yesno": (
        ["Surface", "Type name", "Read the answer from"],
        lambda p: [link(p), code(p["yesno"]), code(p["answer_field"])],
    ),
    "confidence": (
        ["Surface", "Where `choice` / `score` confidence lives"],
        lambda p: [link(p), p["confidence"]],
    ),
    "envelope": (
        ["Surface", "Request shape", "Endpoint"],
        lambda p: [link(p), p["envelope"], code(p["endpoint"])],
    ),
    "env": (
        ["Surface", "Environment variable"],
        lambda p: [link(p), code(p["env"])],
    ),
    "notes": (
        ["Surface", "Worth knowing"],
        lambda p: [link(p), p.get("notes", "—")],
    ),
}


def code(value: str) -> str:
    return "—" if value.strip() == "—" else f"`{value}`"


def code_list(value: str) -> str:
    """Wrap each of several dot-separated names in its own backticks."""
    if value.strip() == "—":
        return "—"
    return " · ".join(f"`{part.strip()}`" for part in value.split("·"))


def link(platform: dict) -> str:
    name = platform["name"]
    if platform.get("official"):
        name += " ⭐"
    url = platform.get("url")
    return f"[{name}]({url})" if url else name


def table(header: list[str], rows: list[list[str]]) -> list[str]:
    out = [
        "| " + " | ".join(header) + " |",
        "|" + "|".join(" --- " for _ in header) + "|",
    ]
    out += [
        "| " + " | ".join(cell.replace("|", "\\|") for cell in row) + " |"
        for row in rows
    ]
    return out


def limits_table(limits: list[dict]) -> list[str]:
    rows = [[f"**{item['k']}**", item["v"], item["why"]] for item in limits]
    return table(["", "Limit", "Why it matters"], rows)


def build() -> str:
    data = json.loads(COMPAT.read_text())
    platforms = data["platforms"]
    original = DOC.read_text()
    text = original

    for name, (header, row_of) in BLOCKS.items():
        start, end = f"<!-- {name}:start -->", f"<!-- {name}:end -->"
        if start not in text or end not in text:
            raise SystemExit(
                f"error: docs/compatibility.md is missing the {start} / {end} markers"
            )
        body = "\n".join(table(header, [row_of(p) for p in platforms]))
        head, _, rest = text.partition(start)
        _, _, tail = rest.partition(end)
        text = f"{head}{start}\n{body}\n{end}{tail}"

    start, end = "<!-- limits:start -->", "<!-- limits:end -->"
    if start in text and end in text:
        body = "\n".join(limits_table(data["limits"]))
        head, _, rest = text.partition(start)
        _, _, tail = rest.partition(end)
        text = f"{head}{start}\n{body}\n{end}{tail}"

    text = text.replace("<!-- as_of -->", data["as_of"])
    return text


def normalise(text: str) -> str:
    """Collapse table cell padding so the check compares data, not formatting.

    A markdown formatter will happily pad every pipe to align columns, which is
    harmless but byte-different from what this script emits. Without this, CI
    would fail for a contributor whose editor runs prettier — a false alarm
    that teaches people to ignore the check. Real data drift still fails.
    """
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            # A separator row is only dashes and colons; length is cosmetic.
            cells = ["-" if set(c) <= set("-: ") and c else c for c in cells]
            lines.append("|" + "|".join(cells) + "|")
        else:
            lines.append(stripped)
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail instead of writing")
    args = parser.parse_args()

    rendered = build()
    current = DOC.read_text()

    if rendered == current:
        print("docs/compatibility.md is up to date")
        return 0
    if normalise(rendered) == normalise(current):
        print("docs/compatibility.md is up to date (formatting differs, data matches)")
        return 0
    if args.check:
        print(
            "error: docs/compatibility.md is out of sync with compat.json.\n"
            "Run 'python3 scripts/build_compat.py' and commit the result.",
            file=sys.stderr,
        )
        return 1

    DOC.write_text(rendered)
    data = json.loads(COMPAT.read_text())
    print(
        f"wrote docs/compatibility.md from {len(data['platforms'])} platforms "
        f"and {len(data['limits'])} limits"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
