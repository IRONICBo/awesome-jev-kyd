<!--
  本文件由 catalog.json 生成。请修改目录数据后运行 `python3 scripts/build_readme.py`。
-->

<div align="center">

# awesome-jev

**全网 Jev（TypeSafe AI 的 System One 决策模型）使用例子索引 —— 按它做的**决策**归类，而不是按提到它的博客归类。**

[![lint](https://github.com/kydlikebtc/awesome-jev/actions/workflows/lint.yml/badge.svg)](https://github.com/kydlikebtc/awesome-jev/actions/workflows/lint.yml) [![links](https://github.com/kydlikebtc/awesome-jev/actions/workflows/links.yml/badge.svg)](https://github.com/kydlikebtc/awesome-jev/actions/workflows/links.yml) [![entries](https://img.shields.io/badge/条目-404-f5a524?style=flat-square)](https://kydlikebtc.github.io/awesome-jev/) [![verified](https://img.shields.io/badge/链接已核实-400-3fb950?style=flat-square)](https://kydlikebtc.github.io/awesome-jev/) [![rechecked](https://img.shields.io/badge/声明可复检-320-58a6ff?style=flat-square)](https://github.com/kydlikebtc/awesome-jev/actions/workflows/claims.yml) [![data](https://img.shields.io/badge/data-CC0--1.0-8b949e?style=flat-square)](LICENSE-CC0) [![code](https://img.shields.io/badge/code-MIT-8b949e?style=flat-square)](LICENSE-MIT)

[可搜索站点](https://kydlikebtc.github.io/awesome-jev/) &nbsp;·&nbsp; [English](README.md) &nbsp;·&nbsp; [决策模式](docs/patterns.md) &nbsp;·&nbsp; [兼容性](docs/compatibility.md) &nbsp;·&nbsp; [核查指南](docs/vetting.md)

<a href="https://kydlikebtc.github.io/awesome-jev/"><img src="docs/screenshots/site-chinese.png" alt="awesome-jev 站点：左侧覆盖度直方图兼作模式筛选器，右侧是密集的条目卡片" width="760"></a>

<sub>点击条形即可筛选。另有两个视图：<a href="https://kydlikebtc.github.io/awesome-jev/?view=prims&lang=zh">三个原语</a> · <a href="https://kydlikebtc.github.io/awesome-jev/?view=compat&lang=zh">兼容性矩阵</a>。每个筛选条件和每个条目都是可分享的 URL。</sub>

</div>

---

## 这是什么

- **Jev** 是 TypeSafe AI 的决策模型。它不生成文本 —— 你给它状态和类型化问题，它返回带校准置信度的类型化答案，快且便宜到可以放进智能体的内层循环。
- **本仓库**收集它的公开使用例子，按所做的**决策**组织。你这周读的那篇资料是一次性的，决策模式不是。
- **凭什么可信：**每一行都写明来源、写明代码实际调用了哪些原语、并标出点开前该知道的事。Jev 的列表有几十个 —— 这一个竞争的是核实严谨度，不是收录数量。

> ⚠️ 不是产品本身，不是 SDK，与 TypeSafe AI 无隶属关系，也不构成推荐。收录只意味着链接可访问、并且有人读过 —— 仅此而已。详见[哪些经过核实](#哪些经过核实哪些没有)。

## Jev 返回什么

三个原语。下面所有模式都由它们构成，而最后一行那个不对称是最常见的 bug 来源。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/primitives-zh-dark.svg">
  <img src="docs/assets/primitives-zh-light.svg" alt="三个面板，分别说明 choice、score、noul 三个原语各自返回什么" width="660">
</picture>

输入**仅支持文本** —— 字符串、JSON 对象、或文本数组。上下文每次请求 **64k** token，其中 state 加最长的那个问题占 **32k**。输出 token 免费。权重未公开，因此无法本地运行。跨平台差异全表见 [`docs/compatibility.md`](docs/compatibility.md)。

## 从这里开始

六条，按阅读顺序。手工挑选 —— 因为「star 最多」和「该先读哪个」不是一回事。

1. **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)**
   <sub>官方第一课：一条工单，一次请求里同时问一个 Choice、一个 Score 和一个 Noul，给了 Python / JS / cURL 三种写法。</sub>

2. **[Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)**
   <sub>官方文档里最有用、却最少被引用的一页。它还解释了一件事：对选项做一个 Choice，和每个选项各问一个 Noul，问的根本不是同一个问题。</sub>

3. **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)**
   <sub>按官方 API 参考编写并逐字段对照核实，但未针对线上 API 实际执行过。</sub>

4. **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)**
   <sub>每次工具调用恰好两个 noul：知道这次调用发生过是否还有意义、以及是否还需要完整原文输出。尽管它自己的描述里用了「打分」，实际并未使用 score 原语。</sub>

5. **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**
   <sub>找到的最好的结构化教程。它明确指出类型化输出不保证决策正确、列出了官方记录的弱项，并且对自己给出的成本示例做了限定而不是拿来营销。</sub>

6. **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)**
   <sub>本目录可信度最高的一条。召回率低于他们现有的摘要器，在相同上下文预算下与「按时间倒序」打平。成本确实低得多。在一个被热炒的模型上公开负面结果，非常少见。</sub>

## 覆盖度

全部决策模式，按例子数量排列长度。这张表同时就是索引 —— 名称链接到下面对应章节。数字为 0 的是待补的研究缺口，不是渲染 bug。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/coverage-zh-dark.svg">
  <img src="docs/assets/coverage-zh-light.svg" alt="十八个决策模式各有多少个目录条目的横向条形图" width="100%">
</picture>

有两个模式目前没有例子。两者都是合理的适用场景，只是还没人公开发表 —— 见 [`docs/status.md`](docs/status.md)。

## 实测，而非宣称

关于这个模型流传的性能数字几乎全是厂商自测，而且参考答案由其他模型的判断推导而来、不是人工 ground truth。下面这些是本目录里的独立实测 —— 其中几条是**负面结果**，这恰恰是它们值得先读的原因。

- **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)** — 把 Jev 压缩方案移植过来，与自家在用的摘要器对比实测，最后公开结论：不采用。
  <sub>`基准测试` · ★247,881 · `Py` · `noul`</sub>
  <sub>本目录可信度最高的一条。召回率低于他们现有的摘要器，在相同上下文预算下与「按时间倒序」打平。成本确实低得多。在一个被热炒的模型上公开负面结果，非常少见。</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)** — 用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。
  <sub>`基准测试` · ★87,191 · `TS` · `choice` · ⚠ `仅影子运行`</sub>
  <sub>接进去了但故意不生效：按他们自己的说法，Jev 返回的任何东西都不会进入标签、缓存行或告警。带黄金测试集。想在不拿生产环境下注的前提下试新模型，这是值得照抄的做法。</sub>

