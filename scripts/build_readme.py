#!/usr/bin/env python3
"""Generate README.md and README.zh-CN.md from catalog.json.

catalog.json is the only place a fact is edited. Both READMEs are build
artifacts, and CI fails if they drift from the catalog, so there is no way to
hand-patch one language and leave the other stale.

Layout logic lives in render() exactly once. The two languages differ only by
the string pack passed in, which is what keeps them structurally identical
instead of slowly diverging.

Run: python3 scripts/build_readme.py
"""

from __future__ import annotations

import datetime as dt
import json
import pathlib
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"
RETIRED = ROOT / "retired.json"

REPO = "kydlikebtc/awesome-jev"
REPO_URL = f"https://github.com/{REPO}"
RAW = f"https://raw.githubusercontent.com/{REPO}/main"

# Order is editorial: the patterns an agent author hits first come first.
PATTERN_ORDER = [
    "tool-selection",
    "intent-routing",
    "context-compaction",
    "safety-gating",
    "output-validation",
    "retry-control",
    "human-escalation",
    "model-routing",
    "fan-out",
    "search-ranking",
    "data-extraction",
    "classification",
    "feature-extraction",
    "document-triage",
    "support-triage",
    "content-scoring",
    "recommendation",
    "overview",
]

KIND_ORDER = [
    "official-docs",
    "sdk",
    "integration",
    "snippet",
    "project",
    "plugin",
    "tutorial",
    "case-study",
    "benchmark",
    "article",
    "video",
    "discussion",
    "alternative",
]

FLAG_ORDER = [
    "not-jev",
    "shadow-mode-only",
    "early-access-required",
    "code-untested",
    "single-commit",
    "no-license",
    "third-party-api-key",
    "vendor-reported",
    "unverified-claims",
    "ai-generated",
    "marketing",
    "paywalled",
    "archived",
]

