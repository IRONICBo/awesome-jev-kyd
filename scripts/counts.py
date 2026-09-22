#!/usr/bin/env python3
"""Print catalog statistics.

Runs in CI so every build logs the shape of the catalog, which makes coverage
gaps visible over time: a pattern with zero entries is a research to-do, not a
rendering bug.

Run: python3 scripts/counts.py
"""

from __future__ import annotations

import json
import pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent

catalog = json.loads((ROOT / "catalog.json").read_text())
retired = json.loads((ROOT / "retired.json").read_text())
schema = json.loads((ROOT / "schema" / "entry.schema.json").read_text())

all_patterns = schema["properties"]["patterns"]["items"]["enum"]
all_kinds = schema["properties"]["kind"]["enum"]

patterns = Counter(pattern for entry in catalog for pattern in entry["patterns"])
kinds = Counter(entry["kind"] for entry in catalog)
languages = Counter(lang for entry in catalog for lang in entry.get("languages", []))
platforms = Counter(item for entry in catalog for item in entry.get("platforms", []))
qtypes = Counter(item for entry in catalog for item in entry.get("question_types", []))
flags = Counter(flag for entry in catalog for flag in entry.get("flags", []))

with_code = sum(1 for entry in catalog if entry.get("has_code"))
official = sum(1 for entry in catalog if entry.get("official"))
hand_zh = sum(1 for entry in catalog if not entry.get("zh_machine"))


def block(title: str, counter: Counter, universe: list[str] | None = None) -> None:
    print(f"\n{title}")
    if universe is not None:
        for key in universe:
            count = counter.get(key, 0)
            bar = "#" * count
            mark = " " if count else "!"
            print(f"  {mark} {key:<24} {count:>3} {bar}")
        missing = [key for key in universe if not counter.get(key)]
        if missing:
            print(f"    no entries yet: {', '.join(missing)}")
    else:
        for key, count in counter.most_common():
            print(f"    {key:<24} {count:>3} {'#' * count}")
        if not counter:
            print("    (none)")


print(f"catalog.json   {len(catalog)} entries")
print(f"retired.json   {len(retired)} entries")
print(f"with code      {with_code}")
print(f"official       {official}")
if catalog:
    print(f"zh hand-written {hand_zh}/{len(catalog)}")

block("by pattern (! = gap)", patterns, all_patterns)
block("by kind (! = gap)", kinds, all_kinds)
block("by language", languages)
block("by platform", platforms)
block("by question type", qtypes)
block("flags", flags)
print()
