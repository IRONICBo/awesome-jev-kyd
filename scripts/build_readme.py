#!/usr/bin/env python3
"""Generate README.md and README.zh-CN.md from catalog.json.

catalog.json is the only place a fact is edited. Both READMEs are build
artifacts, and CI fails if they drift from the catalog, so there is no way to
hand-patch one language and leave the other stale.

Layout logic lives in render() exactly once. The two languages differ only by
the string pack passed in, which is what keeps them structurally identical
instead of slowly diverging.

Readability rules this file enforces, learned the hard way:

* Long `notes` prose only appears in the curated sections, where there are few
  rows and the note *is* the point. In the big pattern tables it would make
  every row several lines tall and destroy scanning, so those carry short flag
  pills instead and the full note lives in catalog.json and on the site.
* One index, not two. The coverage histogram doubles as the table of contents,
  so there is no separate link list repeating the same eighteen counts.
* Anything that is really a table is rendered as a table, not as prose or as a
  comma-separated wall of links.

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
PATTERNS_FILE = ROOT / "patterns.json"
RETIRED = ROOT / "retired.json"

REPO = "kydlikebtc/awesome-jev"
REPO_URL = f"https://github.com/{REPO}"
RAW = f"https://raw.githubusercontent.com/{REPO}/main"
SITE = "https://kydlikebtc.github.io/awesome-jev/"


# The taxonomy lives in patterns.json so build_readme, build_assets and the MCP
# server all read one copy. Three embedded copies was three chances to drift.
_PATTERNS = json.loads(PATTERNS_FILE.read_text())["patterns"]
PATTERN_ORDER = [p["key"] for p in _PATTERNS]
PATTERN_LABELS = {
    p["key"]: (p["en"], p["zh"], p["blurb_en"], p["blurb_zh"]) for p in _PATTERNS
}

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

# The handful of rows a newcomer should open, in reading order. Curated by hand
# because "most starred" is not the same as "read this first" — the limitations
# page has no stars at all and is the most useful page in the docs.
START_HERE = [
    "typesafe-quickstart",
    "typesafe-jaggedness",
    "example-three-primitives",
    "fast-jev-compaction",
    "ai-cookbook-jev-track",
    "hermes-agent-jev-evaluation",
]

# Patterns whose tables are long and mostly context rather than technique.
# Collapsed so the page stays scannable; still fully indexed and searchable.
COLLAPSE = {"overview"}

# The three primitives, rendered as a table rather than described in a
# paragraph. Every fact here is from the official API reference.
PRIMITIVES = [
    {
        "glyph": "◆",
        "name": "choice",
        "returns_en": "one option, plus `probabilities` and `confidence`",
        "returns_zh": "一个选项，附带 `probabilities` 和 `confidence`",
        "limit_en": "up to **255** options",
        "limit_zh": "最多 **255** 个选项",
        "for_en": "pick a tool, a route, a label",
        "for_zh": "选工具、选分支、选标签",
    },
    {
        "glyph": "▮",
        "name": "score",
        "returns_en": "a number, plus `legend`, `probabilities` and `confidence`",
        "returns_zh": "一个数值，附带 `legend`、`probabilities` 和 `confidence`",
        "limit_en": "**2–10** ordered levels, 0-indexed",
        "limit_zh": "**2–10** 个有序级别，从 0 开始",
        "for_en": "rank quality, risk, urgency",
        "for_zh": "给质量、风险、紧急度排序",
    },
    {
        "glyph": "◐",
        "name": "noul",
        "returns_en": "a 0–1 probability in `.noul` — **and no `confidence`**",
        "returns_zh": "`.noul` 里一个 0–1 概率 —— **且不带 `confidence`**",
        "limit_en": 'not called "binary" or "boolean"',
        "limit_zh": "它不叫 binary，也不叫 boolean",
        "for_en": "gate an action, keep or drop an item",
        "for_zh": "拦一个动作、留或弃一个条目",
    },
]

EN = {
    "lang_code": "en",
    "other_readme": "README.zh-CN.md",
    "other_name": "中文",
    "site_label": "Searchable site",
    "tagline": (
        "Every public example of Jev — TypeSafe AI's System One decision model — "
        "indexed by the decision it makes, not by the blog that mentioned it."
    ),
    "generated": "This file is generated from catalog.json. Edit the catalog, then run `python3 scripts/build_readme.py`.",
    "shot_alt": "The awesome-jev site: a coverage histogram down the left acting as the pattern filter, dense entry cards on the right",
    "shot_cap": 'Filter by clicking a bar. Two more views: <a href="https://kydlikebtc.github.io/awesome-jev/?view=prims">primitives</a> · <a href="https://kydlikebtc.github.io/awesome-jev/?view=compat">compatibility</a>. Every filter and entry is a shareable URL.',
    # ---- what this is ----
    "about_h": "What this is",
    "about_rows": [
        (
            "**Jev** is a decision model from TypeSafe AI. It does not write text — you hand it "
            "state plus typed questions and it returns typed answers with calibrated confidence, "
            "fast and cheap enough to sit in an agent's inner loop.",
        ),
        (
            "**This repo** indexes public examples of using it, organised by the *decision* being "
            "made. The resource you read this week is disposable; the decision pattern is not.",
        ),
        (
            "**Why trust it:** every row names where it came from, says which primitives the code "
            "actually calls, and flags what a reader deserves to know before clicking. "
            "There are dozens of Jev lists — this one competes on verification, not on size.",
        ),
    ],
    "about_not": (
        "Not the product, not an SDK, not affiliated with TypeSafe AI, and not a recommendation. "
        "A row means the link resolved and a person read it — nothing more. "
        "See [what is verified](#what-is-verified-and-what-is-not)."
    ),
    # ---- primitives ----
    "prims_h": "What Jev returns",
    "prims_intro": (
        "Three primitives. Every pattern below is built out of them, and the asymmetry in the last "
        "row is the single most common source of bugs."
    ),
    "th_prim": "Primitive",
    "th_returns": "Returns",
    "th_limit": "Limits",
    "th_for": "Used for",
    "prims_after": (
        "Input is **text only** — string, JSON object, or array of text. Context is **64k** tokens "
        "per request, **32k** for the state plus the longest question. Output tokens are free. "
        "There are no published weights, so it cannot be run locally. "
        "Full cross-platform differences: [`docs/compatibility.md`](docs/compatibility.md)."
    ),
    # ---- sections ----
    "l_patterns": "Patterns",
    "l_compat": "Compatibility",
    "l_vetting": "Vetting",
    "cov_alt": "Horizontal bar chart of how many catalog examples exist for each of the eighteen decision patterns",
    "prim_alt": "Three panels describing the choice, score and noul primitives and what each returns",
    "coverage_after": "Two patterns have no examples yet. Both are plausible fits nobody appears to have published — see [`docs/status.md`](docs/status.md).",
    "start_h": "Start here",
    "start_intro": 'Six things in reading order. Hand-picked, because "most starred" is not the same as "read this first".',
    "th_why_read": "Why this one",
    "coverage_h": "Coverage",
    "coverage_intro": (
        "Every decision pattern, sized by how many examples exist. This doubles as the index — "
        "the names link to the sections below. A zero is a research gap, not a rendering bug."
    ),
    "measured_h": "Measured, not claimed",
    "measured_intro": (
        "Almost every performance number circulating about this model is the vendor's own, produced "
        "with reference answers derived from other models' judgements rather than human ground truth. "
        "These are the independent measurements in the catalog — several are **negative results**, "
        "which is exactly why they are worth reading first."
    ),
    "patterns_h": "By decision pattern",
    "patterns_intro": (
        "The primary index. Each heading is a decision an agent has to make; the rows are examples "
        "of making it. Caveats appear as short tags — the full note for each row is in "
        "[`catalog.json`](catalog.json) and on [the site]({site})."
    ),
    "kinds_h": "By resource kind",
    "kinds_intro": "The same rows grouped by what you will find when you open the link.",
    "th_find": "What you will find",
    "repo_h": "Also in this repo",
    "repo_intro": "The parts that are not the catalog.",
    "th_file": "File",
    "th_what": "What it is",
    "verified_h": "What is verified, and what is not",
    "stat_rechecked": "claims re--checked",
    "verified_recheck": (
        "**Re-checked weekly** — {n} rows record the file their primitive claim was read in. "
        "A scheduled job re-reads each one from the repository's default branch and opens an "
        "issue if the claim stopped holding, so an upstream removal cannot leave a false claim "
        "sitting here. Deliberately unpinned to a commit: pinning would verify a historical "
        "snapshot forever."
    ),
    "verified_yes": (
        "**Verified** — the URL returned a success status on the date in `checked`; a person opened "
        "it and wrote the summary from what was there; for code rows the call site was read to "
        "confirm which primitives are used; stars and licences came from the GitHub API."
    ),
    "verified_no": (
        "**Not verified** — whether the code runs, whether any performance claim holds, whether a "
        "project is maintained, or whether any of this suits your system. Nothing here has been "
        "executed, load-tested or security-reviewed."
    ),
    "verified_flags_h": "What the tags mean",
    "th_tag": "Tag",
    "th_means": "Means",
    "data_h": "Machine-readable data",
    "data_intro": "One entry per example, validated against a JSON Schema on every push.",
    "contrib_h": "Contributing and licence",
    "contrib_body": (
        "Corrections take priority over additions — a wrong row costs more than a missing one. "
        "See [CONTRIBUTING.md](CONTRIBUTING.md); the bar is *could a reader act on this row without "
        "opening the link?*"
    ),
    "license_body": (
        "Code in `scripts/`, `site/` and `examples/` is [MIT](LICENSE-MIT). Catalog metadata is "
        "[CC0-1.0](LICENSE-CC0), with a per-row `license` field. Linked works keep their own "
        "licences — `repo_license` records what each declares."
    ),
    # ---- table headers ----
    "th_example": "Example",
    "th_shows": "What it shows",
    "th_kind": "Kind",
    "th_code": "Code",
    "th_caveats": "Caveats",
    "th_pattern": "Pattern",
    "th_count": "Examples",
    "no_entries": "_No entries yet._",
    "retired_h": "Retired links",
    "retired_intro": "Links that stopped resolving, kept so a dead reference stays searchable instead of vanishing.",
    "th_why": "Why",
    "collapse": "rows — click to expand",
    "gap": "no examples yet",
    # ---- stats ----
    "stat_entries": "entries",
    "stat_with_code": "with code",
    "stat_official": "official",
    "stat_verified": "link-verified",
    "stat_patterns": "patterns",
    "stat_retired": "retired",
}

ZH = {
    "lang_code": "zh",
    "other_readme": "README.md",
    "other_name": "English",
    "site_label": "可搜索站点",
    "tagline": (
        "全网 Jev（TypeSafe AI 的 System One 决策模型）使用例子索引 —— "
        "按它做的**决策**归类，而不是按提到它的博客归类。"
    ),
    "generated": "本文件由 catalog.json 生成。请修改目录数据后运行 `python3 scripts/build_readme.py`。",
    "shot_alt": "awesome-jev 站点：左侧覆盖度直方图兼作模式筛选器，右侧是密集的条目卡片",
    "shot_cap": '点击条形即可筛选。另有两个视图：<a href="https://kydlikebtc.github.io/awesome-jev/?view=prims&lang=zh">三个原语</a> · <a href="https://kydlikebtc.github.io/awesome-jev/?view=compat&lang=zh">兼容性矩阵</a>。每个筛选条件和每个条目都是可分享的 URL。',
    "about_h": "这是什么",
    "about_rows": [
        (
            "**Jev** 是 TypeSafe AI 的决策模型。它不生成文本 —— 你给它状态和类型化问题，"
            "它返回带校准置信度的类型化答案，快且便宜到可以放进智能体的内层循环。",
        ),
        (
            "**本仓库**收集它的公开使用例子，按所做的**决策**组织。"
            "你这周读的那篇资料是一次性的，决策模式不是。",
        ),
        (
            "**凭什么可信：**每一行都写明来源、写明代码实际调用了哪些原语、"
            "并标出点开前该知道的事。Jev 的列表有几十个 —— 这一个竞争的是核实严谨度，不是收录数量。",
        ),
    ],
    "about_not": (
        "不是产品本身，不是 SDK，与 TypeSafe AI 无隶属关系，也不构成推荐。"
        "收录只意味着链接可访问、并且有人读过 —— 仅此而已。"
        "详见[哪些经过核实](#哪些经过核实哪些没有)。"
    ),
    "prims_h": "Jev 返回什么",
    "prims_intro": "三个原语。下面所有模式都由它们构成，而最后一行那个不对称是最常见的 bug 来源。",
    "th_prim": "原语",
    "th_returns": "返回",
    "th_limit": "限制",
    "th_for": "用来",
    "prims_after": (
        "输入**仅支持文本** —— 字符串、JSON 对象、或文本数组。上下文每次请求 **64k** token，"
        "其中 state 加最长的那个问题占 **32k**。输出 token 免费。"
        "权重未公开，因此无法本地运行。"
        "跨平台差异全表见 [`docs/compatibility.md`](docs/compatibility.md)。"
    ),
    "l_patterns": "决策模式",
    "l_compat": "兼容性",
    "l_vetting": "核查指南",
    "cov_alt": "十八个决策模式各有多少个目录条目的横向条形图",
    "prim_alt": "三个面板，分别说明 choice、score、noul 三个原语各自返回什么",
    "coverage_after": "有两个模式目前没有例子。两者都是合理的适用场景，只是还没人公开发表 —— 见 [`docs/status.md`](docs/status.md)。",
    "start_h": "从这里开始",
    "start_intro": "六条，按阅读顺序。手工挑选 —— 因为「star 最多」和「该先读哪个」不是一回事。",
    "th_why_read": "为什么是它",
    "coverage_h": "覆盖度",
    "coverage_intro": (
        "全部决策模式，按例子数量排列长度。这张表同时就是索引 —— 名称链接到下面对应章节。"
        "数字为 0 的是待补的研究缺口，不是渲染 bug。"
    ),
    "measured_h": "实测，而非宣称",
    "measured_intro": (
        "关于这个模型流传的性能数字几乎全是厂商自测，而且参考答案由其他模型的判断推导而来、"
        "不是人工 ground truth。下面这些是本目录里的独立实测 —— 其中几条是**负面结果**，"
        "这恰恰是它们值得先读的原因。"
    ),
    "patterns_h": "按决策模式",
    "patterns_intro": (
        "主索引。每个标题是智能体必须做的一个决策；下面的行是做这个决策的例子。"
        "警示以短标记呈现 —— 每行的完整备注在 [`catalog.json`](catalog.json) 和[站点]({site})里。"
    ),
    "kinds_h": "按资源形态",
    "kinds_intro": "同样这些行，按你点开链接后会看到什么来分组。",
    "th_find": "点开会看到",
    "repo_h": "本仓库还有什么",
    "repo_intro": "除目录数据之外的部分。",
    "th_file": "文件",
    "th_what": "是什么",
    "verified_h": "哪些经过核实，哪些没有",
    "stat_rechecked": "\u58f0\u660e\u53ef\u590d\u68c0",
    "verified_recheck": (
        "**每周复检** —— 有 {n} 行记录了其原语声明是在哪个文件里读到的。"
        "定时任务会从该仓库的默认分支重新读取，一旦声明不再成立就开 issue，"
        "因此上游把集成删掉了也不会留下一条假声明。刻意不锁 commit —— "
        "锁了就会永远在校验一个历史快照。"
    ),
    "verified_yes": (
        "**已核实** —— 该链接在 `checked` 日期返回成功状态；有人打开它、按页面实际内容写了摘要；"
        "含代码的行都读过调用处、确认了实际使用的原语；star 数与许可证来自 GitHub API。"
    ),
    "verified_no": (
        "**未核实** —— 代码能否跑通、任何性能宣称是否成立、项目是否仍在维护、"
        "以及这些做法是否适合你的系统。本仓库没有执行过、压测过或做过安全审计。"
    ),
    "verified_flags_h": "这些标记是什么意思",
    "th_tag": "标记",
    "th_means": "含义",
    "data_h": "机器可读数据",
    "data_intro": "每个例子一条记录，每次推送都按 JSON Schema 校验。",
    "contrib_h": "参与贡献与许可",
    "contrib_body": (
        "纠错优先于新增 —— 一个错的条目比一个缺失的条目代价更大。"
        "详见 [CONTRIBUTING.md](CONTRIBUTING.md)；收录标准是：*读者不点开链接，能否据此行动？*"
    ),
    "license_body": (
        "`scripts/`、`site/`、`examples/` 中的代码采用 [MIT](LICENSE-MIT)。"
        "目录元数据采用 [CC0-1.0](LICENSE-CC0)，并带逐行 `license` 字段。"
        "被链接的作品各自保留原许可 —— `repo_license` 记录了各自声明的内容。"
    ),
    "th_example": "例子",
    "th_shows": "展示了什么",
    "th_kind": "形态",
    "th_code": "代码",
    "th_caveats": "警示",
    "th_pattern": "模式",
    "th_count": "例子数",
    "no_entries": "_暂无条目。_",
    "retired_h": "已退休的链接",
    "retired_intro": "已无法访问的链接。保留下来，让失效的引用仍可被搜索到，而不是凭空消失。",
    "th_why": "原因",
    "collapse": "条 —— 点击展开",
    "gap": "暂无例子",
    "stat_entries": "条目",
    "stat_with_code": "含代码",
    "stat_official": "官方",
    "stat_verified": "链接已核实",
    "stat_patterns": "覆盖模式",
    "stat_retired": "已退休",
}


KIND_LABELS = {
    "official-docs": (
        "Official docs",
        "官方文档",
        "Vendor documentation, cookbooks and pattern pages.",
        "厂商文档、cookbook 与模式页。",
    ),
    "sdk": (
        "SDK",
        "SDK",
        "Client libraries, official and community.",
        "客户端库，官方与社区。",
    ),
    "integration": (
        "Integration",
        "平台集成",
        "A gateway, framework or platform route to the model.",
        "接入模型的网关、框架或平台路径。",
    ),
    "snippet": (
        "Snippet",
        "代码片段",
        "Small runnable examples in this repository.",
        "本仓库内的小型可运行样例。",
    ),
    "project": (
        "Project",
        "开源项目",
        "An application or library that calls Jev in anger.",
        "真正在调用 Jev 的应用或库。",
    ),
    "plugin": (
        "Plugin",
        "插件",
        "Editor, agent and MCP integrations you can install.",
        "可安装的编辑器、智能体、MCP 集成。",
    ),
    "tutorial": (
        "Tutorial",
        "教程",
        "Step-by-step material with code.",
        "带代码的分步教学材料。",
    ),
    "case-study": (
        "Case study",
        "落地案例",
        "An account of running it in production.",
        "在生产环境跑它的实录。",
    ),
    "benchmark": (
        "Benchmark",
        "基准测试",
        "Measurement. Check whether it is independent or vendor-reported.",
        "实测。注意区分独立实测与厂商自报。",
    ),
    "article": (
        "Article",
        "文章",
        "Explainers, analysis and launch coverage.",
        "讲解、分析与发布报道。",
    ),
    "video": ("Video", "视频", "Walkthroughs and reviews.", "演示与评测。"),
    "discussion": (
        "Discussion",
        "讨论",
        "Threads worth reading, including the sceptical ones.",
        "值得读的讨论，包括质疑的声音。",
    ),
    "alternative": (
        "Jev-like alternative",
        "Jev 替代实现",
        "Independent reimplementations. These do NOT call Jev.",
        "独立复现实现。它们**不**调用 Jev。",
    ),
}

FLAG_LABELS = {
    "not-jev": (
        "not Jev",
        "并非 Jev",
        "Does not call Jev at all. A compatible API does not imply compatible calibration, so thresholds do not transfer.",
        "完全不调用 Jev。协议兼容不等于校准兼容，所以阈值不能迁移。",
    ),
    "shadow-mode-only": (
        "shadow mode",
        "仅影子运行",
        "Wired in but deliberately inert — nothing it returns reaches a user-visible decision.",
        "接进去了但故意不生效 —— 它返回的东西不会进入任何对用户可见的决策。",
    ),
    "early-access-required": (
        "early access",
        "需早期访问",
        "Needs waitlist access to run.",
        "需要通过等候名单才能运行。",
    ),
    "code-untested": (
        "code untested",
        "代码未实测",
        "The code was read, not executed.",
        "代码是读过的，没有实际运行。",
    ),
    "single-commit": (
        "one commit",
        "仅一次提交",
        "One commit, so maintenance is unlikely.",
        "只有一次提交，基本不会有维护。",
    ),
    "no-license": (
        "no licence",
        "无许可证",
        "No LICENSE file, whatever a README badge claims. A blocker for reuse.",
        "没有 LICENSE 文件，不管 README 徽章怎么写。复用时这是硬障碍。",
    ),
    "third-party-api-key": (
        "3rd-party key",
        "需第三方密钥",
        "Needs a key for a service other than TypeSafe.",
        "需要 TypeSafe 之外某个服务的密钥。",
    ),
    "vendor-reported": (
        "vendor numbers",
        "厂商自报",
        "Repeats the vendor's own benchmarks rather than an independent measurement.",
        "照搬厂商自测数据，不是独立实测。",
    ),
    "unverified-claims": (
        "unverified",
        "宣称未核实",
        "Makes measurement claims that could not be checked.",
        "做出了无法核实的量化宣称。",
    ),
    "ai-generated": (
        "AI-written",
        "疑似 AI 生成",
        "Reads as machine-generated content.",
        "读起来像机器生成的内容。",
    ),
    "marketing": (
        "marketing",
        "营销内容",
        "Published to sell something as much as to explain.",
        "发布目的既是讲解也是推销。",
    ),
    "paywalled": (
        "paywall",
        "付费墙",
        "Behind a paywall or a metered reader.",
        "有付费墙或阅读次数限制。",
    ),
    "archived": (
        "archived",
        "已归档",
        "Development has visibly stopped.",
        "开发明显已经停止。",
    ),
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

# The non-catalog parts of the repo, so navigation is a table rather than a
# scattering of inline links the reader has to hunt for.
REPO_FILES = [
    (
        "docs/patterns.md",
        "Every pattern defined, each with an explicit *when NOT to use this*.",
        "逐个定义每个模式，并明确写出**什么时候不该用它**。",
    ),
    (
        "docs/compatibility.md",
        "Model string, field names, request shape, endpoint and env var differ per platform. This is that table.",
        "模型串、字段名、请求结构、端点、环境变量 —— 每个平台都不一样。这就是那张对照表。",
    ),
    (
        "docs/vetting.md",
        "What to check before trusting a row, and the one mistake most people make.",
        "信任一个条目之前该检查什么，以及大多数人会犯的那一个错。",
    ),
    (
        "docs/status.md",
        "What week one of this ecosystem actually looked like, gaps included.",
        "这个生态第一周的真实样貌，包括缺口。",
    ),
    (
        "docs/method.md",
        "How the catalog was built, what was excluded, and where it is weakest.",
        "目录是如何建起来的、排除了什么、以及它最弱的地方在哪。",
    ),
    (
        "docs/sources.md",
        "Where every row came from, and the licence position.",
        "每一行的来源，以及许可状况。",
    ),
    (
        "examples/",
        "Four runnable examples. One deliberately leaves the threshold policy to you.",
        "四个可运行样例。其中一个刻意把阈值策略留给你写。",
    ),
    (
        "schema/entry.schema.json",
        "What a catalog entry may contain.",
        "一条目录记录允许包含什么。",
    ),
    (
        "mcp/",
        "An MCP server, so an agent can query the catalogue instead of reading it. Caveats travel with every result.",
        "一个 MCP server —— 让智能体可以查询目录而不是阅读它。每条结果都带着它的警示一起返回。",
    ),
    (
        "SKILL.md",
        "An agent skill: the facts that generated Jev code most often gets wrong, and the design rules worth following.",
        "一份 agent 技能：生成的 Jev 代码最常搞错的那些事实，以及值得遵循的设计规则。",
    ),
    (
        "scripts/verify_claims.py",
        "Re-reads every cited call site weekly, so a primitive claim is checkable rather than asserted.",
        "每周重读每一处被引用的调用点 —— 让原语声明可核实，而不只是被断言。",
    ),
    (
        "scripts/refresh_metadata.py",
        "Re-reads stars, licences and archive status from the GitHub API and opens a PR.",
        "从 GitHub API 重新读取 star、许可证与归档状态，并开 PR。",
    ),
]


def esc(text: str) -> str:
    """Escape what would break a markdown table cell."""
    return text.replace("|", "\\|").replace("\n", " ").strip()


def bar(count: int, peak: int, width: int = 16) -> str:
    """A proportional bar from block characters.

    The coverage index is the site's histogram rendered in markdown, so the two
    surfaces tell the same story. Eighths give sub-character resolution, which
    matters when the long tail is 1 or 2 rows against a peak of 53.
    """
    if count <= 0:
        return ""
    units = count / peak * width
    full = int(units)
    eighths = " ▏▎▍▌▋▊▉"
    step = round((units - full) * 8)
    return ("█" * full + (eighths[step] if step else "")) or "▏"


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
    index = field + (1 if lang == "zh" else 0)
    if index >= len(entry):
        raise KeyError(f"label {key!r} has no field {field} for language {lang!r}")
    return entry[index]


def summary_of(entry: dict, lang: str) -> str:
    text = entry["summary_zh"] if lang == "zh" else entry["summary"]
    if lang == "zh" and entry.get("zh_machine"):
        text += " <sub>(机翻)</sub>"
    return esc(text)


def flags_of(entry: dict, lang: str) -> str:
    tags = [
        f"`{label(FLAG_LABELS, flag, lang)}`"
        for flag in FLAG_ORDER
        if flag in entry.get("flags", [])
    ]
    return " ".join(tags) if tags else "—"


def sort_key(entry: dict) -> tuple:
    """Official first, then rows with code, then stars, then title."""
    return (
        not entry.get("official", False),
        not entry.get("has_code", False),
        -(entry.get("stars") or 0),
        entry["title"].lower(),
    )


def entry_list(entries: list[dict], strings: dict, *, notes: bool = False) -> list[str]:
    """Render rows as a list rather than a table.

    Tables lose here. GitHub sizes columns by content, so with 148 rows the
    title column gets squeezed until names wrap onto three lines while the
    summary column hogs the width — measured at a 61px median row height and a
    46px title column. A list has no columns to fight over: one line of title
    and summary, one dim line of signals, and long titles simply wrap normally.

    `notes=True` adds the full note as a third line, for the curated sections
    where there are a handful of rows and the note is why the row is there.
    """
    lang = strings["lang_code"]
    if not entries:
        return [strings["no_entries"], ""]

    lines = []
    for entry in sorted(entries, key=sort_key):
        head = f"- **[{esc(entry['title'])}]({entry['url']})**"
        if entry.get("official"):
            head += " ⭐"
        lines.append(f"{head} — {summary_of(entry, lang)}")

        # Signals go on a dim second line: kind, popularity, author, language,
        # primitives, then caveats last so they read as the final word.
        bits = [f"`{label(KIND_LABELS, entry['kind'], lang)}`"]
        if entry.get("stars") is not None:
            bits.append(f"★{entry['stars']:,}")
        if entry.get("author"):
            bits.append(esc(entry["author"]["name"]))
        for item in entry.get("languages", []):
            bits.append(f"`{LANG_LABELS.get(item, item)}`")
        for item in entry.get("question_types", []):
            bits.append(f"`{item}`")
        flags = [
            f"`{label(FLAG_LABELS, flag, lang)}`"
            for flag in FLAG_ORDER
            if flag in entry.get("flags", [])
        ]
        if flags:
            bits.append("⚠ " + " ".join(flags))
        lines.append(f"  <sub>{' · '.join(bits)}</sub>")

        if notes:
            note = entry.get("notes_zh" if lang == "zh" else "notes")
            if note:
                lines.append(f"  <sub>{esc(note)}</sub>")
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
    by_slug = {entry["slug"]: entry for entry in catalog}

    live_patterns = [key for key in PATTERN_ORDER if by_pattern[key]]
    live_kinds = [key for key in KIND_ORDER if by_kind[key]]
    with_code = sum(1 for entry in catalog if entry.get("has_code"))
    official = sum(1 for entry in catalog if entry.get("official"))
    verified = sum(
        1 for entry in catalog if 200 <= (entry.get("link_status") or 0) < 300
    )
    # Rows whose primitive claim cites a file a machine can re-read weekly.
    # This number is the difference between asserting verification and having it.
    rechecked = sum(1 for entry in catalog if entry.get("evidence"))

    # ---- header ----
    add("<!--")
    add(f"  {strings['generated']}")
    add("-->")
    add("")
    add('<div align="center">')
    add("")
    add("# awesome-jev")
    add("")
    add(f"**{strings['tagline']}**")
    add("")
    add(
        f"[![lint]({REPO_URL}/actions/workflows/lint.yml/badge.svg)]({REPO_URL}/actions/workflows/lint.yml) "
        f"[![links]({REPO_URL}/actions/workflows/links.yml/badge.svg)]({REPO_URL}/actions/workflows/links.yml) "
        f"[![entries](https://img.shields.io/badge/{strings['stat_entries']}-{len(catalog)}-f5a524?style=flat-square)]({SITE}) "
        f"[![verified](https://img.shields.io/badge/{strings['stat_verified'].replace(' ', '%20').replace('-', '--')}-{verified}-3fb950?style=flat-square)]({SITE}) "
        f"[![rechecked](https://img.shields.io/badge/{strings['stat_rechecked'].replace(' ', '%20')}-{rechecked}-58a6ff?style=flat-square)]({REPO_URL}/actions/workflows/claims.yml) "
        "[![data](https://img.shields.io/badge/data-CC0--1.0-8b949e?style=flat-square)](LICENSE-CC0) "
        "[![code](https://img.shields.io/badge/code-MIT-8b949e?style=flat-square)](LICENSE-MIT)"
    )
    add("")
    add(
        f"[{strings['site_label']}]({SITE}) &nbsp;·&nbsp; "
        f"[{strings['other_name']}]({strings['other_readme']}) &nbsp;·&nbsp; "
        f"[{strings['l_patterns']}](docs/patterns.md) &nbsp;·&nbsp; "
        f"[{strings['l_compat']}](docs/compatibility.md) &nbsp;·&nbsp; "
        f"[{strings['l_vetting']}](docs/vetting.md)"
    )
    add("")
    shot = "site-chinese.png" if lang == "zh" else "site-desktop.png"
    add(
        f'<a href="{SITE}"><img src="docs/screenshots/{shot}" '
        f'alt="{strings["shot_alt"]}" width="760"></a>'
    )
    add("")
    add(f"<sub>{strings['shot_cap']}</sub>")
    add("")
    add("</div>")
    add("")
    add("---")
    add("")

    # ---- what this is ----
    add(f"## {strings['about_h']}")
    add("")
    for (line,) in strings["about_rows"]:
        add(f"- {line}")
    add("")
    add(f"> ⚠️ {strings['about_not']}")
    add("")

    # ---- primitives, as a generated figure ----
    add(f"## {strings['prims_h']}")
    add("")
    add(strings["prims_intro"])
    add("")
    add("<picture>")
    add(
        f'  <source media="(prefers-color-scheme: dark)" '
        f'srcset="docs/assets/primitives-{lang}-dark.svg">'
    )
    add(
        f'  <img src="docs/assets/primitives-{lang}-light.svg" '
        f'alt="{strings["prim_alt"]}" width="660">'
    )
    add("</picture>")
    add("")
    add(strings["prims_after"])
    add("")

    # ---- start here ----
    add(f"## {strings['start_h']}")
    add("")
    add(strings["start_intro"])
    add("")
    for index, slug in enumerate(START_HERE, 1):
        entry = by_slug.get(slug)
        if entry is None:
            raise KeyError(
                f"START_HERE names {slug!r}, which is not in catalog.json. Update the list in "
                "build_readme.py when a curated row is renamed or removed."
            )
        why = entry.get("notes_zh" if lang == "zh" else "notes") or summary_of(
            entry, lang
        )
        # An ordered list: a table squeezed the title column until names wrapped.
        add(f"{index}. **[{esc(entry['title'])}]({entry['url']})**")
        add(f"   <sub>{esc(why)}</sub>")
        add("")

    # ---- coverage: a generated figure, not block characters ----
    add(f"## {strings['coverage_h']}")
    add("")
    add(strings["coverage_intro"])
    add("")
    add("<picture>")
    add(
        f'  <source media="(prefers-color-scheme: dark)" '
        f'srcset="docs/assets/coverage-{lang}-dark.svg">'
    )
    add(
        f'  <img src="docs/assets/coverage-{lang}-light.svg" '
        f'alt="{strings["cov_alt"]}" width="100%">'
    )
    add("</picture>")
    add("")
    add(strings["coverage_after"])
    add("")

    # ---- measured results: the differentiator, surfaced early ----
    measured = [
        entry
        for entry in catalog
        if entry["kind"] == "benchmark"
        and "vendor-reported" not in entry.get("flags", [])
    ]
    if measured:
        add(f"## {strings['measured_h']}")
        add("")
        add(strings["measured_intro"])
        add("")
        out.extend(entry_list(measured, strings, notes=True))

    # ---- by pattern ----
    add(f"## {strings['patterns_h']}")
    add("")
    add(strings["patterns_intro"].replace("{site}", SITE))
    add("")
    for key in live_patterns:
        name = label(PATTERN_LABELS, key, lang)
        blurb = label(PATTERN_LABELS, key, lang, field=2)
        rows = by_pattern[key]
        add(f"### {name}")
        add("")
        add(f"_{blurb}_")
        add("")
        if key in COLLAPSE:
            add("<details>")
            add(f"<summary><b>{len(rows)}</b> {strings['collapse']}</summary>")
            add("")
            out.extend(entry_list(rows, strings))
            add("</details>")
            add("")
        else:
            out.extend(entry_list(rows, strings))

    # ---- by kind, as a table with its own bars ----
    add(f"## {strings['kinds_h']}")
    add("")
    add(strings["kinds_intro"])
    add("")
    kind_peak = max((len(by_kind[key]) for key in KIND_ORDER), default=1) or 1
    add(
        f"| {strings['th_kind'] if 'th_kind' in strings else 'Kind'} | {strings['th_count']} | {strings['th_find']} |"
    )
    add("| --- | :-- | --- |")
    for key in live_kinds:
        count = len(by_kind[key])
        add(
            f"| **{label(KIND_LABELS, key, lang)}** | `{count:>2}` {bar(count, kind_peak)} "
            f"| {esc(label(KIND_LABELS, key, lang, field=2))} |"
        )
    add("")

    # ---- the rest of the repo ----
    add(f"## {strings['repo_h']}")
    add("")
    add(strings["repo_intro"])
    add("")
    add(f"| {strings['th_file']} | {strings['th_what']} |")
    add("| --- | --- |")
    for path, what_en, what_zh in REPO_FILES:
        add(f"| [`{path}`]({path}) | {esc(what_zh if lang == 'zh' else what_en)} |")
    add("")

    # ---- verification ----
    add(f"## {strings['verified_h']}")
    add("")
    add(f"- ✅ {strings['verified_yes']}")
    add(f"- 🔁 {strings['verified_recheck'].replace('{n}', str(rechecked))}")
    add(f"- ❌ {strings['verified_no']}")
    add("")
    add(f"### {strings['verified_flags_h']}")
    add("")
    used_flags = [
        flag for flag in FLAG_ORDER if any(flag in e.get("flags", []) for e in catalog)
    ]
    add(f"| {strings['th_tag']} | {strings['th_means']} |")
    add("| --- | --- |")
    for flag in used_flags:
        add(
            f"| `{label(FLAG_LABELS, flag, lang)}` "
            f"| {esc(label(FLAG_LABELS, flag, lang, field=2))} |"
        )
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
            add(
                f"| {esc(entry['title'])} | {esc(why)}{f' `HTTP {status}`' if status else ''} |"
            )
        add("")

    # ---- data ----
    add(f"## {strings['data_h']}")
    add("")
    add(strings["data_intro"])
    add("")
    add(f"| {strings['th_file']} | {strings['th_what']} |")
    add("| --- | --- |")
    add(
        f"| [`catalog.json`]({RAW}/catalog.json) | {len(catalog)} {strings['stat_entries']} |"
    )
    add(
        f"| [`retired.json`]({RAW}/retired.json) | {len(retired)} {strings['stat_retired']} |"
    )
    add(
        f"| [`compat.json`]({RAW}/compat.json) | The platform matrix behind `docs/compatibility.md` |"
    )
    add(
        f"| [`patterns.json`]({RAW}/patterns.json) | The decision taxonomy both generators and the MCP server read |"
    )
    add(
        f"| [`schema/entry.schema.json`]({RAW}/schema/entry.schema.json) | One entry's shape |"
    )
    add(f"| [`llms.txt`]({RAW}/llms.txt) | For agents, with the caveats spelled out |")
    add("")

    # ---- contributing + licence ----
    add(f"## {strings['contrib_h']}")
    add("")
    add(strings["contrib_body"])
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
        print(
            "  top patterns: " + ", ".join(f"{k} {v}" for k, v in counts.most_common(5))
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