EN = {
    "lang_code": "en",
    "other_readme": "README.zh-CN.md",
    "other_name": "中文",
    "tagline": (
        "Every public example of Jev — TypeSafe AI's System One decision model — "
        "indexed by the decision it makes, not by the blog that mentioned it."
    ),
    "generated": "This file is generated from catalog.json. Edit the catalog, then run `python3 scripts/build_readme.py`.",
    "what_is_h": "What Jev is",
    "what_is": (
        "Jev is a decision model from TypeSafe AI. It does not write text. You hand it a block of "
        "state plus typed questions, and it returns a `choice` among up to 255 options, a `score` on "
        "an ordered 2-to-10 level scale, or a `noul` yes-no probability. A `choice` and a `score` "
        "each carry a calibrated confidence, so your code can act automatically above a threshold "
        "and route to a human below it; a `noul` carries none, because its probability *is* the "
        "answer. TypeSafe calls this a *System One* model: the fast, intuitive counterpart to "
        "deliberate System Two reasoning. It is trained with Reinforcement Learning for Calibrated "
        "Decisions (RLCD), for which no paper has been published.\n\n"
        'The yes-no primitive is named **`noul`** — not "binary" and not "boolean", though one '
        "SDK spells it the latter way and much of the press coverage got it wrong. Input is **text "
        "only**, and there are no published weights, so it cannot be run locally."
    ),
    "why_h": "Why a list of examples",
    "why": (
        "Most of what an agent asks a frontier model to do is not writing, it is choosing: which tool "
        "to call, whether to retry, whether a command is safe to run, which context still matters. "
        "Jev is aimed squarely at that inner loop, which means the useful unit of knowledge is a "
        "**decision pattern**, not a product announcement. This catalog is organised that way."
    ),
    "scope_h": "What this repo is and is not",
    "scope_is": "An index of public, attributable examples of Jev in use, plus runnable snippets in [`examples/`](examples/).",
    "scope_not": (
        "Not the product, not an SDK, not affiliated with TypeSafe AI, and not a recommendation. "
        "A row here means the link was reachable and a person read it, nothing more."
    ),
    "toc_h": "Contents",
    "start_h": "Start here",
    "start_intro": "If you have never called Jev, read these in order.",
    "patterns_h": "By decision pattern",
    "patterns_intro": (
        "The primary index. Each heading is a decision an agent has to make; the rows are "
        "examples of making it with Jev."
    ),
    "kinds_h": "By resource kind",
    "kinds_intro": "The same rows again, grouped by what you will find when you open the link.",
    "examples_h": "Runnable examples in this repo",
    "status_h": "Ecosystem status",
    "verified_h": "What is verified, and what is not",
    "verified_yes": "**Verified:** the URL returned a success status on the date in `checked`, and a person opened the page and wrote the summary from what was actually there.",
    "verified_no": (
        "**Not verified:** whether the code runs, whether benchmark claims hold, whether a project is "
        "maintained, or whether any of this is a good idea for your system. Nothing here has been "
        "load-tested or security-reviewed. Rows carrying `code-untested` were read, not executed."
    ),
    "data_h": "Machine-readable data",
    "data_intro": "One entry per example, validated against a JSON Schema on every push.",
    "contrib_h": "Contributing",
    "license_h": "Licence",
    "license_body": (
        "Code in `scripts/`, `site/` and `examples/` is [MIT](LICENSE-MIT). Catalog metadata is "
        "[CC0-1.0](LICENSE-CC0) except rows marked `CC-BY-4.0`, whose attribution is the `sources` "
        "array on the row. Linked works stay under their own licences."
    ),
    # table headers
    "th_example": "Example",
    "th_shows": "What it shows",
    "th_kind": "Kind",
    "th_lang": "Code",
    "th_pattern": "Pattern",
    "th_notes": "Notes",
    "no_entries": "_No entries yet._",
    "retired_h": "Retired links",
    "retired_intro": "Links that stopped resolving. Kept so a dead reference stays searchable instead of vanishing.",
    "th_why": "Why",
    "stat_entries": "entries",
    "stat_with_code": "carry code",
    "stat_official": "official",
    "stat_patterns": "patterns covered",
    "stat_retired": "retired",
    "zh_note": "",
}

