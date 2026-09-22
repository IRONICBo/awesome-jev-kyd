#!/usr/bin/env python3
"""Verify the hand-written docs still state the catalog's real numbers.

README.md, docs/assets/*.svg and docs/compatibility.md are generated, so `lint`
regenerates them and fails on any drift. The files checked here are *not*
generated. They are hand-written prose and marketing copy that happen to quote
counts, and nothing was watching them: between the 148-entry first build and the
404-entry expansion every one of them went stale in silence. llms.txt — the
machine-readable entry point, the file agents read first — spent that whole time
telling them the catalog held 148 rows while shipping 404.

Generating these files instead was considered and rejected. Two of them are
mostly judgement prose (docs/status.md is essays about what week one looked
like), and templating an essay to keep one integer honest is the wrong trade.
site/index.html settles it: its count sits inside a `<meta content="...">`
attribute, where no placeholder marker can live.

This is deliberately an allowlist, not a sweep for stray integers. Some numbers
in these docs are historical *on purpose*: docs/method.md's "the first build
checked 148 entries" is a record of what happened, under a heading that says so.
A guard that "fixed" it would be falsifying the log. Only claims about the
catalog as it stands *now* belong below.

A regex guard's real failure mode is not a false alarm, it is matching nothing
at all and reporting success — reword the sentence and the check evaporates
while staying green. So a pattern that fails to match is a hard error here,
exactly as loud as a wrong number.

Run: python3 scripts/check_doc_counts.py
"""

from __future__ import annotations

import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def facts() -> dict[str, str]:
    """The numbers the docs are allowed to claim, read from the source of truth."""
    catalog = json.loads((ROOT / "catalog.json").read_text())
    schema = json.loads((ROOT / "schema" / "entry.schema.json").read_text())

    all_patterns = schema["properties"]["patterns"]["items"]["enum"]
    covered = {pattern for entry in catalog for pattern in entry["patterns"]}
    hand_zh = sum(1 for entry in catalog if not entry.get("zh_machine"))

    # llms.txt describes the evidence chain in these terms, so the guard has to
    # count the same population: rows that assert which primitives are called.
    asserting = [entry for entry in catalog if entry.get("question_types")]

    return {
        "entries": str(len(catalog)),
        "with_code": str(sum(1 for e in catalog if e.get("has_code"))),
        "official": str(sum(1 for e in catalog if e.get("official"))),
        "link_ok": str(sum(1 for e in catalog if e.get("link_status") == 200)),
        "patterns_covered": f"{len([p for p in all_patterns if p in covered])}"
        f" of {len(all_patterns)}",
        "zh_hand": f"{hand_zh} of {len(catalog)}",
        "asserting_rows": str(len(asserting)),
        "asserting_cited": str(sum(1 for e in asserting if e.get("evidence"))),
    }


# (file, what the number is asserting, pattern with one capture group, fact key)
#
# Every pattern must capture exactly the substring a human would edit, so the
# failure message can quote both sides. Keep the surrounding context in the
# pattern generous enough that it cannot drift onto a different number.
CHECKS: list[tuple[str, str, str, str]] = [
    (
        "llms.txt",
        "summary line — entry count",
        r"indexed by the decision each example makes\. (\d+) entries",
        "entries",
    ),
    (
        "llms.txt",
        "summary line — links verified",
        r"(\d+) returned HTTP 200",
        "link_ok",
    ),
    (
        "llms.txt",
        "machine-readable data — entry count",
        r"Catalog \((\d+) entries\)",
        "entries",
    ),
    (
        "llms.txt",
        "what is verified — rows asserting primitives",
        r"Of the (\d+) rows asserting which primitives",
        "asserting_rows",
    ),
    (
        "llms.txt",
        "what is verified — rows citing an evidence file",
        r"a project's code calls, (\d+) cite the exact file",
        "asserting_cited",
    ),
    (
        "docs/status.md",
        "shape table — entries",
        r"\|\s*Entries\s*\|\s*(\d+)\s*\|",
        "entries",
    ),
    (
        "docs/status.md",
        "shape table — carrying code",
        r"\|\s*Carrying code\s*\|\s*(\d+)\s*\|",
        "with_code",
    ),
    (
        "docs/status.md",
        "shape table — official",
        r"\|\s*Official \(TypeSafe AI's own\)\s*\|\s*(\d+)\s*\|",
        "official",
    ),
    (
        "docs/status.md",
        "shape table — patterns covered",
        r"\|\s*Patterns covered\s*\|\s*(\d+ of \d+)\s*\|",
        "patterns_covered",
    ),
    (
        "docs/status.md",
        "shape table — Chinese hand-written",
        r"\|\s*Chinese summaries hand-written\s*\|\s*(\d+ of \d+)\s*\|",
        "zh_hand",
    ),
    (
        "docs/social-card.html",
        "readout — entries",
        r'<div class="v">(\d+)</div>\s*<div class="k">entries</div>',
        "entries",
    ),
    (
        "docs/social-card.html",
        "readout — with code",
        r'<div class="v">(\d+)</div>\s*<div class="k">with code</div>',
        "with_code",
    ),
    (
        "docs/social-card.html",
        "readout — official",
        r'<div class="v">(\d+)</div>\s*<div class="k">official</div>',
        "official",
    ),
    (
        "docs/social-card.html",
        "readout — link-verified",
        r'<div class="v">(\d+)</div>\s*<div class="k">link-verified</div>',
        "link_ok",
    ),
    (
        "site/index.html",
        "og:description — entry count",
        r'content="(\d+) verified examples of Jev',
        "entries",
    ),
]


