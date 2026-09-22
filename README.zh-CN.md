<!--
  本文件由 catalog.json 生成。请修改目录数据后运行 `python3 scripts/build_readme.py`。
-->

# awesome-jev

[![lint](https://github.com/kydlikebtc/awesome-jev/actions/workflows/lint.yml/badge.svg)](https://github.com/kydlikebtc/awesome-jev/actions/workflows/lint.yml) [![links](https://github.com/kydlikebtc/awesome-jev/actions/workflows/links.yml/badge.svg)](https://github.com/kydlikebtc/awesome-jev/actions/workflows/links.yml) [![entries](https://img.shields.io/badge/条目-148-f5a524)](https://kydlikebtc.github.io/awesome-jev/) [![data: CC0-1.0](https://img.shields.io/badge/data-CC0--1.0-4ec97a)](LICENSE-CC0) [![code: MIT](https://img.shields.io/badge/code-MIT-5fb3d9)](LICENSE-MIT)

> 全网 Jev（TypeSafe AI 的 System One 决策模型）使用例子索引 —— 按它做的**决策**归类，而不是按提到它的博客归类。

**English** · [README.md](README.md) &nbsp;·&nbsp; **可搜索站点** · [kydlikebtc.github.io/awesome-jev/](https://kydlikebtc.github.io/awesome-jev/)

`148` 条目 &nbsp;·&nbsp; `124` 含代码 &nbsp;·&nbsp; `36` 官方 &nbsp;·&nbsp; `144` 链接已核实 &nbsp;·&nbsp; `16/18` 覆盖模式 &nbsp;·&nbsp; `0` 已退休 &nbsp;·&nbsp; `2026-09-22`

<a href="https://kydlikebtc.github.io/awesome-jev/"><img src="docs/screenshots/site-chinese.png" alt="awesome-jev 站点：左侧覆盖度直方图兼作模式筛选器，右侧是密集的条目卡片" width="100%"></a>

<sub>站点左侧那个直方图就是筛选器 —— 每根条是一个决策模式，长度是该模式下的例子数量。站点还有两个参考视图：<a href="https://kydlikebtc.github.io/awesome-jev/?view=prims&lang=zh">三个原语</a> 和 <a href="https://kydlikebtc.github.io/awesome-jev/?view=compat&lang=zh">跨平台对照矩阵</a>。任何筛选条件、视图或单个条目都是可分享的 URL。</sub>

---

## 这是什么

- **Jev** 是 TypeSafe AI 的决策模型。它不生成文本 —— 你给它状态和类型化问题，它返回带校准置信度的类型化答案，快且便宜到可以放进智能体的内层循环。
- **本仓库**收集它的公开使用例子，按所做的**决策**组织。你这周读的那篇资料是一次性的，决策模式不是。
- **凭什么可信：**每一行都写明来源、写明代码实际调用了哪些原语、并标出点开前该知道的事。Jev 的列表有几十个 —— 这一个竞争的是核实严谨度，不是收录数量。

> ⚠️ 不是产品本身，不是 SDK，与 TypeSafe AI 无隶属关系，也不构成推荐。收录只意味着链接可访问、并且有人读过 —— 仅此而已。详见[哪些经过核实](#哪些经过核实哪些没有)。

## Jev 返回什么

三个原语。下面所有模式都由它们构成，而最后一行那个不对称是最常见的 bug 来源。

| | 原语 | 返回 | 限制 | 用来 |
| :-: | --- | --- | --- | --- |
| ◆ | **`choice`** | 一个选项，附带 `probabilities` 和 `confidence` | 最多 **255** 个选项 | 选工具、选分支、选标签 |
| ▮ | **`score`** | 一个数值，附带 `legend`、`probabilities` 和 `confidence` | **2–10** 个有序级别，从 0 开始 | 给质量、风险、紧急度排序 |
| ◐ | **`noul`** | `.noul` 里一个 0–1 概率 —— **且不带 `confidence`** | 它不叫 binary，也不叫 boolean | 拦一个动作、留或弃一个条目 |

输入**仅支持文本** —— 字符串、JSON 对象、或文本数组。上下文每次请求 **64k** token，其中 state 加最长的那个问题占 **32k**。输出 token 免费。权重未公开，因此无法本地运行。跨平台差异全表见 [`docs/compatibility.md`](docs/compatibility.md)。

## 从这里开始

六条，按阅读顺序。手工挑选 —— 因为「star 最多」和「该先读哪个」不是一回事。

| | 例子 | 为什么是它 |
| :-: | --- | --- |
| `1` | **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** | 官方第一课：一条工单，一次请求里同时问一个 Choice、一个 Score 和一个 Noul，给了 Python / JS / cURL 三种写法。 |
| `2` | **[Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)** | 官方文档里最有用、却最少被引用的一页。它还解释了一件事：对选项做一个 Choice，和每个选项各问一个 Noul，问的根本不是同一个问题。 |
| `3` | **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)** | 按官方 API 参考编写并逐字段对照核实，但未针对线上 API 实际执行过。 |
| `4` | **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | 每次工具调用恰好两个 noul：知道这次调用发生过是否还有意义、以及是否还需要完整原文输出。尽管它自己的描述里用了「打分」，实际并未使用 score 原语。 |
| `5` | **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** | 找到的最好的结构化教程。它明确指出类型化输出不保证决策正确、列出了官方记录的弱项，并且对自己给出的成本示例做了限定而不是拿来营销。 |
| `6` | **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)** | 本目录可信度最高的一条。召回率低于他们现有的摘要器，在相同上下文预算下与「按时间倒序」打平。成本确实低得多。在一个被热炒的模型上公开负面结果，非常少见。 |

## 覆盖度

全部决策模式，按例子数量排列长度。这张表同时就是索引 —— 名称链接到下面对应章节。数字为 0 的是待补的研究缺口，不是渲染 bug。

| 模式 | 例子数 | 展示了什么 |
| --- | :-- | --- |
| **[工具选择](#工具选择)** | `25` ███████▌ | 智能体下一步该调用哪个工具或动作。 |
| **[意图路由](#意图路由)** | `20` ██████ | 判断用户意图，把请求分流到正确的分支。 |
| **[上下文压缩](#上下文压缩)** | ` 6` █▊ | 判断哪些工具调用和结果仍然相关，从而丢弃过期上下文。 |
| **[安全闸门](#安全闸门)** | `13` ███▉ | 在执行前判断一个动作是否安全。属纵深防御，绝不是安全边界。 |
| **[输出校验](#输出校验)** | ` 7` ██▏ | 在输出到达用户前，按评分标准检查模型产出。 |
| 重试控制 | `0` &nbsp;·&nbsp; _暂无例子_ | 判断失败的步骤是否值得重试。 |
| **[人工升级](#人工升级)** | `15` ████▌ | 用校准置信度决定哪些情况必须由人来看。 |
| **[模型路由](#模型路由)** | `10` ███ | 选择由哪个下游模型或档位处理请求。 |
| **[并行扇出](#并行扇出)** | `14` ████▎ | 把大量问题（包括推测性的）打包进一次请求，再由代码挑出真正用得上的答案。 |
| **[检索与排序](#检索与排序)** | `15` ████▌ | 对来自廉价检索步骤的候选做打分或重排。 |
| **[结构化抽取](#结构化抽取)** | ` 4` █▎ | 从杂乱文本中取出类型化字段 —— 靠在候选中选择，而不是生成。 |
| **[分类](#分类)** | `18` █████▍ | 把条目归入分类体系，包括用概率遍历的深层层级。 |
| **[机器学习特征抽取](#机器学习特征抽取)** | ` 3` ▉ | 把自由文本转成数值特征，喂给下游的传统模型。 |
| **[文档分拣](#文档分拣)** | ` 1` ▎ | 对进来的文档、发票、表单做分类和路由。 |
| **[工单分拣](#工单分拣)** | ` 7` ██▏ | 按意图和紧急度路由支持工单与会话。 |
| **[内容评分](#内容评分)** | `15` ████▌ | 在有序量表上给质量、风险或相关性打分。 |
| 实时推荐 | `0` &nbsp;·&nbsp; _暂无例子_ | 选择下一步呈现什么，快到能用在实时会话里。 |
| **[总览](#总览)** | `53` ████████████████ | 介绍模型或整个领域，而非单一模式。 |

## 实测，而非宣称

关于这个模型流传的性能数字几乎全是厂商自测，而且参考答案由其他模型的判断推导而来、不是人工 ground truth。下面这些是本目录里的独立实测 —— 其中几条是**负面结果**，这恰恰是它们值得先读的原因。

| 例子 | 展示了什么 | 代码 | 警示 |
| --- | --- | :-- | :-- |
| **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)**<br><sub>基准测试 · ★247,803</sub> | 把 Jev 压缩方案移植过来，与自家在用的摘要器对比实测，最后公开结论：不采用。<br><sub>本目录可信度最高的一条。召回率低于他们现有的摘要器，在相同上下文预算下与「按时间倒序」打平。成本确实低得多。在一个被热炒的模型上公开负面结果，非常少见。</sub> | `Py`<br><sub>noul</sub> | — |
| **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)**<br><sub>基准测试 · ★87,175</sub> | 用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。<br><sub>接进去了但故意不生效：按他们自己的说法，Jev 返回的任何东西都不会进入标签、缓存行或告警。带黄金测试集。想在不拿生产环境下注的前提下试新模型，这是值得照抄的做法。</sub> | `TS`<br><sub>choice</sub> | `仅影子运行` |
| **[no-mistakes: review context selection](https://github.com/kunchenguid/no-mistakes)**<br><sub>基准测试 · ★8,595</sub> | 对每个候选文件打一个 Score 来挑选审查上下文；实测结果是：计费输入明显增加，而实际耗时几乎没改善。<br><sub>他们自己的建议是：这个功能保持可选、默认关闭、不要宣传省钱。诚实的实测就该长这样。</sub> | `Go`<br><sub>score</sub> | — |
| **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)**<br><sub>基准测试 · ★190</sub> | 独立的韩语实测笔记，报告仅仅把选项顺序倒过来，就能让概率移动到足以翻转 0.9 阈值的程度。<br><sub>在所有资料里找到的最具操作价值的工程警示：如果仅仅选项顺序就能把概率推过你的阈值，那你的阈值没有看上去那么稳。这是独立且未被复现的结果，具体幅度请当作指示性数据。</sub> | `Py` | `无许可证` `宣称未核实` |
| **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)**<br><sub>基准测试 · Lindfors</sub> | 找到的最好的独立实测：固定单一模型版本、24 份挪威语文档，开篇就展示了一个模型答错、但同时正确报出低置信度的案例。<br><sub>方法论交代干净，并诚实限定为「单日快照」。开篇就摆失败案例，这才让它成为真正的校准检验，而不是一篇软文。</sub> | — | — |
| **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)**<br><sub>基准测试 · Near Here</sub> | 找到的唯一三方横评，每个模型分别调过提示词，且明确把范围限定在单一任务上、不做通用排名。<br><sub>自我限定很规范：这是用例研究，不是模型排行榜。这种克制比数字本身更少见。</sub> | — | — |

## 按决策模式

主索引。每个标题是智能体必须做的一个决策；下面的行是做这个决策的例子。警示以短标记呈现 —— 每行的完整备注在 [`catalog.json`](catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/)里。

### 工具选择

_智能体下一步该调用哪个工具或动作。_

| 例子 | 展示了什么 | 代码 | 警示 |
| --- | --- | :-- | :-- |
| **[Cookbook: Function calling](https://docs.typesafe.ai/cookbooks/function_calling)** ⭐<br><sub>官方文档</sub> | 把自然语言的交易请求映射到普通的类型化函数：函数名和有限取值的参数各自变成一个带置信度的问题。 | `Py`<br><sub>choice</sub> | — |
| **[Cookbook: Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion)** ⭐<br><sub>官方文档</sub> | 为智能体的一轮对话从 182 个技能里最多挑一个：第一次请求给所有技能排序并顺便问「这轮到底需不需要技能」，第二次细读前三名。 | `Py`<br><sub>choice noul</sub> | — |
| **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐<br><sub>官方文档</sub> | 一个可运行的智能家居助手示例，用类型化决策来解析用户请求。 | `Py` | — |
| **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)**<br><sub>插件 · ★30,896</sub> | 三个可独立安装的 Claude Code 插件 —— 护栏、模型路由、技能推荐 —— 各自带 hook 和测试。 | `Py` `TS`<br><sub>choice score noul</sub> | — |
| **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)**<br><sub>开源项目 · ★30,278</sub> | 把工具目录编译成问题，再从答案还原出 tool call，并为「弃权」和「需确认」两种情况定义了专门的错误类型。 | `Py`<br><sub>choice</sub> | — |
| **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)**<br><sub>开源项目 · ★27,847</sub> | 两段式 MCP 工具检索：先用一个宽 Choice 对整个目录粗排，再给候选短名单配完整描述，每个候选各配一个 Noul 判断它到底是否胜任。 | `Py`<br><sub>choice noul</sub> | — |
| **[Cua driver: jev-use example](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use)**<br><sub>开源项目 · ★25,737</sub> | Python 与 TypeScript 双实现的 computer-use 动作选择：Jev 从不可变候选集里挑下一个浏览器动作，保留 reobserve 和 abstain 两个特殊选项。 | `Py` `TS`<br><sub>choice</sub> | — |
| **[json-render](https://github.com/vercel-labs/json-render)**<br><sub>开源项目 · ★17,964 · Vercel Labs</sub> | Vercel Labs 的生成式 UI 框架。实验里 Jev 不逐 token 写 JSON，只负责选组件、属性和布局。 | `TS`<br><sub>choice</sub> | — |
| **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)**<br><sub>开源项目 · ★16,069 · Browser Use</sub> | Browser Use 做的高速浏览器 Agent。Jev 每一步只判断「做什么、点哪个元素」，要打字才叫小模型。 | `Py`<br><sub>choice</sub> | `厂商自报` |
| **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)**<br><sub>开源项目 · ★6,338</sub> | 从三个维度审查每次工具调用：风险等级、用户是否授权、以及一个显式的提示注入压力检查。 | `TS`<br><sub>choice noul</sub> | — |
| **[jev-trader](https://github.com/jarrodwatts/jev-trader)**<br><sub>开源项目 · ★1,871</sub> | 在 Monad 测试网上做高频做市。Jev 根据价差和成交方向判断下一步买还是卖。 | `TS`<br><sub>choice</sub> | `宣称未核实` |
| **[agent-desktop](https://github.com/lahfir/agent-desktop)**<br><sub>开源项目 · ★1,436</sub> | 桌面自动化。读系统无障碍树，判断下一步该点哪个按钮、菜单或输入框。 | `Rs`<br><sub>choice</sub> | — |
| **[Jev-cu](https://github.com/Sac-Y/Jev-cu)**<br><sub>开源项目 · ★547</sub> | 一个 computer-use 智能体：判断该对无障碍树里哪个元素操作，并单独用一个 noul 判断这个动作是否需要用户显式确认。 | `JS`<br><sub>choice noul</sub> | `无许可证` |
| **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)**<br><sub>插件 · ★398</sub> | 九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。 | `Py`<br><sub>choice score noul</sub> | — |
| **[typesafe-mario](https://github.com/fhshaik/typesafe-mario)**<br><sub>开源项目 · ★336</sub> | 让 Jev 玩《超级马里奥》。不看截图，直接读模拟器 RAM 里的结构化状态，再决定跑、跳、躲。 | `Py`<br><sub>choice score noul</sub> | `代码未实测` `仅一次提交` `无许可证` |
| **[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)**<br><sub>开源项目 · ★212</sub> | 语音驱动的浏览器控制：目标选项每次请求都按当前实时元素列表重建，并且总是包含一个 none 选项。 | `JS`<br><sub>choice score noul</sub> | — |
| **[hyperedit](https://github.com/kevinbadi/hyperedit)**<br><sub>开源项目 · ★173</sub> | 一个 AI 视频编辑器：把编辑指令路由到具体操作、目标片段和轨道，并以关键词路由作为兜底。 | `TS`<br><sub>choice noul</sub> | `无许可证` |
| **[jevpilot](https://github.com/standardagents/jevpilot)**<br><sub>开源项目 · ★152</sub> | 驾驶模拟器的自动驾驶，每个 tick 问两个 choice；只剩单一选项的问题直接在本地短路，不花钱发出去。 | `JS`<br><sub>choice</sub> | `无许可证` |
| **[jev-drone](https://github.com/RomanSlack/jev-drone)**<br><sub>开源项目 · ★117</sub> | 拿 Jev 控无人机。底层飞控继续负责稳定和安全，Jev 只做爬升、刹车、穿越障碍这类上层判断。 | `Py`<br><sub>choice score noul</sub> | `宣称未核实` |
| **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)**<br><sub>开源项目 · ★83</sub> | 一个完全不含语言模型的 tool calling 聊天机器人：一次请求同时问清请求类型、该调哪个工具、以及每个工具的参数。 | `TS`<br><sub>choice noul</sub> | — |
| **[neo4jev](https://github.com/jexp/neo4jev)**<br><sub>开源项目 · ★79</sub> | 把 Jev 塞进知识图谱。每走到一个节点，判断下一条最值得走的边，再一路找下去。 | `Py`<br><sub>choice</sub> | — |
| **[OneVOneJev](https://github.com/emrickgarrett/OneVOneJev)**<br><sub>开源项目 · ★18</sub> | 浏览器里的 1v1 FPS。每个决策 tick 都要判断走位、视角、瞄准、开火和跳跃。 | `TS`<br><sub>choice</sub> | `代码未实测` `无许可证` |
| **[Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py)**<br><sub>代码片段</sub> | 一次问清操作本身、以及每个可能操作各自的目标 —— 于是浏览器的一步永远不需要第二次往返。 | `Py`<br><sub>choice noul</sub> | `代码未实测` |
| **[Example: tool selection with a none option](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/04-tool-selection/main.py)**<br><sub>代码片段</sub> | 把「选哪个工具」的 choice 和「到底需不需要工具」的 noul 配对使用 —— 因为这是两个不同的问题。 | `Py`<br><sub>choice noul</sub> | `代码未实测` |
| **[Jev (Fully Tested) + Browser Use: FASTEST AI Agent I'VE TRIED YET!](https://www.youtube.com/watch?v=SNJ3yuJ_QwY)**<br><sub>视频 · AICodeKing</sub> | 把 Jev 接到 Browser Use 上，驱动一个浏览器自动化智能体。 | — | `宣称未核实` |

### 意图路由

_判断用户意图，把请求分流到正确的分支。_

| 例子 | 展示了什么 | 代码 | 警示 |
| --- | --- | :-- | :-- |
| **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐<br><sub>官方文档</sub> | 一个可运行的智能家居助手示例，用类型化决策来解析用户请求。 | `Py` | — |
| **[Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing)** ⭐<br><sub>官方文档</sub> | 把 confidence 当作第二个维度：答案告诉你「是什么」，置信度告诉你「该不该照它执行」。 | `Py` | — |
| **[Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing)** ⭐<br><sub>官方文档</sub> | 对进来的请求做分类，路由到足够用的最便宜那个处理方：确定性代码、专用 LLM、或人。 | `Py`<br><sub>choice</sub> | — |
| **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)**<br><sub>开源项目 · ★187,483</sub> | 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。 | `Py`<br><sub>choice score noul</sub> | — |
| **[Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html)**<br><sub>平台集成 · ★46,932</sub> | 把下游任务 id 变成 choice 的选项集，并用最小置信度闸门把不确定的运行转给人处理。 | `Py`<br><sub>choice</sub> | — |
| **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)**<br><sub>开源项目 · ★12,276</sub> | 七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。 | `TS`<br><sub>choice noul</sub> | — |
| **[Real Python: hello-jev](https://github.com/realpython/materials/tree/master/hello-jev)**<br><sub>教程 · ★5,205 · Real Python</sub> | 带对照组的教学示例：同一个问询台任务，一份是只认 Y/N 的纯 Python 写法，旁边是一个能读出意图的 Noul。 | `Py`<br><sub>noul</sub> | — |
| **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br><sub>教程 · ★4,554</sub> | 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。 | `Py`<br><sub>choice score noul</sub> | — |
| **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)**<br><sub>开源项目 · ★1,340</sub> | 一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。 | `Java`<br><sub>choice score noul</sub> | — |
| **[jev-search](https://github.com/superagents-lab/jev-search)**<br><sub>开源项目 · ★382</sub> | Jev 驱动的网页搜索：先选时间窗口和最佳查询改写，再分批对结果逐条用 noul 重排。 | `TS`<br><sub>choice noul</sub> | — |
| **[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)**<br><sub>开源项目 · ★212</sub> | 语音驱动的浏览器控制：目标选项每次请求都按当前实时元素列表重建，并且总是包含一个 none 选项。 | `JS`<br><sub>choice score noul</sub> | — |
| **[hyperedit](https://github.com/kevinbadi/hyperedit)**<br><sub>开源项目 · ★173</sub> | 一个 AI 视频编辑器：把编辑指令路由到具体操作、目标片段和轨道，并以关键词路由作为兜底。 | `TS`<br><sub>choice noul</sub> | `无许可证` |
| **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)**<br><sub>开源项目 · ★83</sub> | 一个完全不含语言模型的 tool calling 聊天机器人：一次请求同时问清请求类型、该调哪个工具、以及每个工具的参数。 | `TS`<br><sub>choice noul</sub> | — |
| **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)**<br><sub>教程 · Flavio Copes</sub> | 技术密度最高的独立讲解：JS / Python / AI SDK 三种代码、三种应答结构、进阶模式，还诚实列出了模型的失效场景。 | `JS` `Py` `TS`<br><sub>choice score noul</sub> | — |
| **[Example: confidence-gated escalation](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-confidence-gate/main.py)**<br><sub>代码片段</sub> | 带「自动执行或转人工」闸门的路由；策略函数刻意留空 —— 阈值该定在哪，是你的决定。 | `Py`<br><sub>choice</sub> | `代码未实测` |
| **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)**<br><sub>教程 · Mehul Gupta</sub> | 逐个用例走一遍 —— 智能体路由、智能体内部的决策层、工单分拣 —— 每个都给出具体的选项集和示例响应。 | `Py`<br><sub>choice</sub> | `付费墙` |
| **[Jev on Netlify AI Gateway](https://www.netlify.com/changelog/typesafe-jev-ai-gateway/)**<br><sub>平台集成</sub> | 在 Netlify function 里零配置调用：直接用官方 SDK，不需要 API key、baseURL 或 provider 配置，按 Netlify credits 计费。 | `TS`<br><sub>choice</sub> | — |
| **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)**<br><sub>平台集成</sub> | LangChain 集成：一个分类器，外加用于模型路由、以及在高风险工具调用执行前拦截它的实验性 middleware。 | `Py`<br><sub>choice score noul</sub> | `需早期访问` |
| **[Using TypeSafe Jev with the AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk)**<br><sub>教程</sub> | Vercel 最完整的实操指南：单问题与多问题调用、按概率阈值路由，以及用 mock evaluation 模型写单元测试。 | `TS`<br><sub>noul choice score</sub> | — |
| **[jevai.org community showcase cases](https://www.jevai.org/cases)**<br><sub>开源项目</sub> | 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。 | — | `宣称未核实` |

### 上下文压缩

_判断哪些工具调用和结果仍然相关，从而丢弃过期上下文。_

| 例子 | 展示了什么 | 代码 | 警示 |
| --- | --- | :-- | :-- |
| **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)**<br><sub>基准测试 · ★247,803</sub> | 把 Jev 压缩方案移植过来，与自家在用的摘要器对比实测，最后公开结论：不采用。 | `Py`<br><sub>noul</sub> | — |
| **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)**<br><sub>开源项目 · ★19,990</sub> | 把记忆召回的整套检索栈替换掉 —— 不用 embedding、不用 BM25、不用重排器 —— 改为对每条候选记忆批量问一个 Noul。 | `Rs`<br><sub>noul</sub> | — |
| **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)**<br><sub>插件 · ★6,005 · tamaratran</sub> | 一个 Claude Code 插件，用逐条决策取代压缩式摘要：过期的工具调用被丢弃或截断，保留下来的全部逐字不变。 | `TS`<br><sub>noul</sub> | — |
| **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)**<br><sub>插件 · ★398</sub> | 九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。 | `Py`<br><sub>choice score noul</sub> | — |
| **[jev-pruner](https://github.com/tamaratran/jev-pruner)**<br><sub>插件 · ★134 · tamaratran</sub> | 在模型看到之前先修剪冗长的 shell 输出，每个片段问一个 Noul。 | `TS`<br><sub>noul</sub> | — |
| **[Winnow](https://github.com/GhalebDweikat/winnow)**<br><sub>插件 · ★54</sub> | 给 Claude Code 做上下文垃圾回收。Read / Bash / Grep 吐一大堆时，Jev 先判断哪些真和当前任务有关。 | `Py`<br><sub>noul</sub> | — |

### 安全闸门

_在执行前判断一个动作是否安全。属纵深防御，绝不是安全边界。_

| 例子 | 展示了什么 | 代码 | 警示 |
| --- | --- | :-- | :-- |
| **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐<br><sub>官方文档</sub> | 给每条召回的段落打分，再由代码决定哪些能进入回答模型 —— 矛盾的标记保留，夹带提示注入的直接丢弃。 | `Py` | — |
| **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐<br><sub>官方文档</sub> | 用一次请求筛查 LLM 应用的每一条进出消息，既点明风险类型、又给「照做会造成多大危害」打分。 | `Py`<br><sub>noul score</sub> | — |
| **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)**<br><sub>开源项目 · ★42,304</sub> | 作为审核 API 的直接替代：一次请求并行问多个 Noul，每个危害类别一个，且每条指令都带反注入前缀。 | `Go`<br><sub>noul</sub> | — |
| **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)**<br><sub>插件 · ★30,896</sub> | 三个可独立安装的 Claude Code 插件 —— 护栏、模型路由、技能推荐 —— 各自带 hook 和测试。 | `Py` `TS`<br><sub>choice score noul</sub> | — |
| **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)**<br><sub>平台集成 · ★18,214</sub> | LangChain 集成的 JavaScript 对应版本，分类器与 middleware 形状一致。 | `TS`<br><sub>choice score noul</sub> | — |
| **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)**<br><sub>开源项目 · ★6,338</sub> | 从三个维度审查每次工具调用：风险等级、用户是否授权、以及一个显式的提示注入压力检查。 | `TS`<br><sub>choice noul</sub> | — |
| **[agentgateway: CI-validated LLM guardrail](https://github.com/agentgateway/agentgateway)**<br><sub>开源项目 · ★4,969</sub> | 三个共用同一严重度量表的 Score 问题，两项以上越线即拦截请求，并且失败时默认关闭。 | `Rs`<br><sub>score</sub> | — |
| **[Jev-cu](https://github.com/Sac-Y/Jev-cu)**<br><sub>开源项目 · ★547</sub> | 一个 computer-use 智能体：判断该对无障碍树里哪个元素操作，并单独用一个 noul 判断这个动作是否需要用户显式确认。 | `JS`<br><sub>choice noul</sub> | `无许可证` |
| **[jev-mcp](https://github.com/jkudish/jev-mcp)**<br><sub>插件 · ★240</sub> | 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。 | `JS`<br><sub>choice score noul</sub> | — |
| **[jev-drone](https://github.com/RomanSlack/jev-drone)**<br><sub>开源项目 · ★117</sub> | 拿 Jev 控无人机。底层飞控继续负责稳定和安全，Jev 只做爬升、刹车、穿越障碍这类上层判断。 | `Py`<br><sub>choice score noul</sub> | `宣称未核实` |
| **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)**<br><sub>开源项目 · ★42 · brainstormity</sub> | 一个 Discord 审核机器人：用 Choice 给每条消息定级、用 Noul 表示封禁紧急度，管理员一旦赦免，该消息会作为「安全先例」注入后续请求。 | `Py`<br><sub>choice noul</sub> | — |
| **[Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)**<br><sub>文章 · Sydney Runkle, Hunter Lovell</sub> | LangChain 的讲解兼集成实操：三种问题类型，加上模型路由、以及在高风险工具调用执行前拦截它。 | `Py` | `厂商自报` |
| **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)**<br><sub>平台集成</sub> | LangChain 集成：一个分类器，外加用于模型路由、以及在高风险工具调用执行前拦截它的实验性 middleware。 | `Py`<br><sub>choice score noul</sub> | `需早期访问` |

### 输出校验

_在输出到达用户前，按评分标准检查模型产出。_

| 例子 | 展示了什么 | 代码 | 警示 |
| --- | --- | :-- | :-- |
| **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐<br><sub>官方文档</sub> | 用一个 Choice 对着原文核查引用是否错误或凭空编造，并用它的置信度把边缘情况标出来送审。 | `Py`<br><sub>choice</sub> | — |
| **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐<br><sub>官方文档</sub> | 用一次请求筛查 LLM 应用的每一条进出消息，既点明风险类型、又给「照做会造成多大危害」打分。 | `Py`<br><sub>noul score</sub> | — |
| **[jev-mcp](https://github.com/jkudish/jev-mcp)**<br><sub>插件 · ★240</sub> | 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。 | `JS`<br><sub>choice score noul</sub> | — |
| **[perch: semantic code linting](https://github.com/lakeday-org/perch)**<br><sub>开源项目 · ★167</sub> | 先用 tree-sitter 找出并排序方法，再把用户自写的 YAML 规则编译成 noul；严重度取评分量表的期望值，而不是概率最高的那一档。 | `JS`<br><sub>choice score noul</sub> | — |
| **[Canny](https://github.com/qkal/Canny)**<br><sub>开源项目 · ★28</sub> | 防 Coding Agent 嘴硬说自己做完了。看工具输出、代码 diff 和测试结果，再判断完成声明靠不靠谱。 | `TS`<br><sub>noul score</sub> | — |
| **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)**<br><sub>基准测试 · Near Here</sub> | 找到的唯一三方横评，每个模型分别调过提示词，且明确把范围限定在单一任务上、不做通用排名。 | — | — |
| **[TypeSafe's Jev: Can decision models replace LLM judges?](https://arize.com/blog/typesafe-jev-llm-judge/)**<br><sub>文章 · Laurie Voss</sub> | 汇总了目前已有的第三方评测，并讨论决策模型能在多大程度上顶替 LLM 评判者。 | — | — |

### 人工升级

_用校准置信度决定哪些情况必须由人来看。_

| 例子 | 展示了什么 | 代码 | 警示 |
| --- | --- | :-- | :-- |
| **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐<br><sub>官方文档</sub> | 把年报分入 75 个行业组，再根据答案自身的置信度决定：报这个细分组，还是退回上一层的大类。 | `Py`<br><sub>choice</sub> | — |
| **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐<br><sub>官方文档</sub> | 用一个 Choice 对着原文核查引用是否错误或凭空编造，并用它的置信度把边缘情况标出来送审。 | `Py`<br><sub>choice</sub> | — |
| **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐<br><sub>官方文档</sub> | 判断两份商品目录间 450 个候选配对里哪些指的是同一个东西 —— 一个 Score 就够，它的三级正好对应三种可执行动作。 | `Py`<br><sub>score</sub> | — |
| **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐<br><sub>官方文档</sub> | 在内容审核决策里显式加入「不确定」这个选项，并衡量标签一致率与自动处置比例之间的取舍。 | `Py`<br><sub>choice</sub> | — |
| **[Cookbook: Self-consistency with nouls](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook)** ⭐<br><sub>官方文档</sub> | 把不确定的概率转人工复核，同时保留底层的 noul 数值本身，而不是压成一个标签了事。 | `Py`<br><sub>noul</sub> | — |
| **[Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing)** ⭐<br><sub>官方文档</sub> | 把 confidence 当作第二个维度：答案告诉你「是什么」，置信度告诉你「该不该照它执行」。 | `Py` | — |
| **[Confidence](https://docs.typesafe.ai/confidence)** ⭐<br><sub>官方文档</sub> | confidence 如何从概率分布推导出来，以及为什么在一种问题类型上调好的阈值不能挪到另一种上用。 | — | — |
| **[Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html)**<br><sub>平台集成 · ★46,932</sub> | 把下游任务 id 变成 choice 的选项集，并用最小置信度闸门把不确定的运行转给人处理。 | `Py`<br><sub>choice</sub> | — |
| **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)**<br><sub>开源项目 · ★30,278</sub> | 把工具目录编译成问题，再从答案还原出 tool call，并为「弃权」和「需确认」两种情况定义了专门的错误类型。 | `Py`<br><sub>choice</sub> | — |
| **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)**<br><sub>开源项目 · ★12,276</sub> | 七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。 | `TS`<br><sub>choice noul</sub> | — |
| **[jev-review](https://github.com/devagrawal09/jev-review)**<br><sub>开源项目 · ★495</sub> | 代码审查前先过一遍 Jev，把高风险改动挑出来，再交给更贵的大模型或人。带本地看板。 | `TS`<br><sub>choice score noul</sub> | `已归档` |
| **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)**<br><sub>基准测试 · ★190</sub> | 独立的韩语实测笔记，报告仅仅把选项顺序倒过来，就能让概率移动到足以翻转 0.9 阈值的程度。 | `Py` | `无许可证` `宣称未核实` |
| **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)**<br><sub>开源项目 · ★42 · brainstormity</sub> | 一个 Discord 审核机器人：用 Choice 给每条消息定级、用 Noul 表示封禁紧急度，管理员一旦赦免，该消息会作为「安全先例」注入后续请求。 | `Py`<br><sub>choice noul</sub> | — |
| **[Example: confidence-gated escalation](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-confidence-gate/main.py)**<br><sub>代码片段</sub> | 带「自动执行或转人工」闸门的路由；策略函数刻意留空 —— 阈值该定在哪，是你的决定。 | `Py`<br><sub>choice</sub> | `代码未实测` |
| **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)**<br><sub>基准测试 · Lindfors</sub> | 找到的最好的独立实测：固定单一模型版本、24 份挪威语文档，开篇就展示了一个模型答错、但同时正确报出低置信度的案例。 | — | — |

### 模型路由

_选择由哪个下游模型或档位处理请求。_

| 例子 | 展示了什么 | 代码 | 警示 |
| --- | --- | :-- | :-- |
| **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐<br><sub>官方文档</sub> | 「小模型 → 校验 → 推理模型」的两段级联，用一小部分成本拿到接近大推理模型的质量。 | `Py` | — |
| **[Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing)** ⭐<br><sub>官方文档</sub> | 对进来的请求做分类，路由到足够用的最便宜那个处理方：确定性代码、专用 LLM、或人。 | `Py`<br><sub>choice</sub> | — |
| **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)**<br><sub>插件 · ★30,896</sub> | 三个可独立安装的 Claude Code 插件 —— 护栏、模型路由、技能推荐 —— 各自带 hook 和测试。 | `Py` `TS`<br><sub>choice score noul</sub> | — |
| **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)**<br><sub>平台集成 · ★18,214</sub> | LangChain 集成的 JavaScript 对应版本，分类器与 middleware 形状一致。 | `TS`<br><sub>choice score noul</sub> | — |
| **[jev-review](https://github.com/devagrawal09/jev-review)**<br><sub>开源项目 · ★495</sub> | 代码审查前先过一遍 Jev，把高风险改动挑出来，再交给更贵的大模型或人。带本地看板。 | `TS`<br><sub>choice score noul</sub> | `已归档` |
| **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)**<br><sub>插件 · ★398</sub> | 九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。 | `Py`<br><sub>choice score noul</sub> | — |
| **[jev-codex-router](https://github.com/0xNatoshi/jev-codex-router)**<br><sub>插件 · ★177</sub> | 先让 Jev 判断这一轮编程任务有多难，再决定模型档位、推理深度和速度模式。 | `JS`<br><sub>choice score</sub> | — |
| **[Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)**<br><sub>文章 · Sydney Runkle, Hunter Lovell</sub> | LangChain 的讲解兼集成实操：三种问题类型，加上模型路由、以及在高风险工具调用执行前拦截它。 | `Py` | `厂商自报` |
| **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)**<br><sub>教程 · Mehul Gupta</sub> | 逐个用例走一遍 —— 智能体路由、智能体内部的决策层、工单分拣 —— 每个都给出具体的选项集和示例响应。 | `Py`<br><sub>choice</sub> | `付费墙` |
| **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)**<br><sub>平台集成</sub> | LangChain 集成：一个分类器，外加用于模型路由、以及在高风险工具调用执行前拦截它的实验性 middleware。 | `Py`<br><sub>choice score noul</sub> | `需早期访问` |

### 并行扇出

_把大量问题（包括推测性的）打包进一次请求，再由代码挑出真正用得上的答案。_

| 例子 | 展示了什么 | 代码 | 警示 |
| --- | --- | :-- | :-- |
| **[Cookbook: Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions)** ⭐<br><sub>官方文档</sub> | 对一篇长文提 13 个合规问题，证明全部打包进一次调用便宜得多、也快得多，而答案不变。 | `Py` | — |
| **[Pattern: Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out)** ⭐<br><sub>官方文档</sub> | 把大量问题（包括可能用不上的）打包进一次请求，之后再由代码决定哪些答案真的用得上。 | `Py` | — |
| **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐<br><sub>官方文档</sub> | 官方第一课：一条工单，一次请求里同时问一个 Choice、一个 Score 和一个 Noul，给了 Python / JS / cURL 三种写法。 | `Py` `TS` `sh`<br><sub>choice score noul</sub> | — |
| **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)**<br><sub>开源项目 · ★187,483</sub> | 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。 | `Py`<br><sub>choice score noul</sub> | — |
| **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)**<br><sub>开源项目 · ★42,304</sub> | 作为审核 API 的直接替代：一次请求并行问多个 Noul，每个危害类别一个，且每条指令都带反注入前缀。 | `Go`<br><sub>noul</sub> | — |
| **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)**<br><sub>开源项目 · ★16,069 · Browser Use</sub> | Browser Use 做的高速浏览器 Agent。Jev 每一步只判断「做什么、点哪个元素」，要打字才叫小模型。 | `Py`<br><sub>choice</sub> | `厂商自报` |
| **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br><sub>教程 · ★4,554</sub> | 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。 | `Py`<br><sub>choice score noul</sub> | — |
| **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)**<br><sub>开源项目 · ★83</sub> | 一个完全不含语言模型的 tool calling 聊天机器人：一次请求同时问清请求类型、该调哪个工具、以及每个工具的参数。 | `TS`<br><sub>choice noul</sub> | — |
| **[OneVOneJev](https://github.com/emrickgarrett/OneVOneJev)**<br><sub>开源项目 · ★18</sub> | 浏览器里的 1v1 FPS。每个决策 tick 都要判断走位、视角、瞄准、开火和跳跃。 | `TS`<br><sub>choice</sub> | `代码未实测` `无许可证` |
| **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)**<br><sub>教程 · Flavio Copes</sub> | 技术密度最高的独立讲解：JS / Python / AI SDK 三种代码、三种应答结构、进阶模式，还诚实列出了模型的失效场景。 | `JS` `Py` `TS`<br><sub>choice score noul</sub> | — |
| **[Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py)**<br><sub>代码片段</sub> | 一次问清操作本身、以及每个可能操作各自的目标 —— 于是浏览器的一步永远不需要第二次往返。 | `Py`<br><sub>choice noul</sub> | `代码未实测` |
| **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)**<br><sub>代码片段</sub> | 最小化的第一次调用：同时问一个 choice、一个 score 和一个 noul，并标注了容易踩的那几处不对称。 | `Py`<br><sub>choice score noul</sub> | `代码未实测` |
| **[Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/)**<br><sub>平台集成</sub> | Workers AI binding 与 REST 示例：一次调用同时问 noul、choice、score，并给出含逐答案置信度的完整响应。 | `TS` `sh`<br><sub>noul choice score</sub> | — |
| **[Using TypeSafe Jev with the AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk)**<br><sub>教程</sub> | Vercel 最完整的实操指南：单问题与多问题调用、按概率阈值路由，以及用 mock evaluation 模型写单元测试。 | `TS`<br><sub>noul choice score</sub> | — |

### 检索与排序

_对来自廉价检索步骤的候选做打分或重排。_

| 例子 | 展示了什么 | 代码 | 警示 |
| --- | --- | :-- | :-- |
| **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐<br><sub>官方文档</sub> | 给每条召回的段落打分，再由代码决定哪些能进入回答模型 —— 矛盾的标记保留，夹带提示注入的直接丢弃。 | `Py` | — |
| **[Cookbook: Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find)** ⭐<br><sub>官方文档</sub> | 对一份服务条款做语义检索：一次请求用 Choice 给 218 个行号打分，同时用 Noul 判断文档里到底有没有答案。 | `Py`<br><sub>choice noul</sub> | — |
| **[Cookbook: Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe)** ⭐<br><sub>官方文档</sub> | 对 40 个法律检索问题各取 30 条 BM25 候选，按「问题-候选」逐对提问重排，top-1 与 top-10 准确率均大幅提升。 | `Py` | — |
| **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)**<br><sub>开源项目 · ★187,483</sub> | 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。 | `Py`<br><sub>choice score noul</sub> | — |
| **[OpenViking: retrieval reranking](https://github.com/volcengine/OpenViking)**<br><sub>开源项目 · ★38,359</sub> | 单次批量请求里对每个候选文档问一个 Noul，直接把「是」的概率当相关性分数。 | `Py`<br><sub>noul</sub> | — |
| **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)**<br><sub>开源项目 · ★27,847</sub> | 两段式 MCP 工具检索：先用一个宽 Choice 对整个目录粗排，再给候选短名单配完整描述，每个候选各配一个 Noul 判断它到底是否胜任。 | `Py`<br><sub>choice noul</sub> | — |
| **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)**<br><sub>开源项目 · ★19,990</sub> | 把记忆召回的整套检索栈替换掉 —— 不用 embedding、不用 BM25、不用重排器 —— 改为对每条候选记忆批量问一个 Noul。 | `Rs`<br><sub>noul</sub> | — |
| **[LanceDB TypeSafeReranker](https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py)**<br><sub>开源项目 · ★11,494</sub> | 向量数据库的重排器：对每条结果问一个 Noul，把「是」的概率当作绝对相关性分数 —— 可以跨查询比较。 | `Py`<br><sub>noul</sub> | — |
| **[no-mistakes: review context selection](https://github.com/kunchenguid/no-mistakes)**<br><sub>基准测试 · ★8,595</sub> | 对每个候选文件打一个 Score 来挑选审查上下文；实测结果是：计费输入明显增加，而实际耗时几乎没改善。 | `Go`<br><sub>score</sub> | — |
| **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)**<br><sub>开源项目 · ★1,340</sub> | 一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。 | `Java`<br><sub>choice score noul</sub> | — |
| **[jev-search](https://github.com/superagents-lab/jev-search)**<br><sub>开源项目 · ★382</sub> | Jev 驱动的网页搜索：先选时间窗口和最佳查询改写，再分批对结果逐条用 noul 重排。 | `TS`<br><sub>choice noul</sub> | — |
| **[pg-jev](https://github.com/realZachi/pg-jev)**<br><sub>开源项目 · ★284</sub> | 一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。 | `Py` `sh`<br><sub>choice score noul</sub> | — |
| **[jev-mcp](https://github.com/jkudish/jev-mcp)**<br><sub>插件 · ★240</sub> | 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。 | `JS`<br><sub>choice score noul</sub> | — |
| **[neo4jev](https://github.com/jexp/neo4jev)**<br><sub>开源项目 · ★79</sub> | 把 Jev 塞进知识图谱。每走到一个节点，判断下一条最值得走的边，再一路找下去。 | `Py`<br><sub>choice</sub> | — |
| **[Blink](https://github.com/ellipsis-dev/blink)**<br><sub>开源项目 · ★50</sub> | 把 Jev 当代码库导航器。每走到一层目录，就判断哪些文件和当前问题最相关，再继续往下找。 | `TS`<br><sub>choice</sub> | `无许可证` |

### 结构化抽取

_从杂乱文本中取出类型化字段 —— 靠在候选中选择，而不是生成。_

| 例子 | 展示了什么 | 代码 | 警示 |
| --- | --- | :-- | :-- |
| **[Cookbook: Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook)** ⭐<br><sub>官方文档</sub> | 抽取绝对与相对日期：先问文档里点明了哪些部分，再在代码里做解析与校验，并按置信度决定是否送审。 | `Py` | — |
| **[Cookbook: Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook)** ⭐<br><sub>官方文档</sub> | 先用正则找出候选的邮箱、电话、金额，再让模型挑出被问到的那一段，于是代码拿到的是逐字原值。 | `Py`<br><sub>choice</sub> | — |
| **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐<br><sub>官方文档</sub> | 用两次请求把丢了格式的纯文本还原成 Markdown：一次把硬换行的段落重新接起来，一次给每个块分类。 | `Py` | — |
| **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐<br><sub>官方文档</sub> | 「小模型 → 校验 → 推理模型」的两段级联，用一小部分成本拿到接近大推理模型的质量。 | `Py` | — |

### 分类

_把条目归入分类体系，包括用概率遍历的深层层级。_

| 例子 | 展示了什么 | 代码 | 警示 |
| --- | --- | :-- | :-- |
| **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐<br><sub>官方文档</sub> | 把年报分入 75 个行业组，再根据答案自身的置信度决定：报这个细分组，还是退回上一层的大类。 | `Py`<br><sub>choice</sub> | — |
| **[Cookbook: Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification)** ⭐<br><sub>官方文档</sub> | 用对 Choice 概率做并行 beam search 的方式，遍历专利、零售、生物医学、源码这几套很深的分类体系。 | `Py`<br><sub>choice</sub> | — |
| **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐<br><sub>官方文档</sub> | 判断两份商品目录间 450 个候选配对里哪些指的是同一个东西 —— 一个 Score 就够，它的三级正好对应三种可执行动作。 | `Py`<br><sub>score</sub> | — |
| **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐<br><sub>官方文档</sub> | 用两次请求把丢了格式的纯文本还原成 Markdown：一次把硬换行的段落重新接起来，一次给每个块分类。 | `Py` | — |
| **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)**<br><sub>基准测试 · ★87,175</sub> | 用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。 | `TS`<br><sub>choice</sub> | `仅影子运行` |
| **[json-render](https://github.com/vercel-labs/json-render)**<br><sub>开源项目 · ★17,964 · Vercel Labs</sub> | Vercel Labs 的生成式 UI 框架。实验里 Jev 不逐 token 写 JSON，只负责选组件、属性和布局。 | `TS`<br><sub>choice</sub> | — |
| **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)**<br><sub>开源项目 · ★12,276</sub> | 七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。 | `TS`<br><sub>choice noul</sub> | — |
| **[pg-jev](https://github.com/realZachi/pg-jev)**<br><sub>开源项目 · ★284</sub> | 一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。 | `Py` `sh`<br><sub>choice score noul</sub> | — |
| **[jev-mcp](https://github.com/jkudish/jev-mcp)**<br><sub>插件 · ★240</sub> | 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。 | `JS`<br><sub>choice score noul</sub> | — |
| **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)**<br><sub>基准测试 · ★190</sub> | 独立的韩语实测笔记，报告仅仅把选项顺序倒过来，就能让概率移动到足以翻转 0.9 阈值的程度。 | `Py` | `无许可证` `宣称未核实` |
| **[perch: semantic code linting](https://github.com/lakeday-org/perch)**<br><sub>开源项目 · ★167</sub> | 先用 tree-sitter 找出并排序方法，再把用户自写的 YAML 规则编译成 noul；严重度取评分量表的期望值，而不是概率最高的那一档。 | `JS`<br><sub>choice score noul</sub> | — |
| **[Prism](https://github.com/irfndi/prism-liquidity-agent)**<br><sub>开源项目 · ★68</sub> | 不直接让 Jev 下单。它判断 toxic flow、市场压力、均值回归之类的状态，再交给原来的策略。 | `TS`<br><sub>choice score</sub> | — |
| **[Blink](https://github.com/ellipsis-dev/blink)**<br><sub>开源项目 · ★50</sub> | 把 Jev 当代码库导航器。每走到一层目录，就判断哪些文件和当前问题最相关，再继续往下找。 | `TS`<br><sub>choice</sub> | `无许可证` |
| **[SemDecide](https://github.com/sharziki/semdecide)**<br><sub>插件 · ★27</sub> | 把 Jev 做成命令行。Shell 里直接分类、打分、过滤，适合接爬虫、CI 和数据流水线。 | `Py` `sh`<br><sub>choice score noul</sub> | — |
| **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)**<br><sub>基准测试 · Lindfors</sub> | 找到的最好的独立实测：固定单一模型版本、24 份挪威语文档，开篇就展示了一个模型答错、但同时正确报出低置信度的案例。 | — | — |
| **[Jev - The Ultimate Classification Model?](https://youtube.com/watch?v=X117w2Rark8)**<br><sub>视频 · Sam Witteveen</sub> | 一位 ML 工程师从分类任务角度做的讲解 —— 这个切入角度最贴近模型的实际能力。 | — | — |
| **[jevai.org community showcase cases](https://www.jevai.org/cases)**<br><sub>开源项目</sub> | 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。 | — | `宣称未核实` |
| **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)**<br><sub>基准测试 · Near Here</sub> | 找到的唯一三方横评，每个模型分别调过提示词，且明确把范围限定在单一任务上、不做通用排名。 | — | — |

### 机器学习特征抽取

_把自由文本转成数值特征，喂给下游的传统模型。_

| 例子 | 展示了什么 | 代码 | 警示 |
| --- | --- | :-- | :-- |
| **[Cookbook: Autoresearch feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery)** ⭐<br><sub>官方文档</sub> | 一个自动研究循环：自己提出问题、把自由文本转成数值特征、再用误差反过来改进下游的梯度提升回归模型。 | `Py` | — |
| **[Prism](https://github.com/irfndi/prism-liquidity-agent)**<br><sub>开源项目 · ★68</sub> | 不直接让 Jev 下单。它判断 toxic flow、市场压力、均值回归之类的状态，再交给原来的策略。 | `TS`<br><sub>choice score</sub> | — |
| **[jev-curate](https://github.com/AkashPriyadarshii/jev-curate)**<br><sub>开源项目 · ★18</sub> | 拿 Jev 筛训练数据。JSONL / Parquet 先做质量、相关性和风险判断，再决定哪些进后面的训练。 | `Rs`<br><sub>score noul</sub> | — |

### 文档分拣

_对进来的文档、发票、表单做分类和路由。_

| 例子 | 展示了什么 | 代码 | 警示 |
| --- | --- | :-- | :-- |
| **[jevai.org community showcase cases](https://www.jevai.org/cases)**<br><sub>开源项目</sub> | 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。 | — | `宣称未核实` |

### 工单分拣

_按意图和紧急度路由支持工单与会话。_

| 例子 | 展示了什么 | 代码 | 警示 |
| --- | --- | :-- | :-- |
| **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐<br><sub>官方文档</sub> | 官方第一课：一条工单，一次请求里同时问一个 Choice、一个 Score 和一个 Noul，给了 Python / JS / cURL 三种写法。 | `Py` `TS` `sh`<br><sub>choice score noul</sub> | — |
| **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br><sub>教程 · ★4,554</sub> | 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。 | `Py`<br><sub>choice score noul</sub> | — |
| **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)**<br><sub>代码片段</sub> | 最小化的第一次调用：同时问一个 choice、一个 score 和一个 noul，并标注了容易踩的那几处不对称。 | `Py`<br><sub>choice score noul</sub> | `代码未实测` |
| **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)**<br><sub>教程 · Mehul Gupta</sub> | 逐个用例走一遍 —— 智能体路由、智能体内部的决策层、工单分拣 —— 每个都给出具体的选项集和示例响应。 | `Py`<br><sub>choice</sub> | `付费墙` |
| **[Jev on AI/ML API](https://docs.aimlapi.com/api-references/decision-models/typesafe/jev)**<br><sub>平台集成</sub> | 又一个网关接入路径，值得记一笔是因为它的端点路径和请求外壳跟原生 API、跟 Cloudflare 都不一样。 | `Py`<br><sub>noul choice score</sub> | — |
| **[Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/)**<br><sub>平台集成</sub> | Workers AI binding 与 REST 示例：一次调用同时问 noul、choice、score，并给出含逐答案置信度的完整响应。 | `TS` `sh`<br><sub>noul choice score</sub> | — |
| **[spring-ai-typesafe](https://spring.io/blog/2026/09/21/spring-ai-typesafe-structured-judgment)**<br><sub>平台集成</sub> | 社区维护的 Spring AI starter，把类型化决策带到 Java，用 builder API 封装三种问题类型。 | `Java`<br><sub>choice score noul</sub> | — |

### 内容评分

_在有序量表上给质量、风险或相关性打分。_

| 例子 | 展示了什么 | 代码 | 警示 |
| --- | --- | :-- | :-- |
| **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐<br><sub>官方文档</sub> | 在内容审核决策里显式加入「不确定」这个选项，并衡量标签一致率与自动处置比例之间的取舍。 | `Py`<br><sub>choice</sub> | — |
| **[Pattern: Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring)** ⭐<br><sub>官方文档</sub> | 把一个笼统的判断拆成若干原子评分，再用你自己代码里的权重（而不是提示词里的）组合起来。 | `Py`<br><sub>score</sub> | — |
| **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)**<br><sub>开源项目 · ★187,483</sub> | 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。 | `Py`<br><sub>choice score noul</sub> | — |
| **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)**<br><sub>基准测试 · ★87,175</sub> | 用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。 | `TS`<br><sub>choice</sub> | `仅影子运行` |
| **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br><sub>教程 · ★4,554</sub> | 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。 | `Py`<br><sub>choice score noul</sub> | — |
| **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)**<br><sub>开源项目 · ★1,340</sub> | 一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。 | `Java`<br><sub>choice score noul</sub> | — |
| **[jev-review](https://github.com/devagrawal09/jev-review)**<br><sub>开源项目 · ★495</sub> | 代码审查前先过一遍 Jev，把高风险改动挑出来，再交给更贵的大模型或人。带本地看板。 | `TS`<br><sub>choice score noul</sub> | `已归档` |
| **[pg-jev](https://github.com/realZachi/pg-jev)**<br><sub>开源项目 · ★284</sub> | 一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。 | `Py` `sh`<br><sub>choice score noul</sub> | — |
| **[perch: semantic code linting](https://github.com/lakeday-org/perch)**<br><sub>开源项目 · ★167</sub> | 先用 tree-sitter 找出并排序方法，再把用户自写的 YAML 规则编译成 noul；严重度取评分量表的期望值，而不是概率最高的那一档。 | `JS`<br><sub>choice score noul</sub> | — |
| **[killmyidea](https://github.com/monteduro/killmyidea)**<br><sub>开源项目 · ★73</sub> | 输入一个创业点子，Jev 从多个维度打分，最后给你 KILL、FIX 或 SHIP。 | `TS`<br><sub>score choice</sub> | `无许可证` |
| **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)**<br><sub>开源项目 · ★42 · brainstormity</sub> | 一个 Discord 审核机器人：用 Choice 给每条消息定级、用 Noul 表示封禁紧急度，管理员一旦赦免，该消息会作为「安全先例」注入后续请求。 | `Py`<br><sub>choice noul</sub> | — |
| **[SemDecide](https://github.com/sharziki/semdecide)**<br><sub>插件 · ★27</sub> | 把 Jev 做成命令行。Shell 里直接分类、打分、过滤，适合接爬虫、CI 和数据流水线。 | `Py` `sh`<br><sub>choice score noul</sub> | — |
| **[jev-curate](https://github.com/AkashPriyadarshii/jev-curate)**<br><sub>开源项目 · ★18</sub> | 拿 Jev 筛训练数据。JSONL / Parquet 先做质量、相关性和风险判断，再决定哪些进后面的训练。 | `Rs`<br><sub>score noul</sub> | — |
| **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)**<br><sub>教程 · Flavio Copes</sub> | 技术密度最高的独立讲解：JS / Python / AI SDK 三种代码、三种应答结构、进阶模式，还诚实列出了模型的失效场景。 | `JS` `Py` `TS`<br><sub>choice score noul</sub> | — |
| **[jevai.org community showcase cases](https://www.jevai.org/cases)**<br><sub>开源项目</sub> | 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。 | — | `宣称未核实` |

### 总览

_介绍模型或整个领域，而非单一模式。_

<details>
<summary><b>53</b> 条 —— 点击展开</summary>

| 例子 | 展示了什么 | 代码 | 警示 |
| --- | --- | :-- | :-- |
| **[typesafe-ai/skills](https://github.com/typesafe-ai/skills)** ⭐<br><sub>插件 · ★1,565</sub> | Claude Code 插件背后的官方技能仓库，里面的 SKILL.md 教会智能体如何使用 System One API。 | `sh` | — |
| **[system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python)** ⭐<br><sub>SDK · ★241</sub> | 一个可直接替换 TypeSafeClient 的适配器，底层走普通 LLM API —— 没有 Jev 权限也能跑 Jev 形状的代码。 | `Py` | — |
| **[@typesafe-ai/sdk (TypeScript / JavaScript)](https://github.com/typesafe-ai/typesafe-sdk-js)** ⭐<br><sub>SDK · ★214</sub> | 官方 TypeScript 客户端。同时提供 ESM、CJS 和类型声明，辅助函数是小写的 choice()/score()/noul()。 | `TS` `JS`<br><sub>choice score noul</sub> | — |
| **[typesafe-sdk (Python)](https://github.com/typesafe-ai/typesafe-sdk-python)** ⭐<br><sub>SDK · ★186</sub> | 官方 Python 客户端。含同步与异步客户端、支持 retry-after 的重试策略，以及 Choice/Score/Noul 辅助类。 | `Py`<br><sub>choice score noul</sub> | — |
| **[API reference](https://docs.typesafe.ai/api)** ⭐<br><sub>官方文档</sub> | 唯一的端点 POST /v1/systemone，给出三种问题类型的完整请求与应答结构。 | `sh` `Py` `TS` | — |
| **[Models, pricing and limits](https://docs.typesafe.ai/models)** ⭐<br><sub>官方文档</sub> | 权威参数表：jev-1.13.0、输入 $0.042/Mtok 且输出免费、64k 上下文、state 加最长问题 32k、仅支持文本输入。 | `sh` `Py` `TS` | — |
| **[Official agent skill for Claude Code](https://docs.typesafe.ai/agent-skill)** ⭐<br><sub>官方文档</sub> | 把 TypeSafe 官方技能装进 Claude Code，让智能体自己写出正确的 Jev 调用，不必每次手动贴 API 结构。 | `sh` | — |
| **[Primitives: Choice, Score, Noul](https://docs.typesafe.ai/primitives)** ⭐<br><sub>官方文档</sub> | 三个原语各自的用途与 criteria 写法，含 Choice 最多 255 个选项、Score 只能 2–10 级这些硬限制。 | `Py` `TS`<br><sub>choice score noul</sub> | — |
| **[Introducing System One models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)** ⭐<br><sub>文章 · Diogo Almeida</sub> | 发布博文：什么是 System One 模型、为什么要把决策从生成里拆出来，以及厂商自报的延迟与成本数字。 | — | `厂商自报` |
| **[Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)** ⭐<br><sub>官方文档</sub> | 厂商自己列出的失效场景：字面化理解、算术与计数、日期比较、间接指代、夹杂大量无关细节的长 state、对抗性内容。 | — | — |
| **[Use case map](https://docs.typesafe.ai/concepts/use-case-map)** ⭐<br><sub>官方文档</sub> | 厂商自己的分类体系：五大类、十九个行业方向、十种决策形态（从分类一直到结构化数据抽取）。 | — | — |
| **[OpenCode Zen: Jev resale](https://github.com/anomalyco/opencode)**<br><sub>平台集成 · ★209,172</sub> | 一个编程智能体，其托管网关转售 Jev，还提供一个免费档位的模型 id。 | `TS` | — |
| **[Opik TypeSafe tracker](https://github.com/comet-ml/opik/blob/main/sdks/python/src/opik/integrations/typesafe/opik_tracker.py)**<br><sub>开源项目 · ★22,187</sub> | 包装同步与异步客户端，把每次 system_one 调用记录成一个可追踪的 span。 | `Py` | — |
| **[@effect/ai-typesafe](https://github.com/Effect-TS/effect)**<br><sub>平台集成 · ★16,165</sub> | 在 Jev 之上实现 Effect 的 DecisionModel 接口，并罕见地坦白说明取整行为尚未核实。 | `TS`<br><sub>choice score noul</sub> | — |
| **[rig-typesafeai](https://github.com/0xPlaygrounds/rig)**<br><sub>平台集成 · ★8,692</sub> | Rust 集成，选项数量在编译期检查 —— 超过 255 个选项的 Choice 会编译失败，而不是运行时才报错。 | `Rs`<br><sub>choice score noul</sub> | — |
| **[Bifrost TypeSafe gateway route](https://github.com/maximhq/bifrost/tree/dev/core/providers/typesafe)**<br><sub>开源项目 · ★8,222</sub> | 一个 Go 网关 provider，对原生 API 做一比一透传 —— 官方 SDK 只需改 base URL 即可使用。 | `Go` | — |
| **[Kiln: Jev adapter](https://github.com/Kiln-AI/Kiln)**<br><sub>平台集成 · ★5,078</sub> | 一个接进 adapter registry 的「JSON Schema 转问题」编译器，并诚实说明了它无法支持的场景。 | `Py`<br><sub>choice score noul</sub> | — |
| **[ruby_llm: TypeSafe provider](https://github.com/crmne/ruby_llm)**<br><sub>平台集成 · ★4,396</sub> | 带专门 System One 协议的 Ruby provider，是 Ruby 侧接入 Jev 的主要路径。 | `Rb`<br><sub>choice score noul</sub> | — |
| **[SemIf](https://github.com/TheoLeeCJ/SemIf)**<br><sub>Jev 替代实现 · ★3,312</sub> | 一个独立的「语义 if」实现，开门见山声明与 Jev 和 TypeSafe 无隶属关系。 | `Py` | `并非 Jev` |
| **[kev](https://github.com/jaredpalmer/kev)**<br><sub>Jev 替代实现 · ★2,544 · Jared Palmer</sub> | 一套可训练、可自托管的 Jev-like 决策模型，API 与 System One 兼容 —— 官方 SDK 可以直接指向你自己的服务。 | `Py`<br><sub>choice score noul</sub> | `并非 Jev` |
| **[NanoJev](https://github.com/TianyuCodings/NanoJev)**<br><sub>Jev 替代实现 · ★1,830</sub> | 自称 Jev 的「nano 复刻版」，用途是拿来读，不是拿来上生产。 | `Py` | `并非 Jev` |
| **[jevlike](https://github.com/vinnylarouge/jevlike)**<br><sub>Jev 替代实现 · ★1,169 · vinnylarouge</sub> | 一个独立可训练的模型，输入输出形状与 Jev 相同：文本加 N 个选项进，每个选项一个概率出，单次前向完成。 | `Py` | `并非 Jev` |
| **[simple-jev](https://github.com/featherless-ai/simple-jev)**<br><sub>Jev 替代实现 · ★455</sub> | 通过读取 next-token logits，把任意开源权重模型变成 Jev 形状的端点 —— JSON 由服务端组装，而不是模型生成。 | `Py` | `并非 Jev` |
| **[jev-skill](https://github.com/wuyoscar/jev-skill)**<br><sub>插件 · ★372</sub> | 一个 agent 技能加 CLI：校验三种原语、在产生计费调用前要求明确同意、并禁止在模拟时编造输出。 | `Py`<br><sub>choice score noul</sub> | — |
| **[awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects)**<br><sub>开源项目 · ★326 · logicrw</sub> | 一个同类目录，主打生态广度：来源锚定到具体 commit、四语 README、以及一个生成式站点。 | `JS` | — |
| **[typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp)**<br><sub>插件 · ★225</sub> | 最适合刚拿到 API 的人。把 Jev 接进 Claude Code、Claude Desktop、Codex 和 Pi，随时做 Choice / Score / Noul。 | `Go`<br><sub>choice score noul</sub> | — |
| **[awesome-jev (fatwang2)](https://github.com/fatwang2/awesome-jev)**<br><sub>开源项目 · ★187 · fatwang2</sub> | 一个同类目录，提交由 Jev 自己审核，其多语言社区客户端清单相当完整。 | `JS` | — |
| **[OpenDecision](https://github.com/deepanwadhwa/OpenDecision)**<br><sub>Jev 替代实现 · ★51 · deepanwadhwa</sub> | 一个开源语义决策引擎，本地跑零样本模型，其 FastAPI 服务已验证与官方 SDK 协议兼容。 | `Py`<br><sub>choice score noul</sub> | `并非 Jev` |
| **[@ai-sdk/typesafe-ai provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai)**<br><sub>SDK</sub> | 直连 TypeSafe 的 AI SDK provider 包，示例覆盖三种问题类型以及嵌套的 criteria 写法。 | `TS` `JS`<br><sub>choice score noul</sub> | — |
| **[aegis: TypeSafe as a first-class provider](https://github.com/dvjn/aegis)**<br><sub>开源项目 · ★0 · dvjn</sub> | 一个个人 Rust AI 网关，内置 TypeSafe provider，用真实响应体测试了用量提取与别名解析。 | `Rs` | `代码未实测` |
| **[Build Your Own JEV Locally: Run a 100% Private AI Agent on Your Machine](https://medium.com/coding-nexus/build-your-own-jev-locally-run-a-100-private-ai-agent-on-your-machine-bb98126d394a)**<br><sub>Jev 替代实现 · DataScience Nexus</sub> | 标题误导：它并没有在跑 Jev，而是用开源 LLM 加受约束的 next-token 打分，自己搭一个 Jev-like 决策引擎。 | `Py` | `并非 Jev` `代码未实测` `付费墙` |
| **[Jev Explained: How to Add Fast, Typed Decisions to an AI Agent](https://aihubmix.com/blog/jev-explained-how-to-add-fast-typed-decisions-to-an-ai-agent)**<br><sub>文章</sub> | 第三方解读文章，给了一张有用的架构草图，还罕见地诚实列出了「不该用决策模型」的场景。 | `Py` | `代码未实测` |
| **[jevai.org community site](https://www.jevai.org/)**<br><sub>开源项目</sub> | 一个与官方无关的社区站：有 playground、预设决策 API、MCP 服务、可下载技能，以及一个社区应用展示廊。 | `sh` | `需第三方密钥` `宣称未核实` |
| **[Tracing Jev calls with Langfuse](https://langfuse.com/integrations/model-providers/typesafe)**<br><sub>平台集成</sub> | 目前唯一有 Jev 专用可观测性的平台：一个 OpenInference instrumentor，通过 OpenTelemetry 追踪每次决策调用。 | `Py`<br><sub>choice score noul</sub> | — |
| **[TypeSafe AI Jev now available on AI Gateway](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway)**<br><sub>平台集成</sub> | Vercel 在 AI Gateway 上线 Jev 的公告，附 experimental_evaluate 示例，模型串为 typesafe-ai/jev。 | `TS`<br><sub>noul</sub> | — |
| **[TypeSafe models in Pydantic AI](https://pydantic.dev/docs/ai/models/typesafe/)**<br><sub>平台集成</sub> | Pydantic AI 的一方支持：用 typesafe:jev-latest 这个模型串、配 output_type=bool 建 Agent。 | `Py` | — |
| **[TypeSafe pass-through on LiteLLM](https://docs.litellm.ai/docs/pass_through/typesafe)**<br><sub>平台集成</sub> | 通过 LiteLLM 代理 Jev，统一密钥与成本追踪，/typesafe/ 下的任意路径都直接透传。 | `sh` | — |
| **[TypeSafe-compatible API on Vercel AI Gateway](https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe)**<br><sub>平台集成</sub> | 只改一个 baseURL 就能把官方 TypeSafe SDK 指向 Vercel，也可以直接用 cURL 调网关的 systemone 端点。 | `TS` `sh`<br><sub>noul</sub> | — |
| **[typesafe-go](https://github.com/Nibir1/typesafe-go)**<br><sub>SDK · ★0 · Nibir1</sub> | 零依赖的社区 Go SDK，还带一个静态分析器，能在编译期指出设计不良的问题。 | `Go`<br><sub>choice score noul</sub> | `代码未实测` |
| **[awesome-jev (yibie)](https://github.com/yibie/awesome-jev)**<br><sub>开源项目 · ★1,010</sub> | 目前这个领域里 star 数最高的同类目录。 | — | `无许可证` |
| **[A new kind of AI model from a ChatGPT inventor is thrilling developers](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)**<br><sub>文章 · Tim Fernholz</sub> | 唯一一篇引用了开发者一手说法（而非厂商数字）的发布报道，其中还提醒：解释阈值的责任现在落在你自己头上。 | — | — |
| **[AI model "Jev" to make machines decide faster](https://www.heise.de/en/news/AI-model-Jev-to-make-machines-decide-faster-11457071.html)**<br><sub>文章 · Tomislav Bezmalinović</sub> | 重点落在可解释性的缺失 —— 模型不给出语言层面的理由 —— 以及所有已公布基准都出自厂商自己。 | — | — |
| **[Hacker News: Introducing System One Models and Jev](https://news.ycombinator.com/item?id=49717558)**<br><sub>讨论</sub> | 发布讨论帖，也是质疑最集中的地方：RLCD 缺乏支撑材料、延迟对比不对等、以及官方刻意不公开基准。 | — | — |
| **[Jev (AI model) on Wikipedia](https://en.wikipedia.org/wiki/Jev_(AI_model))**<br><sub>文章</sub> | 最大价值在于当索引用：它的参考文献列表是找到值得读的报道的最快路径。 | — | — |
| **[Jev by TypeSafe: A Decision Model for AI Agents](https://beam.ai/agentic-insights/jev-typesafe-ai-agents)**<br><sub>文章</sub> | 从智能体开发者角度，讲决策模型在智能体技术栈里的位置。 | — | `营销内容` |
| **[Jev Cuts AI Decision Costs 100x And Vercel, Cloudflare Rushed To Add It](https://www.forbes.com/sites/josipamajic/2026/09/19/jev-cuts-ai-decision-costs-100x-and-vercel-cloudflare-rushed-to-add-it/)**<br><sub>文章 · Josipa Majic Predin</sub> | 主流媒体对这次发布、以及各家网关上线速度的报道。 | — | `厂商自报` `付费墙` |
| **[Jev From TypeSafe is a New Class of AI Model that is FAST and CHEAP - But There is a Caveat!](https://youtube.com/watch?v=qdji39XXgEY)**<br><sub>视频 · Gary Explains</sub> | 一篇把限制直接写进标题、而不是藏在正文里的评测。 | — | — |
| **[Jev: System One models for Prod, not God](https://www.latent.space/p/jev)**<br><sub>讨论 · Latent Space</sub> | 唯一的长篇创始人访谈：为什么 RLHF 是错的优化目标、为什么不公开基准、以及全合成数据的路线。 | — | — |
| **[Jev: TypeSafe's System One Model Explained](https://www.datacamp.com/blog/system-one-models-jev)**<br><sub>文章 · Matt Crabtree</sub> | 对架构、宣称的基准和定价的中立综述，并明确指出当时还没有出现大规模的独立复现。 | — | — |
| **[jevai.org community app gallery](https://www.jevai.org/apps)**<br><sub>开源项目</sub> | 从社交帖子里策展的 36 个社区作品：浏览器智能体、表格工具、按意图搜邮箱、会判断的广告拦截、游戏与机器人。 | — | `宣称未核实` |
| **[RLCD explained: Reinforcement Learning for Calibrated Decisions](https://systemonemodels.org/guides/rlcd-explained/)**<br><sub>文章</sub> | 一份独立整理，其最有价值的结论是否定性的：RLCD 没有论文、没有奖励函数、没有数据集说明、也没有可复现的评测。 | — | — |
| **[TypeSafe AI debuts model for machines that plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711)**<br><sub>文章 · Thomas Claburn</sub> | 最具怀疑视角的主流报道：它质疑「不会幻觉」的说法 —— 格式正确的答案不等于正确的答案。 | — | — |
| **[TypeSafe on OpenRouter](https://openrouter.ai/typesafe)**<br><sub>平台集成</sub> | OpenRouter 上的 Jev 条目，有自己的模型 id，以及「输入收费、输出免费」这种少见的定价结构。 | — | — |

</details>

## 按资源形态

同样这些行，按你点开链接后会看到什么来分组。

| 形态 | 例子数 | 点开会看到 |
| --- | :-- | --- |
| **官方文档** | `31` ███████████▎ | 厂商文档、cookbook 与模式页。 |
| **SDK** | ` 5` █▉ | 客户端库，官方与社区。 |
| **平台集成** | `18` ██████▌ | 接入模型的网关、框架或平台路径。 |
| **代码片段** | ` 4` █▌ | 本仓库内的小型可运行样例。 |
| **开源项目** | `44` ████████████████ | 真正在调用 Jev 的应用或库。 |
| **插件** | `11` ████ | 可安装的编辑器、智能体、MCP 集成。 |
| **教程** | ` 5` █▉ | 带代码的分步教学材料。 |
| **基准测试** | ` 6` ██▏ | 实测。注意区分独立实测与厂商自报。 |
| **文章** | `12` ████▍ | 讲解、分析与发布报道。 |
| **视频** | ` 3` █▏ | 演示与评测。 |
| **讨论** | ` 2` ▊ | 值得读的讨论，包括质疑的声音。 |
| **Jev 替代实现** | ` 7` ██▌ | 独立复现实现。它们**不**调用 Jev。 |

## 本仓库还有什么

除目录数据之外的部分。

| 文件 | 是什么 |
| --- | --- |
| [`docs/patterns.md`](docs/patterns.md) | 逐个定义每个模式，并明确写出**什么时候不该用它**。 |
| [`docs/compatibility.md`](docs/compatibility.md) | 模型串、字段名、请求结构、端点、环境变量 —— 每个平台都不一样。这就是那张对照表。 |
| [`docs/vetting.md`](docs/vetting.md) | 信任一个条目之前该检查什么，以及大多数人会犯的那一个错。 |
| [`docs/status.md`](docs/status.md) | 这个生态第一周的真实样貌，包括缺口。 |
| [`docs/method.md`](docs/method.md) | 目录是如何建起来的、排除了什么、以及它最弱的地方在哪。 |
| [`docs/sources.md`](docs/sources.md) | 每一行的来源，以及许可状况。 |
| [`examples/`](examples/) | 四个可运行样例。其中一个刻意把阈值策略留给你写。 |
| [`schema/entry.schema.json`](schema/entry.schema.json) | 一条目录记录允许包含什么。 |

## 哪些经过核实，哪些没有

- ✅ **已核实** —— 该链接在 `checked` 日期返回成功状态；有人打开它、按页面实际内容写了摘要；含代码的行都读过调用处、确认了实际使用的原语；star 数与许可证来自 GitHub API。
- ❌ **未核实** —— 代码能否跑通、任何性能宣称是否成立、项目是否仍在维护、以及这些做法是否适合你的系统。本仓库没有执行过、压测过或做过安全审计。

### 这些标记是什么意思

| 标记 | 含义 |
| --- | --- |
| `并非 Jev` | 完全不调用 Jev。协议兼容不等于校准兼容，所以阈值不能迁移。 |
| `仅影子运行` | 接进去了但故意不生效 —— 它返回的东西不会进入任何对用户可见的决策。 |
| `需早期访问` | 需要通过等候名单才能运行。 |
| `代码未实测` | 代码是读过的，没有实际运行。 |
| `仅一次提交` | 只有一次提交，基本不会有维护。 |
| `无许可证` | 没有 LICENSE 文件，不管 README 徽章怎么写。复用时这是硬障碍。 |
| `需第三方密钥` | 需要 TypeSafe 之外某个服务的密钥。 |
| `厂商自报` | 照搬厂商自测数据，不是独立实测。 |
| `宣称未核实` | 做出了无法核实的量化宣称。 |
| `营销内容` | 发布目的既是讲解也是推销。 |
| `付费墙` | 有付费墙或阅读次数限制。 |
| `已归档` | 开发明显已经停止。 |

## 机器可读数据

每个例子一条记录，每次推送都按 JSON Schema 校验。

| 文件 | 是什么 |
| --- | --- |
| [`catalog.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/catalog.json) | 148 条目 |
| [`retired.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/retired.json) | 0 已退休 |
| [`compat.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/compat.json) | The platform matrix behind `docs/compatibility.md` |
| [`schema/entry.schema.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/schema/entry.schema.json) | One entry's shape |
| [`llms.txt`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/llms.txt) | For agents, with the caveats spelled out |

## 参与贡献与许可

纠错优先于新增 —— 一个错的条目比一个缺失的条目代价更大。详见 [CONTRIBUTING.md](CONTRIBUTING.md)；收录标准是：*读者不点开链接，能否据此行动？*

`scripts/`、`site/`、`examples/` 中的代码采用 [MIT](LICENSE-MIT)。目录元数据采用 [CC0-1.0](LICENSE-CC0)，并带逐行 `license` 字段。被链接的作品各自保留原许可 —— `repo_license` 记录了各自声明的内容。