ZH = {
    "lang_code": "zh",
    "other_readme": "README.md",
    "other_name": "English",
    "tagline": (
        "全网 Jev（TypeSafe AI 的 System One 决策模型）使用例子索引 —— "
        "按它做的**决策**归类，而不是按提到它的博客归类。"
    ),
    "generated": "本文件由 catalog.json 生成。请修改目录数据后运行 `python3 scripts/build_readme.py`。",
    "what_is_h": "Jev 是什么",
    "what_is": (
        "Jev 是 TypeSafe AI 的决策模型。它不生成文本。你给它一段状态和若干类型化问题，它返回："
        "最多 255 个选项中的一个 `choice`、2 至 10 级有序量表上的一个 `score`、或一个 `noul` 是非概率。"
        "`choice` 和 `score` 各自带一个校准后的置信度，于是你的代码可以在阈值以上自动执行、"
        "在阈值以下转人工；而 `noul` 不带置信度 —— 它的概率**本身就是**答案。TypeSafe 称之为 "
        "*System One* 模型：与需要深思的 System Two 推理相对的那个快速直觉系统。"
        "它使用面向校准决策的强化学习（RLCD）训练，但该方法尚未发表论文。\n\n"
        "是非原语的名字是 **`noul`** —— 不叫 binary，也不叫 boolean，尽管有一个 SDK 用了后者的拼法、"
        "而且大量媒体报道写错了。输入**仅支持文本**；且权重未公开，因此无法本地运行。\n\n"
        "> ⚠️ **中文用户特别注意：** 官方文档明确说明英语是主要训练语言，"
        "中日韩文「能处理但不同等」（handled but not equally well）。"
        "在中文内容上依赖它之前，请先自己测，并格外留意置信度。"
    ),
    "why_h": "为什么要收集例子",
    "why": (
        "智能体交给前沿模型做的事，大部分不是写作，而是**选择**：调哪个工具、该不该重试、"
        "这条命令能不能安全执行、哪些上下文还有用。Jev 瞄准的正是这个内层循环 —— "
        "所以真正有价值的知识单位是**决策模式**，而不是产品公告。本目录就按这个维度组织。"
    ),
    "scope_h": "本仓库是什么、不是什么",
    "scope_is": "一份公开、可溯源的 Jev 使用例子索引，外加 [`examples/`](examples/) 里可运行的最小样例。",
    "scope_not": (
        "不是产品本身，不是 SDK，与 TypeSafe AI 无隶属关系，也不构成推荐。"
        "收录只意味着链接可访问、并且有人真的读过，仅此而已。"
    ),
    "toc_h": "目录",
    "start_h": "从这里开始",
    "start_intro": "如果你从没调用过 Jev，按顺序读这几条。",
    "patterns_h": "按决策模式",
    "patterns_intro": "主索引。每个标题是智能体必须做的一个决策；下面的行是用 Jev 做这个决策的例子。",
    "kinds_h": "按资源形态",
    "kinds_intro": "同样这些行，按你点开链接后会看到什么来分组。",
    "examples_h": "本仓库内的可运行样例",
    "status_h": "生态现状",
    "verified_h": "哪些经过核实，哪些没有",
    "verified_yes": "**已核实：** 该链接在 `checked` 日期返回了成功状态，并且有人打开页面、按页面实际内容写了摘要。",
    "verified_no": (
        "**未核实：** 代码能否跑通、性能宣称是否成立、项目是否仍在维护、"
        "以及这些做法是否适合你的系统。本仓库没有做过压测或安全审计。"
        "标了 `code-untested` 的行是读过、没跑过。"
    ),
    "data_h": "机器可读数据",
    "data_intro": "每个例子一条记录，每次推送都按 JSON Schema 校验。",
    "contrib_h": "参与贡献",
    "license_h": "许可",
    "license_body": (
        "`scripts/`、`site/`、`examples/` 中的代码采用 [MIT](LICENSE-MIT)。"
        "目录元数据采用 [CC0-1.0](LICENSE-CC0)，标记为 `CC-BY-4.0` 的行除外 —— "
        "其署名即该行的 `sources` 数组。被链接的作品各自保留其原许可。"
    ),
    "th_example": "例子",
    "th_shows": "展示了什么",
    "th_kind": "形态",
    "th_lang": "代码",
    "th_pattern": "模式",
    "th_notes": "备注",
    "no_entries": "_暂无条目。_",
    "retired_h": "已退休的链接",
    "retired_intro": "已经无法访问的链接。保留下来，让失效的引用仍然可被搜索到，而不是凭空消失。",
    "th_why": "原因",
    "stat_entries": "条目",
    "stat_with_code": "含代码",
    "stat_official": "官方",
    "stat_patterns": "覆盖模式",
    "stat_retired": "已退休",
    "zh_note": "",
}