- **[no-mistakes: review context selection](https://github.com/kunchenguid/no-mistakes)** — 对每个候选文件打一个 Score 来挑选审查上下文；实测结果是：计费输入明显增加，而实际耗时几乎没改善。
  <sub>`基准测试` · ★8,598 · `Go` · `score`</sub>
  <sub>他们自己的建议是：这个功能保持可选、默认关闭、不要宣传省钱。诚实的实测就该长这样。</sub>

- **[hippo-memory](https://github.com/kitfunso/hippo-memory)** — 受生物启发的智能体记忆：衰减、检索强化与巩固。零运行时依赖，基于 SQLite。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★752 · kitfunso · `TS`</sub>

- **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)** — 独立的韩语实测笔记，报告仅仅把选项顺序倒过来，就能让概率移动到足以翻转 0.9 阈值的程度。
  <sub>`基准测试` · ★190 · `Py` · ⚠ `无许可证` `宣称未核实`</sub>
  <sub>在所有资料里找到的最具操作价值的工程警示：如果仅仅选项顺序就能把概率推过你的阈值，那你的阈值没有看上去那么稳。这是独立且未被复现的结果，具体幅度请当作指示性数据。</sub>

- **[windtunnel](https://github.com/nekuda-ai/WindTunnel)** — 一个 WebMCP 基准，衡量 WebMCP 与其他浏览器智能体接口的差距。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★76 · nekuda-ai · `TS`</sub>

- **[jevbench](https://github.com/fstandhartinger/jevbench)** — JevBench v1 —— 面向 Jev 这类类型化决策模型的基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★71 · fstandhartinger · `Py`</sub>

- **[typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark)** — 一个模仿其结构化输出形状的网关，用于与之对比测试。
  <sub>`基准测试` · ★37 · iammrduncan · `TS`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — 只读的交易日志与复盘 harness：Jev 类型化判断、智能体集成，以及一个可复现的金融基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★26 · myc0576 · `Py`</sub>

- **[jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas)** — 独立的、基于证据的能力地图：Jev 在哪些场景站得住、在哪些场景崩掉 —— 附真实 API 调用凭据。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★24 · zaious · `Py`</sub>

- **[jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)** — 面向类型化决策模型的概率感知评测：校准度、选择性风险、延迟，以及可复现的基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★17 · abdelstark · `Py`</sub>

- **[jev-benchmark](https://github.com/wondertwins/jev-benchmark)** — Jev 的基准与 playground：国际象棋，以及语音转写中的说话对象判定。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★6 · wondertwins · `Py`</sub>

- **[jev-korean-benchmark](https://github.com/mahlernim/jev-korean-benchmark)** — 可复现的早期访问评测：Jev 在韩语理解与医学文本上的表现，附运行时与成本证据。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★6 · mahlernim · `Py` · ⚠ `无许可证`</sub>

- **[jev-little-airways](https://github.com/lbotinelly/jev-little-airways)** — Jev 的能力展示与研究：一次 show-and-tell 式的考察。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★5 · lbotinelly · `TS`</sub>

- **[jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench)** — 与专用重排模型在 14 个数据集上的独立横评。
  <sub>`基准测试` · ★5 · anessbelbati · `Py`</sub>
  <sub>这是独立实测而非厂商数字，而且直接对比了专门做重排的模型 —— 这正是 search-ranking 模式该看的对比。</sub>

- **[legalforecastbench](https://github.com/johnhughes3/LegalForecastBench)** — LegalForecast-MTD 基准 alpha 版与官方评测流程。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★5 · johnhughes3 · `Py`</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — 在一个它不可能见过的任务上做独立校准测试：900 条规则生成的支持工单。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★4 · scienthoon · `Py`</sub>

- **[jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab)** — 在 DSPy 工作流中对 Jev 决策做可复现的校准与选择性风险基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★3 · jmanhype · `Py`</sub>

- **[jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench)** — 在 2000 封钓鱼邮件上对比 Jev 与一个轻量 LLM：准确率、校准度、延迟、成本。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★3 · anisselbd · `Py` · ⚠ `无许可证`</sub>

- **[jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark)** — 在一个智能体失败归因基准上，把 Jev 与一个强 LLM 做对比测试。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★2 · tokentrim · `Py`</sub>

- **[jev-eval](https://github.com/4esv/jev-eval)** — 在你自己的标注分类数据上，把 Jev 与任意 OpenRouter 模型做基准对比：准确率与校准度。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · 4esv · `Py` · ⚠ `无许可证`</sub>

- **[padflow-jev-evals](https://github.com/zsavage8/padflow-jev-evals)** — 来自某土地开发 SaaS 的类型化决策基准：schema、匿名标注数据与运行器。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · zsavage8 · `Py`</sub>

- **[jev-calibration-audit](https://github.com/jujumilk3/jev-calibration-audit)** — 仅通过 API 对 Jev 做的独立校准审计。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · jujumilk3 · `Py`</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — 给 Jev 的有限样本保证：用保形风险控制把校准概率转成可证的约束。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · nikkoxgonzales · `Py`</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — 按 Jev 概率做 ORDER BY 能否给出站得住脚的排序？独立的排序、校准与不变量实测。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · yodablocks · `Py`</sub>

- **[jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)** — 衡量 Jev 在文件片段中识别真实密钥凭据的能力。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · teyhouse · `Py` · ⚠ `无许可证`</sub>

- **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)** — 找到的最好的独立实测：固定单一模型版本、24 份挪威语文档，开篇就展示了一个模型答错、但同时正确报出低置信度的案例。
  <sub>`基准测试` · Lindfors</sub>
  <sub>方法论交代干净，并诚实限定为「单日快照」。开篇就摆失败案例，这才让它成为真正的校准检验，而不是一篇软文。</sub>

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)** — 找到的唯一三方横评，每个模型分别调过提示词，且明确把范围限定在单一任务上、不做通用排名。
  <sub>`基准测试` · Near Here</sub>
  <sub>自我限定很规范：这是用例研究，不是模型排行榜。这种克制比数字本身更少见。</sub>

## 按决策模式

主索引。每个标题是智能体必须做的一个决策；下面的行是做这个决策的例子。警示以短标记呈现 —— 每行的完整备注在 [`catalog.json`](catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/)里。

### 工具选择

_智能体下一步该调用哪个工具或动作。_

- **[Cookbook: Function calling](https://docs.typesafe.ai/cookbooks/function_calling)** ⭐ — 把自然语言的交易请求映射到普通的类型化函数：函数名和有限取值的参数各自变成一个带置信度的问题。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion)** ⭐ — 为智能体的一轮对话从 182 个技能里最多挑一个：第一次请求给所有技能排序并顺便问「这轮到底需不需要技能」，第二次细读前三名。
  <sub>`官方文档` · `Py` · `choice` · `noul`</sub>

- **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐ — 一个可运行的智能家居助手示例，用类型化决策来解析用户请求。
  <sub>`官方文档` · `Py`</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)** — 三个可独立安装的 Claude Code 插件 —— 护栏、模型路由、技能推荐 —— 各自带 hook 和测试。
  <sub>`插件` · ★30,899 · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)** — 把工具目录编译成问题，再从答案还原出 tool call，并为「弃权」和「需确认」两种情况定义了专门的错误类型。
  <sub>`开源项目` · ★30,279 · `Py` · `choice`</sub>

- **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)** — 两段式 MCP 工具检索：先用一个宽 Choice 对整个目录粗排，再给候选短名单配完整描述，每个候选各配一个 Noul 判断它到底是否胜任。
  <sub>`开源项目` · ★27,855 · `Py` · `choice` · `noul`</sub>

- **[Cua driver: jev-use example](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use)** — Python 与 TypeScript 双实现的 computer-use 动作选择：Jev 从不可变候选集里挑下一个浏览器动作，保留 reobserve 和 abstain 两个特殊选项。
  <sub>`开源项目` · ★25,834 · `Py` · `TS` · `choice`</sub>

- **[json-render](https://github.com/vercel-labs/json-render)** — Vercel Labs 的生成式 UI 框架。实验里 Jev 不逐 token 写 JSON，只负责选组件、属性和布局。
  <sub>`开源项目` · ★17,994 · Vercel Labs · `TS` · `choice`</sub>

- **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)** — Browser Use 做的高速浏览器 Agent。Jev 每一步只判断「做什么、点哪个元素」，要打字才叫小模型。
  <sub>`开源项目` · ★16,758 · Browser Use · `Py` · `choice` · ⚠ `厂商自报`</sub>

- **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)** — 从三个维度审查每次工具调用：风险等级、用户是否授权、以及一个显式的提示注入压力检查。
  <sub>`开源项目` · ★6,338 · `TS` · `choice` · `noul`</sub>

- **[jev-trader](https://github.com/jarrodwatts/jev-trader)** — 在 Monad 测试网上做高频做市。Jev 根据价差和成交方向判断下一步买还是卖。
  <sub>`开源项目` · ★1,911 · `TS` · `choice` · ⚠ `宣称未核实`</sub>

- **[agent-desktop](https://github.com/lahfir/agent-desktop)** — 桌面自动化。读系统无障碍树，判断下一步该点哪个按钮、菜单或输入框。
  <sub>`开源项目` · ★1,449 · `Rs` · `choice`</sub>

- **[typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)** — macOS 上的 computer use：OCR 屏幕、分类下一步动作、点击。每步成本不到一分钱的零头。
  <sub>`开源项目` · ★775 · awlevin · `Py`</sub>

- **[tiptour-macos](https://github.com/milind-soni/tiptour-macos)** — 开源的快速本地 computer use。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★644 · milind-soni · `Swift` · ⚠ `无许可证`</sub>

- **[Jev-cu](https://github.com/Sac-Y/Jev-cu)** — 一个 computer-use 智能体：判断该对无障碍树里哪个元素操作，并单独用一个 noul 判断这个动作是否需要用户显式确认。
  <sub>`开源项目` · ★557 · `JS` · `choice` · `noul`</sub>

- **[foreman](https://github.com/thruwire/foreman)** — 一个「软件工厂工头」，用 Jev 决定智能体流水线下一步该做什么。
  <sub>`开源项目` · ★482 · thruwire · `Py`</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** — 九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。
  <sub>`插件` · ★408 · `Py` · `choice` · `score` · `noul`</sub>

- **[jev-browser-use](https://github.com/wy-coliney/jev-browser-use)** — 把循环拆开：Jev 负责点击，推理模型负责思考与验证。
  <sub>`开源项目` · ★341 · wy-coliney · `JS`</sub>

- **[typesafe-mario](https://github.com/fhshaik/typesafe-mario)** — 让 Jev 玩《超级马里奥》。不看截图，直接读模拟器 RAM 里的结构化状态，再决定跑、跳、躲。
  <sub>`开源项目` · ★340 · `Py` · `choice` · `score` · `noul` · ⚠ `代码未实测` `仅一次提交` `无许可证`</sub>

- **[mobile-jev](https://github.com/droidrun/mobile-jev)** — 移动端 computer use：由 Jev 决定手机屏幕上的下一个动作。
  <sub>`开源项目` · ★336 · droidrun · `JS`</sub>

- **[jev-browser](https://github.com/jkudish/jev-browser)** — 浏览器自动化，下一步动作由 Jev 选择。
  <sub>`开源项目` · ★235 · jkudish · `TS`</sub>

- **[quackd](https://github.com/rokbenko/quackd)** — 统管所有机器人的 CLI：每台机器人配一个 LLM 作大脑，由 Jev 做决策。 <sub>(机翻)</sub>
  <sub>`插件` · ★228 · rokbenko · `Py`</sub>

- **[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)** — 语音驱动的浏览器控制：目标选项每次请求都按当前实时元素列表重建，并且总是包含一个 none 选项。
  <sub>`开源项目` · ★222 · `JS` · `choice` · `score` · `noul`</sub>

- **[hyperedit](https://github.com/kevinbadi/hyperedit)** — 一个 AI 视频编辑器：把编辑指令路由到具体操作、目标片段和轨道，并以关键词路由作为兜底。
  <sub>`开源项目` · ★179 · `TS` · `choice` · `noul` · ⚠ `无许可证`</sub>

- **[embodied-jev](https://github.com/FBddcz/embodied-jev)** — EmbodiedJev：基于 MuJoCo 的机器人决策工作台。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★167 · fbddcz · `Py`</sub>

- **[jevpilot](https://github.com/standardagents/jevpilot)** — 驾驶模拟器的自动驾驶，每个 tick 问两个 choice；只剩单一选项的问题直接在本地短路，不花钱发出去。
  <sub>`开源项目` · ★162 · `JS` · `choice` · ⚠ `无许可证`</sub>

- **[jevrouter](https://github.com/BillionsBobby/JevRouter)** — 面向模型、工具和子智能体的路由器。
  <sub>`开源项目` · ★151 · billionsbobby · `TS`</sub>

- **[pi-jev](https://github.com/y0usaf/pi-jev)** — 给编程智能体做的决策层：一个可度量的工具调用闸门，外加一个返回校准答案的类型化提问。
  <sub>`插件` · ★135 · y0usaf · `TS`</sub>

- **[jev-drone](https://github.com/RomanSlack/jev-drone)** — 拿 Jev 控无人机。底层飞控继续负责稳定和安全，Jev 只做爬升、刹车、穿越障碍这类上层判断。
  <sub>`开源项目` · ★121 · `Py` · `choice` · `score` · `noul` · ⚠ `宣称未核实`</sub>

- **[jev-gateway](https://github.com/vinilana/jev-gateway)** — 把 Jev 接进编程智能体，用于工具调用的推理判断。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★121 · vinilana · `TS`</sub>

- **[skillranker](https://github.com/Dicklesworthstone/skillranker)** — 用当前会话上下文给智能体的技能排序以决定下一步，带 Claude Code hook。
  <sub>`插件` · ★110 · dicklesworthstone · `Rs` · ⚠ `无许可证`</sub>

- **[fastbrowse](https://github.com/agent-labs-dev/fastbrowse)** — 快速浏览器智能体：Jev 从页面现有内容里挑动作，LLM 负责阅读与规划。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★94 · agent-labs-dev · `Py`</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)** — 一个完全不含语言模型的 tool calling 聊天机器人：一次请求同时问清请求类型、该调哪个工具、以及每个工具的参数。
  <sub>`开源项目` · ★86 · `TS` · `choice` · `noul`</sub>

- **[jev-dsh-decision](https://github.com/Devin-AXIS/jev-dsh-decision)** — Jev DSH 决策引擎：面向 Agent Harness 的结构化决策插件，原生支持 DeepSeek Harness。 <sub>(机翻)</sub>
  <sub>`插件` · ★85 · devin-axis · `JS` · ⚠ `无许可证`</sub>

- **[neo4jev](https://github.com/jexp/neo4jev)** — 把 Jev 塞进知识图谱。每走到一个节点，判断下一条最值得走的边，再一路找下去。
  <sub>`开源项目` · ★83 · `Py` · `choice`</sub>

- **[windtunnel](https://github.com/nekuda-ai/WindTunnel)** — 一个 WebMCP 基准，衡量 WebMCP 与其他浏览器智能体接口的差距。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★76 · nekuda-ai · `TS`</sub>

- **[jev-desktop](https://github.com/yikangy873-gif/jev-desktop)** — 在 Codex Computer Use 内部做动作选择。 <sub>(机翻)</sub>
  <sub>`插件` · ★60 · yikangy873-gif · `JS`</sub>

- **[jev-libero](https://github.com/Dimweaker/jev-libero)** — 精细的机器人控制，带物理预览与可配置的 LIBERO 任务。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★52 · dimweaker · `Py`</sub>

- **[jev-reviewer](https://github.com/choxos/jev-reviewer)** — 系统综述的数据抽取：让 Jev 从论文及其补充材料里按抽取表取值，并附原文引用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★32 · choxos · `JS`</sub>

- **[robojev](https://github.com/lykycy123/RoboJEV)** — 在 MuJoCo 里对 Franka Panda 做两阶段 JEV 控制。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★29 · lykycy123 · `Py`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — 只读的交易日志与复盘 harness：Jev 类型化判断、智能体集成，以及一个可复现的金融基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★26 · myc0576 · `Py`</sub>

- **[pi-jev-auto-mode](https://github.com/jomatsu/pi-jev-auto-mode)** — 给 Pi 编程智能体做的自动模式：在语义层面自动批准 bash、写入和编辑类工具调用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★23 · jomatsu · `TS`</sub>

- **[tsai-sc](https://github.com/phyous/tsai-sc)** — 通过键鼠操作一款 90 年代即时战略游戏，并记录每次动作的概率。
  <sub>`开源项目` · ★22 · phyous · `Py`</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — 给所有编程智能体做的自动模式：结合会话上下文给每次工具调用打风险分（拒绝／询问／放行）。 <sub>(机翻)</sub>
  <sub>`插件` · ★21 · leepokai · `JS`</sub>

- **[OneVOneJev](https://github.com/emrickgarrett/OneVOneJev)** — 浏览器里的 1v1 FPS。每个决策 tick 都要判断走位、视角、瞄准、开火和跳跃。
  <sub>`开源项目` · ★20 · `TS` · `choice` · ⚠ `代码未实测` `无许可证`</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)** — 开源的 macOS computer use 与原生 GUI 自动化，运行在 Apple 芯片上。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★19 · jcpsimmons · `JS`</sub>

- **[jevalyn](https://github.com/Ray-Hughes/jevalyn)** — 给 Rails 应用的决策层：对 Jev System One API 的 Rails 原生封装。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★17 · ray-hughes · `Rb`</sub>

- **[jev-for-chrome](https://github.com/chy4pro/jev-for-chrome)** — Jev for Chrome：用亚秒级决策模型驱动你正在看的那个标签页。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★16 · chy4pro · `TS`</sub>

- **[jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab)** — 多无人机自主实验室：展示 Jev 的反射式决策，可选叠加 System 2 战略指导。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★15 · khordoo · `TS` · ⚠ `无许可证`</sub>

- **[jev-use](https://github.com/shitianfang/jev-use)** — 一个智能体插件：把不需要文本输出的步骤交给 Jev，而不是主模型。
  <sub>`插件` · ★15 · shitianfang · `JS`</sub>

- **[live-jev](https://github.com/vinilana/live-jev)** — 浏览器里的 2D 自动驾驶仿真，由 Jev 决策模型驱动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★15 · vinilana · `JS` · ⚠ `无许可证`</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — 用 Jev 给收件箱分类：打标、移动、标记、通知，全部配置驱动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★14 · parth-kp · `Py`</sub>

- **[evoke](https://github.com/evoke-build/evoke)** — 反射式软件：一句话变成对一个小程序的调用，由 Jev 选择。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10 · evoke-build · `Rs`</sub>

- **[jev-askable-arm](https://github.com/TarunTomar122/jev-askable-arm)** — 在仿真机械臂上执行零样本英文目标：Jev 串联写死的原语动作。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10 · taruntomar122 · `Py`</sub>

- **[jev-harness](https://github.com/AntonioCoppe/jev-harness)** — Jev 决策 harness：置信闸门、影子模式、配方与评测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★9 · antoniocoppe · `TS`</sub>

- **[super-jev](https://github.com/Kevthetech143/super-jev)** — 小而可扩展的「决策到动作」harness。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · kevthetech143 · `Py`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — 可观测的浏览器潜行游戏：Jev 做类型化的守卫判断，确定性代码掌管世界规则。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · abdelstark · `TS`</sub>

- **[jev-doom-agent](https://github.com/lukaske/jev-doom-agent)** — 浏览器原生的 Doom 智能体实验，带结构化空间状态与实时决策遥测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · lukaske · `TS` · ⚠ `无许可证`</sub>

- **[pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)** — 给 pi 编程智能体的运行时约束：每个有副作用的工具调用执行前，先对照你说过的话检查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · nyarlathoteppppp · `TS`</sub>

- **[jev-agent-browser](https://github.com/forvela/jev-agent-browser)** — 由 Jev 驱动的快速有界浏览器智能体：类型化动作、调研、分类与安全编排。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · forvela · `JS`</sub>

- **[bicameral](https://github.com/AbdelStark/bicameral)** — 混合式编程 harness：System 2 负责写，System 1（Jev）负责反射式动作。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · abdelstark · `TS`</sub>

- **[slidepilot](https://github.com/harshil1712/slidepilot)** — 给 Slidev 做的语音驱动语义自动翻页，由 Cloudflare Agents 与 Jev 驱动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · harshil1712 · `TS`</sub>

- **[typesafe-jev](https://github.com/gtaras7/typesafe-jev)** — 用 Jev 筛选一整个文件夹的简历：类型化判断、可编辑的策略、免费重新打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · gtaras7 · `TS`</sub>

- **[jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study)** — 独立的 Jev 1.13.0 行为研究：报告、受控提示实验、原始结果与离线验证。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · rinnecoder · `Py`</sub>

- **[jev-mobile](https://github.com/Friedjof/jev-mobile)** — 结合 Mobile MCP 的快速 Android 结构化控制循环。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · friedjof · `Py`</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — 八个最小可运行示例：把 Jev 用在机械与电气工程场景。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · foadsf · `Py`</sub>

- **[jev-git](https://github.com/AkashPriyadarshii/jev-git)** — 亚秒级的 Git pre-commit / pre-push 语义反射闸门。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · akashpriyadarshii · `Rs`</sub>

- **[jev-ra](https://github.com/brnyxx/jev-ra)** — 给编程智能体的浏览器操作，号称比 browser-use 快 3–5 倍：每一步由 Jev 决策。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · brnyxx · `Py`</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — 基于 Jev 的类型化、策略驱动决策工作流：置信路由、回退与评测。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · hamakyo · `TS`</sub>

- **[pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)** — 一个 pi 扩展，把 Jev 判断暴露成五个 pi 工具，让模型能做狭义的语义判断。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · legacybridge-tech · `TS` · ⚠ `无许可证`</sub>

- **[tsai-civ2](https://github.com/phyous/tsai-civ2)** — 让 Jev 在浏览器里玩初代《文明 II》，实时展示动作概率。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · phyous · `Py` · ⚠ `无许可证`</sub>

- **[jev-browser-skill](https://github.com/zurfyx/jev-browser-skill)** — 让约 100 毫秒的 Jev 决策模型驱动你的浏览器 —— 给 Claude Code 和 Codex 的即插即用技能。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · zurfyx · `JS`</sub>

- **[jev-engineering](https://github.com/eugeniughelbur/jev-engineering)** — 面向 AI 智能体的决策层：约 400 毫秒、两百分之一美分的类型化校准决策，用于拦截工具调用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · eugeniughelbur · `Py`</sub>

- **[Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py)** — 一次问清操作本身、以及每个可能操作各自的目标 —— 于是浏览器的一步永远不需要第二次往返。
  <sub>`代码片段` · `Py` · `choice` · `noul` · ⚠ `代码未实测`</sub>

- **[Example: tool selection with a none option](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/04-tool-selection/main.py)** — 把「选哪个工具」的 choice 和「到底需不需要工具」的 noul 配对使用 —— 因为这是两个不同的问题。
  <sub>`代码片段` · `Py` · `choice` · `noul` · ⚠ `代码未实测`</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — 给 AI 智能体的免费类型化判断：把分类／筛查／打分／校验卸载给 Jev。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · yuyang2230 · `Py`</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — 给 Jev 的有限样本保证：用保形风险控制把校准概率转成可证的约束。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · nikkoxgonzales · `Py`</sub>

- **[snake-jev](https://github.com/siroccomask/snake-jev)** — 由并行 Jev 判断控制的贪吃蛇，每个游戏 tick 一次 API 调用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · siroccomask · `Py`</sub>

- **[Jev (Fully Tested) + Browser Use: FASTEST AI Agent I'VE TRIED YET!](https://www.youtube.com/watch?v=SNJ3yuJ_QwY)** — 把 Jev 接到 Browser Use 上，驱动一个浏览器自动化智能体。
  <sub>`视频` · AICodeKing · ⚠ `宣称未核实`</sub>

### 意图路由

_判断用户意图，把请求分流到正确的分支。_

- **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐ — 一个可运行的智能家居助手示例，用类型化决策来解析用户请求。
  <sub>`官方文档` · `Py`</sub>

- **[Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing)** ⭐ — 把 confidence 当作第二个维度：答案告诉你「是什么」，置信度告诉你「该不该照它执行」。
  <sub>`官方文档` · `Py`</sub>

- **[Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing)** ⭐ — 对进来的请求做分类，路由到足够用的最便宜那个处理方：确定性代码、专用 LLM、或人。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。
  <sub>`开源项目` · ★187,482 · `Py` · `choice` · `score` · `noul`</sub>

- **[Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html)** — 把下游任务 id 变成 choice 的选项集，并用最小置信度闸门把不确定的运行转给人处理。
  <sub>`平台集成` · ★46,934 · `Py` · `choice`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)** — 七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。
  <sub>`开源项目` · ★12,278 · `TS` · `choice` · `noul`</sub>

- **[Real Python: hello-jev](https://github.com/realpython/materials/tree/master/hello-jev)** — 带对照组的教学示例：同一个问询台任务，一份是只认 Y/N 的纯 Python 写法，旁边是一个能读出意图的 Noul。
  <sub>`教程` · ★5,205 · Real Python · `Py` · `noul`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。
  <sub>`教程` · ★4,559 · `Py` · `choice` · `score` · `noul`</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** — 一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。
  <sub>`开源项目` · ★1,950 · `Java` · `choice` · `score` · `noul`</sub>

- **[foreman](https://github.com/thruwire/foreman)** — 一个「软件工厂工头」，用 Jev 决定智能体流水线下一步该做什么。
  <sub>`开源项目` · ★482 · thruwire · `Py`</sub>

- **[jev-search](https://github.com/superagents-lab/jev-search)** — Jev 驱动的网页搜索：先选时间窗口和最佳查询改写，再分批对结果逐条用 noul 重排。
  <sub>`开源项目` · ★390 · `TS` · `choice` · `noul`</sub>

- **[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)** — 语音驱动的浏览器控制：目标选项每次请求都按当前实时元素列表重建，并且总是包含一个 none 选项。
  <sub>`开源项目` · ★222 · `JS` · `choice` · `score` · `noul`</sub>

- **[hyperedit](https://github.com/kevinbadi/hyperedit)** — 一个 AI 视频编辑器：把编辑指令路由到具体操作、目标片段和轨道，并以关键词路由作为兜底。
  <sub>`开源项目` · ★179 · `TS` · `choice` · `noul` · ⚠ `无许可证`</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)** — 一个完全不含语言模型的 tool calling 聊天机器人：一次请求同时问清请求类型、该调哪个工具、以及每个工具的参数。
  <sub>`开源项目` · ★86 · `TS` · `choice` · `noul`</sub>

- **[jev-social](https://github.com/socai-io/jev-social)** — 社交平台调研，带类型化路由和浏览器取证。
  <sub>`开源项目` · ★46 · socai-io · `JS`</sub>

- **[ha-jev](https://github.com/AboveColin/HA-Jev)** — 一个 Home Assistant 集成：把类型化答案变成传感器，并提供可用于自动化的动作。
  <sub>`平台集成` · ★45 · abovecolin · `Py`</sub>

- **[hono-jev-router](https://github.com/yusukebe/hono-jev-router)** — 按语义路由 HTTP 请求 —— 给 Web 框架做的语义路由器。
  <sub>`开源项目` · ★45 · yusukebe · `TS`</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — 用 Jev 给收件箱分类：打标、移动、标记、通知，全部配置驱动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★14 · parth-kp · `Py`</sub>

- **[jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench)** — 在 2000 封钓鱼邮件上对比 Jev 与一个轻量 LLM：准确率、校准度、延迟、成本。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★3 · anisselbd · `Py` · ⚠ `无许可证`</sub>

- **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)** — 技术密度最高的独立讲解：JS / Python / AI SDK 三种代码、三种应答结构、进阶模式，还诚实列出了模型的失效场景。
  <sub>`教程` · Flavio Copes · `JS` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Example: confidence-gated escalation](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-confidence-gate/main.py)** — 带「自动执行或转人工」闸门的路由；策略函数刻意留空 —— 阈值该定在哪，是你的决定。
  <sub>`代码片段` · `Py` · `choice` · ⚠ `代码未实测`</sub>

- **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)** — 逐个用例走一遍 —— 智能体路由、智能体内部的决策层、工单分拣 —— 每个都给出具体的选项集和示例响应。
  <sub>`教程` · Mehul Gupta · `Py` · `choice` · ⚠ `付费墙`</sub>

- **[Jev on Netlify AI Gateway](https://www.netlify.com/changelog/typesafe-jev-ai-gateway/)** — 在 Netlify function 里零配置调用：直接用官方 SDK，不需要 API key、baseURL 或 provider 配置，按 Netlify credits 计费。
  <sub>`平台集成` · `TS` · `choice`</sub>

- **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)** — LangChain 集成：一个分类器，外加用于模型路由、以及在高风险工具调用执行前拦截它的实验性 middleware。
  <sub>`平台集成` · `Py` · `choice` · `score` · `noul` · ⚠ `需早期访问`</sub>

- **[Using TypeSafe Jev with the AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk)** — Vercel 最完整的实操指南：单问题与多问题调用、按概率阈值路由，以及用 mock evaluation 模型写单元测试。
  <sub>`教程` · `TS` · `noul` · `choice` · `score`</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。
  <sub>`开源项目` · ⚠ `宣称未核实`</sub>

### 上下文压缩

_判断哪些工具调用和结果仍然相关，从而丢弃过期上下文。_

- **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)** — 把 Jev 压缩方案移植过来，与自家在用的摘要器对比实测，最后公开结论：不采用。
  <sub>`基准测试` · ★247,881 · `Py` · `noul`</sub>

- **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)** — 把记忆召回的整套检索栈替换掉 —— 不用 embedding、不用 BM25、不用重排器 —— 改为对每条候选记忆批量问一个 Noul。
  <sub>`开源项目` · ★19,996 · `Rs` · `noul`</sub>

- **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** — 一个 Claude Code 插件，用逐条决策取代压缩式摘要：过期的工具调用被丢弃或截断，保留下来的全部逐字不变。
  <sub>`插件` · ★6,090 · tamaratran · `TS` · `noul`</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** — 九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。
  <sub>`插件` · ★408 · `Py` · `choice` · `score` · `noul`</sub>

- **[compact-adviser](https://github.com/kunchenguid/compact-adviser)** — 判断工作是否已完成或已记录，据此提示运行上下文压缩。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★174 · kunchenguid · `TS`</sub>

- **[jev-pruner](https://github.com/tamaratran/jev-pruner)** — 在模型看到之前先修剪冗长的 shell 输出，每个片段问一个 Noul。
  <sub>`插件` · ★137 · tamaratran · `TS` · `noul`</sub>

- **[Winnow](https://github.com/GhalebDweikat/winnow)** — 给 Claude Code 做上下文垃圾回收。Read / Bash / Grep 吐一大堆时，Jev 先判断哪些真和当前任务有关。
  <sub>`插件` · ★59 · `Py` · `noul`</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — 给 Claude Code 和 Codex 做的上下文裁剪代理：由 Jev 判断哪些历史还需要 —— 实测而非宣称。 <sub>(机翻)</sub>
  <sub>`插件` · ★22 · compozy · `TS`</sub>

- **[omp-jev-compaction](https://github.com/jerryfane/omp-jev-compaction)** — 给 omp 做的逐字保留式 Jev 打分上下文削减。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · jerryfane · `TS`</sub>

- **[pi-jev-context](https://github.com/Nyarlathoteppppp/pi-jev-context)** — 一个 Pi 扩展：感知新鲜度的读取去重、Jev 日志过滤，模型表现优先、省 token 其次。 <sub>(机翻)</sub>
  <sub>`插件` · ★6 · nyarlathoteppppp · `TS`</sub>

- **[jselect](https://github.com/keltokhy/jselect)** — 在 token 预算内给 AI 挑出有用证据：快速、带来源链接的上下文选择器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · keltokhy · `Py`</sub>

### 安全闸门

_在执行前判断一个动作是否安全。属纵深防御，绝不是安全边界。_

- **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐ — 给每条召回的段落打分，再由代码决定哪些能进入回答模型 —— 矛盾的标记保留，夹带提示注入的直接丢弃。
  <sub>`官方文档` · `Py`</sub>

- **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐ — 用一次请求筛查 LLM 应用的每一条进出消息，既点明风险类型、又给「照做会造成多大危害」打分。
  <sub>`官方文档` · `Py` · `noul` · `score`</sub>

- **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)** — 作为审核 API 的直接替代：一次请求并行问多个 Noul，每个危害类别一个，且每条指令都带反注入前缀。
  <sub>`开源项目` · ★42,345 · `Go` · `noul`</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)** — 三个可独立安装的 Claude Code 插件 —— 护栏、模型路由、技能推荐 —— 各自带 hook 和测试。
  <sub>`插件` · ★30,899 · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)** — LangChain 集成的 JavaScript 对应版本，分类器与 middleware 形状一致。
  <sub>`平台集成` · ★18,214 · `TS` · `choice` · `score` · `noul`</sub>

- **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)** — 从三个维度审查每次工具调用：风险等级、用户是否授权、以及一个显式的提示注入压力检查。
  <sub>`开源项目` · ★6,338 · `TS` · `choice` · `noul`</sub>

- **[agentgateway: CI-validated LLM guardrail](https://github.com/agentgateway/agentgateway)** — 三个共用同一严重度量表的 Score 问题，两项以上越线即拦截请求，并且失败时默认关闭。
  <sub>`开源项目` · ★4,971 · `Rs` · `score`</sub>

- **[Jev-cu](https://github.com/Sac-Y/Jev-cu)** — 一个 computer-use 智能体：判断该对无障碍树里哪个元素操作，并单独用一个 noul 判断这个动作是否需要用户显式确认。
  <sub>`开源项目` · ★557 · `JS` · `choice` · `noul`</sub>

- **[vexjoy-agent](https://github.com/notque/vexjoy-agent)** — 带 Jev 智能路由的 AI 智能体：把大白话请求分派给合适的专家智能体。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★423 · notque · `Py`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。
  <sub>`插件` · ★253 · `JS` · `choice` · `score` · `noul`</sub>

- **[quackd](https://github.com/rokbenko/quackd)** — 统管所有机器人的 CLI：每台机器人配一个 LLM 作大脑，由 Jev 做决策。 <sub>(机翻)</sub>
  <sub>`插件` · ★228 · rokbenko · `Py`</sub>

- **[pi-jev](https://github.com/y0usaf/pi-jev)** — 给编程智能体做的决策层：一个可度量的工具调用闸门，外加一个返回校准答案的类型化提问。
  <sub>`插件` · ★135 · y0usaf · `TS`</sub>

- **[jev-drone](https://github.com/RomanSlack/jev-drone)** — 拿 Jev 控无人机。底层飞控继续负责稳定和安全，Jev 只做爬升、刹车、穿越障碍这类上层判断。
  <sub>`开源项目` · ★121 · `Py` · `choice` · `score` · `noul` · ⚠ `宣称未核实`</sub>

- **[jev-gateway](https://github.com/vinilana/jev-gateway)** — 把 Jev 接进编程智能体，用于工具调用的推理判断。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★121 · vinilana · `TS`</sub>

- **[youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection)** — 结合实时音频与字幕检测 YouTube 视频里的赞助片段。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★81 · trungdq88 · `JS` · ⚠ `无许可证`</sub>

- **[grok-bot-jev](https://github.com/Bodila51/grok-bot-jev)** — 把 Jev 接到 Grok Bot 上作为廉价决策层，含用量闸门与技能模板。 <sub>(机翻)</sub>
  <sub>`插件` · ★74 · bodila51 · `Py`</sub>

- **[jevals](https://github.com/openlayer-ai/jevals)** — 把智能体评测与护栏做成 Jev 决策：每条 trace 一次请求，成本不到一美分的零头。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★53 · openlayer-ai · `Py`</sub>

- **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)** — 一个 Discord 审核机器人：用 Choice 给每条消息定级、用 Noul 表示封禁紧急度，管理员一旦赦免，该消息会作为「安全先例」注入后续请求。
  <sub>`开源项目` · ★41 · brainstormity · `Py` · `choice` · `noul`</sub>

- **[is-malicious](https://github.com/luantak/is-malicious)** — 代码库扫描器，帮你避免运行恶意代码。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★22 · luantak · `TS`</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — 给所有编程智能体做的自动模式：结合会话上下文给每次工具调用打风险分（拒绝／询问／放行）。 <sub>(机翻)</sub>
  <sub>`插件` · ★21 · leepokai · `JS`</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)** — 开源的 macOS computer use 与原生 GUI 自动化，运行在 Apple 芯片上。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★19 · jcpsimmons · `JS`</sub>

- **[jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)** — 面向类型化决策模型的概率感知评测：校准度、选择性风险、延迟，以及可复现的基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★17 · abdelstark · `Py`</sub>

- **[patdown](https://github.com/tyler-dot-earth/patdown)** — 用 Jev 做拦截、引导与「模糊 lint」，让智能体遵守你的规则与约定。含 CLI 与 GitHub Action。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★14 · tyler-dot-earth · `TS` · ⚠ `无许可证`</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-jev)** — 类型化的 System One 决策、排序、校验，以及可选启用的 Hermes 工具闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★12 · keeltrace · `Py`</sub>

- **[pi-jev-router](https://github.com/mejiasd3v/pi-jev-router)** — 通过 Vercel AI Gateway 为 Pi 做自动模型路由。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★12 · mejiasd3v · `JS`</sub>

- **[jev-harness](https://github.com/AntonioCoppe/jev-harness)** — Jev 决策 harness：置信闸门、影子模式、配方与评测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★9 · antoniocoppe · `TS`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — 可观测的浏览器潜行游戏：Jev 做类型化的守卫判断，确定性代码掌管世界规则。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · abdelstark · `TS`</sub>

- **[augustus](https://github.com/24601/Augustus)** — 面向决策模型这一类别的 agent 技能：分类器、编解码器、专用 AR 头、System One。 <sub>(机翻)</sub>
  <sub>`插件` · ★6 · 24601 · `Py`</sub>

- **[daf-jev](https://github.com/docxology/daf-jev)** — 可组合的 Python 工具包：问题构造器、置信闸门等。 <sub>(机翻)</sub>
  <sub>`插件` · ★5 · docxology · `Py`</sub>

- **[diffjury](https://github.com/raihankhan-rk/diffjury)** — PR 风险路由器兼代码审查教练。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · raihankhan-rk · `TS` · ⚠ `无许可证`</sub>

- **[jev-block-android-ad](https://github.com/ufec/jev-block-android-ad)** — Android 上的通知与短信过滤：不是匹配关键词，而是由模型判断。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · ufec · `Kt`</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — 在一个它不可能见过的任务上做独立校准测试：900 条规则生成的支持工单。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★4 · scienthoon · `Py`</sub>

- **[jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab)** — 在 DSPy 工作流中对 Jev 决策做可复现的校准与选择性风险基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★3 · jmanhype · `Py`</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — 用 Jev 把 Claude Code 的技能清单削减约 75%：给每个已安装技能打相关性分，其余隐藏。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · shivampansuriya · `JS`</sub>

- **[jev-web-analyzer](https://github.com/replynodes/jev-web-analyzer)** — 看看 Jev 怎么评价你的 SaaS 网站。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · replynodes · `TS`</sub>

- **[jev-audio-beeper](https://github.com/santos-sanz/jev-audio-beeper)** — 用 Jev 类型化决策加 ffmpeg 实现的低延迟音频消音原型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · santos-sanz · `TS` · ⚠ `无许可证`</sub>

- **[jev-git](https://github.com/AkashPriyadarshii/jev-git)** — 亚秒级的 Git pre-commit / pre-push 语义反射闸门。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · akashpriyadarshii · `Rs`</sub>

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)** — 给 Spring WebFlux 的非阻塞 Starter，实现一个语义熔断器来检测静默故障。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · vicente-md · `Java` · ⚠ `无许可证`</sub>

- **[jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)** — 由 Jev 判断一批日志是否值得处理：类型化问题、置信闸门，不执行任何动作。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · jyatesdotdev · `Py`</sub>

- **[assay-001](https://github.com/jourdanlabs/assay-001)** — ASSAY-001：对 Jev 校准度与类型安全宣称的独立、预注册验证。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · jourdanlabs · `Py` · ⚠ `无许可证`</sub>

- **[Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)** — LangChain 的讲解兼集成实操：三种问题类型，加上模型路由、以及在高风险工具调用执行前拦截它。
  <sub>`文章` · Sydney Runkle, Hunter Lovell · `Py` · ⚠ `厂商自报`</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — 给 Jev 的有限样本保证：用保形风险控制把校准概率转成可证的约束。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · nikkoxgonzales · `Py`</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — 按 Jev 概率做 ORDER BY 能否给出站得住脚的排序？独立的排序、校准与不变量实测。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · yodablocks · `Py`</sub>

- **[jev-packs](https://github.com/dtduc-git/jev-packs)** — 证据门控的 Jev 问题包注册表：精选问题、黄金样例与实测证据。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · dtduc-git · `Py`</sub>

- **[jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)** — 衡量 Jev 在文件片段中识别真实密钥凭据的能力。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · teyhouse · `Py` · ⚠ `无许可证`</sub>

- **[jev-spam-eval](https://github.com/bitnovus/jev-spam-eval)** — 用 Jev 的 Noul 问题做零样本垃圾邮件过滤，并与 TF-IDF 基线对比。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · bitnovus · `Py`</sub>

- **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)** — LangChain 集成：一个分类器，外加用于模型路由、以及在高风险工具调用执行前拦截它的实验性 middleware。
  <sub>`平台集成` · `Py` · `choice` · `score` · `noul` · ⚠ `需早期访问`</sub>

- **[openclaw-typesafe-ai](https://github.com/Olli0103/openclaw-typesafe-ai)** — 给 OpenClaw 的可选类型化 Jev 决策，带 SecretRef 凭据与严格的 API 校验。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · olli0103 · `TS`</sub>

- **[progressgate](https://github.com/AshutoshVJTI/progressgate)** — 检测 AI 智能体循环中的语义停滞。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ashutoshvjti · `TS`</sub>

- **[wakegate](https://github.com/shitianfang/wakegate)** — 在唤醒一个休眠智能体之前，先问 Jev 这次唤醒是否值得一次完整的 LLM 轮次。失败时默认放行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · shitianfang · `TS`</sub>

### 输出校验

_在输出到达用户前，按评分标准检查模型产出。_

- **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐ — 用一个 Choice 对着原文核查引用是否错误或凭空编造，并用它的置信度把边缘情况标出来送审。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐ — 用一次请求筛查 LLM 应用的每一条进出消息，既点明风险类型、又给「照做会造成多大危害」打分。
  <sub>`官方文档` · `Py` · `noul` · `score`</sub>

- **[vexjoy-agent](https://github.com/notque/vexjoy-agent)** — 带 Jev 智能路由的 AI 智能体：把大白话请求分派给合适的专家智能体。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★423 · notque · `Py`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。
  <sub>`插件` · ★253 · `JS` · `choice` · `score` · `noul`</sub>

- **[jev-review](https://github.com/NiazMorshed2007/jev-review)** — 一个本地优先的 MCP 插件，供编程智能体做持续的代码质量审查。
  <sub>`插件` · ★198 · niazmorshed2007 · `TS`</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — 先用 tree-sitter 找出并排序方法，再把用户自写的 YAML 规则编译成 noul；严重度取评分量表的期望值，而不是概率最高的那一档。
  <sub>`开源项目` · ★168 · `JS` · `choice` · `score` · `noul`</sub>

- **[jev-eval-agent](https://github.com/vinilana/jev-eval-agent)** — 一个把评测工作通过类型化决策来路由的智能体。
  <sub>`开源项目` · ★103 · vinilana · `TS` · ⚠ `无许可证`</sub>

- **[formanator](https://github.com/timrogers/formanator)** — 从命令行和 MCP 客户端提交福利报销单。 <sub>(机翻)</sub>
  <sub>`插件` · ★99 · timrogers · `Rs`</sub>

- **[supercov](https://github.com/supercorp-ai/supercov)** — 给编程智能体用的代码质量与覆盖率判断，Rust 实现。
  <sub>`开源项目` · ★95 · supercorp-ai · `Rs`</sub>

- **[fastbrowse](https://github.com/agent-labs-dev/fastbrowse)** — 快速浏览器智能体：Jev 从页面现有内容里挑动作，LLM 负责阅读与规划。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★94 · agent-labs-dev · `Py`</sub>

- **[jev-lint](https://github.com/mizchi/jev-lint)** — 用 Jev 打分器给代码中的文本做 lint。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★70 · mizchi · `TS`</sub>

- **[jev-libero](https://github.com/Dimweaker/jev-libero)** — 精细的机器人控制，带物理预览与可配置的 LIBERO 任务。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★52 · dimweaker · `Py`</sub>

- **[vibecheck](https://github.com/RafalWilinski/vibecheck)** — Chrome 扩展：发推之前先用 Jev 给你的帖子做个氛围检查。 <sub>(机翻)</sub>
  <sub>`插件` · ★47 · rafalwilinski · `JS` · ⚠ `无许可证`</sub>

- **[jev-reviewer](https://github.com/choxos/jev-reviewer)** — 系统综述的数据抽取：让 Jev 从论文及其补充材料里按抽取表取值，并附原文引用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★32 · choxos · `JS`</sub>

- **[Canny](https://github.com/qkal/Canny)** — 防 Coding Agent 嘴硬说自己做完了。看工具输出、代码 diff 和测试结果，再判断完成声明靠不靠谱。
  <sub>`开源项目` · ★31 · `TS` · `noul` · `score`</sub>

- **[snifftest](https://github.com/DanRWilloughby/snifftest)** — 识别 AI 写作痕迹的文风 linter：零依赖，可计数规则外加一个判断模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★27 · danrwilloughby · `TS`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — 只读的交易日志与复盘 harness：Jev 类型化判断、智能体集成，以及一个可复现的金融基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★26 · myc0576 · `Py`</sub>

- **[jev-column-race](https://github.com/goodrahstar/jev-column-race)** — Jev 对比一个轻量 LLM：标注 1000 条应用评论，快 4.1 倍、便宜 7 倍。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★22 · goodrahstar · `JS`</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — 给 Claude Code 和 Codex 做的上下文裁剪代理：由 Jev 判断哪些历史还需要 —— 实测而非宣称。 <sub>(机翻)</sub>
  <sub>`插件` · ★22 · compozy · `TS`</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — 给所有编程智能体做的自动模式：结合会话上下文给每次工具调用打风险分（拒绝／询问／放行）。 <sub>(机翻)</sub>
  <sub>`插件` · ★21 · leepokai · `JS`</sub>

- **[invalidate](https://github.com/chopratejas/invalidate)** — AI 记忆的失效层：每条事实都有租期，新证据会终结它。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★15 · chopratejas · `Py`</sub>

- **[patdown](https://github.com/tyler-dot-earth/patdown)** — 用 Jev 做拦截、引导与「模糊 lint」，让智能体遵守你的规则与约定。含 CLI 与 GitHub Action。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★14 · tyler-dot-earth · `TS` · ⚠ `无许可证`</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-jev)** — 类型化的 System One 决策、排序、校验，以及可选启用的 Hermes 工具闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★12 · keeltrace · `Py`</sub>

- **[jevlint](https://github.com/iamtoomas/JevLint)** — 可配置的语义 lint，带文件级 NOUL 判断与一个「魔法字符串」插件。 <sub>(机翻)</sub>
  <sub>`插件` · ★11 · huntedman · `TS`</sub>

- **[jev-commit](https://github.com/valentynkit/jev-commit)** — 一个 pre-commit 钩子：一次调用判断提交信息与 diff 是否相符。
  <sub>`开源项目` · ★9 · valentynkit · `Py`</sub>

- **[jev-feels](https://github.com/Qew7/jev-feels)** — 把语义决策变成普通 Ruby —— feels?、decide、score，以及 Rails 校验与模式匹配。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · qew7 · `Rb`</sub>

- **[pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)** — 给 pi 编程智能体的运行时约束：每个有副作用的工具调用执行前，先对照你说过的话检查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · nyarlathoteppppp · `TS`</sub>

- **[augustus](https://github.com/24601/Augustus)** — 面向决策模型这一类别的 agent 技能：分类器、编解码器、专用 AR 头、System One。 <sub>(机翻)</sub>
  <sub>`插件` · ★6 · 24601 · `Py`</sub>

- **[riff](https://github.com/scale-venture-partners/riff)** — 小而快的文风 linter：ruff 式的规则编码，由 Jev 支撑。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · scale-venture-partners · `Py`</sub>

- **[citation-verifier](https://github.com/MarissaFamularo/citation-verifier)** — 核查每篇被引论文是否支持引用它的那句话：一个模型证明引文，Jev 打分，人来裁定。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · marissafamularo · `JS`</sub>

- **[diffjury](https://github.com/raihankhan-rk/diffjury)** — PR 风险路由器兼代码审查教练。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · raihankhan-rk · `TS` · ⚠ `无许可证`</sub>

- **[jev-block-android-ad](https://github.com/ufec/jev-block-android-ad)** — Android 上的通知与短信过滤：不是匹配关键词，而是由模型判断。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · ufec · `Kt`</sub>

- **[jev-oas-sentinel](https://github.com/ShuhanSun/jev-oas-sentinel)** — 用确定性检查加 Jev 语义判断，揪出藏在 OpenAPI 描述文字里的破坏性变更。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · shuhansun · `Py`</sub>

- **[jev-pref](https://github.com/doeixd/jev-pref)** — 把 AGENTS.md 里的偏好变成一个由 Jev 驱动的快速 AI linter。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · doeixd · `JS`</sub>

- **[jev-spec](https://github.com/nozomi-koborinai/jev-spec)** — 每次提交都检查规格漂移：用 Jev 对照你的 Markdown 规格检查代码。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · nozomi-koborinai · `TS`</sub>

- **[hermes-jev-plugin](https://github.com/ajensenwaud/hermes-jev-plugin)** — 给 Hermes Agent 的 Jev 决策工具：check／route／score／evaluate 四件套。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · ajensenwaud · `Py`</sub>

- **[jev-auto-router](https://github.com/miniLV/Jev-Auto-Router)** — 实验性的逐次调用 GPT 模型路由，通过 Jev 与一个本地 Rescue 层为 Codex 服务。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · minilv · `TS`</sub>

- **[jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study)** — 独立的 Jev 1.13.0 行为研究：报告、受控提示实验、原始结果与离线验证。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · rinnecoder · `Py`</sub>

- **[jevkit](https://github.com/ariel-frischer/jevkit)** — 用 Rust 写的快速 CLI：类型化决策，付费之前先离线 lint。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · ariel-frischer · `Rs`</sub>

- **[jod](https://github.com/mateonunez/jod)** — 构建在 Jev 之上的语义 schema：先在本地校验状态，再投影出类型化答案。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · mateonunez · `TS`</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — 八个最小可运行示例：把 Jev 用在机械与电气工程场景。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · foadsf · `Py`</sub>

- **[jev-scout](https://github.com/AkashPriyadarshii/jev-scout)** — 由 Jev 打分驱动的开源仓库与 crate 侦察工具。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · akashpriyadarshii · `Rs`</sub>

- **[limpet](https://github.com/noplan-inc/limpet)** — 一个 Stop 钩子，阻止编程智能体过早收工 —— 用大白话写规则，由 Jev 裁定。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · noplan-inc · `Py`</sub>

- **[tripwire](https://github.com/noelzappy/tripwire)** — 在用户看到之前先审判每一条 LLM 响应。提供 AI SDK middleware 与 OpenAI 兼容代理。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★2 · noelzappy · `TS`</sub>

- **[jev-review-action](https://github.com/fatwang2/jev-review-action)** — 可配置的 GitHub 提交审查与 PR 分类，不使用任何文本生成模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · fatwang2 · `JS`</sub>

- **[assay-001](https://github.com/jourdanlabs/assay-001)** — ASSAY-001：对 Jev 校准度与类型安全宣称的独立、预注册验证。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · jourdanlabs · `Py` · ⚠ `无许可证`</sub>

- **[human-compiler](https://github.com/asfarsadewa/human-compiler)** — 人类语言的编译器：粘贴文本，得到诊断，由 Jev 度量。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · asfarsadewa · `TS`</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — 给 AI 智能体的免费类型化判断：把分类／筛查／打分／校验卸载给 Jev。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · yuyang2230 · `Py`</sub>

- **[openclaw-typesafe-ai](https://github.com/Olli0103/openclaw-typesafe-ai)** — 给 OpenClaw 的可选类型化 Jev 决策，带 SecretRef 凭据与严格的 API 校验。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · olli0103 · `TS`</sub>

- **[plotveil](https://github.com/Dearest/plotveil)** — YouTube 评论的安静剧透拦截器：每条评论一次类型化 Noul 决策。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · dearest · `TS`</sub>

- **[pytest-jev](https://github.com/allebee/pytest-jev)** — 给 pytest 的语义断言：测试 LLM 应用输出的含义，由 Jev 判定。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · allebee · `Py`</sub>

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)** — 找到的唯一三方横评，每个模型分别调过提示词，且明确把范围限定在单一任务上、不做通用排名。
  <sub>`基准测试` · Near Here</sub>

- **[TypeSafe's Jev: Can decision models replace LLM judges?](https://arize.com/blog/typesafe-jev-llm-judge/)** — 汇总了目前已有的第三方评测，并讨论决策模型能在多大程度上顶替 LLM 评判者。
  <sub>`文章` · Laurie Voss</sub>

### 重试控制

_判断失败的步骤是否值得重试。_

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)** — 给 Spring WebFlux 的非阻塞 Starter，实现一个语义熔断器来检测静默故障。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · vicente-md · `Java` · ⚠ `无许可证`</sub>

### 人工升级

_用校准置信度决定哪些情况必须由人来看。_

- **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐ — 把年报分入 75 个行业组，再根据答案自身的置信度决定：报这个细分组，还是退回上一层的大类。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐ — 用一个 Choice 对着原文核查引用是否错误或凭空编造，并用它的置信度把边缘情况标出来送审。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐ — 判断两份商品目录间 450 个候选配对里哪些指的是同一个东西 —— 一个 Score 就够，它的三级正好对应三种可执行动作。
  <sub>`官方文档` · `Py` · `score`</sub>

- **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐ — 在内容审核决策里显式加入「不确定」这个选项，并衡量标签一致率与自动处置比例之间的取舍。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Self-consistency with nouls](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook)** ⭐ — 把不确定的概率转人工复核，同时保留底层的 noul 数值本身，而不是压成一个标签了事。
  <sub>`官方文档` · `Py` · `noul`</sub>

- **[Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing)** ⭐ — 把 confidence 当作第二个维度：答案告诉你「是什么」，置信度告诉你「该不该照它执行」。
  <sub>`官方文档` · `Py`</sub>

- **[Confidence](https://docs.typesafe.ai/confidence)** ⭐ — confidence 如何从概率分布推导出来，以及为什么在一种问题类型上调好的阈值不能挪到另一种上用。
  <sub>`官方文档`</sub>

- **[Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html)** — 把下游任务 id 变成 choice 的选项集，并用最小置信度闸门把不确定的运行转给人处理。
  <sub>`平台集成` · ★46,934 · `Py` · `choice`</sub>

- **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)** — 把工具目录编译成问题，再从答案还原出 tool call，并为「弃权」和「需确认」两种情况定义了专门的错误类型。
  <sub>`开源项目` · ★30,279 · `Py` · `choice`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)** — 七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。
  <sub>`开源项目` · ★12,278 · `TS` · `choice` · `noul`</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)** — 代码审查前先过一遍 Jev，把高风险改动挑出来，再交给更贵的大模型或人。带本地看板。
  <sub>`开源项目` · ★510 · `TS` · `choice` · `score` · `noul`</sub>

- **[jev-align](https://github.com/sutro-sh/jev-align)** — 从人类反馈出发，构建经过校准的决策函数。
  <sub>`开源项目` · ★271 · sutro-sh · `Py`</sub>

- **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)** — 独立的韩语实测笔记，报告仅仅把选项顺序倒过来，就能让概率移动到足以翻转 0.9 阈值的程度。
  <sub>`基准测试` · ★190 · `Py` · ⚠ `无许可证` `宣称未核实`</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — 用一套 TypeScript 接口对接 40 家 AI 供应商，覆盖生成、流式与决策三种推理形态。 <sub>(机翻)</sub>
  <sub>`插件` · ★137 · juspay · `TS`</sub>

- **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)** — 一个 Discord 审核机器人：用 Choice 给每条消息定级、用 Noul 表示封禁紧急度，管理员一旦赦免，该消息会作为「安全先例」注入后续请求。
  <sub>`开源项目` · ★41 · brainstormity · `Py` · `choice` · `noul`</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — 用你自己的标注数据校准 Jev 的问题：在标注样本上调 criteria，在留出集上确认。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★31 · smkrv · `TS`</sub>

- **[jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)** — 面向类型化决策模型的概率感知评测：校准度、选择性风险、延迟，以及可复现的基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★17 · abdelstark · `Py`</sub>

- **[jevalyn](https://github.com/Ray-Hughes/jevalyn)** — 给 Rails 应用的决策层：对 Jev System One API 的 Rails 原生封装。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★17 · ray-hughes · `Rb`</sub>

- **[jevwire](https://github.com/Brainwires/jevwire)** — 给智能体的 Jev 决策层：MCP server、可嵌入的 DecisionModel 库，以及一个只做升级的 Claude Code 插件。 <sub>(机翻)</sub>
  <sub>`插件` · ★15 · brainwires · `TS`</sub>

- **[jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router)** — 类型化、带置信度感知的 agent 技能路由。 <sub>(机翻)</sub>
  <sub>`插件` · ★13 · godsboy · `Py`</sub>

- **[jev-forge](https://github.com/zwliJay/jev-forge)** — 面向 Jev 式决策模型的开源训练与推理栈。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★11 · zwlijay · `Py` · ⚠ `并非 Jev` `无许可证`</sub>

- **[jevcal](https://github.com/abhixhek/jevcal)** — 对着一个 LLM 教师模型做校准、定阈值和漂移检查 —— 而不是靠猜。
  <sub>`开源项目` · ★10 · abhixhek · `Py`</sub>

- **[jev-harness](https://github.com/AntonioCoppe/jev-harness)** — Jev 决策 harness：置信闸门、影子模式、配方与评测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★9 · antoniocoppe · `TS`</sub>

- **[daf-jev](https://github.com/docxology/daf-jev)** — 可组合的 Python 工具包：问题构造器、置信闸门等。 <sub>(机翻)</sub>
  <sub>`插件` · ★5 · docxology · `Py`</sub>

- **[jev-block-android-ad](https://github.com/ufec/jev-block-android-ad)** — Android 上的通知与短信过滤：不是匹配关键词，而是由模型判断。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · ufec · `Kt`</sub>

- **[poorjev](https://github.com/rupeshpoojary9/poorjev)** — 开源的本地 Jev 替代品：一个有可证校准置信度的 System One 决策层。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★5 · rupeshpoojary9 · `Py` · ⚠ `并非 Jev`</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — 在一个它不可能见过的任务上做独立校准测试：900 条规则生成的支持工单。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★4 · scienthoon · `Py`</sub>

- **[qwen-rlcd](https://github.com/shamazharikh/qwen-rlcd)** — 基于 Qwen3.5-0.8B 的 Jev 风格校准决策模型（Choice／Score／Noul）。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★4 · shamazharikh · `Py` · ⚠ `并非 Jev` `无许可证`</sub>

- **[jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab)** — 在 DSPy 工作流中对 Jev 决策做可复现的校准与选择性风险基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★3 · jmanhype · `Py`</sub>

- **[jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench)** — 在 2000 封钓鱼邮件上对比 Jev 与一个轻量 LLM：准确率、校准度、延迟、成本。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★3 · anisselbd · `Py` · ⚠ `无许可证`</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — 基于 Jev 的类型化、策略驱动决策工作流：置信路由、回退与评测。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · hamakyo · `TS`</sub>

- **[pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)** — 一个 pi 扩展，把 Jev 判断暴露成五个 pi 工具，让模型能做狭义的语义判断。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · legacybridge-tech · `TS` · ⚠ `无许可证`</sub>

- **[jev-eval](https://github.com/4esv/jev-eval)** — 在你自己的标注分类数据上，把 Jev 与任意 OpenRouter 模型做基准对比：准确率与校准度。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · 4esv · `Py` · ⚠ `无许可证`</sub>

- **[jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)** — 由 Jev 判断一批日志是否值得处理：类型化问题、置信闸门，不执行任何动作。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · jyatesdotdev · `Py`</sub>

- **[padflow-jev-evals](https://github.com/zsavage8/padflow-jev-evals)** — 来自某土地开发 SaaS 的类型化决策基准：schema、匿名标注数据与运行器。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · zsavage8 · `Py`</sub>

- **[assay-001](https://github.com/jourdanlabs/assay-001)** — ASSAY-001：对 Jev 校准度与类型安全宣称的独立、预注册验证。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · jourdanlabs · `Py` · ⚠ `无许可证`</sub>

- **[Example: confidence-gated escalation](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-confidence-gate/main.py)** — 带「自动执行或转人工」闸门的路由；策略函数刻意留空 —— 阈值该定在哪，是你的决定。
  <sub>`代码片段` · `Py` · `choice` · ⚠ `代码未实测`</sub>

- **[jev-calibration-audit](https://github.com/jujumilk3/jev-calibration-audit)** — 仅通过 API 对 Jev 做的独立校准审计。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · jujumilk3 · `Py`</sub>

- **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)** — 找到的最好的独立实测：固定单一模型版本、24 份挪威语文档，开篇就展示了一个模型答错、但同时正确报出低置信度的案例。
  <sub>`基准测试` · Lindfors</sub>

### 模型路由

_选择由哪个下游模型或档位处理请求。_

- **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐ — 「小模型 → 校验 → 推理模型」的两段级联，用一小部分成本拿到接近大推理模型的质量。
  <sub>`官方文档` · `Py`</sub>

- **[Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing)** ⭐ — 对进来的请求做分类，路由到足够用的最便宜那个处理方：确定性代码、专用 LLM、或人。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)** — 三个可独立安装的 Claude Code 插件 —— 护栏、模型路由、技能推荐 —— 各自带 hook 和测试。
  <sub>`插件` · ★30,899 · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)** — LangChain 集成的 JavaScript 对应版本，分类器与 middleware 形状一致。
  <sub>`平台集成` · ★18,214 · `TS` · `choice` · `score` · `noul`</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)** — 代码审查前先过一遍 Jev，把高风险改动挑出来，再交给更贵的大模型或人。带本地看板。
  <sub>`开源项目` · ★510 · `TS` · `choice` · `score` · `noul`</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** — 九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。
  <sub>`插件` · ★408 · `Py` · `choice` · `score` · `noul`</sub>

- **[jev-codex-router](https://github.com/0xNatoshi/jev-codex-router)** — 先让 Jev 判断这一轮编程任务有多难，再决定模型档位、推理深度和速度模式。
  <sub>`插件` · ★188 · `JS` · `choice` · `score`</sub>

- **[jevrouter](https://github.com/BillionsBobby/JevRouter)** — 面向模型、工具和子智能体的路由器。
  <sub>`开源项目` · ★151 · billionsbobby · `TS`</sub>

- **[jev-eval-agent](https://github.com/vinilana/jev-eval-agent)** — 一个把评测工作通过类型化决策来路由的智能体。
  <sub>`开源项目` · ★103 · vinilana · `TS` · ⚠ `无许可证`</sub>

- **[jev-use](https://github.com/shitianfang/jev-use)** — 一个智能体插件：把不需要文本输出的步骤交给 Jev，而不是主模型。
  <sub>`插件` · ★15 · shitianfang · `JS`</sub>

- **[pi-jev-router](https://github.com/mejiasd3v/pi-jev-router)** — 通过 Vercel AI Gateway 为 Pi 做自动模型路由。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★12 · mejiasd3v · `JS`</sub>

- **[jev-router](https://github.com/prismhq/jev-router)** — 开源 LLM 路由器，在 LiteLLM 之上用 Jev 选模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · prismhq · `Py`</sub>

- **[jev-auto-router](https://github.com/miniLV/Jev-Auto-Router)** — 实验性的逐次调用 GPT 模型路由，通过 Jev 与一个本地 Rescue 层为 Codex 服务。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · minilv · `TS`</sub>

- **[tiershift](https://github.com/iamvatsalpatel/tiershift)** — 把每次 LLM 调用下沉到能胜任的最便宜模型，路由由 Jev 在约 180 毫秒内决定，无需训练。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · iamvatsalpatel · `TS`</sub>

- **[janus](https://github.com/FirasSX914/Janus)** — 先在你自己的数据上衡量何时该用 Jev、何时该用别的模型，再据此路由。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · firassx914 · `Py`</sub>

- **[jev-engineering](https://github.com/eugeniughelbur/jev-engineering)** — 面向 AI 智能体的决策层：约 400 毫秒、两百分之一美分的类型化校准决策，用于拦截工具调用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · eugeniughelbur · `Py`</sub>

- **[Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)** — LangChain 的讲解兼集成实操：三种问题类型，加上模型路由、以及在高风险工具调用执行前拦截它。
  <sub>`文章` · Sydney Runkle, Hunter Lovell · `Py` · ⚠ `厂商自报`</sub>

- **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)** — 逐个用例走一遍 —— 智能体路由、智能体内部的决策层、工单分拣 —— 每个都给出具体的选项集和示例响应。
  <sub>`教程` · Mehul Gupta · `Py` · `choice` · ⚠ `付费墙`</sub>

- **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)** — LangChain 集成：一个分类器，外加用于模型路由、以及在高风险工具调用执行前拦截它的实验性 middleware。
  <sub>`平台集成` · `Py` · `choice` · `score` · `noul` · ⚠ `需早期访问`</sub>

### 并行扇出

_把大量问题（包括推测性的）打包进一次请求，再由代码挑出真正用得上的答案。_

- **[Cookbook: Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions)** ⭐ — 对一篇长文提 13 个合规问题，证明全部打包进一次调用便宜得多、也快得多，而答案不变。
  <sub>`官方文档` · `Py`</sub>

- **[Pattern: Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out)** ⭐ — 把大量问题（包括可能用不上的）打包进一次请求，之后再由代码决定哪些答案真的用得上。
  <sub>`官方文档` · `Py`</sub>

- **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐ — 官方第一课：一条工单，一次请求里同时问一个 Choice、一个 Score 和一个 Noul，给了 Python / JS / cURL 三种写法。
  <sub>`官方文档` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。
  <sub>`开源项目` · ★187,482 · `Py` · `choice` · `score` · `noul`</sub>

- **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)** — 作为审核 API 的直接替代：一次请求并行问多个 Noul，每个危害类别一个，且每条指令都带反注入前缀。
  <sub>`开源项目` · ★42,345 · `Go` · `noul`</sub>

- **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)** — Browser Use 做的高速浏览器 Agent。Jev 每一步只判断「做什么、点哪个元素」，要打字才叫小模型。
  <sub>`开源项目` · ★16,758 · Browser Use · `Py` · `choice` · ⚠ `厂商自报`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。
  <sub>`教程` · ★4,559 · `Py` · `choice` · `score` · `noul`</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)** — 一个完全不含语言模型的 tool calling 聊天机器人：一次请求同时问清请求类型、该调哪个工具、以及每个工具的参数。
  <sub>`开源项目` · ★86 · `TS` · `choice` · `noul`</sub>

- **[jev-sift](https://github.com/kbhuw/jev-sift)** — 先分类，再选择性阅读：可移植的批量文本分类插件与 MCP 工具。 <sub>(机翻)</sub>
  <sub>`插件` · ★45 · kbhuw · `JS` · ⚠ `无许可证`</sub>

- **[pi-typesafe](https://github.com/DevMortimer/pi-typesafe)** — 给 Pi 用的 Jev 决策：批量评估工具、终端 playground，以及给扩展作者的类型化 API。 <sub>(机翻)</sub>
  <sub>`插件` · ★40 · devmortimer · `TS`</sub>

- **[OneVOneJev](https://github.com/emrickgarrett/OneVOneJev)** — 浏览器里的 1v1 FPS。每个决策 tick 都要判断走位、视角、瞄准、开火和跳跃。
  <sub>`开源项目` · ★20 · `TS` · `choice` · ⚠ `代码未实测` `无许可证`</sub>

- **[slop-grader](https://github.com/lukstei/slop-grader)** — 基于规则的文本评分器：每条规则并行跑过每一行，不跳读、不漏行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★13 · lukstei · `TS`</sub>

- **[jev-forge](https://github.com/zwliJay/jev-forge)** — 面向 Jev 式决策模型的开源训练与推理栈。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★11 · zwlijay · `Py` · ⚠ `并非 Jev` `无许可证`</sub>

- **[duckdb-jev](https://github.com/prasanthj/duckdb-jev)** — 高吞吐的原生 DuckDB 扩展，支持批量与流式的分类、打分与筛选。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · prasanthj · `C++`</sub>

- **[jev-tree](https://github.com/reachjalil/jev-tree)** — 在分类体系上做递归 Jev choice —— 在不突破 255 选项上限的前提下，从更多选项中做选择。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · reachjalil · `TS`</sub>

- **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)** — 技术密度最高的独立讲解：JS / Python / AI SDK 三种代码、三种应答结构、进阶模式，还诚实列出了模型的失效场景。
  <sub>`教程` · Flavio Copes · `JS` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py)** — 一次问清操作本身、以及每个可能操作各自的目标 —— 于是浏览器的一步永远不需要第二次往返。
  <sub>`代码片段` · `Py` · `choice` · `noul` · ⚠ `代码未实测`</sub>

- **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)** — 最小化的第一次调用：同时问一个 choice、一个 score 和一个 noul，并标注了容易踩的那几处不对称。
  <sub>`代码片段` · `Py` · `choice` · `score` · `noul` · ⚠ `代码未实测`</sub>

- **[Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/)** — Workers AI binding 与 REST 示例：一次调用同时问 noul、choice、score，并给出含逐答案置信度的完整响应。
  <sub>`平台集成` · `TS` · `sh` · `noul` · `choice` · `score`</sub>

- **[snake-jev](https://github.com/siroccomask/snake-jev)** — 由并行 Jev 判断控制的贪吃蛇，每个游戏 tick 一次 API 调用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · siroccomask · `Py`</sub>

- **[Using TypeSafe Jev with the AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk)** — Vercel 最完整的实操指南：单问题与多问题调用、按概率阈值路由，以及用 mock evaluation 模型写单元测试。
  <sub>`教程` · `TS` · `noul` · `choice` · `score`</sub>

### 检索与排序

_对来自廉价检索步骤的候选做打分或重排。_

- **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐ — 给每条召回的段落打分，再由代码决定哪些能进入回答模型 —— 矛盾的标记保留，夹带提示注入的直接丢弃。
  <sub>`官方文档` · `Py`</sub>

- **[Cookbook: Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find)** ⭐ — 对一份服务条款做语义检索：一次请求用 Choice 给 218 个行号打分，同时用 Noul 判断文档里到底有没有答案。
  <sub>`官方文档` · `Py` · `choice` · `noul`</sub>

- **[Cookbook: Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe)** ⭐ — 对 40 个法律检索问题各取 30 条 BM25 候选，按「问题-候选」逐对提问重排，top-1 与 top-10 准确率均大幅提升。
  <sub>`官方文档` · `Py`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。
  <sub>`开源项目` · ★187,482 · `Py` · `choice` · `score` · `noul`</sub>

- **[OpenViking: retrieval reranking](https://github.com/volcengine/OpenViking)** — 单次批量请求里对每个候选文档问一个 Noul，直接把「是」的概率当相关性分数。
  <sub>`开源项目` · ★38,384 · `Py` · `noul`</sub>

- **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)** — 两段式 MCP 工具检索：先用一个宽 Choice 对整个目录粗排，再给候选短名单配完整描述，每个候选各配一个 Noul 判断它到底是否胜任。
  <sub>`开源项目` · ★27,855 · `Py` · `choice` · `noul`</sub>

- **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)** — 把记忆召回的整套检索栈替换掉 —— 不用 embedding、不用 BM25、不用重排器 —— 改为对每条候选记忆批量问一个 Noul。
  <sub>`开源项目` · ★19,996 · `Rs` · `noul`</sub>

- **[LanceDB TypeSafeReranker](https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py)** — 向量数据库的重排器：对每条结果问一个 Noul，把「是」的概率当作绝对相关性分数 —— 可以跨查询比较。
  <sub>`开源项目` · ★11,496 · `Py` · `noul`</sub>

- **[no-mistakes: review context selection](https://github.com/kunchenguid/no-mistakes)** — 对每个候选文件打一个 Score 来挑选审查上下文；实测结果是：计费输入明显增加，而实际耗时几乎没改善。
  <sub>`基准测试` · ★8,598 · `Go` · `score`</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** — 一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。
  <sub>`开源项目` · ★1,950 · `Java` · `choice` · `score` · `noul`</sub>

- **[hippo-memory](https://github.com/kitfunso/hippo-memory)** — 受生物启发的智能体记忆：衰减、检索强化与巩固。零运行时依赖，基于 SQLite。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★752 · kitfunso · `TS`</sub>

- **[jev-search](https://github.com/superagents-lab/jev-search)** — Jev 驱动的网页搜索：先选时间窗口和最佳查询改写，再分批对结果逐条用 noul 重排。
  <sub>`开源项目` · ★390 · `TS` · `choice` · `noul`</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — 一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。
  <sub>`开源项目` · ★291 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。
  <sub>`插件` · ★253 · `JS` · `choice` · `score` · `noul`</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — 用一套 TypeScript 接口对接 40 家 AI 供应商，覆盖生成、流式与决策三种推理形态。 <sub>(机翻)</sub>
  <sub>`插件` · ★137 · juspay · `TS`</sub>

- **[jev-semgrep](https://github.com/uehaj/jev-semgrep)** — 按含义 grep，跨语言：Jev 给每一行按含义打分，可用 AND/OR/NOT 组合多个含义。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★125 · uehaj · `JS` · ⚠ `无许可证`</sub>

- **[skillranker](https://github.com/Dicklesworthstone/skillranker)** — 用当前会话上下文给智能体的技能排序以决定下一步，带 Claude Code hook。
  <sub>`插件` · ★110 · dicklesworthstone · `Rs` · ⚠ `无许可证`</sub>

- **[jev-shell-history](https://github.com/mrnugget/jev-shell-history)** — Fish 风格的 zsh 历史自动建议，由 Jev 排序而不是按时间。
  <sub>`开源项目` · ★96 · mrnugget · `TS` · ⚠ `无许可证`</sub>

- **[neo4jev](https://github.com/jexp/neo4jev)** — 把 Jev 塞进知识图谱。每走到一个节点，判断下一条最值得走的边，再一路找下去。
  <sub>`开源项目` · ★83 · `Py` · `choice`</sub>

- **[jegrep](https://github.com/can1357/jegrep)** — 语义 grep：用描述来找代码。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★76 · can1357 · `Rs`</sub>

- **[Blink](https://github.com/ellipsis-dev/blink)** — 把 Jev 当代码库导航器。每走到一层目录，就判断哪些文件和当前问题最相关，再继续往下找。
  <sub>`开源项目` · ★56 · `TS` · `choice` · ⚠ `无许可证`</sub>

- **[jev-social](https://github.com/socai-io/jev-social)** — 社交平台调研，带类型化路由和浏览器取证。
  <sub>`开源项目` · ★46 · socai-io · `JS`</sub>

- **[jgrep](https://github.com/keltokhy/jgrep)** — grep，但模式是一段描述：用 Jev 按含义过滤行，约 200 毫秒处理上千行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★17 · keltokhy · `Py`</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-jev)** — 类型化的 System One 决策、排序、校验，以及可选启用的 Hermes 工具闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★12 · keeltrace · `Py`</sub>

- **[jevql](https://github.com/kylemclaren/jevql)** — 给 Postgres 用的语义 SQL，由 Jev 驱动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★11 · kylemclaren · `Go`</sub>

- **[every](https://github.com/sufianetaouil/every)** — 对代码库里每一个函数问一个是非问题，几秒内得到排序结果 —— 模式本身是一个问题的 grep。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · sufianetaouil · `Py`</sub>

- **[jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench)** — 与专用重排模型在 14 个数据集上的独立横评。
  <sub>`基准测试` · ★5 · anessbelbati · `Py`</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — 用 Jev 把 Claude Code 的技能清单削减约 75%：给每个已安装技能打相关性分，其余隐藏。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · shivampansuriya · `JS`</sub>

- **[llama-index-jev](https://github.com/WiktorB2004/llama-index-jev)** — 由 Jev 驱动的 LlamaIndex 重排器与路由器 —— 类型化的分数与选择，比 LLM-as-judge 便宜。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · wiktorb2004 · `Py`</sub>

- **[jev-reranker](https://github.com/shinpr/jev-reranker)** — 用 Jev 对 JSON 搜索结果做重排、过滤与压缩。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · shinpr · `Rs`</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — 基于 Jev 的类型化、策略驱动决策工作流：置信路由、回退与评测。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · hamakyo · `TS`</sub>

- **[jev-engineering](https://github.com/eugeniughelbur/jev-engineering)** — 面向 AI 智能体的决策层：约 400 毫秒、两百分之一美分的类型化校准决策，用于拦截工具调用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · eugeniughelbur · `Py`</sub>

- **[jev-bfs](https://github.com/komikat/jev-bfs)** — 用 Jev 直接排序来跑维基百科链接竞速，带实时终端显示。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · komikat · `Py`</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — 按 Jev 概率做 ORDER BY 能否给出站得住脚的排序？独立的排序、校准与不变量实测。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · yodablocks · `Py`</sub>

- **[jevgrep](https://github.com/allebee/jevgrep)** — 按含义 grep：管道传入任意文本，用大白话问一个是非问题，只留下匹配的行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · allebee · `Py`</sub>

### 结构化抽取

_从杂乱文本中取出类型化字段 —— 靠在候选中选择，而不是生成。_

- **[Cookbook: Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook)** ⭐ — 抽取绝对与相对日期：先问文档里点明了哪些部分，再在代码里做解析与校验，并按置信度决定是否送审。
  <sub>`官方文档` · `Py`</sub>

- **[Cookbook: Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook)** ⭐ — 先用正则找出候选的邮箱、电话、金额，再让模型挑出被问到的那一段，于是代码拿到的是逐字原值。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐ — 用两次请求把丢了格式的纯文本还原成 Markdown：一次把硬换行的段落重新接起来，一次给每个块分类。
  <sub>`官方文档` · `Py`</sub>

- **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐ — 「小模型 → 校验 → 推理模型」的两段级联，用一小部分成本拿到接近大推理模型的质量。
  <sub>`官方文档` · `Py`</sub>

- **[jev-reviewer](https://github.com/choxos/jev-reviewer)** — 系统综述的数据抽取：让 Jev 从论文及其补充材料里按抽取表取值，并附原文引用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★32 · choxos · `JS`</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)** — 开源的 macOS computer use 与原生 GUI 自动化，运行在 Apple 芯片上。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★19 · jcpsimmons · `JS`</sub>

### 分类

_把条目归入分类体系，包括用概率遍历的深层层级。_

- **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐ — 把年报分入 75 个行业组，再根据答案自身的置信度决定：报这个细分组，还是退回上一层的大类。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification)** ⭐ — 用对 Choice 概率做并行 beam search 的方式，遍历专利、零售、生物医学、源码这几套很深的分类体系。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐ — 判断两份商品目录间 450 个候选配对里哪些指的是同一个东西 —— 一个 Score 就够，它的三级正好对应三种可执行动作。
  <sub>`官方文档` · `Py` · `score`</sub>

- **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐ — 用两次请求把丢了格式的纯文本还原成 Markdown：一次把硬换行的段落重新接起来，一次给每个块分类。
  <sub>`官方文档` · `Py`</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)** — 用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。
  <sub>`基准测试` · ★87,191 · `TS` · `choice` · ⚠ `仅影子运行`</sub>

- **[json-render](https://github.com/vercel-labs/json-render)** — Vercel Labs 的生成式 UI 框架。实验里 Jev 不逐 token 写 JSON，只负责选组件、属性和布局。
  <sub>`开源项目` · ★17,994 · Vercel Labs · `TS` · `choice`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)** — 七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。
  <sub>`开源项目` · ★12,278 · `TS` · `choice` · `noul`</sub>

- **[tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier)** — 基于 Jev 决策的税务文档分页分类器，在 261 种 IRS 表单上达到严格全对，每页约 $0.001。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★361 · kyotofin · `TS`</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — 一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。
  <sub>`开源项目` · ★291 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。
  <sub>`插件` · ★253 · `JS` · `choice` · `score` · `noul`</sub>

- **[docjev](https://github.com/jerryjliu/docjev)** — 非常快的文档分类与切分器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★207 · jerryjliu · `Py`</sub>

- **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)** — 独立的韩语实测笔记，报告仅仅把选项顺序倒过来，就能让概率移动到足以翻转 0.9 阈值的程度。
  <sub>`基准测试` · ★190 · `Py` · ⚠ `无许可证` `宣称未核实`</sub>

- **[unclutter](https://github.com/kitze/unclutter)** — 一个浏览器扩展，用可复用的模板规则清除页面杂物。
  <sub>`开源项目` · ★181 · kitze · `TS`</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — 先用 tree-sitter 找出并排序方法，再把用户自写的 YAML 规则编译成 noul；严重度取评分量表的期望值，而不是概率最高的那一档。
  <sub>`开源项目` · ★168 · `JS` · `choice` · `score` · `noul`</sub>

- **[pg_typesafe](https://github.com/giuliosmall/pg_typesafe)** — 用于 Jev 分类决策的 PostgreSQL 扩展（预 alpha）。 <sub>(机翻)</sub>
  <sub>`插件` · ★81 · giuliosmall · `C`</sub>

- **[youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection)** — 结合实时音频与字幕检测 YouTube 视频里的赞助片段。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★81 · trungdq88 · `JS` · ⚠ `无许可证`</sub>

- **[Prism](https://github.com/irfndi/prism-liquidity-agent)** — 不直接让 Jev 下单。它判断 toxic flow、市场压力、均值回归之类的状态，再交给原来的策略。
  <sub>`开源项目` · ★71 · `TS` · `choice` · `score`</sub>

- **[typesafe-adblock](https://github.com/realZachi/typesafe-adblock)** — 一个 Chrome 扩展，逐个询问 DOM 元素是不是广告。
  <sub>`开源项目` · ★68 · realzachi · `JS`</sub>

- **[Blink](https://github.com/ellipsis-dev/blink)** — 把 Jev 当代码库导航器。每走到一层目录，就判断哪些文件和当前问题最相关，再继续往下找。
  <sub>`开源项目` · ★56 · `TS` · `choice` · ⚠ `无许可证`</sub>

- **[ha-jev](https://github.com/AboveColin/HA-Jev)** — 一个 Home Assistant 集成：把类型化答案变成传感器，并提供可用于自动化的动作。
  <sub>`平台集成` · ★45 · abovecolin · `Py`</sub>

- **[jev-sift](https://github.com/kbhuw/jev-sift)** — 先分类，再选择性阅读：可移植的批量文本分类插件与 MCP 工具。 <sub>(机翻)</sub>
  <sub>`插件` · ★45 · kbhuw · `JS` · ⚠ `无许可证`</sub>

- **[commit-miner](https://github.com/devanshbatham/commit-miner)** — 用 Jev 对 Git 提交的 diff 与信息做分类：缺陷修复、安全修复、变更类型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★33 · devanshbatham · `Rs` · ⚠ `无许可证`</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — 用你自己的标注数据校准 Jev 的问题：在标注样本上调 criteria，在留出集上确认。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★31 · smkrv · `TS`</sub>

- **[SemDecide](https://github.com/sharziki/semdecide)** — 把 Jev 做成命令行。Shell 里直接分类、打分、过滤，适合接爬虫、CI 和数据流水线。
  <sub>`插件` · ★31 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[jev-column-race](https://github.com/goodrahstar/jev-column-race)** — Jev 对比一个轻量 LLM：标注 1000 条应用评论，快 4.1 倍、便宜 7 倍。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★22 · goodrahstar · `JS`</sub>

- **[jev-mcp](https://github.com/blakestone-x/jev-mcp)** — 一个 MCP server，把分类、打分、检查、匹配、筛选暴露给任意智能体。
  <sub>`插件` · ★18 · blakestone-x · `Py`</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — 用 Jev 给收件箱分类：打标、移动、标记、通知，全部配置驱动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★14 · parth-kp · `Py`</sub>

- **[jevframe](https://github.com/ktaletsk/jevframe)** — 给 pandas 和 Polars 的语义 AI：用自然语言问题对 DataFrame 的行做分类、情感分析与打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★12 · ktaletsk · `Py`</sub>

- **[evoke](https://github.com/evoke-build/evoke)** — 反射式软件：一句话变成对一个小程序的调用，由 Jev 选择。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10 · evoke-build · `Rs`</sub>

- **[jevlogs](https://github.com/reachjalil/jevlogs)** — 面向 OpenTelemetry 的开源 Jev 日志分拣：在昂贵的 LLM 分析之前先给信号打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★9 · reachjalil · `JS`</sub>

- **[jev-dsl](https://github.com/inanna-malick/jev-dsl)** — 面向智能体的 Haskell DSL：类型化数据包、类型推断，答案与问题同构。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · inanna-malick · `Hs`</sub>

- **[augustus](https://github.com/24601/Augustus)** — 面向决策模型这一类别的 agent 技能：分类器、编解码器、专用 AR 头、System One。 <sub>(机翻)</sub>
  <sub>`插件` · ★6 · 24601 · `Py`</sub>

- **[jev-agent-browser](https://github.com/forvela/jev-agent-browser)** — 由 Jev 驱动的快速有界浏览器智能体：类型化动作、调研、分类与安全编排。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · forvela · `JS`</sub>

- **[duckdb-jev](https://github.com/prasanthj/duckdb-jev)** — 高吞吐的原生 DuckDB 扩展，支持批量与流式的分类、打分与筛选。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · prasanthj · `C++`</sub>

- **[jev-document-classification](https://github.com/Charlyhno-eng/jev-document-classification)** — 对文本文档做快速且低成本的分类。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · charlyhno-eng · `TS`</sub>

- **[jev-skip](https://github.com/valentynkit/jev-skip)** — 读字幕、在观看时判断，从而跳过视频里的赞助段落。
  <sub>`开源项目` · ★3 · valentynkit · `TS`</sub>

- **[jev-tree](https://github.com/reachjalil/jev-tree)** — 在分类体系上做递归 Jev choice —— 在不突破 255 选项上限的前提下，从更多选项中做选择。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · reachjalil · `TS`</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — 八个最小可运行示例：把 Jev 用在机械与电气工程场景。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · foadsf · `Py`</sub>

- **[jev-ids](https://github.com/jev-ids/jev-ids)** — 基于 Jev 的高速、省 token 的入侵检测系统。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · jev-ids · `Py`</sub>

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)** — 给 Spring WebFlux 的非阻塞 Starter，实现一个语义熔断器来检测静默故障。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · vicente-md · `Java` · ⚠ `无许可证`</sub>

- **[jev-eval](https://github.com/4esv/jev-eval)** — 在你自己的标注分类数据上，把 Jev 与任意 OpenRouter 模型做基准对比：准确率与校准度。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · 4esv · `Py` · ⚠ `无许可证`</sub>

- **[jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)** — 由 Jev 判断一批日志是否值得处理：类型化问题、置信闸门，不执行任何动作。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · jyatesdotdev · `Py`</sub>

- **[jev-review-action](https://github.com/fatwang2/jev-review-action)** — 可配置的 GitHub 提交审查与 PR 分类，不使用任何文本生成模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · fatwang2 · `JS`</sub>

- **[jev-triage](https://github.com/cephalization/jev-triage)** — 拉取并同步大型仓库以做 issue 分拣。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · cephalization · `TS`</sub>

- **[discoprint](https://github.com/lirantal/discoprint)** — 用 Jev 按主题、情绪与歌词复杂度给一位艺人的全部作品分类，并可视化呈现。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · lirantal · `JS`</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — 给 AI 智能体的免费类型化判断：把分类／筛查／打分／校验卸载给 Jev。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · yuyang2230 · `Py`</sub>

- **[jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)** — 衡量 Jev 在文件片段中识别真实密钥凭据的能力。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · teyhouse · `Py` · ⚠ `无许可证`</sub>

- **[progressgate](https://github.com/AshutoshVJTI/progressgate)** — 检测 AI 智能体循环中的语义停滞。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ashutoshvjti · `TS`</sub>

- **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)** — 找到的最好的独立实测：固定单一模型版本、24 份挪威语文档，开篇就展示了一个模型答错、但同时正确报出低置信度的案例。
  <sub>`基准测试` · Lindfors</sub>

- **[Jev - The Ultimate Classification Model?](https://youtube.com/watch?v=X117w2Rark8)** — 一位 ML 工程师从分类任务角度做的讲解 —— 这个切入角度最贴近模型的实际能力。
  <sub>`视频` · Sam Witteveen</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。
  <sub>`开源项目` · ⚠ `宣称未核实`</sub>

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)** — 找到的唯一三方横评，每个模型分别调过提示词，且明确把范围限定在单一任务上、不做通用排名。
  <sub>`基准测试` · Near Here</sub>

### 机器学习特征抽取

_把自由文本转成数值特征，喂给下游的传统模型。_

- **[Cookbook: Autoresearch feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery)** ⭐ — 一个自动研究循环：自己提出问题、把自由文本转成数值特征、再用误差反过来改进下游的梯度提升回归模型。
  <sub>`官方文档` · `Py`</sub>

- **[nimble](https://github.com/bespokelabsai/nimble)** — 本地类型化决策、对比式数据筛选与模型评测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1,543 · bespokelabsai · `Py` · ⚠ `无许可证`</sub>

- **[jev-align](https://github.com/sutro-sh/jev-align)** — 从人类反馈出发，构建经过校准的决策函数。
  <sub>`开源项目` · ★271 · sutro-sh · `Py`</sub>

- **[Prism](https://github.com/irfndi/prism-liquidity-agent)** — 不直接让 Jev 下单。它判断 toxic flow、市场压力、均值回归之类的状态，再交给原来的策略。
  <sub>`开源项目` · ★71 · `TS` · `choice` · `score`</sub>

- **[jev-curate](https://github.com/AkashPriyadarshii/jev-curate)** — 拿 Jev 筛训练数据。JSONL / Parquet 先做质量、相关性和风险判断，再决定哪些进后面的训练。
  <sub>`开源项目` · ★21 · `Rs` · `score` · `noul`</sub>

- **[tiershift](https://github.com/iamvatsalpatel/tiershift)** — 把每次 LLM 调用下沉到能胜任的最便宜模型，路由由 Jev 在约 180 毫秒内决定，无需训练。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · iamvatsalpatel · `TS`</sub>

### 文档分拣

_对进来的文档、发票、表单做分类和路由。_

- **[tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier)** — 基于 Jev 决策的税务文档分页分类器，在 261 种 IRS 表单上达到严格全对，每页约 $0.001。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★361 · kyotofin · `TS`</sub>

- **[docjev](https://github.com/jerryjliu/docjev)** — 非常快的文档分类与切分器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★207 · jerryjliu · `Py`</sub>

- **[formanator](https://github.com/timrogers/formanator)** — 从命令行和 MCP 客户端提交福利报销单。 <sub>(机翻)</sub>
  <sub>`插件` · ★99 · timrogers · `Rs`</sub>

- **[jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas)** — 独立的、基于证据的能力地图：Jev 在哪些场景站得住、在哪些场景崩掉 —— 附真实 API 调用凭据。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★24 · zaious · `Py`</sub>

- **[jev-document-classification](https://github.com/Charlyhno-eng/jev-document-classification)** — 对文本文档做快速且低成本的分类。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · charlyhno-eng · `TS`</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。
  <sub>`开源项目` · ⚠ `宣称未核实`</sub>

### 工单分拣

_按意图和紧急度路由支持工单与会话。_

- **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐ — 官方第一课：一条工单，一次请求里同时问一个 Choice、一个 Score 和一个 Noul，给了 Python / JS / cURL 三种写法。
  <sub>`官方文档` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。
  <sub>`教程` · ★4,559 · `Py` · `choice` · `score` · `noul`</sub>

- **[spring-ai-typesafe](https://spring.io/blog/2026/09/21/spring-ai-typesafe-structured-judgment)** — 社区维护的 Spring AI starter，把类型化决策带到 Java，用 builder API 封装三种问题类型。
  <sub>`平台集成` · ★19 · `Java` · `choice` · `score` · `noul`</sub>

- **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)** — 最小化的第一次调用：同时问一个 choice、一个 score 和一个 noul，并标注了容易踩的那几处不对称。
  <sub>`代码片段` · `Py` · `choice` · `score` · `noul` · ⚠ `代码未实测`</sub>

- **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)** — 逐个用例走一遍 —— 智能体路由、智能体内部的决策层、工单分拣 —— 每个都给出具体的选项集和示例响应。
  <sub>`教程` · Mehul Gupta · `Py` · `choice` · ⚠ `付费墙`</sub>

- **[Jev on AI/ML API](https://docs.aimlapi.com/api-references/decision-models/typesafe/jev)** — 又一个网关接入路径，值得记一笔是因为它的端点路径和请求外壳跟原生 API、跟 Cloudflare 都不一样。
  <sub>`平台集成` · `Py` · `noul` · `choice` · `score`</sub>

- **[Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/)** — Workers AI binding 与 REST 示例：一次调用同时问 noul、choice、score，并给出含逐答案置信度的完整响应。
  <sub>`平台集成` · `TS` · `sh` · `noul` · `choice` · `score`</sub>

### 内容评分

_在有序量表上给质量、风险或相关性打分。_

- **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐ — 在内容审核决策里显式加入「不确定」这个选项，并衡量标签一致率与自动处置比例之间的取舍。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Pattern: Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring)** ⭐ — 把一个笼统的判断拆成若干原子评分，再用你自己代码里的权重（而不是提示词里的）组合起来。
  <sub>`官方文档` · `Py` · `score`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。
  <sub>`开源项目` · ★187,482 · `Py` · `choice` · `score` · `noul`</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)** — 用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。
  <sub>`基准测试` · ★87,191 · `TS` · `choice` · ⚠ `仅影子运行`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。
  <sub>`教程` · ★4,559 · `Py` · `choice` · `score` · `noul`</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** — 一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。
  <sub>`开源项目` · ★1,950 · `Java` · `choice` · `score` · `noul`</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)** — 代码审查前先过一遍 Jev，把高风险改动挑出来，再交给更贵的大模型或人。带本地看板。
  <sub>`开源项目` · ★510 · `TS` · `choice` · `score` · `noul`</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — 一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。
  <sub>`开源项目` · ★291 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[jev-review](https://github.com/NiazMorshed2007/jev-review)** — 一个本地优先的 MCP 插件，供编程智能体做持续的代码质量审查。
  <sub>`插件` · ★198 · niazmorshed2007 · `TS`</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — 先用 tree-sitter 找出并排序方法，再把用户自写的 YAML 规则编译成 noul；严重度取评分量表的期望值，而不是概率最高的那一档。
  <sub>`开源项目` · ★168 · `JS` · `choice` · `score` · `noul`</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — 用一套 TypeScript 接口对接 40 家 AI 供应商，覆盖生成、流式与决策三种推理形态。 <sub>(机翻)</sub>
  <sub>`插件` · ★137 · juspay · `TS`</sub>

- **[llm2jev](https://github.com/Yinsongxu/LLM2Jev)** — 把本地语言模型改造成 Jev 兼容的结构化决策引擎，输出 Choice、Score、Noul。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★127 · yinsongxu · `Py`</sub>

- **[jev-semgrep](https://github.com/uehaj/jev-semgrep)** — 按含义 grep，跨语言：Jev 给每一行按含义打分，可用 AND/OR/NOT 组合多个含义。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★125 · uehaj · `JS` · ⚠ `无许可证`</sub>

- **[supercov](https://github.com/supercorp-ai/supercov)** — 给编程智能体用的代码质量与覆盖率判断，Rust 实现。
  <sub>`开源项目` · ★95 · supercorp-ai · `Rs`</sub>

- **[jevmeter](https://github.com/ChetasLua/jevmeter)** — 给视频里的每一句话打分，并把结果渲染成一个实时仪表。
  <sub>`开源项目` · ★81 · chetaslua · `Py`</sub>

- **[killmyidea](https://github.com/monteduro/killmyidea)** — 输入一个创业点子，Jev 从多个维度打分，最后给你 KILL、FIX 或 SHIP。
  <sub>`开源项目` · ★78 · `TS` · `score` · `choice` · ⚠ `无许可证`</sub>

- **[jev-lint](https://github.com/mizchi/jev-lint)** — 用 Jev 打分器给代码中的文本做 lint。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★70 · mizchi · `TS`</sub>

- **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)** — 一个 Discord 审核机器人：用 Choice 给每条消息定级、用 Noul 表示封禁紧急度，管理员一旦赦免，该消息会作为「安全先例」注入后续请求。
  <sub>`开源项目` · ★41 · brainstormity · `Py` · `choice` · `noul`</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — 用你自己的标注数据校准 Jev 的问题：在标注样本上调 criteria，在留出集上确认。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★31 · smkrv · `TS`</sub>

- **[SemDecide](https://github.com/sharziki/semdecide)** — 把 Jev 做成命令行。Shell 里直接分类、打分、过滤，适合接爬虫、CI 和数据流水线。
  <sub>`插件` · ★31 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[snifftest](https://github.com/DanRWilloughby/snifftest)** — 识别 AI 写作痕迹的文风 linter：零依赖，可计数规则外加一个判断模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★27 · danrwilloughby · `TS`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — 只读的交易日志与复盘 harness：Jev 类型化判断、智能体集成，以及一个可复现的金融基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★26 · myc0576 · `Py`</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — 给 Claude Code 和 Codex 做的上下文裁剪代理：由 Jev 判断哪些历史还需要 —— 实测而非宣称。 <sub>(机翻)</sub>
  <sub>`插件` · ★22 · compozy · `TS`</sub>

- **[jev-curate](https://github.com/AkashPriyadarshii/jev-curate)** — 拿 Jev 筛训练数据。JSONL / Parquet 先做质量、相关性和风险判断，再决定哪些进后面的训练。
  <sub>`开源项目` · ★21 · `Rs` · `score` · `noul`</sub>

- **[jev-mcp](https://github.com/blakestone-x/jev-mcp)** — 一个 MCP server，把分类、打分、检查、匹配、筛选暴露给任意智能体。
  <sub>`插件` · ★18 · blakestone-x · `Py`</sub>

- **[jevalyn](https://github.com/Ray-Hughes/jevalyn)** — 给 Rails 应用的决策层：对 Jev System One API 的 Rails 原生封装。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★17 · ray-hughes · `Rb`</sub>

- **[slop-grader](https://github.com/lukstei/slop-grader)** — 基于规则的文本评分器：每条规则并行跑过每一行，不跳读、不漏行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★13 · lukstei · `TS`</sub>

- **[jevframe](https://github.com/ktaletsk/jevframe)** — 给 pandas 和 Polars 的语义 AI：用自然语言问题对 DataFrame 的行做分类、情感分析与打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★12 · ktaletsk · `Py`</sub>

- **[jev-forge](https://github.com/zwliJay/jev-forge)** — 面向 Jev 式决策模型的开源训练与推理栈。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★11 · zwlijay · `Py` · ⚠ `并非 Jev` `无许可证`</sub>

- **[jevlint](https://github.com/iamtoomas/JevLint)** — 可配置的语义 lint，带文件级 NOUL 判断与一个「魔法字符串」插件。 <sub>(机翻)</sub>
  <sub>`插件` · ★11 · huntedman · `TS`</sub>

- **[jevlogs](https://github.com/reachjalil/jevlogs)** — 面向 OpenTelemetry 的开源 Jev 日志分拣：在昂贵的 LLM 分析之前先给信号打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★9 · reachjalil · `JS`</sub>

- **[jev-feels](https://github.com/Qew7/jev-feels)** — 把语义决策变成普通 Ruby —— feels?、decide、score，以及 Rails 校验与模式匹配。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · qew7 · `Rb`</sub>

- **[omp-jev-compaction](https://github.com/jerryfane/omp-jev-compaction)** — 给 omp 做的逐字保留式 Jev 打分上下文削减。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · jerryfane · `TS`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — 可观测的浏览器潜行游戏：Jev 做类型化的守卫判断，确定性代码掌管世界规则。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · abdelstark · `TS`</sub>

- **[jev-dsl](https://github.com/inanna-malick/jev-dsl)** — 面向智能体的 Haskell DSL：类型化数据包、类型推断，答案与问题同构。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · inanna-malick · `Hs`</sub>

- **[a0-typesafe-ai](https://github.com/3clyp50/a0-typesafe-ai)** — 给 Agent Zero 的 Jev 判断，带类型化工具与概率卡片。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · 3clyp50 · `Py`</sub>

- **[citation-verifier](https://github.com/MarissaFamularo/citation-verifier)** — 核查每篇被引论文是否支持引用它的那句话：一个模型证明引文，Jev 打分，人来裁定。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · marissafamularo · `JS`</sub>

- **[poorjev](https://github.com/rupeshpoojary9/poorjev)** — 开源的本地 Jev 替代品：一个有可证校准置信度的 System One 决策层。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★5 · rupeshpoojary9 · `Py` · ⚠ `并非 Jev`</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — 在一个它不可能见过的任务上做独立校准测试：900 条规则生成的支持工单。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★4 · scienthoon · `Py`</sub>

- **[qwen-rlcd](https://github.com/shamazharikh/qwen-rlcd)** — 基于 Qwen3.5-0.8B 的 Jev 风格校准决策模型（Choice／Score／Noul）。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★4 · shamazharikh · `Py` · ⚠ `并非 Jev` `无许可证`</sub>

- **[typesafe-cli](https://github.com/y0usaf/typesafe-cli)** — 在 shell 里向 Jev 提类型化问题：noul、choice、score 都以数字返回，而不是散文。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · y0usaf · `TS`</sub>

- **[typesafe-jev](https://github.com/gtaras7/typesafe-jev)** — 用 Jev 筛选一整个文件夹的简历：类型化判断、可编辑的策略、免费重新打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · gtaras7 · `TS`</sub>

- **[dsh-jev](https://github.com/noetion/dsh-jev)** — 注册 jev_ask 的 DSH 包，提供 noul、choice、score 三种答案。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · noetion · `TS`</sub>

- **[jev-judgment](https://github.com/HyunjunJeon/jev-judgment)** — Agent 技能：把编程智能体的封闭式判断交给 Jev。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · hyunjunjeon · `Py`</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — 用 Jev 把 Claude Code 的技能清单削减约 75%：给每个已安装技能打相关性分，其余隐藏。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · shivampansuriya · `JS`</sub>

- **[jevchess](https://github.com/choxos/jevchess)** — 让 Jev 与任意 OpenRouter 模型、Stockfish 或你本人下国际象棋，单页网页应用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · choxos · `JS`</sub>

- **[llama-index-jev](https://github.com/WiktorB2004/llama-index-jev)** — 由 Jev 驱动的 LlamaIndex 重排器与路由器 —— 类型化的分数与选择，比 LLM-as-judge 便宜。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · wiktorb2004 · `Py`</sub>

- **[pagegrade](https://github.com/kitze/pagegrade)** — 给页面各区块的清晰度、文案与页面 SEO 打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · kitze · `TS`</sub>

- **[prompt2jev](https://github.com/sumleo/prompt2jev)** — 把自然语言、LLM 提示或跑提示的代码，转换成一个 Jev 决策。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · sumleo · `Py`</sub>

- **[vgi-typesafe](https://github.com/Query-farm/vgi-typesafe)** — 一个 VGI worker，把 System One 的 choice／noul／score 以可 LATERAL 连接的表函数形式暴露给 DuckDB／SQL。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · query-farm · `Py`</sub>

- **[jev-scout](https://github.com/AkashPriyadarshii/jev-scout)** — 由 Jev 打分驱动的开源仓库与 crate 侦察工具。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · akashpriyadarshii · `Rs`</sub>

- **[limpet](https://github.com/noplan-inc/limpet)** — 一个 Stop 钩子，阻止编程智能体过早收工 —— 用大白话写规则，由 Jev 裁定。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · noplan-inc · `Py`</sub>

- **[pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)** — 一个 pi 扩展，把 Jev 判断暴露成五个 pi 工具，让模型能做狭义的语义判断。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · legacybridge-tech · `TS` · ⚠ `无许可证`</sub>

- **[tripwire](https://github.com/noelzappy/tripwire)** — 在用户看到之前先审判每一条 LLM 响应。提供 AI SDK middleware 与 OpenAI 兼容代理。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★2 · noelzappy · `TS`</sub>

- **[gpt-vs-jev](https://github.com/TanayPadar/gpt-vs-jev)** — 在同一输入上对比 GPT 的生成式语言与 JEV 的结构化 Noul 决策。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · tanaypadar · `TS`</sub>

- **[jev-wrapped](https://github.com/gaborishka/jev-wrapped)** — Telegram 频道年度透视：Jev 评判一年的帖子，生成一张卡片，跑在一个 Cloudflare Worker 上。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · gaborishka · `JS`</sub>

- **[padflow-jev-evals](https://github.com/zsavage8/padflow-jev-evals)** — 来自某土地开发 SaaS 的类型化决策基准：schema、匿名标注数据与运行器。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · zsavage8 · `Py`</sub>

- **[s1-rs](https://github.com/AbdelStark/s1-rs)** — Rust 的类型化 System One 层（Choice／Score／Noul）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · abdelstark · `Rs`</sub>

- **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)** — 技术密度最高的独立讲解：JS / Python / AI SDK 三种代码、三种应答结构、进阶模式，还诚实列出了模型的失效场景。
  <sub>`教程` · Flavio Copes · `JS` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — 给 Jev 的有限样本保证：用保形风险控制把校准概率转成可证的约束。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · nikkoxgonzales · `Py`</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — 按 Jev 概率做 ORDER BY 能否给出站得住脚的排序？独立的排序、校准与不变量实测。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · yodablocks · `Py`</sub>

- **[jev-packs](https://github.com/dtduc-git/jev-packs)** — 证据门控的 Jev 问题包注册表：精选问题、黄金样例与实测证据。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · dtduc-git · `Py`</sub>

- **[pytest-jev](https://github.com/allebee/pytest-jev)** — 给 pytest 的语义断言：测试 LLM 应用输出的含义，由 Jev 判定。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · allebee · `Py`</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。
  <sub>`开源项目` · ⚠ `宣称未核实`</sub>

### 总览

_介绍模型或整个领域，而非单一模式。_

<details>
<summary><b>128</b> 条 —— 点击展开</summary>

- **[Official agent skill for Claude Code](https://docs.typesafe.ai/agent-skill)** ⭐ — 把 TypeSafe 官方技能装进 Claude Code，让智能体自己写出正确的 Jev 调用，不必每次手动贴 API 结构。
  <sub>`官方文档` · ★1,645 · `sh`</sub>

- **[typesafe-ai/skills](https://github.com/typesafe-ai/skills)** ⭐ — Claude Code 插件背后的官方技能仓库，里面的 SKILL.md 教会智能体如何使用 System One API。
  <sub>`插件` · ★1,645 · `sh`</sub>

- **[system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python)** ⭐ — 一个可直接替换 TypeSafeClient 的适配器，底层走普通 LLM API —— 没有 Jev 权限也能跑 Jev 形状的代码。
  <sub>`SDK` · ★249 · `Py`</sub>

- **[@typesafe-ai/sdk (TypeScript / JavaScript)](https://github.com/typesafe-ai/typesafe-sdk-js)** ⭐ — 官方 TypeScript 客户端。同时提供 ESM、CJS 和类型声明，辅助函数是小写的 choice()/score()/noul()。
  <sub>`SDK` · ★218 · `TS` · `JS` · `choice` · `score` · `noul`</sub>

- **[typesafe-sdk (Python)](https://github.com/typesafe-ai/typesafe-sdk-python)** ⭐ — 官方 Python 客户端。含同步与异步客户端、支持 retry-after 的重试策略，以及 Choice/Score/Noul 辅助类。
  <sub>`SDK` · ★194 · `Py` · `choice` · `score` · `noul`</sub>

- **[API reference](https://docs.typesafe.ai/api)** ⭐ — 唯一的端点 POST /v1/systemone，给出三种问题类型的完整请求与应答结构。
  <sub>`官方文档` · `sh` · `Py` · `TS`</sub>

- **[Models, pricing and limits](https://docs.typesafe.ai/models)** ⭐ — 权威参数表：jev-1.13.0、输入 $0.042/Mtok 且输出免费、64k 上下文、state 加最长问题 32k、仅支持文本输入。
  <sub>`官方文档` · `sh` · `Py` · `TS`</sub>

- **[Primitives: Choice, Score, Noul](https://docs.typesafe.ai/primitives)** ⭐ — 三个原语各自的用途与 criteria 写法，含 Choice 最多 255 个选项、Score 只能 2–10 级这些硬限制。
  <sub>`官方文档` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Introducing System One models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)** ⭐ — 发布博文：什么是 System One 模型、为什么要把决策从生成里拆出来，以及厂商自报的延迟与成本数字。
  <sub>`文章` · Diogo Almeida · ⚠ `厂商自报`</sub>

- **[Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)** ⭐ — 厂商自己列出的失效场景：字面化理解、算术与计数、日期比较、间接指代、夹杂大量无关细节的长 state、对抗性内容。
  <sub>`官方文档`</sub>

- **[Use case map](https://docs.typesafe.ai/concepts/use-case-map)** ⭐ — 厂商自己的分类体系：五大类、十九个行业方向、十种决策形态（从分类一直到结构化数据抽取）。
  <sub>`官方文档`</sub>

- **[OpenCode Zen: Jev resale](https://github.com/anomalyco/opencode)** — 一个编程智能体，其托管网关转售 Jev，还提供一个免费档位的模型 id。
  <sub>`平台集成` · ★209,234 · `TS`</sub>

- **[litellm](https://github.com/BerriAI/litellm)** — 高性能 AI 网关：Rust 内核加 Python SDK，以 OpenAI 或原生格式调用上百种 LLM API。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★59,374 · berriai · `Py` · ⚠ `无许可证`</sub>

- **[oh-my-pi](https://github.com/can1357/oh-my-pi)** — 深度整合 IDE 的编程智能体。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★32,448 · can1357 · `TS`</sub>

- **[openwork](https://github.com/different-ai/openwork)** — 某协作工具的开源替代品。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★23,687 · different-ai · `TS` · ⚠ `并非 Jev` `无许可证`</sub>

- **[Opik TypeSafe tracker](https://github.com/comet-ml/opik/blob/main/sdks/python/src/opik/integrations/typesafe/opik_tracker.py)** — 包装同步与异步客户端，把每次 system_one 调用记录成一个可追踪的 span。
  <sub>`开源项目` · ★22,188 · `Py`</sub>

- **[@effect/ai-typesafe](https://github.com/Effect-TS/effect)** — 在 Jev 之上实现 Effect 的 DecisionModel 接口，并罕见地坦白说明取整行为尚未核实。
  <sub>`平台集成` · ★16,167 · `TS` · `choice` · `score` · `noul`</sub>

- **[rig-typesafeai](https://github.com/0xPlaygrounds/rig)** — Rust 集成，选项数量在编译期检查 —— 超过 255 个选项的 Choice 会编译失败，而不是运行时才报错。
  <sub>`平台集成` · ★8,693 · `Rs` · `choice` · `score` · `noul`</sub>

- **[Bifrost TypeSafe gateway route](https://github.com/maximhq/bifrost/tree/dev/core/providers/typesafe)** — 一个 Go 网关 provider，对原生 API 做一比一透传 —— 官方 SDK 只需改 base URL 即可使用。
  <sub>`开源项目` · ★8,230 · `Go`</sub>

- **[Kiln: Jev adapter](https://github.com/Kiln-AI/Kiln)** — 一个接进 adapter registry 的「JSON Schema 转问题」编译器，并诚实说明了它无法支持的场景。
  <sub>`平台集成` · ★5,078 · `Py` · `choice` · `score` · `noul`</sub>

- **[laya-mlx](https://github.com/mizorewww/laya-mlx)** — 给 Laya 类型化决策模型的原生 MLX 运行时：短决策 7–14 毫秒，不生成文本。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4,500 · mizorewww · `Py`</sub>

- **[ruby_llm: TypeSafe provider](https://github.com/crmne/ruby_llm)** — 带专门 System One 协议的 Ruby provider，是 Ruby 侧接入 Jev 的主要路径。
  <sub>`平台集成` · ★4,396 · `Rb` · `choice` · `score` · `noul`</sub>

- **[SemIf](https://github.com/TheoLeeCJ/SemIf)** — 一个独立的「语义 if」实现，开门见山声明与 Jev 和 TypeSafe 无隶属关系。
  <sub>`Jev 替代实现` · ★3,427 · `Py` · ⚠ `并非 Jev`</sub>

- **[kev](https://github.com/jaredpalmer/kev)** — 一套可训练、可自托管的 Jev-like 决策模型，API 与 System One 兼容 —— 官方 SDK 可以直接指向你自己的服务。
  <sub>`Jev 替代实现` · ★2,764 · Jared Palmer · `Py` · `choice` · `score` · `noul` · ⚠ `并非 Jev`</sub>

- **[NanoJev](https://github.com/TianyuCodings/NanoJev)** — 自称 Jev 的「nano 复刻版」，用途是拿来读，不是拿来上生产。
  <sub>`Jev 替代实现` · ★1,887 · `Py` · ⚠ `并非 Jev`</sub>

- **[jevlike](https://github.com/vinnylarouge/jevlike)** — 一个独立可训练的模型，输入输出形状与 Jev 相同：文本加 N 个选项进，每个选项一个概率出，单次前向完成。
  <sub>`Jev 替代实现` · ★1,183 · vinnylarouge · `Py` · ⚠ `并非 Jev`</sub>

- **[celesto](https://github.com/CelestoAI/celesto)** — 给 AI 智能体的安全持久化计算环境。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★959 · celestoai · `Py`</sub>

- **[distill](https://github.com/samuelfaj/distill)** — 用远更少的 token 完成远更多的事。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★682 · samuelfaj · `Rs`</sub>

- **[aiavatarkit](https://github.com/uezo/aiavatarkit)** — 快速构建基于 AI 的对话式虚拟形象。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★678 · uezo · `Py`</sub>

- **[simple-jev](https://github.com/featherless-ai/simple-jev)** — 通过读取 next-token logits，把任意开源权重模型变成 Jev 形状的端点 —— JSON 由服务端组装，而不是模型生成。
  <sub>`Jev 替代实现` · ★462 · `Py` · ⚠ `并非 Jev`</sub>

- **[jev-skill](https://github.com/wuyoscar/jev-skill)** — 一个 agent 技能加 CLI：校验三种原语、在产生计费调用前要求明确同意、并禁止在模拟时编造输出。
  <sub>`插件` · ★395 · `Py` · `choice` · `score` · `noul`</sub>

- **[awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects)** — 一个同类目录，主打生态广度：来源锚定到具体 commit、四语 README、以及一个生成式站点。
  <sub>`开源项目` · ★339 · logicrw · `JS`</sub>

- **[openjev](https://github.com/razorback16/openjev)** — 基于开源扩散模型的 Jev 兼容决策服务。
  <sub>`Jev 替代实现` · ★288 · razorback16 · `Py` · ⚠ `并非 Jev`</sub>

- **[decider](https://github.com/Mapika/decider)** — 一族 System One 风格的模型，从开源基座微调而来，做单次类型化决策。
  <sub>`Jev 替代实现` · ★287 · mapika · `Py` · ⚠ `并非 Jev`</sub>

- **[rizzo-flow](https://github.com/Rizzo-AI-Academy/rizzo-flow)** — Jev 的开源本地版：由 LLM 产出类型化决策，且不生成任何 token。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★261 · rizzo-ai-academy · `Py` · ⚠ `并非 Jev`</sub>

- **[openjev-sglang](https://github.com/ekzhang/openjev-sglang)** — 用开源模型提供的 Jev 兼容端点，仅做 prefill。
  <sub>`Jev 替代实现` · ★259 · ekzhang · `Py` · ⚠ `并非 Jev` `无许可证`</sub>

- **[awesome-jev (heyjunpenn)](https://github.com/heyjunpenn/awesome-jev)** — 覆盖最广的同类目录：数百个项目、六种语言，且它的 README 本身就是被解析的数据源。
  <sub>`开源项目` · ★256 · heyjunpenn · `TS` · ⚠ `无许可证`</sub>

- **[typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp)** — 最适合刚拿到 API 的人。把 Jev 接进 Claude Code、Claude Desktop、Codex 和 Pi，随时做 Choice / Score / Noul。
  <sub>`插件` · ★234 · `Go` · `choice` · `score` · `noul`</sub>

- **[laya](https://github.com/receptron/laya)** — 通过 ONNX Runtime 从 Node.js／TypeScript 运行开源的 Jev 兼容 System-1 决策模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★216 · receptron · `TS`</sub>

- **[jeff](https://github.com/logan-markewich/jeff)** — 自托管的 Jev 直接替代品，底层由 GliFormer 驱动。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★207 · logan-markewich · `Py` · ⚠ `并非 Jev`</sub>

- **[awesome-jev (fatwang2)](https://github.com/fatwang2/awesome-jev)** — 一个同类目录，提交由 Jev 自己审核，其多语言社区客户端清单相当完整。
  <sub>`开源项目` · ★187 · fatwang2 · `JS`</sub>

- **[djev-spark](https://github.com/mmastrac/djev-spark)** — 在 DGX Spark 上跑 DiffusionGemma NVFP4 结构化决策的容器配方。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★170 · mmastrac · `TS` · ⚠ `无许可证`</sub>

- **[stanley-code](https://github.com/devagrawal09/stanley-code)** — 给编程智能体的有界 Jev 工作流。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★111 · devagrawal09 · `TS`</sub>

- **[open-jev](https://github.com/daseinlabs/open-jev)** — 带自定义微调的开源 Jev 实现。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★95 · daseinlabs · `Py` · ⚠ `并非 Jev` `无许可证`</sub>

- **[advocaat](https://github.com/pithings/advocaat)** — 一个小巧的类型化客户端，用来对你自己的数据提问。
  <sub>`SDK` · ★89 · pithings · `TS`</sub>

- **[jevbench](https://github.com/fstandhartinger/jevbench)** — JevBench v1 —— 面向 Jev 这类类型化决策模型的基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★71 · fstandhartinger · `Py`</sub>

- **[jev-voice](https://github.com/kevinbadi/jev-voice)** — 对你的 Mac 说话：本地 whisper.cpp + 每条命令一次 Jev 调用 + macOS 自动化。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★68 · kevinbadi · `Py`</sub>

- **[agent-router](https://github.com/nidhi-singh02/agent-router)** — CLI：为一个任务挑选编程智能体与模型／推理强度，然后启动它。 <sub>(机翻)</sub>
  <sub>`插件` · ★63 · nidhi-singh02 · `TS`</sub>

- **[OpenDecision](https://github.com/deepanwadhwa/OpenDecision)** — 一个开源语义决策引擎，本地跑零样本模型，其 FastAPI 服务已验证与官方 SDK 协议兼容。
  <sub>`Jev 替代实现` · ★52 · deepanwadhwa · `Py` · `choice` · `score` · `noul` · ⚠ `并非 Jev`</sub>

- **[ruby_decision_model](https://github.com/obie/ruby_decision_model)** — 面向 Jev 这类决策模型的 Ruby 客户端。 <sub>(机翻)</sub>
  <sub>`SDK` · ★49 · obie · `Rb`</sub>

- **[jev-rules](https://github.com/EliaAlberti/jev-rules)** — 由 Jev 挑出哪些规则适用于当前提示，让模型只看到相关的那些。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★46 · eliaalberti · `JS`</sub>

- **[litjev](https://github.com/zhengxuyu/litjev)** — 把任意现成 LLM 变成一个 Jev 式的决策层。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★38 · zhengxuyu · `Py` · ⚠ `并非 Jev`</sub>

- **[openthai-systemone](https://github.com/iapp-technology/openthai-systemone)** — OpenThai-SystemOne：开源的泰语加英语 System One 决策模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★38 · iapp-technology · `Py`</sub>

- **[ask-jev-skill](https://github.com/shantanugoel/ask-jev-skill)** — 给 Hermes 及其他智能体用的技能，用来向 Jev 提问。 <sub>(机翻)</sub>
  <sub>`插件` · ★37 · shantanugoel · `Py`</sub>

- **[typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark)** — 一个模仿其结构化输出形状的网关，用于与之对比测试。
  <sub>`基准测试` · ★37 · iammrduncan · `TS`</sub>

- **[jev-seo](https://github.com/AkashPriyadarshii/jev-seo)** — 用 Rust 写的 agent 优先 SEO/GEO CLI 套件与 MCP server。 <sub>(机翻)</sub>
  <sub>`插件` · ★32 · akashpriyadarshii · `Rs`</sub>

- **[jev (Elixir/OTP)](https://github.com/dannote/jev)** — 把 Jev 做成 OTP 进程：从 GenServer 回复，并对答案做模式匹配。
  <sub>`SDK` · ★28 · dannote · `Ex`</sub>

- **[refgarden](https://github.com/AlbionaHoti/refgarden)** — 面向创作者的空间参考浏览器：本地 Jev 查询选择、元数据高亮与带来源链接的合集。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★27 · albionahoti · `TS` · ⚠ `并非 Jev`</sub>

- **[jev-trades](https://github.com/zadescoxp/Jev-Trades)** — 用 Jev 驱动的交易机器人。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★24 · zadescoxp · `Py`</sub>

- **[jevify](https://github.com/altryne/jevify)** — 一个 agent 技能：发现适合用 Jev 的场景、设计类型化问题，并从近期社区实验中学习。 <sub>(机翻)</sub>
  <sub>`插件` · ★21 · altryne · `Py`</sub>

- **[ruby_llm-typesafe](https://github.com/kieranklaassen/ruby_llm-typesafe)** — 给某个 Ruby LLM 库做的结构化输出 provider。
  <sub>`平台集成` · ★18 · kieranklaassen · `Rb`</sub>

- **[jevocks](https://github.com/unicodeveloper/jevocks)** — 用 Jev 看每日股票状态。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★16 · unicodeveloper · `TS` · ⚠ `无许可证`</sub>

- **[swift-typesafe](https://github.com/ainame/swift-typesafe)** — 非官方 Swift SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★14 · ainame · `Swift`</sub>

- **[jev](https://github.com/BorisLeMeec/jev)** — 一个 Jev 的 Claude Code 插件。 <sub>(机翻)</sub>
  <sub>`插件` · ★13 · borislemeec · `Go`</sub>

- **[jev-foundation-models](https://github.com/peterfriese/jev-foundation-models)** — 轻量的原生 Swift 6 桥接，把 Jev 接入 Apple 的 Foundation Models。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★13 · peterfriese · `Swift`</sub>

- **[jev-cli](https://github.com/tumf/jev-cli)** — 小巧的零依赖 Jev 命令行工具。 <sub>(机翻)</sub>
  <sub>`SDK` · ★12 · tumf · `Py`</sub>

- **[jev_stock](https://github.com/sosopop/jev_stock)** — 实验性框架：从结构化市场数据预测短期股价方向。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★12 · sosopop · `Py` · ⚠ `无许可证`</sub>

- **[typesafe-skill-router](https://github.com/DECRUX9812/typesafe-skill-router)** — 给 Hermes Agent 的技能路由：在模型调用之前，指出唯一值得加载的那个技能。 <sub>(机翻)</sub>
  <sub>`插件` · ★12 · decrux9812 · `Py`</sub>

- **[typesafe-ai](https://github.com/Twister915/typesafe-ai)** — Rust 的类型化客户端，含异步与阻塞后端，以及可观测的重试。 <sub>(机翻)</sub>
  <sub>`SDK` · ★11 · twister915 · `Rs`</sub>

- **[typesafe-playground](https://github.com/kavehmz/typesafe-playground)** — 围绕 Jev 的交互式实验，从工单路由到带真实 AI 决策的 3D 驾驶仿真。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★11 · kavehmz · `JS` · ⚠ `无许可证`</sub>

- **[pi-quiet-ask](https://github.com/HyunjunJeon/pi-quiet-ask)** — 把 Jev 作为 pi 编程智能体的安静决策层。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10 · hyunjunjeon · `TS`</sub>

- **[xtags](https://github.com/manifoldor/xtags)** — 在 X 的时间线上，给每条帖子标出它想让你干什么 —— 判断来自只返回概率、不生成文本的 Jev。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10 · manifoldor · `JS`</sub>

- **[typesafe-sdk-go](https://github.com/Tangerg/typesafe-sdk-go)** — Go SDK —— 类型化问题进，概率分布出。 <sub>(机翻)</sub>
  <sub>`SDK` · ★9 · tangerg · `Go`</sub>

- **[jev-benchmark](https://github.com/wondertwins/jev-benchmark)** — Jev 的基准与 playground：国际象棋，以及语音转写中的说话对象判定。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★6 · wondertwins · `Py`</sub>

- **[jev-korean-benchmark](https://github.com/mahlernim/jev-korean-benchmark)** — 可复现的早期访问评测：Jev 在韩语理解与医学文本上的表现，附运行时与成本证据。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★6 · mahlernim · `Py` · ⚠ `无许可证`</sub>

- **[typesafe-sdk](https://github.com/joshmn/typesafe-sdk)** — typesafe.ai 的 Ruby 客户端。 <sub>(机翻)</sub>
  <sub>`SDK` · ★6 · joshmn · `Rb`</sub>

- **[typesafeai-dotnet-sdk](https://github.com/saibimajdi/typesafeai-dotnet-sdk)** — 社区维护的 .NET SDK，支持 noul、choice、score 三种类型化问题。 <sub>(机翻)</sub>
  <sub>`SDK` · ★6 · saibimajdi · `C#`</sub>

- **[jev-little-airways](https://github.com/lbotinelly/jev-little-airways)** — Jev 的能力展示与研究：一次 show-and-tell 式的考察。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★5 · lbotinelly · `TS`</sub>

- **[legalforecastbench](https://github.com/johnhughes3/LegalForecastBench)** — LegalForecast-MTD 基准 alpha 版与官方评测流程。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★5 · johnhughes3 · `Py`</sub>

- **[typesafe_sdk (Elixir)](https://github.com/nshkrdotcom/typesafe_sdk)** — 官方 SDK 的 Elixir 移植。
  <sub>`SDK` · ★5 · nshkrdotcom · `Ex`</sub>

- **[jev-system-one](https://github.com/haseeb-heaven/jev-system-one)** — 打磨过的终端界面，输出答案的同时给出透明的决策报告。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · haseeb-heaven · `Py`</sub>

- **[typesafe-ai-rs](https://github.com/gilljon/typesafe-ai-rs)** — 独立的 Rust SDK，同时提供异步与阻塞两种形式。 <sub>(机翻)</sub>
  <sub>`SDK` · ★4 · gilljon · `Rs`</sub>

- **[typesafe-sdk-swift](https://github.com/alterhq/typesafe-sdk-swift)** — 非官方的 Swift 客户端库。 <sub>(机翻)</sub>
  <sub>`SDK` · ★4 · alterhq · `Swift`</sub>

- **[jcm-router](https://github.com/adarshmishra07/jcm-router)** — 本地代理：逐条消息用 Jev 选择 Claude 模型与推理强度，并路由子智能体。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · adarshmishra07 · `TS`</sub>

- **[new-api-plugin-typesafe](https://github.com/FFatTiger/new-api-plugin-typesafe)** — 给 new-api 的 Jev 任务插件：原生 /v1/systemone、同步评估。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · ffattiger · `JS`</sub>

- **[soupbase](https://github.com/spoonnotfound/soupbase)** — Jev 版海龟汤。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · spoonnotfound · `TS`</sub>

- **[switchboard](https://github.com/ruban-24/switchboard)** — 开源、模型无关的决策路由器，面向 Claude Code 和 Codex。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · ruban-24 · `TS`</sub>

- **[typesafe-sdk-java](https://github.com/Premo-Cloud/typesafe-sdk-java)** — 社区维护的 Java 客户端（非官方）。 <sub>(机翻)</sub>
  <sub>`SDK` · ★3 · premo-cloud · `Java`</sub>

- **[got-jev](https://github.com/phureewat29/jev-got)** — 以《权力的游戏》为素材的 Jev 概念验证。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · phureewat29 · `TS` · ⚠ `无许可证`</sub>

- **[jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark)** — 在一个智能体失败归因基准上，把 Jev 与一个强 LLM 做对比测试。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★2 · tokentrim · `Py`</sub>

- **[jev-canvas](https://github.com/gaborishka/jev-canvas)** — 用语音加手指指向在 tldraw 画布上作画：由 Jev 决定动作与目标。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · gaborishka · `JS`</sub>

- **[jevclient](https://github.com/AboveColin/jevclient)** — Jev 的异步 Python 客户端：类型化问题进，概率与选择出，没有散文需要解析。 <sub>(机翻)</sub>
  <sub>`SDK` · ★2 · abovecolin · `Py`</sub>

- **[jevgo](https://github.com/fgn/jevgo)** — System One API 的 Go 客户端，可选接入 Langfuse 观测。 <sub>(机翻)</sub>
  <sub>`SDK` · ★2 · fgn · `Go`</sub>

- **[jevtown](https://github.com/gaborishka/jevtown)** — 一个社交网络：真人写帖，一万个 AI 人格来回应。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · gaborishka · `JS`</sub>

- **[typesafeai.net](https://github.com/Hawxy/TypeSafeAI.Net)** — 面向 TypeSafe AI 平台的 .NET SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★2 · hawxy · `C#`</sub>

- **[askjev](https://github.com/pZacca/askjev)** — 非官方的 Jev MCP server。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · pzacca · `TS`</sub>

- **[jev-skill-router](https://github.com/shimo4228/jev-skill-router)** — Claude Code 插件：询问 Jev 哪个已安装技能适配当前提示，并记录答案（先影子运行）。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · shimo4228 · `Py`</sub>

- **[typesafe-ai-playground](https://github.com/markjaquith/typesafe-ai-playground)** — 围绕 Jev 做实验的 playground。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · markjaquith · `Rs`</sub>

- **[typesafe-go](https://github.com/zhirschtritt/typesafe-go)** — 地道的 Go SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · zhirschtritt · `Go`</sub>

- **[typesafe-rs](https://github.com/AbdelStark/typesafe-rs)** — 以延迟为先的 System One Rust SDK。 <sub>(机翻)</sub>
  <sub>`SDK` · ★1 · abdelstark · `Rs`</sub>

- **[@ai-sdk/typesafe-ai provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai)** — 直连 TypeSafe 的 AI SDK provider 包，示例覆盖三种问题类型以及嵌套的 criteria 写法。
  <sub>`SDK` · `TS` · `JS` · `choice` · `score` · `noul`</sub>

- **[aegis: TypeSafe as a first-class provider](https://github.com/dvjn/aegis)** — 一个个人 Rust AI 网关，内置 TypeSafe provider，用真实响应体测试了用量提取与别名解析。
  <sub>`开源项目` · ★0 · dvjn · `Rs` · ⚠ `代码未实测` `无许可证`</sub>

- **[Build Your Own JEV Locally: Run a 100% Private AI Agent on Your Machine](https://medium.com/coding-nexus/build-your-own-jev-locally-run-a-100-private-ai-agent-on-your-machine-bb98126d394a)** — 标题误导：它并没有在跑 Jev，而是用开源 LLM 加受约束的 next-token 打分，自己搭一个 Jev-like 决策引擎。
  <sub>`Jev 替代实现` · DataScience Nexus · `Py` · ⚠ `并非 Jev` `代码未实测` `付费墙`</sub>

- **[Jev Explained: How to Add Fast, Typed Decisions to an AI Agent](https://aihubmix.com/blog/jev-explained-how-to-add-fast-typed-decisions-to-an-ai-agent)** — 第三方解读文章，给了一张有用的架构草图，还罕见地诚实列出了「不该用决策模型」的场景。
  <sub>`文章` · `Py` · ⚠ `代码未实测`</sub>

- **[jev-t-rex-runner](https://github.com/joshlarsen/jev-t-rex-runner)** — 由 Jev 模型来玩 Chrome 恐龙小游戏。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · joshlarsen · `JS`</sub>

- **[jevai.org community site](https://www.jevai.org/)** — 一个与官方无关的社区站：有 playground、预设决策 API、MCP 服务、可下载技能，以及一个社区应用展示廊。
  <sub>`开源项目` · `sh` · ⚠ `需第三方密钥` `宣称未核实`</sub>

- **[kunobi-jev](https://github.com/kunobi-ninja/kunobi-jev)** — System One API 的 Rust 客户端。 <sub>(机翻)</sub>
  <sub>`SDK` · ★0 · kunobi-ninja · `Rs`</sub>

- **[labs](https://github.com/kiarina/labs)** — 用于实验、研究与调查的小型独立项目集。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · kiarina · `Py`</sub>

- **[Tracing Jev calls with Langfuse](https://langfuse.com/integrations/model-providers/typesafe)** — 目前唯一有 Jev 专用可观测性的平台：一个 OpenInference instrumentor，通过 OpenTelemetry 追踪每次决策调用。
  <sub>`平台集成` · `Py` · `choice` · `score` · `noul`</sub>

- **[TypeSafe AI Jev now available on AI Gateway](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway)** — Vercel 在 AI Gateway 上线 Jev 的公告，附 experimental_evaluate 示例，模型串为 typesafe-ai/jev。
  <sub>`平台集成` · `TS` · `noul`</sub>

- **[TypeSafe models in Pydantic AI](https://pydantic.dev/docs/ai/models/typesafe/)** — Pydantic AI 的一方支持：用 typesafe:jev-latest 这个模型串、配 output_type=bool 建 Agent。
  <sub>`平台集成` · `Py`</sub>

- **[TypeSafe pass-through on LiteLLM](https://docs.litellm.ai/docs/pass_through/typesafe)** — 通过 LiteLLM 代理 Jev，统一密钥与成本追踪，/typesafe/ 下的任意路径都直接透传。
  <sub>`平台集成` · `sh`</sub>

- **[TypeSafe-compatible API on Vercel AI Gateway](https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe)** — 只改一个 baseURL 就能把官方 TypeSafe SDK 指向 Vercel，也可以直接用 cURL 调网关的 systemone 端点。
  <sub>`平台集成` · `TS` · `sh` · `noul`</sub>

- **[typesafe-go](https://github.com/Nibir1/typesafe-go)** — 零依赖的社区 Go SDK，还带一个静态分析器，能在编译期指出设计不良的问题。
  <sub>`SDK` · ★0 · Nibir1 · `Go` · `choice` · `score` · `noul` · ⚠ `代码未实测`</sub>

- **[awesome-jev (yibie)](https://github.com/yibie/awesome-jev)** — 目前这个领域里 star 数最高的同类目录。
  <sub>`开源项目` · ★1,094 · ⚠ `无许可证`</sub>

- **[A new kind of AI model from a ChatGPT inventor is thrilling developers](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)** — 唯一一篇引用了开发者一手说法（而非厂商数字）的发布报道，其中还提醒：解释阈值的责任现在落在你自己头上。
  <sub>`文章` · Tim Fernholz</sub>

- **[AI model "Jev" to make machines decide faster](https://www.heise.de/en/news/AI-model-Jev-to-make-machines-decide-faster-11457071.html)** — 重点落在可解释性的缺失 —— 模型不给出语言层面的理由 —— 以及所有已公布基准都出自厂商自己。
  <sub>`文章` · Tomislav Bezmalinović</sub>

- **[Hacker News: Introducing System One Models and Jev](https://news.ycombinator.com/item?id=49717558)** — 发布讨论帖，也是质疑最集中的地方：RLCD 缺乏支撑材料、延迟对比不对等、以及官方刻意不公开基准。
  <sub>`讨论`</sub>

- **[Jev (AI model) on Wikipedia](https://en.wikipedia.org/wiki/Jev_(AI_model))** — 最大价值在于当索引用：它的参考文献列表是找到值得读的报道的最快路径。
  <sub>`文章`</sub>

- **[Jev by TypeSafe: A Decision Model for AI Agents](https://beam.ai/agentic-insights/jev-typesafe-ai-agents)** — 从智能体开发者角度，讲决策模型在智能体技术栈里的位置。
  <sub>`文章` · ⚠ `营销内容`</sub>

- **[Jev Cuts AI Decision Costs 100x And Vercel, Cloudflare Rushed To Add It](https://www.forbes.com/sites/josipamajic/2026/09/19/jev-cuts-ai-decision-costs-100x-and-vercel-cloudflare-rushed-to-add-it/)** — 主流媒体对这次发布、以及各家网关上线速度的报道。
  <sub>`文章` · Josipa Majic Predin · ⚠ `厂商自报` `付费墙`</sub>

- **[Jev From TypeSafe is a New Class of AI Model that is FAST and CHEAP - But There is a Caveat!](https://youtube.com/watch?v=qdji39XXgEY)** — 一篇把限制直接写进标题、而不是藏在正文里的评测。
  <sub>`视频` · Gary Explains</sub>

- **[Jev: System One models for Prod, not God](https://www.latent.space/p/jev)** — 唯一的长篇创始人访谈：为什么 RLHF 是错的优化目标、为什么不公开基准、以及全合成数据的路线。
  <sub>`讨论` · Latent Space</sub>

- **[Jev: TypeSafe's System One Model Explained](https://www.datacamp.com/blog/system-one-models-jev)** — 对架构、宣称的基准和定价的中立综述，并明确指出当时还没有出现大规模的独立复现。
  <sub>`文章` · Matt Crabtree</sub>

- **[jevai.org community app gallery](https://www.jevai.org/apps)** — 从社交帖子里策展的 36 个社区作品：浏览器智能体、表格工具、按意图搜邮箱、会判断的广告拦截、游戏与机器人。
  <sub>`开源项目` · ⚠ `宣称未核实`</sub>

- **[RLCD explained: Reinforcement Learning for Calibrated Decisions](https://systemonemodels.org/guides/rlcd-explained/)** — 一份独立整理，其最有价值的结论是否定性的：RLCD 没有论文、没有奖励函数、没有数据集说明、也没有可复现的评测。
  <sub>`文章`</sub>

- **[TypeSafe AI debuts model for machines that plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711)** — 最具怀疑视角的主流报道：它质疑「不会幻觉」的说法 —— 格式正确的答案不等于正确的答案。
  <sub>`文章` · Thomas Claburn</sub>

- **[TypeSafe on OpenRouter](https://openrouter.ai/typesafe)** — OpenRouter 上的 Jev 条目，有自己的模型 id，以及「输入收费、输出免费」这种少见的定价结构。
  <sub>`平台集成`</sub>

</details>

## 按资源形态

同样这些行，按你点开链接后会看到什么来分组。

| 形态 | 例子数 | 点开会看到 |
| --- | :-- | --- |
| **官方文档** | `31` ██▌ | 厂商文档、cookbook 与模式页。 |
| **SDK** | `24` ██ | 客户端库，官方与社区。 |
| **平台集成** | `22` █▉ | 接入模型的网关、框架或平台路径。 |
| **代码片段** | ` 4` ▍ | 本仓库内的小型可运行样例。 |
| **开源项目** | `194` ████████████████ | 真正在调用 Jev 的应用或库。 |
| **插件** | `60` █████ | 可安装的编辑器、智能体、MCP 集成。 |
| **教程** | ` 5` ▍ | 带代码的分步教学材料。 |
| **基准测试** | `28` ██▎ | 实测。注意区分独立实测与厂商自报。 |
| **文章** | `12` █ | 讲解、分析与发布报道。 |
| **视频** | ` 3` ▎ | 演示与评测。 |
| **讨论** | ` 2` ▏ | 值得读的讨论，包括质疑的声音。 |
| **Jev 替代实现** | `19` █▋ | 独立复现实现。它们**不**调用 Jev。 |

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
| [`mcp/`](mcp/) | 一个 MCP server —— 让智能体可以查询目录而不是阅读它。每条结果都带着它的警示一起返回。 |
| [`SKILL.md`](SKILL.md) | 一份 agent 技能：生成的 Jev 代码最常搞错的那些事实，以及值得遵循的设计规则。 |
| [`scripts/verify_claims.py`](scripts/verify_claims.py) | 每周重读每一处被引用的调用点 —— 让原语声明可核实，而不只是被断言。 |
| [`scripts/refresh_metadata.py`](scripts/refresh_metadata.py) | 从 GitHub API 重新读取 star、许可证与归档状态，并开 PR。 |

## 哪些经过核实，哪些没有

- ✅ **已核实** —— 该链接在 `checked` 日期返回成功状态；有人打开它、按页面实际内容写了摘要；含代码的行都读过调用处、确认了实际使用的原语；star 数与许可证来自 GitHub API。
- 🔁 **每周复检** —— 有 320 行记录了其原语声明是在哪个文件里读到的。定时任务会从该仓库的默认分支重新读取，一旦声明不再成立就开 issue，因此上游把集成删掉了也不会留下一条假声明。刻意不锁 commit —— 锁了就会永远在校验一个历史快照。
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

## 机器可读数据

每个例子一条记录，每次推送都按 JSON Schema 校验。

| 文件 | 是什么 |
| --- | --- |
| [`catalog.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/catalog.json) | 404 条目 |
| [`retired.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/retired.json) | 0 已退休 |
| [`compat.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/compat.json) | The platform matrix behind `docs/compatibility.md` |
| [`patterns.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/patterns.json) | The decision taxonomy both generators and the MCP server read |
| [`schema/entry.schema.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/schema/entry.schema.json) | One entry's shape |
| [`llms.txt`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/llms.txt) | For agents, with the caveats spelled out |

## 参与贡献与许可

纠错优先于新增 —— 一个错的条目比一个缺失的条目代价更大。详见 [CONTRIBUTING.md](CONTRIBUTING.md)；收录标准是：*读者不点开链接，能否据此行动？*

`scripts/`、`site/`、`examples/` 中的代码采用 [MIT](LICENSE-MIT)。目录元数据采用 [CC0-1.0](LICENSE-CC0)，并带逐行 `license` 字段。被链接的作品各自保留原许可 —— `repo_license` 记录了各自声明的内容。