def line_of(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


# The social card's "Coverage by pattern" panel is a hand-picked top-N, so which
# patterns it shows is an editorial call and not something to enforce. What each
# one *says* is not: the card shipped "Intent routing 20" long after intent
# routing had become 26 and slipped from second place to eighth.
#
# So this scans whatever pairs are there and checks each against the catalog.
# Display names come from patterns.json, which already exists precisely so the
# README builder, the figure builder and the MCP server cannot drift apart; this
# makes it the fourth reader rather than a fifth copy of the same table.
BAR = re.compile(r'<span>([^<]+)</span><span class="n">(\d+)</span>')
CARD = "docs/social-card.html"


def check_pattern_bars(catalog: list[dict]) -> list[str]:
    names = {
        pattern["en"]: pattern["key"]
        for pattern in json.loads((ROOT / "patterns.json").read_text())["patterns"]
    }
    counts: dict[str, int] = {}
    for entry in catalog:
        for pattern in entry["patterns"]:
            counts[pattern] = counts.get(pattern, 0) + 1

    text = (ROOT / CARD).read_text()
    pairs = list(BAR.finditer(text))
    if not pairs:
        return [
            f"{CARD}: found no pattern bars at all. The markup changed; update "
            f"BAR in scripts/check_doc_counts.py."
        ]

    problems = []
    for match in pairs:
        label, shown = html.unescape(match.group(1)), match.group(2)
        key = names.get(label)
        if key is None:
            problems.append(
                f"{CARD}:{line_of(text, match.start(1))}: {label!r} is not a "
                f"pattern name in patterns.json"
            )
        elif int(shown) != counts.get(key, 0):
            problems.append(
                f"{CARD}:{line_of(text, match.start(2))}: bar for {label!r} says "
                f"{shown}, catalog.json says {counts.get(key, 0)}"
            )
    return problems


def main() -> int:
    truth = facts()
    problems: list[str] = []
    cache: dict[str, str] = {}

    for path, label, pattern, key in CHECKS:
        text = cache.get(path)
        if text is None:
            file = ROOT / path
            if not file.exists():
                problems.append(f"{path}: missing, but {label!r} is checked against it")
                continue
            text = cache[path] = file.read_text()

        matches = list(re.finditer(pattern, text))
        expected = truth[key]

        if not matches:
            # Not a pass. The prose was reworded out from under the guard, and a
            # guard that cannot find its subject is not guarding anything.
            problems.append(
                f"{path}: pattern for {label!r} matched nothing.\n"
                f"    The wording changed, or the number was deleted. Either fix the\n"
                f"    doc or update the pattern in scripts/check_doc_counts.py.\n"
                f"    pattern: {pattern}"
            )
            continue

        for match in matches:
            found = match.group(1)
            if found != expected:
                problems.append(
                    f"{path}:{line_of(text, match.start(1))}: {label} says "
                    f"{found!r}, catalog.json says {expected!r}"
                )

    problems += check_pattern_bars(json.loads((ROOT / "catalog.json").read_text()))

    if problems:
        print(
            "error: docs state counts that the catalog contradicts\n", file=sys.stderr
        )
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        print(
            f"\n{len(problems)} problem(s). Run 'python3 scripts/counts.py' for the "
            "live numbers.",
            file=sys.stderr,
        )
        return 1

    bars = len(BAR.findall((ROOT / CARD).read_text()))
    print(f"{len(CHECKS)} doc counts and {bars} pattern bars agree with catalog.json:")
    for key, value in truth.items():
        print(f"  {key:<17} {value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