# Display labels. Keys must stay in sync with schema enums; build fails loudly
# if the catalog uses a value with no label rather than printing a raw slug.
PATTERN_LABELS = {
    "tool-selection": (
        "Tool selection",
        "工具选择",
        "Which tool or action the agent should call next.",
        "智能体下一步该调用哪个工具或动作。",
    ),
    "intent-routing": (
        "Intent routing",
        "意图路由",
        "Classify what the user wants and send the request down the right branch.",
        "判断用户意图，把请求分流到正确的分支。",
    ),
    "context-compaction": (
        "Context compaction",
        "上下文压缩",
        "Decide which tool calls and results still matter so stale context can be dropped.",
        "判断哪些工具调用和结果仍然相关，从而丢弃过期上下文。",
    ),
    "safety-gating": (
        "Safety gating",
        "安全闸门",
        "Decide whether an action is safe to run before running it.",
        "在执行前判断一个动作是否安全。",
    ),
    "output-validation": (
        "Output validation",
        "输出校验",
        "Check a model's output against a rubric before it reaches a user.",
        "在输出到达用户前，按评分标准检查模型产出。",
    ),
    "retry-control": (
        "Retry control",
        "重试控制",
        "Decide whether a failed step is worth retrying.",
        "判断失败的步骤是否值得重试。",
    ),
    "human-escalation": (
        "Human escalation",
        "人工升级",
        "Use calibrated confidence to decide what a person must see.",
        "用校准置信度决定哪些情况必须由人来看。",
    ),
    "model-routing": (
        "Model routing",
        "模型路由",
        "Pick which downstream model or tier should handle a request.",
        "选择由哪个下游模型或档位处理请求。",
    ),
    "fan-out": (
        "Speculative fan-out",
        "并行扇出",
        "Pack many questions — including speculative ones — into one request and let code pick what mattered.",
        "把大量问题（包括推测性的）打包进一次请求，再由代码挑出真正用得上的答案。",
    ),
    "search-ranking": (
        "Search & ranking",
        "检索与排序",
        "Score or re-rank candidates from a cheaper retrieval step.",
        "对来自廉价检索步骤的候选做打分或重排。",
    ),
    "data-extraction": (
        "Structured extraction",
        "结构化抽取",
        "Pull typed fields out of messy text by choosing among candidates rather than generating them.",
        "从杂乱文本中取出类型化字段 —— 靠在候选中选择，而不是生成。",
    ),
    "classification": (
        "Classification",
        "分类",
        "Put an item into a taxonomy, including deep hierarchies walked with probabilities.",
        "把条目归入分类体系，包括用概率遍历的深层层级。",
    ),
    "feature-extraction": (
        "ML feature extraction",
        "机器学习特征抽取",
        "Turn free text into numeric features for a classical downstream model.",
        "把自由文本转成数值特征，喂给下游的传统模型。",
    ),
    "document-triage": (
        "Document triage",
        "文档分拣",
        "Classify and route incoming documents, invoices and forms.",
        "对进来的文档、发票、表单做分类和路由。",
    ),
    "support-triage": (
        "Support triage",
        "工单分拣",
        "Route support tickets and conversations by intent and urgency.",
        "按意图和紧急度路由支持工单与会话。",
    ),
    "content-scoring": (
        "Content scoring",
        "内容评分",
        "Score quality, risk or relevance on an ordered scale.",
        "在有序量表上给质量、风险或相关性打分。",
    ),
    "recommendation": (
        "Recommendation",
        "实时推荐",
        "Choose what to surface next, fast enough for a live conversation.",
        "选择下一步呈现什么，快到能用在实时会话里。",
    ),
    "overview": (
        "Overview",
        "总览",
        "Surveys the model or the space rather than one pattern.",
        "介绍模型或整个领域，而非单一模式。",
    ),
}

KIND_LABELS = {
    "official-docs": ("Official docs", "官方文档"),
    "sdk": ("SDK", "SDK"),
    "integration": ("Integration", "平台集成"),
    "snippet": ("Snippet", "代码片段"),
    "project": ("Project", "开源项目"),
    "plugin": ("Plugin", "插件"),
    "tutorial": ("Tutorial", "教程"),
    "case-study": ("Case study", "落地案例"),
    "benchmark": ("Benchmark", "基准测试"),
    "article": ("Article", "文章"),
    "video": ("Video", "视频"),
    "discussion": ("Discussion", "讨论"),
    "alternative": ("Jev-like alternative", "Jev 替代实现"),
}

FLAG_LABELS = {
    "not-jev": ("not Jev itself", "并非 Jev 本身"),
    "shadow-mode-only": ("shadow mode", "仅影子运行"),
    "single-commit": ("one commit", "仅一次提交"),
    "no-license": ("no licence", "无许可证"),
    "vendor-reported": ("vendor numbers", "厂商自报数据"),
    "early-access-required": ("early access", "需早期访问"),
    "code-untested": ("code untested", "代码未实测"),
    "third-party-api-key": ("3rd-party key", "需第三方密钥"),
    "unverified-claims": ("unverified claims", "宣称未核实"),
    "ai-generated": ("AI-written", "疑似 AI 生成"),
    "marketing": ("marketing", "营销内容"),
    "paywalled": ("paywall", "付费墙"),
    "archived": ("archived", "已归档"),
}

LANG_LABELS = {
    "python": "Py",
    "typescript": "TS",
    "javascript": "JS",
    "go": "Go",
    "rust": "Rs",
    "shell": "sh",
    "java": "Java",
    "ruby": "Rb",
    "php": "PHP",
    "csharp": "C#",
}


def esc(text: str) -> str:
    """Escape what would break a markdown table cell."""
    return text.replace("|", "\\|").replace("\n", " ").strip()


def anchor(text: str) -> str:
    """GitHub's heading-to-anchor rule, enough of it for our headings."""
    slug = text.lower()
    slug = "".join(ch for ch in slug if ch.isalnum() or ch in " -_\u4e00-\u9fff")
    return slug.strip().replace(" ", "-")


def label(mapping: dict, key: str, lang: str, *, field: int = 0) -> str:
    entry = mapping.get(key)
    if entry is None:
        raise KeyError(
            f"no display label for {key!r}. Add it to build_readme.py when you add a schema enum value."
        )
    return entry[field + (1 if lang == "zh" else 0)]


def title_cell(entry: dict) -> str:
    text = f"[{esc(entry['title'])}]({entry['url']})"
    if entry.get("official"):
        text += " ⭐"
    author = entry.get("author", {}).get("name")
    if author:
        text += f"<br><sub>{esc(author)}</sub>"
    return text


def code_cell(entry: dict, lang: str) -> str:
    if not entry.get("has_code"):
        return "—"
    langs = [LANG_LABELS.get(item, item) for item in entry.get("languages", [])]
    qtypes = entry.get("question_types", [])
    parts = []
    if langs:
        parts.append(" ".join(f"`{item}`" for item in langs))
    if qtypes:
        parts.append("<sub>" + "/".join(qtypes) + "</sub>")
    return "<br>".join(parts) if parts else "✓"


def notes_cell(entry: dict, lang: str) -> str:
    bits = []
    for flag in FLAG_ORDER:
        if flag in entry.get("flags", []):
            bits.append(f"`{label(FLAG_LABELS, flag, lang)}`")
    note = entry.get("notes_zh" if lang == "zh" else "notes")
    if note:
        bits.append(esc(note))
    return " ".join(bits) if bits else "—"


def summary_of(entry: dict, lang: str) -> str:
    text = entry["summary_zh"] if lang == "zh" else entry["summary"]
    if lang == "zh" and entry.get("zh_machine"):
        text += " <sub>(机翻)</sub>"
    return esc(text)


def sort_key(entry: dict) -> tuple:
    """Official first, then entries with code, then stars, then title."""
    return (
        not entry.get("official", False),
        not entry.get("has_code", False),
        -(entry.get("stars") or 0),
        entry["title"].lower(),
    )


def pattern_table(entries: list[dict], strings: dict) -> list[str]:
    lang = strings["lang_code"]
    if not entries:
        return [strings["no_entries"], ""]
    lines = [
        f"| {strings['th_example']} | {strings['th_shows']} | {strings['th_kind']} | {strings['th_lang']} | {strings['th_notes']} |",
        "| --- | --- | --- | --- | --- |",
    ]
    for entry in sorted(entries, key=sort_key):
        lines.append(
            "| "
            + " | ".join(
                [
                    title_cell(entry),
                    summary_of(entry, lang),
                    label(KIND_LABELS, entry["kind"], lang),
                    code_cell(entry, lang),
                    notes_cell(entry, lang),
                ]
            )
            + " |"
        )
    lines.append("")
    return lines


def render(catalog: list[dict], retired: list[dict], strings: dict, today: str) -> str:
    lang = strings["lang_code"]
    out: list[str] = []
    add = out.append

    by_pattern: dict[str, list[dict]] = {key: [] for key in PATTERN_ORDER}
    for entry in catalog:
        for pattern in entry["patterns"]:
            by_pattern[pattern].append(entry)

    by_kind: dict[str, list[dict]] = {key: [] for key in KIND_ORDER}
    for entry in catalog:
        by_kind[entry["kind"]].append(entry)

    live_patterns = [key for key in PATTERN_ORDER if by_pattern[key]]
    live_kinds = [key for key in KIND_ORDER if by_kind[key]]

    with_code = sum(1 for entry in catalog if entry.get("has_code"))
    official = sum(1 for entry in catalog if entry.get("official"))

    # ---- header ----
    add("<!--")
    add(f"  {strings['generated']}")
    add("-->")
    add("")
    add("# awesome-jev")
    add("")
    add(
        f"[![lint]({REPO_URL}/actions/workflows/lint.yml/badge.svg)]({REPO_URL}/actions/workflows/lint.yml) "
        f"[![links]({REPO_URL}/actions/workflows/links.yml/badge.svg)]({REPO_URL}/actions/workflows/links.yml) "
        f"[![entries](https://img.shields.io/badge/{strings['stat_entries']}-{len(catalog)}-1f6feb)]({REPO_URL}) "
        "[![data: CC0-1.0](https://img.shields.io/badge/data-CC0--1.0-brightgreen)](LICENSE-CC0) "
        "[![code: MIT](https://img.shields.io/badge/code-MIT-blue)](LICENSE-MIT)"
    )
    add("")
    add(f"> {strings['tagline']}")
    add("")
    add(
        f"**{strings['other_name']}:** [{strings['other_readme']}]({strings['other_readme']})"
    )
    add("")

    # ---- stats line ----
    add(
        f"`{len(catalog)}` {strings['stat_entries']} · "
        f"`{with_code}` {strings['stat_with_code']} · "
        f"`{official}` {strings['stat_official']} · "
        f"`{len(live_patterns)}/{len(PATTERN_ORDER)}` {strings['stat_patterns']} · "
        f"`{len(retired)}` {strings['stat_retired']} · "
        f"`{today}`"
    )
    add("")

    # ---- what is jev ----
    add(f"## {strings['what_is_h']}")
    add("")
    add(strings["what_is"])
    add("")
    add(f"## {strings['why_h']}")
    add("")
    add(strings["why"])
    add("")
    add(f"## {strings['scope_h']}")
    add("")
    add(f"- ✅ {strings['scope_is']}")
    add(f"- ❌ {strings['scope_not']}")
    add("")

    # ---- toc ----
    add(f"## {strings['toc_h']}")
    add("")
    add(f"- [{strings['patterns_h']}](#{anchor(strings['patterns_h'])})")
    for key in live_patterns:
        name = label(PATTERN_LABELS, key, lang)
        add(f"  - [{name}](#{anchor(name)}) `{len(by_pattern[key])}`")
    add(f"- [{strings['kinds_h']}](#{anchor(strings['kinds_h'])})")
    add(f"- [{strings['examples_h']}](#{anchor(strings['examples_h'])})")
    add(f"- [{strings['status_h']}](#{anchor(strings['status_h'])})")
    add(f"- [{strings['verified_h']}](#{anchor(strings['verified_h'])})")
    add(f"- [{strings['data_h']}](#{anchor(strings['data_h'])})")
    add(f"- [{strings['contrib_h']}](#{anchor(strings['contrib_h'])})")
    add("")

    # ---- by pattern ----
    add(f"## {strings['patterns_h']}")
    add("")
    add(strings["patterns_intro"])
    add("")
    if not live_patterns:
        add(strings["no_entries"])
        add("")
    for key in live_patterns:
        name = label(PATTERN_LABELS, key, lang)
        blurb = label(PATTERN_LABELS, key, lang, field=2)
        add(f"### {name}")
        add("")
        add(f"_{blurb}_")
        add("")
        out.extend(pattern_table(by_pattern[key], strings))

    # ---- by kind ----
    add(f"## {strings['kinds_h']}")
    add("")
    add(strings["kinds_intro"])
    add("")
    if not live_kinds:
        add(strings["no_entries"])
        add("")
    for key in live_kinds:
        name = label(KIND_LABELS, key, lang)
        items = ", ".join(
            f"[{esc(entry['title'])}]({entry['url']})"
            for entry in sorted(by_kind[key], key=sort_key)
        )
        add(f"- **{name}** `{len(by_kind[key])}` — {items}")
    add("")

    # ---- in-repo examples ----
    add(f"## {strings['examples_h']}")
    add("")
    add(f"<!-- examples-table:start -->")
    add(f"See [`examples/README.md`](examples/README.md).")
    add(f"<!-- examples-table:end -->")
    add("")

    # ---- status ----
    add(f"## {strings['status_h']}")
    add("")
    add("<!-- status:start -->")
    add(f"See [`docs/status.md`](docs/status.md).")
    add("<!-- status:end -->")
    add("")

    # ---- verification ----
    add(f"## {strings['verified_h']}")
    add("")
    add(f"- {strings['verified_yes']}")
    add(f"- {strings['verified_no']}")
    add("")

    if retired:
        add(f"### {strings['retired_h']}")
        add("")
        add(strings["retired_intro"])
        add("")
        add(f"| {strings['th_example']} | {strings['th_why']} |")
        add("| --- | --- |")
        for entry in sorted(retired, key=lambda item: item["title"].lower()):
            why = entry.get("notes_zh" if lang == "zh" else "notes") or "—"
            status = entry.get("link_status")
            suffix = f" `HTTP {status}`" if status else ""
            add(f"| {esc(entry['title'])} | {esc(why)}{suffix} |")
        add("")

    # ---- data ----
    add(f"## {strings['data_h']}")
    add("")
    add(strings["data_intro"])
    add("")
    add(f"- Catalog — [`catalog.json`]({RAW}/catalog.json)")
    add(f"- Retired — [`retired.json`]({RAW}/retired.json)")
    add(f"- Schema — [`schema/entry.schema.json`]({RAW}/schema/entry.schema.json)")
    add(f"- For agents — [`llms.txt`]({RAW}/llms.txt)")
    add("")

    # ---- contributing ----
    add(f"## {strings['contrib_h']}")
    add("")
    add(f"- [CONTRIBUTING.md](CONTRIBUTING.md)")
    add(f"- [docs/method.md](docs/method.md)")
    add(f"- [docs/patterns.md](docs/patterns.md)")
    add(f"- [docs/vetting.md](docs/vetting.md)")
    add("")
    add(f"## {strings['license_h']}")
    add("")
    add(strings["license_body"])
    add("")

    return "\n".join(out)


def main() -> int:
    catalog = json.loads(CATALOG.read_text())
    retired = json.loads(RETIRED.read_text())
    today = dt.date.today().isoformat()

    try:
        (ROOT / "README.md").write_text(render(catalog, retired, EN, today))
        (ROOT / "README.zh-CN.md").write_text(render(catalog, retired, ZH, today))
    except KeyError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    counts = Counter(pattern for entry in catalog for pattern in entry["patterns"])
    print(f"wrote README.md and README.zh-CN.md from {len(catalog)} entries")
    if counts:
        top = ", ".join(f"{key} {value}" for key, value in counts.most_common(5))
        print(f"  top patterns: {top}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
