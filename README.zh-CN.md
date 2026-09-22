<!--
  本文件由 catalog.json 生成。请修改目录数据后运行 `python3 scripts/build_readme.py`。
-->

# awesome-jev

[![lint](https://github.com/kydlikebtc/awesome-jev/actions/workflows/lint.yml/badge.svg)](https://github.com/kydlikebtc/awesome-jev/actions/workflows/lint.yml) [![links](https://github.com/kydlikebtc/awesome-jev/actions/workflows/links.yml/badge.svg)](https://github.com/kydlikebtc/awesome-jev/actions/workflows/links.yml) [![entries](https://img.shields.io/badge/条目-148-1f6feb)](https://github.com/kydlikebtc/awesome-jev) [![data: CC0-1.0](https://img.shields.io/badge/data-CC0--1.0-brightgreen)](LICENSE-CC0) [![code: MIT](https://img.shields.io/badge/code-MIT-blue)](LICENSE-MIT)

> 全网 Jev（TypeSafe AI 的 System One 决策模型）使用例子索引 —— 按它做的**决策**归类，而不是按提到它的博客归类。

**English:** [README.md](README.md)

`148` 条目 · `124` 含代码 · `36` 官方 · `16/18` 覆盖模式 · `0` 已退休 · `2026-09-22`

## Jev 是什么

Jev 是 TypeSafe AI 的决策模型。它不生成文本。你给它一段状态和若干类型化问题，它返回：最多 255 个选项中的一个 `choice`、2 至 10 级有序量表上的一个 `score`、或一个 `noul` 是非概率。`choice` 和 `score` 各自带一个校准后的置信度，于是你的代码可以在阈值以上自动执行、在阈值以下转人工；而 `noul` 不带置信度 —— 它的概率**本身就是**答案。TypeSafe 称之为 *System One* 模型：与需要深思的 System Two 推理相对的那个快速直觉系统。它使用面向校准决策的强化学习（RLCD）训练，但该方法尚未发表论文。

是非原语的名字是 **`noul`** —— 不叫 binary，也不叫 boolean，尽管有一个 SDK 用了后者的拼法、而且大量媒体报道写错了。输入**仅支持文本**；且权重未公开，因此无法本地运行。

> ⚠️ **中文用户特别注意：** 官方文档明确说明英语是主要训练语言，中日韩文「能处理但不同等」（handled but not equally well）。在中文内容上依赖它之前，请先自己测，并格外留意置信度。

## 为什么要收集例子

智能体交给前沿模型做的事，大部分不是写作，而是**选择**：调哪个工具、该不该重试、这条命令能不能安全执行、哪些上下文还有用。Jev 瞄准的正是这个内层循环 —— 所以真正有价值的知识单位是**决策模式**，而不是产品公告。本目录就按这个维度组织。

## 本仓库是什么、不是什么

- ✅ 一份公开、可溯源的 Jev 使用例子索引，外加 [`examples/`](examples/) 里可运行的最小样例。
- ❌ 不是产品本身，不是 SDK，与 TypeSafe AI 无隶属关系，也不构成推荐。收录只意味着链接可访问、并且有人真的读过，仅此而已。

## 目录

- [按决策模式](#按决策模式)
  - [工具选择](#工具选择) `25`
  - [意图路由](#意图路由) `20`
  - [上下文压缩](#上下文压缩) `6`
  - [安全闸门](#安全闸门) `13`
  - [输出校验](#输出校验) `7`
  - [人工升级](#人工升级) `15`
  - [模型路由](#模型路由) `10`
  - [并行扇出](#并行扇出) `14`
  - [检索与排序](#检索与排序) `15`
  - [结构化抽取](#结构化抽取) `4`
  - [分类](#分类) `18`
  - [机器学习特征抽取](#机器学习特征抽取) `3`
  - [文档分拣](#文档分拣) `1`
  - [工单分拣](#工单分拣) `7`
  - [内容评分](#内容评分) `15`
  - [总览](#总览) `53`
- [按资源形态](#按资源形态)
- [本仓库内的可运行样例](#本仓库内的可运行样例)
- [生态现状](#生态现状)
- [哪些经过核实，哪些没有](#哪些经过核实哪些没有)
- [机器可读数据](#机器可读数据)
- [参与贡献](#参与贡献)

## 按决策模式

主索引。每个标题是智能体必须做的一个决策；下面的行是用 Jev 做这个决策的例子。

### 工具选择

_智能体下一步该调用哪个工具或动作。_

| 例子 | 展示了什么 | 形态 | 代码 | 备注 |
| --- | --- | --- | --- | --- |
| [Cookbook: Function calling](https://docs.typesafe.ai/cookbooks/function_calling) ⭐ | 把自然语言的交易请求映射到普通的类型化函数：函数名和有限取值的参数各自变成一个带置信度的问题。 | 官方文档 | `Py`<br><sub>choice</sub> | 「这东西能不能替代 tool calling」的参考答案 —— 对取值有限的参数，可以。 |
| [Cookbook: Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion) ⭐ | 为智能体的一轮对话从 182 个技能里最多挑一个：第一次请求给所有技能排序并顺便问「这轮到底需不需要技能」，第二次细读前三名。 | 官方文档 | `Py`<br><sub>choice/noul</sub> | 如果你在维护一个技能/工具目录很大的智能体，这篇可以直接照搬。 |
| [Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home) ⭐ | 一个可运行的智能家居助手示例，用类型化决策来解析用户请求。 | 官方文档 | `Py` | — |
| [claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates) | 三个可独立安装的 Claude Code 插件 —— 护栏、模型路由、技能推荐 —— 各自带 hook 和测试。 | 插件 | `Py` `TS`<br><sub>choice/score/noul</sub> | 它的技能推荐插件实现了同名官方 cookbook，包括「不把技能清单给主模型看」这一步，从而让选择真正由 Jev 做出。 |
| [Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe) | 把工具目录编译成问题，再从答案还原出 tool call，并为「弃权」和「需确认」两种情况定义了专门的错误类型。 | 开源项目 | `Py`<br><sub>choice</sub> | 它的 docstring 把约束讲得很直白：Jev 不是 LLM、没有 tool calling，所以这个 provider 负责双向翻译。 |
| [FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py) | 两段式 MCP 工具检索：先用一个宽 Choice 对整个目录粗排，再给候选短名单配完整描述，每个候选各配一个 Noul 判断它到底是否胜任。 | 开源项目 | `Py`<br><sub>choice/noul</sub> | 逐候选的那个 Noul 才是关键：它让检索在没有工具匹配时返回空，而不是自信地返回最不离谱的那个。 |
| [Cua driver: jev-use example](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use) | Python 与 TypeScript 双实现的 computer-use 动作选择：Jev 从不可变候选集里挑下一个浏览器动作，保留 reobserve 和 abstain 两个特殊选项。 | 开源项目 | `Py` `TS`<br><sub>choice</sub> | 它的严谨程度值得照搬：校验每个概率有限且在区间内、拒绝候选集之外的答案、发送类型化坐标而非截图字节，还提供 mock 适配器让整个循环无密钥无网络也能跑。 |
| [json-render](https://github.com/vercel-labs/json-render)<br><sub>Vercel Labs</sub> | Vercel Labs 的生成式 UI 框架。实验里 Jev 不逐 token 写 JSON，只负责选组件、属性和布局。 | 开源项目 | `TS`<br><sub>choice</sub> | 对生成式 UI 的一个真正不同的理解：从组件注册表里做选择、而不是生成标记，意味着输出不可能引用一个不存在的组件。 |
| [jev-ultrafast](https://github.com/browser-use/jev-ultrafast)<br><sub>Browser Use</sub> | Browser Use 做的高速浏览器 Agent。Jev 每一步只判断「做什么、点哪个元素」，要打字才叫小模型。 | 开源项目 | `Py`<br><sub>choice</sub> | `厂商自报数据` 教科书级的并行扇出例子：一次请求同时返回操作本身、以及若干可能操作各自的推测性目标，再由代码取用实际相关的那个。航班搜索耗时是项目自报数字。 |
| [DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat) | 从三个维度审查每次工具调用：风险等级、用户是否授权、以及一个显式的提示注入压力检查。 | 开源项目 | `TS`<br><sub>choice/noul</sub> | 把「提示注入压力」单独作为一个问题来问，这个设计值得照抄 —— 但请参见 docs/patterns.md，理解为什么这属于纵深防御而非安全边界。 |
| [jev-trader](https://github.com/jarrodwatts/jev-trader) | 在 Monad 测试网上做高频做市。Jev 根据价差和成交方向判断下一步买还是卖。 | 开源项目 | `TS`<br><sub>choice</sub> | `宣称未核实` 收录是作为延迟示例，不是作为策略。它跑在测试网上。本目录不构成任何投资建议；在不可逆交易前放一个概率性决策，应当接受 docs/patterns.md 里 safety-gating 一节所述的审视。 |
| [agent-desktop](https://github.com/lahfir/agent-desktop) | 桌面自动化。读系统无障碍树，判断下一步该点哪个按钮、菜单或输入框。 | 开源项目 | `Rs`<br><sub>choice</sub> | 用无障碍树而不是截图，正好契合模型只接受文本输入的限制，中间不需要一个会丢信息的视觉步骤。 |
| [Jev-cu](https://github.com/Sac-Y/Jev-cu) | 一个 computer-use 智能体：判断该对无障碍树里哪个元素操作，并单独用一个 noul 判断这个动作是否需要用户显式确认。 | 开源项目 | `JS`<br><sub>choice/noul</sub> | `无许可证` 它的风险 noul 明确列举了需要人介入的情形 —— 删除、发送、付款、权限、凭据 —— 并由本地策略闸门执行阈值。只发文本，从不发截图。无许可证文件。 |
| [hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) | 九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。 | 插件 | `Py`<br><sub>choice/score/noul</sub> | 值得一提的是它公开了一个被放弃的用法：用 Jev 做交接摘要的召回率，反而不如原始对话记录。 |
| [typesafe-mario](https://github.com/fhshaik/typesafe-mario) | 让 Jev 玩《超级马里奥》。不看截图，直接读模拟器 RAM 里的结构化状态，再决定跑、跳、躲。 | 开源项目 | `Py`<br><sub>choice/score/noul</sub> | `代码未实测` `仅一次提交` `无许可证` 很好地示范了「喂结构化状态而非像素」—— 毕竟模型只接受文本。仅一次提交且无许可证，请当作可读的演示、而非可依赖的代码。 |
| [jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser) | 语音驱动的浏览器控制：目标选项每次请求都按当前实时元素列表重建，并且总是包含一个 none 选项。 | 开源项目 | `JS`<br><sub>choice/score/noul</sub> | 它锁定具体模型版本而不是跟随别名 —— 一旦你调好了阈值，这就是正确做法。它还单独用一个 noul 判断命令是否具破坏性。 |
| [hyperedit](https://github.com/kevinbadi/hyperedit) | 一个 AI 视频编辑器：把编辑指令路由到具体操作、目标片段和轨道，并以关键词路由作为兜底。 | 开源项目 | `TS`<br><sub>choice/noul</sub> | `无许可证` 保留一条确定性的关键词路由作为兜底是个合理模式：模型改善常见情形，但不成为硬依赖。无许可证文件。 |
| [jevpilot](https://github.com/standardagents/jevpilot) | 驾驶模拟器的自动驾驶，每个 tick 问两个 choice；只剩单一选项的问题直接在本地短路，不花钱发出去。 | 开源项目 | `JS`<br><sub>choice</sub> | `无许可证` 两个值得偷的优化：答案已被唯一确定的问题就不要发出去；以及对状态表做无损重构以减少 token。无许可证文件。 |
| [jev-drone](https://github.com/RomanSlack/jev-drone) | 拿 Jev 控无人机。底层飞控继续负责稳定和安全，Jev 只做爬升、刹车、穿越障碍这类上层判断。 | 开源项目 | `Py`<br><sub>choice/score/noul</sub> | `宣称未核实` 分层才是重点：判断以几赫兹运行，而控制与安全反射快上几个数量级、且完全在代码里。它自报的数字来自一次短程运行，作者本人也这么说明。 |
| [jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat) | 一个完全不含语言模型的 tool calling 聊天机器人：一次请求同时问清请求类型、该调哪个工具、以及每个工具的参数。 | 开源项目 | `TS`<br><sub>choice/noul</sub> | 本目录里最纯粹的演示：已核实完全不含 LLM。想知道「只靠封闭集决策」能把智能体循环推进到哪一步、又在哪里必须停下，读它。 |
| [neo4jev](https://github.com/jexp/neo4jev) | 把 Jev 塞进知识图谱。每走到一个节点，判断下一条最值得走的边，再一路找下去。 | 开源项目 | `Py`<br><sub>choice</sub> | 图遍历天然契合：每一跳都是在当前节点的边集上做封闭选择，而整条路径便宜的前提正是每一跳都便宜。 |
| [OneVOneJev](https://github.com/emrickgarrett/OneVOneJev) | 浏览器里的 1v1 FPS。每个决策 tick 都要判断走位、视角、瞄准、开火和跳跃。 | 开源项目 | `TS`<br><sub>choice</sub> | `代码未实测` `无许可证` 主要价值在于它是个延迟压力测试：实时循环是对「每次决策一个往返」最严苛的场景。无许可证文件。 |
| [Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py) | 一次问清操作本身、以及每个可能操作各自的目标 —— 于是浏览器的一步永远不需要第二次往返。 | 代码片段 | `Py`<br><sub>choice/noul</sub> | `代码未实测` 按官方 API 参考编写，未针对线上 API 实际执行。注意预算：推测性问题很便宜，但它们和其他内容共享每次请求 64k 的上下文。 |
| [Example: tool selection with a none option](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/04-tool-selection/main.py) | 把「选哪个工具」的 choice 和「到底需不需要工具」的 noul 配对使用 —— 因为这是两个不同的问题。 | 代码片段 | `Py`<br><sub>choice/noul</sub> | `代码未实测` 没有退出选项的封闭集无法「拒绝」，只会返回最不离谱的那个工具。加一个 none 选项就是解法。 |
| [Jev (Fully Tested) + Browser Use: FASTEST AI Agent I'VE TRIED YET!](https://www.youtube.com/watch?v=SNJ3yuJ_QwY)<br><sub>AICodeKing</sub> | 把 Jev 接到 Browser Use 上，驱动一个浏览器自动化智能体。 | 视频 | — | `宣称未核实` 频道元数据已核实，但演示内容未逐段核对。标题里的最高级是该频道的惯用风格，不是实测结论。 |

### 意图路由

_判断用户意图，把请求分流到正确的分支。_

| 例子 | 展示了什么 | 形态 | 代码 | 备注 |
| --- | --- | --- | --- | --- |
| [Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home) ⭐ | 一个可运行的智能家居助手示例，用类型化决策来解析用户请求。 | 官方文档 | `Py` | — |
| [Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) ⭐ | 把 confidence 当作第二个维度：答案告诉你「是什么」，置信度告诉你「该不该照它执行」。 | 官方文档 | `Py` | — |
| [Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing) ⭐ | 对进来的请求做分类，路由到足够用的最便宜那个处理方：确定性代码、专用 LLM、或人。 | 官方文档 | `Py`<br><sub>choice</sub> | — |
| [AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe) | 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。 | 开源项目 | `Py`<br><sub>choice/score/noul</sub> | 目前找到的工程最严谨的集成。因为官方没有公开 Jev 的 tokenizer，它把序列化请求保守限制在 30,976 UTF-8 字节；响应含非法 UTF-8 时用 base64 保留原始字节而非替换字符。 |
| [Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html) | 把下游任务 id 变成 choice 的选项集，并用最小置信度闸门把不确定的运行转给人处理。 | 平台集成 | `Py`<br><sub>choice</sub> | 用校准过的决策给数据流水线做分支很契合，而且文档明智地建议锁定版本号、而不是跟着别名走。 |
| [Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero) | 七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。 | 开源项目 | `TS`<br><sub>choice/noul</sub> | 「阈值该设多少」的最佳答案是：没有单一答案。这里不同决策的阈值从 0.3 到 0.9 不等，取决于判错的代价。 |
| [Real Python: hello-jev](https://github.com/realpython/materials/tree/master/hello-jev)<br><sub>Real Python</sub> | 带对照组的教学示例：同一个问询台任务，一份是只认 Y/N 的纯 Python 写法，旁边是一个能读出意图的 Noul。 | 教程 | `Py`<br><sub>noul</sub> | 最平缓的入门点。README 把 SDK 指向 OpenRouter，于是不注册 TypeSafe 账号也能试；它用的是双侧阈值，中间区间重问一次。 |
| [ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook) | 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。 | 教程 | `Py`<br><sub>choice/score/noul</sub> | 找到的最好的结构化教程。它明确指出类型化输出不保证决策正确、列出了官方记录的弱项，并且对自己给出的成本示例做了限定而不是拿来营销。 |
| [jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) | 一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。 | 开源项目 | `Java`<br><sub>choice/score/noul</sub> | 手机端的一个清晰分工：Jev 负责判断与排序，其他模型负责读屏和写字。它会读取屏幕上的消息内容，运行前请先考虑隐私影响。 |
| [jev-search](https://github.com/superagents-lab/jev-search) | Jev 驱动的网页搜索：先选时间窗口和最佳查询改写，再分批对结果逐条用 noul 重排。 | 开源项目 | `TS`<br><sub>choice/noul</sub> | 把整条检索链都变成决策：查哪些引擎、如何改写查询、哪些结果留下。 |
| [jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser) | 语音驱动的浏览器控制：目标选项每次请求都按当前实时元素列表重建，并且总是包含一个 none 选项。 | 开源项目 | `JS`<br><sub>choice/score/noul</sub> | 它锁定具体模型版本而不是跟随别名 —— 一旦你调好了阈值，这就是正确做法。它还单独用一个 noul 判断命令是否具破坏性。 |
| [hyperedit](https://github.com/kevinbadi/hyperedit) | 一个 AI 视频编辑器：把编辑指令路由到具体操作、目标片段和轨道，并以关键词路由作为兜底。 | 开源项目 | `TS`<br><sub>choice/noul</sub> | `无许可证` 保留一条确定性的关键词路由作为兜底是个合理模式：模型改善常见情形，但不成为硬依赖。无许可证文件。 |
| [jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat) | 一个完全不含语言模型的 tool calling 聊天机器人：一次请求同时问清请求类型、该调哪个工具、以及每个工具的参数。 | 开源项目 | `TS`<br><sub>choice/noul</sub> | 本目录里最纯粹的演示：已核实完全不含 LLM。想知道「只靠封闭集决策」能把智能体循环推进到哪一步、又在哪里必须停下，读它。 |
| [A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)<br><sub>Flavio Copes</sub> | 技术密度最高的独立讲解：JS / Python / AI SDK 三种代码、三种应答结构、进阶模式，还诚实列出了模型的失效场景。 | 教程 | `JS` `Py` `TS`<br><sub>choice/score/noul</sub> | 想看代码的话，这是最好的单篇第三方文章。作者把算术、日期、计数列为失效场景，说明他真用过模型，而不是抄新闻稿。 |
| [Example: confidence-gated escalation](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-confidence-gate/main.py) | 带「自动执行或转人工」闸门的路由；策略函数刻意留空 —— 阈值该定在哪，是你的决定。 | 代码片段 | `Py`<br><sub>choice</sub> | `代码未实测` 文档字符串里列出了取舍：一个阈值还是两个、是否按队列区分、以及什么时候「第二名的概率」比置信度更重要。 |
| [Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)<br><sub>Mehul Gupta</sub> | 逐个用例走一遍 —— 智能体路由、智能体内部的决策层、工单分拣 —— 每个都给出具体的选项集和示例响应。 | 教程 | `Py`<br><sub>choice</sub> | `付费墙` 这位作者两篇里更有用的一篇。副标题承诺的免费通道，正文其实没给。 |
| [Jev on Netlify AI Gateway](https://www.netlify.com/changelog/typesafe-jev-ai-gateway/) | 在 Netlify function 里零配置调用：直接用官方 SDK，不需要 API key、baseURL 或 provider 配置，按 Netlify credits 计费。 | 平台集成 | `TS`<br><sub>choice</sub> | 如果你本来就部署在 Netlify，这是门槛最低的试用方式。需要 Node.js 20 及以上。 |
| [langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe) | LangChain 集成：一个分类器，外加用于模型路由、以及在高风险工具调用执行前拦截它的实验性 middleware。 | 平台集成 | `Py`<br><sub>choice/score/noul</sub> | `需早期访问` 目前是 alpha 版。AutoModeMiddleware 是已公开的、最清楚的「拦截破坏性工具调用」示例。 |
| [Using TypeSafe Jev with the AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk) | Vercel 最完整的实操指南：单问题与多问题调用、按概率阈值路由，以及用 mock evaluation 模型写单元测试。 | 教程 | `TS`<br><sub>noul/choice/score</sub> | 需要 AI SDK 7.0.105 及以上才有 experimental_evaluate。置信度在 providerMetadata 上，不在 answer 上。 |
| [jevai.org community showcase cases](https://www.jevai.org/cases) | 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。 | 开源项目 | — | `宣称未核实` 站点自己标注为「Community Inspiration」，即非官方内容，也未经 TypeSafe 审核。 |

### 上下文压缩

_判断哪些工具调用和结果仍然相关，从而丢弃过期上下文。_

| 例子 | 展示了什么 | 形态 | 代码 | 备注 |
| --- | --- | --- | --- | --- |
| [Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent) | 把 Jev 压缩方案移植过来，与自家在用的摘要器对比实测，最后公开结论：不采用。 | 基准测试 | `Py`<br><sub>noul</sub> | 本目录可信度最高的一条。召回率低于他们现有的摘要器，在相同上下文预算下与「按时间倒序」打平。成本确实低得多。在一个被热炒的模型上公开负面结果，非常少见。 |
| [jcode: memory recall without embeddings](https://github.com/1jehuang/jcode) | 把记忆召回的整套检索栈替换掉 —— 不用 embedding、不用 BM25、不用重排器 —— 改为对每条候选记忆批量问一个 Noul。 | 开源项目 | `Rs`<br><sub>noul</sub> | 找到的最激进的替换：它是移除检索基础设施，而不是给它做增强。这个取舍在大规模下是否成立，尚无实测。 |
| [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)<br><sub>tamaratran</sub> | 一个 Claude Code 插件，用逐条决策取代压缩式摘要：过期的工具调用被丢弃或截断，保留下来的全部逐字不变。 | 插件 | `TS`<br><sub>noul</sub> | 每次工具调用恰好两个 noul：知道这次调用发生过是否还有意义、以及是否还需要完整原文输出。尽管它自己的描述里用了「打分」，实际并未使用 score 原语。 |
| [hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) | 九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。 | 插件 | `Py`<br><sub>choice/score/noul</sub> | 值得一提的是它公开了一个被放弃的用法：用 Jev 做交接摘要的召回率，反而不如原始对话记录。 |
| [jev-pruner](https://github.com/tamaratran/jev-pruner)<br><sub>tamaratran</sub> | 在模型看到之前先修剪冗长的 shell 输出，每个片段问一个 Noul。 | 插件 | `TS`<br><sub>noul</sub> | 与 fast-jev-compaction 同一作者，范围更窄。如果你只想修剪 Bash 输出、不想动整段对话记录，这个更合适。 |
| [Winnow](https://github.com/GhalebDweikat/winnow) | 给 Claude Code 做上下文垃圾回收。Read / Bash / Grep 吐一大堆时，Jev 先判断哪些真和当前任务有关。 | 插件 | `Py`<br><sub>noul</sub> | 采用「保留/丢弃」双阈值，并提供一个召回命令取回全文 —— 这是有损过滤该有的安全阀。 |

### 安全闸门

_在执行前判断一个动作是否安全。_

| 例子 | 展示了什么 | 形态 | 代码 | 备注 |
| --- | --- | --- | --- | --- |
| [Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) ⭐ | 给每条召回的段落打分，再由代码决定哪些能进入回答模型 —— 矛盾的标记保留，夹带提示注入的直接丢弃。 | 官方文档 | `Py` | — |
| [Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails) ⭐ | 用一次请求筛查 LLM 应用的每一条进出消息，既点明风险类型、又给「照做会造成多大危害」打分。 | 官方文档 | `Py`<br><sub>noul/score</sub> | 有用，但请对照 docs/patterns.md 的 safety-gating 一节：概率性筛查属于纵深防御，不是安全边界。 |
| [sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api) | 作为审核 API 的直接替代：一次请求并行问多个 Noul，每个危害类别一个，且每条指令都带反注入前缀。 | 开源项目 | `Go`<br><sub>noul</sub> | 最清楚地展示了并行扇出如何改变成本结构：逐类别的危害筛查从「每类一次请求」变成「总共一次请求」。 |
| [claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates) | 三个可独立安装的 Claude Code 插件 —— 护栏、模型路由、技能推荐 —— 各自带 hook 和测试。 | 插件 | `Py` `TS`<br><sub>choice/score/noul</sub> | 它的技能推荐插件实现了同名官方 cookbook，包括「不把技能清单给主模型看」这一步，从而让选择真正由 Jev 做出。 |
| [@langchain/typesafe](https://github.com/langchain-ai/langchainjs) | LangChain 集成的 JavaScript 对应版本，分类器与 middleware 形状一致。 | 平台集成 | `TS`<br><sub>choice/score/noul</sub> | — |
| [DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat) | 从三个维度审查每次工具调用：风险等级、用户是否授权、以及一个显式的提示注入压力检查。 | 开源项目 | `TS`<br><sub>choice/noul</sub> | 把「提示注入压力」单独作为一个问题来问，这个设计值得照抄 —— 但请参见 docs/patterns.md，理解为什么这属于纵深防御而非安全边界。 |
| [agentgateway: CI-validated LLM guardrail](https://github.com/agentgateway/agentgateway) | 三个共用同一严重度量表的 Score 问题，两项以上越线即拦截请求，并且失败时默认关闭。 | 开源项目 | `Rs`<br><sub>score</sub> | 闸门失败时默认关闭是正确的默认值，也很容易做错。注意与本目录里那些交易类例子的对比 —— 它们刻意选择失败时开放。 |
| [Jev-cu](https://github.com/Sac-Y/Jev-cu) | 一个 computer-use 智能体：判断该对无障碍树里哪个元素操作，并单独用一个 noul 判断这个动作是否需要用户显式确认。 | 开源项目 | `JS`<br><sub>choice/noul</sub> | `无许可证` 它的风险 noul 明确列举了需要人介入的情形 —— 删除、发送、付款、权限、凭据 —— 并由本地策略闸门执行阈值。只发文本，从不发截图。无许可证文件。 |
| [jev-mcp](https://github.com/jkudish/jev-mcp) | 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。 | 插件 | `JS`<br><sub>choice/score/noul</sub> | 把一个模型拆成按任务命名的多个工具，对智能体很友好：它只需选一个动词，而不必自己组装问题。 |
| [jev-drone](https://github.com/RomanSlack/jev-drone) | 拿 Jev 控无人机。底层飞控继续负责稳定和安全，Jev 只做爬升、刹车、穿越障碍这类上层判断。 | 开源项目 | `Py`<br><sub>choice/score/noul</sub> | `宣称未核实` 分层才是重点：判断以几赫兹运行，而控制与安全反射快上几个数量级、且完全在代码里。它自报的数字来自一次短程运行，作者本人也这么说明。 |
| [Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)<br><sub>brainstormity</sub> | 一个 Discord 审核机器人：用 Choice 给每条消息定级、用 Noul 表示封禁紧急度，管理员一旦赦免，该消息会作为「安全先例」注入后续请求。 | 开源项目 | `Py`<br><sub>choice/noul</sub> | 找到的最清晰的终端应用，也是唯一用「上下文内先例」来抑制重复误判的。README 提到许可，但仓库里没有 LICENSE 文件。 |
| [Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)<br><sub>Sydney Runkle, Hunter Lovell</sub> | LangChain 的讲解兼集成实操：三种问题类型，加上模型路由、以及在高风险工具调用执行前拦截它。 | 文章 | `Py` | `厂商自报数据` 文中照搬厂商 200x/400x 的数字，没有独立实测。该页 <title> 标签与此处采用的页面标题不一致。 |
| [langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe) | LangChain 集成：一个分类器，外加用于模型路由、以及在高风险工具调用执行前拦截它的实验性 middleware。 | 平台集成 | `Py`<br><sub>choice/score/noul</sub> | `需早期访问` 目前是 alpha 版。AutoModeMiddleware 是已公开的、最清楚的「拦截破坏性工具调用」示例。 |

### 输出校验

_在输出到达用户前，按评分标准检查模型产出。_

| 例子 | 展示了什么 | 形态 | 代码 | 备注 |
| --- | --- | --- | --- | --- |
| [Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check) ⭐ | 用一个 Choice 对着原文核查引用是否错误或凭空编造，并用它的置信度把边缘情况标出来送审。 | 官方文档 | `Py`<br><sub>choice</sub> | — |
| [Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails) ⭐ | 用一次请求筛查 LLM 应用的每一条进出消息，既点明风险类型、又给「照做会造成多大危害」打分。 | 官方文档 | `Py`<br><sub>noul/score</sub> | 有用，但请对照 docs/patterns.md 的 safety-gating 一节：概率性筛查属于纵深防御，不是安全边界。 |
| [jev-mcp](https://github.com/jkudish/jev-mcp) | 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。 | 插件 | `JS`<br><sub>choice/score/noul</sub> | 把一个模型拆成按任务命名的多个工具，对智能体很友好：它只需选一个动词，而不必自己组装问题。 |
| [perch: semantic code linting](https://github.com/lakeday-org/perch) | 先用 tree-sitter 找出并排序方法，再把用户自写的 YAML 规则编译成 noul；严重度取评分量表的期望值，而不是概率最高的那一档。 | 开源项目 | `JS`<br><sub>choice/score/noul</sub> | 找到的概率处理最讲究的一个。在 score 的各级上取期望值、而不是取概率最高的那一档，才是对「score 究竟返回了什么」的正确统计读法。 |
| [Canny](https://github.com/qkal/Canny) | 防 Coding Agent 嘴硬说自己做完了。看工具输出、代码 diff 和测试结果，再判断完成声明靠不靠谱。 | 开源项目 | `TS`<br><sub>noul/score</sub> | 这个模式用得很到位：被校验的对象是智能体对自己的声明 —— 而这恰恰是独立评判者最有价值的地方。 |
| [Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)<br><sub>Near Here</sub> | 找到的唯一三方横评，每个模型分别调过提示词，且明确把范围限定在单一任务上、不做通用排名。 | 基准测试 | — | 自我限定很规范：这是用例研究，不是模型排行榜。这种克制比数字本身更少见。 |
| [TypeSafe's Jev: Can decision models replace LLM judges?](https://arize.com/blog/typesafe-jev-llm-judge/)<br><sub>Laurie Voss</sub> | 汇总了目前已有的第三方评测，并讨论决策模型能在多大程度上顶替 LLM 评判者。 | 文章 | — | 作为汇总很有用。注意它本身不是实测 —— 文中说明 Arize 当时还没跑自己的基准。 |

### 人工升级

_用校准置信度决定哪些情况必须由人来看。_

| 例子 | 展示了什么 | 形态 | 代码 | 备注 |
| --- | --- | --- | --- | --- |
| [Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence) ⭐ | 把年报分入 75 个行业组，再根据答案自身的置信度决定：报这个细分组，还是退回上一层的大类。 | 官方文档 | `Py`<br><sub>choice</sub> | 「与其猜一个细标签，不如退回粗标签」—— 整套 cookbook 里最可复用的一个想法。 |
| [Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check) ⭐ | 用一个 Choice 对着原文核查引用是否错误或凭空编造，并用它的置信度把边缘情况标出来送审。 | 官方文档 | `Py`<br><sub>choice</sub> | — |
| [Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment) ⭐ | 判断两份商品目录间 450 个候选配对里哪些指的是同一个东西 —— 一个 Score 就够，它的三级正好对应三种可执行动作。 | 官方文档 | `Py`<br><sub>score</sub> | 设计很优雅：把量表的级别直接设成「合并 / 不动 / 转人工」，于是根本不需要再去拟合阈值。 |
| [Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook) ⭐ | 在内容审核决策里显式加入「不确定」这个选项，并衡量标签一致率与自动处置比例之间的取舍。 | 官方文档 | `Py`<br><sub>choice</sub> | 最清楚地展示了定阈值时你实际在权衡的东西：自动化率 vs 错误率。 |
| [Cookbook: Self-consistency with nouls](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook) ⭐ | 把不确定的概率转人工复核，同时保留底层的 noul 数值本身，而不是压成一个标签了事。 | 官方文档 | `Py`<br><sub>noul</sub> | — |
| [Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) ⭐ | 把 confidence 当作第二个维度：答案告诉你「是什么」，置信度告诉你「该不该照它执行」。 | 官方文档 | `Py` | — |
| [Confidence](https://docs.typesafe.ai/confidence) ⭐ | confidence 如何从概率分布推导出来，以及为什么在一种问题类型上调好的阈值不能挪到另一种上用。 | 官方文档 | — | 「自动执行还是转人工」这套设计的理论基础。定任何阈值前都该先读。 |
| [Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html) | 把下游任务 id 变成 choice 的选项集，并用最小置信度闸门把不确定的运行转给人处理。 | 平台集成 | `Py`<br><sub>choice</sub> | 用校准过的决策给数据流水线做分支很契合，而且文档明智地建议锁定版本号、而不是跟着别名走。 |
| [Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe) | 把工具目录编译成问题，再从答案还原出 tool call，并为「弃权」和「需确认」两种情况定义了专门的错误类型。 | 开源项目 | `Py`<br><sub>choice</sub> | 它的 docstring 把约束讲得很直白：Jev 不是 LLM、没有 tool calling，所以这个 provider 负责双向翻译。 |
| [Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero) | 七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。 | 开源项目 | `TS`<br><sub>choice/noul</sub> | 「阈值该设多少」的最佳答案是：没有单一答案。这里不同决策的阈值从 0.3 到 0.9 不等，取决于判错的代价。 |
| [jev-review](https://github.com/devagrawal09/jev-review) | 代码审查前先过一遍 Jev，把高风险改动挑出来，再交给更贵的大模型或人。带本地看板。 | 开源项目 | `TS`<br><sub>choice/score/noul</sub> | `已归档` 它记录的多阶段流水线值得一读，但提交在创建次日就停了 —— 请当作设计参考，而不是仍在维护的工具。 |
| [Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til) | 独立的韩语实测笔记，报告仅仅把选项顺序倒过来，就能让概率移动到足以翻转 0.9 阈值的程度。 | 基准测试 | `Py` | `无许可证` `宣称未核实` 在所有资料里找到的最具操作价值的工程警示：如果仅仅选项顺序就能把概率推过你的阈值，那你的阈值没有看上去那么稳。这是独立且未被复现的结果，具体幅度请当作指示性数据。 |
| [Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)<br><sub>brainstormity</sub> | 一个 Discord 审核机器人：用 Choice 给每条消息定级、用 Noul 表示封禁紧急度，管理员一旦赦免，该消息会作为「安全先例」注入后续请求。 | 开源项目 | `Py`<br><sub>choice/noul</sub> | 找到的最清晰的终端应用，也是唯一用「上下文内先例」来抑制重复误判的。README 提到许可，但仓库里没有 LICENSE 文件。 |
| [Example: confidence-gated escalation](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-confidence-gate/main.py) | 带「自动执行或转人工」闸门的路由；策略函数刻意留空 —— 阈值该定在哪，是你的决定。 | 代码片段 | `Py`<br><sub>choice</sub> | `代码未实测` 文档字符串里列出了取舍：一个阈值还是两个、是否按队列区分、以及什么时候「第二名的概率」比置信度更重要。 |
| [An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)<br><sub>Lindfors</sub> | 找到的最好的独立实测：固定单一模型版本、24 份挪威语文档，开篇就展示了一个模型答错、但同时正确报出低置信度的案例。 | 基准测试 | — | 方法论交代干净，并诚实限定为「单日快照」。开篇就摆失败案例，这才让它成为真正的校准检验，而不是一篇软文。 |

### 模型路由

_选择由哪个下游模型或档位处理请求。_

| 例子 | 展示了什么 | 形态 | 代码 | 备注 |
| --- | --- | --- | --- | --- |
| [Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade) ⭐ | 「小模型 → 校验 → 推理模型」的两段级联，用一小部分成本拿到接近大推理模型的质量。 | 官方文档 | `Py` | — |
| [Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing) ⭐ | 对进来的请求做分类，路由到足够用的最便宜那个处理方：确定性代码、专用 LLM、或人。 | 官方文档 | `Py`<br><sub>choice</sub> | — |
| [claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates) | 三个可独立安装的 Claude Code 插件 —— 护栏、模型路由、技能推荐 —— 各自带 hook 和测试。 | 插件 | `Py` `TS`<br><sub>choice/score/noul</sub> | 它的技能推荐插件实现了同名官方 cookbook，包括「不把技能清单给主模型看」这一步，从而让选择真正由 Jev 做出。 |
| [@langchain/typesafe](https://github.com/langchain-ai/langchainjs) | LangChain 集成的 JavaScript 对应版本，分类器与 middleware 形状一致。 | 平台集成 | `TS`<br><sub>choice/score/noul</sub> | — |
| [jev-review](https://github.com/devagrawal09/jev-review) | 代码审查前先过一遍 Jev，把高风险改动挑出来，再交给更贵的大模型或人。带本地看板。 | 开源项目 | `TS`<br><sub>choice/score/noul</sub> | `已归档` 它记录的多阶段流水线值得一读，但提交在创建次日就停了 —— 请当作设计参考，而不是仍在维护的工具。 |
| [hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) | 九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。 | 插件 | `Py`<br><sub>choice/score/noul</sub> | 值得一提的是它公开了一个被放弃的用法：用 Jev 做交接摘要的召回率，反而不如原始对话记录。 |
| [jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) | 先让 Jev 判断这一轮编程任务有多难，再决定模型档位、推理深度和速度模式。 | 插件 | `JS`<br><sub>choice/score</sub> | 先给难度打分、再在代码里映射到档位，而不是直接选档位 —— 这是两种模型路由写法里更好维护的那个。 |
| [Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)<br><sub>Sydney Runkle, Hunter Lovell</sub> | LangChain 的讲解兼集成实操：三种问题类型，加上模型路由、以及在高风险工具调用执行前拦截它。 | 文章 | `Py` | `厂商自报数据` 文中照搬厂商 200x/400x 的数字，没有独立实测。该页 <title> 标签与此处采用的页面标题不一致。 |
| [Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)<br><sub>Mehul Gupta</sub> | 逐个用例走一遍 —— 智能体路由、智能体内部的决策层、工单分拣 —— 每个都给出具体的选项集和示例响应。 | 教程 | `Py`<br><sub>choice</sub> | `付费墙` 这位作者两篇里更有用的一篇。副标题承诺的免费通道，正文其实没给。 |
| [langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe) | LangChain 集成：一个分类器，外加用于模型路由、以及在高风险工具调用执行前拦截它的实验性 middleware。 | 平台集成 | `Py`<br><sub>choice/score/noul</sub> | `需早期访问` 目前是 alpha 版。AutoModeMiddleware 是已公开的、最清楚的「拦截破坏性工具调用」示例。 |

### 并行扇出

_把大量问题（包括推测性的）打包进一次请求，再由代码挑出真正用得上的答案。_

| 例子 | 展示了什么 | 形态 | 代码 | 备注 |
| --- | --- | --- | --- | --- |
| [Cookbook: Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions) ⭐ | 对一篇长文提 13 个合规问题，证明全部打包进一次调用便宜得多、也快得多，而答案不变。 | 官方文档 | `Py` | 最清楚地说明了为什么 state 只被读一次、而所有问题是并行评估的。 |
| [Pattern: Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out) ⭐ | 把大量问题（包括可能用不上的）打包进一次请求，之后再由代码决定哪些答案真的用得上。 | 官方文档 | `Py` | — |
| [Quickstart](https://docs.typesafe.ai/introduction/quickstart) ⭐ | 官方第一课：一条工单，一次请求里同时问一个 Choice、一个 Score 和一个 Noul，给了 Python / JS / cURL 三种写法。 | 官方文档 | `Py` `TS` `sh`<br><sub>choice/score/noul</sub> | — |
| [AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe) | 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。 | 开源项目 | `Py`<br><sub>choice/score/noul</sub> | 目前找到的工程最严谨的集成。因为官方没有公开 Jev 的 tokenizer，它把序列化请求保守限制在 30,976 UTF-8 字节；响应含非法 UTF-8 时用 base64 保留原始字节而非替换字符。 |
| [sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api) | 作为审核 API 的直接替代：一次请求并行问多个 Noul，每个危害类别一个，且每条指令都带反注入前缀。 | 开源项目 | `Go`<br><sub>noul</sub> | 最清楚地展示了并行扇出如何改变成本结构：逐类别的危害筛查从「每类一次请求」变成「总共一次请求」。 |
| [jev-ultrafast](https://github.com/browser-use/jev-ultrafast)<br><sub>Browser Use</sub> | Browser Use 做的高速浏览器 Agent。Jev 每一步只判断「做什么、点哪个元素」，要打字才叫小模型。 | 开源项目 | `Py`<br><sub>choice</sub> | `厂商自报数据` 教科书级的并行扇出例子：一次请求同时返回操作本身、以及若干可能操作各自的推测性目标，再由代码取用实际相关的那个。航班搜索耗时是项目自报数字。 |
| [ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook) | 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。 | 教程 | `Py`<br><sub>choice/score/noul</sub> | 找到的最好的结构化教程。它明确指出类型化输出不保证决策正确、列出了官方记录的弱项，并且对自己给出的成本示例做了限定而不是拿来营销。 |
| [jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat) | 一个完全不含语言模型的 tool calling 聊天机器人：一次请求同时问清请求类型、该调哪个工具、以及每个工具的参数。 | 开源项目 | `TS`<br><sub>choice/noul</sub> | 本目录里最纯粹的演示：已核实完全不含 LLM。想知道「只靠封闭集决策」能把智能体循环推进到哪一步、又在哪里必须停下，读它。 |
| [OneVOneJev](https://github.com/emrickgarrett/OneVOneJev) | 浏览器里的 1v1 FPS。每个决策 tick 都要判断走位、视角、瞄准、开火和跳跃。 | 开源项目 | `TS`<br><sub>choice</sub> | `代码未实测` `无许可证` 主要价值在于它是个延迟压力测试：实时循环是对「每次决策一个往返」最严苛的场景。无许可证文件。 |
| [A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)<br><sub>Flavio Copes</sub> | 技术密度最高的独立讲解：JS / Python / AI SDK 三种代码、三种应答结构、进阶模式，还诚实列出了模型的失效场景。 | 教程 | `JS` `Py` `TS`<br><sub>choice/score/noul</sub> | 想看代码的话，这是最好的单篇第三方文章。作者把算术、日期、计数列为失效场景，说明他真用过模型，而不是抄新闻稿。 |
| [Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py) | 一次问清操作本身、以及每个可能操作各自的目标 —— 于是浏览器的一步永远不需要第二次往返。 | 代码片段 | `Py`<br><sub>choice/noul</sub> | `代码未实测` 按官方 API 参考编写，未针对线上 API 实际执行。注意预算：推测性问题很便宜，但它们和其他内容共享每次请求 64k 的上下文。 |
| [Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py) | 最小化的第一次调用：同时问一个 choice、一个 score 和一个 noul，并标注了容易踩的那几处不对称。 | 代码片段 | `Py`<br><sub>choice/score/noul</sub> | `代码未实测` 按官方 API 参考编写并逐字段对照核实，但未针对线上 API 实际执行过。 |
| [Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/) | Workers AI binding 与 REST 示例：一次调用同时问 noul、choice、score，并给出含逐答案置信度的完整响应。 | 平台集成 | `TS` `sh`<br><sub>noul/choice/score</sub> | 这里模型串是 typesafe/jev，且 state 与 questions 被包在 `input` 对象里。原生客户端不能只换 URL 就移植过来。 |
| [Using TypeSafe Jev with the AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk) | Vercel 最完整的实操指南：单问题与多问题调用、按概率阈值路由，以及用 mock evaluation 模型写单元测试。 | 教程 | `TS`<br><sub>noul/choice/score</sub> | 需要 AI SDK 7.0.105 及以上才有 experimental_evaluate。置信度在 providerMetadata 上，不在 answer 上。 |

### 检索与排序

_对来自廉价检索步骤的候选做打分或重排。_

| 例子 | 展示了什么 | 形态 | 代码 | 备注 |
| --- | --- | --- | --- | --- |
| [Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) ⭐ | 给每条召回的段落打分，再由代码决定哪些能进入回答模型 —— 矛盾的标记保留，夹带提示注入的直接丢弃。 | 官方文档 | `Py` | — |
| [Cookbook: Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find) ⭐ | 对一份服务条款做语义检索：一次请求用 Choice 给 218 个行号打分，同时用 Noul 判断文档里到底有没有答案。 | 官方文档 | `Py`<br><sub>choice/noul</sub> | 一个巧妙设计：那个 Noul 防止了「在一堆无关的行里自信地挑出最好的一行」。 |
| [Cookbook: Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe) ⭐ | 对 40 个法律检索问题各取 30 条 BM25 候选，按「问题-候选」逐对提问重排，top-1 与 top-10 准确率均大幅提升。 | 官方文档 | `Py` | — |
| [AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe) | 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。 | 开源项目 | `Py`<br><sub>choice/score/noul</sub> | 目前找到的工程最严谨的集成。因为官方没有公开 Jev 的 tokenizer，它把序列化请求保守限制在 30,976 UTF-8 字节；响应含非法 UTF-8 时用 base64 保留原始字节而非替换字符。 |
| [OpenViking: retrieval reranking](https://github.com/volcengine/OpenViking) | 单次批量请求里对每个候选文档问一个 Noul，直接把「是」的概率当相关性分数。 | 开源项目 | `Py`<br><sub>noul</sub> | — |
| [FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py) | 两段式 MCP 工具检索：先用一个宽 Choice 对整个目录粗排，再给候选短名单配完整描述，每个候选各配一个 Noul 判断它到底是否胜任。 | 开源项目 | `Py`<br><sub>choice/noul</sub> | 逐候选的那个 Noul 才是关键：它让检索在没有工具匹配时返回空，而不是自信地返回最不离谱的那个。 |
| [jcode: memory recall without embeddings](https://github.com/1jehuang/jcode) | 把记忆召回的整套检索栈替换掉 —— 不用 embedding、不用 BM25、不用重排器 —— 改为对每条候选记忆批量问一个 Noul。 | 开源项目 | `Rs`<br><sub>noul</sub> | 找到的最激进的替换：它是移除检索基础设施，而不是给它做增强。这个取舍在大规模下是否成立，尚无实测。 |
| [LanceDB TypeSafeReranker](https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py) | 向量数据库的重排器：对每条结果问一个 Noul，把「是」的概率当作绝对相关性分数 —— 可以跨查询比较。 | 开源项目 | `Py`<br><sub>noul</sub> | 注意它的设计主张：因为 noul 是绝对概率而不是相对排名，分数可以跨查询比较，固定阈值才有意义。 |
| [no-mistakes: review context selection](https://github.com/kunchenguid/no-mistakes) | 对每个候选文件打一个 Score 来挑选审查上下文；实测结果是：计费输入明显增加，而实际耗时几乎没改善。 | 基准测试 | `Go`<br><sub>score</sub> | 他们自己的建议是：这个功能保持可选、默认关闭、不要宣传省钱。诚实的实测就该长这样。 |
| [jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) | 一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。 | 开源项目 | `Java`<br><sub>choice/score/noul</sub> | 手机端的一个清晰分工：Jev 负责判断与排序，其他模型负责读屏和写字。它会读取屏幕上的消息内容，运行前请先考虑隐私影响。 |
| [jev-search](https://github.com/superagents-lab/jev-search) | Jev 驱动的网页搜索：先选时间窗口和最佳查询改写，再分批对结果逐条用 noul 重排。 | 开源项目 | `TS`<br><sub>choice/noul</sub> | 把整条检索链都变成决策：查哪些引擎、如何改写查询、哪些结果留下。 |
| [pg-jev](https://github.com/realZachi/pg-jev) | 一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。 | 开源项目 | `Py` `sh`<br><sub>choice/score/noul</sub> | 找到的最出人意料的集成。把校准决策放进 SQL 函数，改变了这类判断能存在的位置 —— 但也意味着一条查询从此会花钱、并且会阻塞在网络调用上。 |
| [jev-mcp](https://github.com/jkudish/jev-mcp) | 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。 | 插件 | `JS`<br><sub>choice/score/noul</sub> | 把一个模型拆成按任务命名的多个工具，对智能体很友好：它只需选一个动词，而不必自己组装问题。 |
| [neo4jev](https://github.com/jexp/neo4jev) | 把 Jev 塞进知识图谱。每走到一个节点，判断下一条最值得走的边，再一路找下去。 | 开源项目 | `Py`<br><sub>choice</sub> | 图遍历天然契合：每一跳都是在当前节点的边集上做封闭选择，而整条路径便宜的前提正是每一跳都便宜。 |
| [Blink](https://github.com/ellipsis-dev/blink) | 把 Jev 当代码库导航器。每走到一层目录，就判断哪些文件和当前问题最相关，再继续往下找。 | 开源项目 | `TS`<br><sub>choice</sub> | `无许可证` 逐层下降本质上和官方层级分类 cookbook 里「在层级上做 beam search」是同一个形状，只是这里作用在文件系统上。 |

### 结构化抽取

_从杂乱文本中取出类型化字段 —— 靠在候选中选择，而不是生成。_

| 例子 | 展示了什么 | 形态 | 代码 | 备注 |
| --- | --- | --- | --- | --- |
| [Cookbook: Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook) ⭐ | 抽取绝对与相对日期：先问文档里点明了哪些部分，再在代码里做解析与校验，并按置信度决定是否送审。 | 官方文档 | `Py` | 注意这里的分工：模型只负责点明部件，算术交给代码。日期比较是官方承认的弱项。 |
| [Cookbook: Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook) ⭐ | 先用正则找出候选的邮箱、电话、金额，再让模型挑出被问到的那一段，于是代码拿到的是逐字原值。 | 官方文档 | `Py`<br><sub>choice</sub> | 用「不会生成」的模型做抽取的核心思路：先枚举候选，再做选择。 |
| [Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat) ⭐ | 用两次请求把丢了格式的纯文本还原成 Markdown：一次把硬换行的段落重新接起来，一次给每个块分类。 | 官方文档 | `Py` | 展示了「伴随问题」的写法：只在另一个答案让它变得相关时才去读它。 |
| [Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade) ⭐ | 「小模型 → 校验 → 推理模型」的两段级联，用一小部分成本拿到接近大推理模型的质量。 | 官方文档 | `Py` | — |

### 分类

_把条目归入分类体系，包括用概率遍历的深层层级。_

| 例子 | 展示了什么 | 形态 | 代码 | 备注 |
| --- | --- | --- | --- | --- |
| [Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence) ⭐ | 把年报分入 75 个行业组，再根据答案自身的置信度决定：报这个细分组，还是退回上一层的大类。 | 官方文档 | `Py`<br><sub>choice</sub> | 「与其猜一个细标签，不如退回粗标签」—— 整套 cookbook 里最可复用的一个想法。 |
| [Cookbook: Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification) ⭐ | 用对 Choice 概率做并行 beam search 的方式，遍历专利、零售、生物医学、源码这几套很深的分类体系。 | 官方文档 | `Py`<br><sub>choice</sub> | 单个 Choice 最多 255 选项这个上限的绕法。 |
| [Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment) ⭐ | 判断两份商品目录间 450 个候选配对里哪些指的是同一个东西 —— 一个 Score 就够，它的三级正好对应三种可执行动作。 | 官方文档 | `Py`<br><sub>score</sub> | 设计很优雅：把量表的级别直接设成「合并 / 不动 / 转人工」，于是根本不需要再去拟合阈值。 |
| [Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat) ⭐ | 用两次请求把丢了格式的纯文本还原成 Markdown：一次把硬换行的段落重新接起来，一次给每个块分类。 | 官方文档 | `Py` | 展示了「伴随问题」的写法：只在另一个答案让它变得相关时才去读它。 |
| [worldmonitor: news threat classification](https://github.com/koala73/worldmonitor) | 用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。 | 基准测试 | `TS`<br><sub>choice</sub> | `仅影子运行` 接进去了但故意不生效：按他们自己的说法，Jev 返回的任何东西都不会进入标签、缓存行或告警。带黄金测试集。想在不拿生产环境下注的前提下试新模型，这是值得照抄的做法。 |
| [json-render](https://github.com/vercel-labs/json-render)<br><sub>Vercel Labs</sub> | Vercel Labs 的生成式 UI 框架。实验里 Jev 不逐 token 写 JSON，只负责选组件、属性和布局。 | 开源项目 | `TS`<br><sub>choice</sub> | 对生成式 UI 的一个真正不同的理解：从组件注册表里做选择、而不是生成标记，意味着输出不可能引用一个不存在的组件。 |
| [Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero) | 七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。 | 开源项目 | `TS`<br><sub>choice/noul</sub> | 「阈值该设多少」的最佳答案是：没有单一答案。这里不同决策的阈值从 0.3 到 0.9 不等，取决于判错的代价。 |
| [pg-jev](https://github.com/realZachi/pg-jev) | 一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。 | 开源项目 | `Py` `sh`<br><sub>choice/score/noul</sub> | 找到的最出人意料的集成。把校准决策放进 SQL 函数，改变了这类判断能存在的位置 —— 但也意味着一条查询从此会花钱、并且会阻塞在网络调用上。 |
| [jev-mcp](https://github.com/jkudish/jev-mcp) | 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。 | 插件 | `JS`<br><sub>choice/score/noul</sub> | 把一个模型拆成按任务命名的多个工具，对智能体很友好：它只需选一个动词，而不必自己组装问题。 |
| [Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til) | 独立的韩语实测笔记，报告仅仅把选项顺序倒过来，就能让概率移动到足以翻转 0.9 阈值的程度。 | 基准测试 | `Py` | `无许可证` `宣称未核实` 在所有资料里找到的最具操作价值的工程警示：如果仅仅选项顺序就能把概率推过你的阈值，那你的阈值没有看上去那么稳。这是独立且未被复现的结果，具体幅度请当作指示性数据。 |
| [perch: semantic code linting](https://github.com/lakeday-org/perch) | 先用 tree-sitter 找出并排序方法，再把用户自写的 YAML 规则编译成 noul；严重度取评分量表的期望值，而不是概率最高的那一档。 | 开源项目 | `JS`<br><sub>choice/score/noul</sub> | 找到的概率处理最讲究的一个。在 score 的各级上取期望值、而不是取概率最高的那一档，才是对「score 究竟返回了什么」的正确统计读法。 |
| [Prism](https://github.com/irfndi/prism-liquidity-agent) | 不直接让 Jev 下单。它判断 toxic flow、市场压力、均值回归之类的状态，再交给原来的策略。 | 开源项目 | `TS`<br><sub>choice/score</sub> | 两个金融类条目中架构更稳妥的一个：模型只负责刻画状态，下单由原有代码决定。不构成投资建议。 |
| [Blink](https://github.com/ellipsis-dev/blink) | 把 Jev 当代码库导航器。每走到一层目录，就判断哪些文件和当前问题最相关，再继续往下找。 | 开源项目 | `TS`<br><sub>choice</sub> | `无许可证` 逐层下降本质上和官方层级分类 cookbook 里「在层级上做 beam search」是同一个形状，只是这里作用在文件系统上。 |
| [SemDecide](https://github.com/sharziki/semdecide) | 把 Jev 做成命令行。Shell 里直接分类、打分、过滤，适合接爬虫、CI 和数据流水线。 | 插件 | `Py` `sh`<br><sub>choice/score/noul</sub> | 能从管道里调用的语义判断，确实是一个新的 shell 原语。项目还小，接入要紧的流程前请先读代码。 |
| [An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)<br><sub>Lindfors</sub> | 找到的最好的独立实测：固定单一模型版本、24 份挪威语文档，开篇就展示了一个模型答错、但同时正确报出低置信度的案例。 | 基准测试 | — | 方法论交代干净，并诚实限定为「单日快照」。开篇就摆失败案例，这才让它成为真正的校准检验，而不是一篇软文。 |
| [Jev - The Ultimate Classification Model?](https://youtube.com/watch?v=X117w2Rark8)<br><sub>Sam Witteveen</sub> | 一位 ML 工程师从分类任务角度做的讲解 —— 这个切入角度最贴近模型的实际能力。 | 视频 | — | 元数据已核实；本条目未逐段核对视频内容。 |
| [jevai.org community showcase cases](https://www.jevai.org/cases) | 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。 | 开源项目 | — | `宣称未核实` 站点自己标注为「Community Inspiration」，即非官方内容，也未经 TypeSafe 审核。 |
| [Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)<br><sub>Near Here</sub> | 找到的唯一三方横评，每个模型分别调过提示词，且明确把范围限定在单一任务上、不做通用排名。 | 基准测试 | — | 自我限定很规范：这是用例研究，不是模型排行榜。这种克制比数字本身更少见。 |

### 机器学习特征抽取

_把自由文本转成数值特征，喂给下游的传统模型。_

| 例子 | 展示了什么 | 形态 | 代码 | 备注 |
| --- | --- | --- | --- | --- |
| [Cookbook: Autoresearch feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery) ⭐ | 一个自动研究循环：自己提出问题、把自由文本转成数值特征、再用误差反过来改进下游的梯度提升回归模型。 | 官方文档 | `Py` | 整套里最不寻常的用法：概率本身就是训练特征，模型输出根本不会被用户看到。 |
| [Prism](https://github.com/irfndi/prism-liquidity-agent) | 不直接让 Jev 下单。它判断 toxic flow、市场压力、均值回归之类的状态，再交给原来的策略。 | 开源项目 | `TS`<br><sub>choice/score</sub> | 两个金融类条目中架构更稳妥的一个：模型只负责刻画状态，下单由原有代码决定。不构成投资建议。 |
| [jev-curate](https://github.com/AkashPriyadarshii/jev-curate) | 拿 Jev 筛训练数据。JSONL / Parquet 先做质量、相关性和风险判断，再决定哪些进后面的训练。 | 开源项目 | `Rs`<br><sub>score/noul</sub> | 数据集筛选在经济性上很合适：百万量级的逐行判断，正是廉价决策调用胜过 LLM 的那个体量。 |

### 文档分拣

_对进来的文档、发票、表单做分类和路由。_

| 例子 | 展示了什么 | 形态 | 代码 | 备注 |
| --- | --- | --- | --- | --- |
| [jevai.org community showcase cases](https://www.jevai.org/cases) | 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。 | 开源项目 | — | `宣称未核实` 站点自己标注为「Community Inspiration」，即非官方内容，也未经 TypeSafe 审核。 |

### 工单分拣

_按意图和紧急度路由支持工单与会话。_

| 例子 | 展示了什么 | 形态 | 代码 | 备注 |
| --- | --- | --- | --- | --- |
| [Quickstart](https://docs.typesafe.ai/introduction/quickstart) ⭐ | 官方第一课：一条工单，一次请求里同时问一个 Choice、一个 Score 和一个 Noul，给了 Python / JS / cURL 三种写法。 | 官方文档 | `Py` `TS` `sh`<br><sub>choice/score/noul</sub> | — |
| [ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook) | 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。 | 教程 | `Py`<br><sub>choice/score/noul</sub> | 找到的最好的结构化教程。它明确指出类型化输出不保证决策正确、列出了官方记录的弱项，并且对自己给出的成本示例做了限定而不是拿来营销。 |
| [Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py) | 最小化的第一次调用：同时问一个 choice、一个 score 和一个 noul，并标注了容易踩的那几处不对称。 | 代码片段 | `Py`<br><sub>choice/score/noul</sub> | `代码未实测` 按官方 API 参考编写并逐字段对照核实，但未针对线上 API 实际执行过。 |
| [Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)<br><sub>Mehul Gupta</sub> | 逐个用例走一遍 —— 智能体路由、智能体内部的决策层、工单分拣 —— 每个都给出具体的选项集和示例响应。 | 教程 | `Py`<br><sub>choice</sub> | `付费墙` 这位作者两篇里更有用的一篇。副标题承诺的免费通道，正文其实没给。 |
| [Jev on AI/ML API](https://docs.aimlapi.com/api-references/decision-models/typesafe/jev) | 又一个网关接入路径，值得记一笔是因为它的端点路径和请求外壳跟原生 API、跟 Cloudflare 都不一样。 | 平台集成 | `Py`<br><sub>noul/choice/score</sub> | 请求发往 /v1/decisions 而不是 /v1/systemone。又一个换网关前该读 docs/compatibility.md 的理由。 |
| [Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/) | Workers AI binding 与 REST 示例：一次调用同时问 noul、choice、score，并给出含逐答案置信度的完整响应。 | 平台集成 | `TS` `sh`<br><sub>noul/choice/score</sub> | 这里模型串是 typesafe/jev，且 state 与 questions 被包在 `input` 对象里。原生客户端不能只换 URL 就移植过来。 |
| [spring-ai-typesafe](https://spring.io/blog/2026/09/21/spring-ai-typesafe-structured-judgment) | 社区维护的 Spring AI starter，把类型化决策带到 Java，用 builder API 封装三种问题类型。 | 平台集成 | `Java`<br><sub>choice/score/noul</sub> | 由 spring-ai-community 维护，不是 Spring 官方团队。目前找到的唯一 Java 路径。 |

### 内容评分

_在有序量表上给质量、风险或相关性打分。_

| 例子 | 展示了什么 | 形态 | 代码 | 备注 |
| --- | --- | --- | --- | --- |
| [Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook) ⭐ | 在内容审核决策里显式加入「不确定」这个选项，并衡量标签一致率与自动处置比例之间的取舍。 | 官方文档 | `Py`<br><sub>choice</sub> | 最清楚地展示了定阈值时你实际在权衡的东西：自动化率 vs 错误率。 |
| [Pattern: Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring) ⭐ | 把一个笼统的判断拆成若干原子评分，再用你自己代码里的权重（而不是提示词里的）组合起来。 | 官方文档 | `Py`<br><sub>score</sub> | — |
| [AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe) | 七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。 | 开源项目 | `Py`<br><sub>choice/score/noul</sub> | 目前找到的工程最严谨的集成。因为官方没有公开 Jev 的 tokenizer，它把序列化请求保守限制在 30,976 UTF-8 字节；响应含非法 UTF-8 时用 base64 保留原始字节而非替换字符。 |
| [worldmonitor: news threat classification](https://github.com/koala73/worldmonitor) | 用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。 | 基准测试 | `TS`<br><sub>choice</sub> | `仅影子运行` 接进去了但故意不生效：按他们自己的说法，Jev 返回的任何东西都不会进入标签、缓存行或告警。带黄金测试集。想在不拿生产环境下注的前提下试新模型，这是值得照抄的做法。 |
| [ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook) | 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。 | 教程 | `Py`<br><sub>choice/score/noul</sub> | 找到的最好的结构化教程。它明确指出类型化输出不保证决策正确、列出了官方记录的弱项，并且对自己给出的成本示例做了限定而不是拿来营销。 |
| [jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) | 一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。 | 开源项目 | `Java`<br><sub>choice/score/noul</sub> | 手机端的一个清晰分工：Jev 负责判断与排序，其他模型负责读屏和写字。它会读取屏幕上的消息内容，运行前请先考虑隐私影响。 |
| [jev-review](https://github.com/devagrawal09/jev-review) | 代码审查前先过一遍 Jev，把高风险改动挑出来，再交给更贵的大模型或人。带本地看板。 | 开源项目 | `TS`<br><sub>choice/score/noul</sub> | `已归档` 它记录的多阶段流水线值得一读，但提交在创建次日就停了 —— 请当作设计参考，而不是仍在维护的工具。 |
| [pg-jev](https://github.com/realZachi/pg-jev) | 一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。 | 开源项目 | `Py` `sh`<br><sub>choice/score/noul</sub> | 找到的最出人意料的集成。把校准决策放进 SQL 函数，改变了这类判断能存在的位置 —— 但也意味着一条查询从此会花钱、并且会阻塞在网络调用上。 |
| [perch: semantic code linting](https://github.com/lakeday-org/perch) | 先用 tree-sitter 找出并排序方法，再把用户自写的 YAML 规则编译成 noul；严重度取评分量表的期望值，而不是概率最高的那一档。 | 开源项目 | `JS`<br><sub>choice/score/noul</sub> | 找到的概率处理最讲究的一个。在 score 的各级上取期望值、而不是取概率最高的那一档，才是对「score 究竟返回了什么」的正确统计读法。 |
| [killmyidea](https://github.com/monteduro/killmyidea) | 输入一个创业点子，Jev 从多个维度打分，最后给你 KILL、FIX 或 SHIP。 | 开源项目 | `TS`<br><sub>score/choice</sub> | `无许可证` 一个小而完整的复合评分例子：若干原子评分在代码里合成三种动作之一 —— 正是官方 composite-scoring 模式推荐的形状。 |
| [Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)<br><sub>brainstormity</sub> | 一个 Discord 审核机器人：用 Choice 给每条消息定级、用 Noul 表示封禁紧急度，管理员一旦赦免，该消息会作为「安全先例」注入后续请求。 | 开源项目 | `Py`<br><sub>choice/noul</sub> | 找到的最清晰的终端应用，也是唯一用「上下文内先例」来抑制重复误判的。README 提到许可，但仓库里没有 LICENSE 文件。 |
| [SemDecide](https://github.com/sharziki/semdecide) | 把 Jev 做成命令行。Shell 里直接分类、打分、过滤，适合接爬虫、CI 和数据流水线。 | 插件 | `Py` `sh`<br><sub>choice/score/noul</sub> | 能从管道里调用的语义判断，确实是一个新的 shell 原语。项目还小，接入要紧的流程前请先读代码。 |
| [jev-curate](https://github.com/AkashPriyadarshii/jev-curate) | 拿 Jev 筛训练数据。JSONL / Parquet 先做质量、相关性和风险判断，再决定哪些进后面的训练。 | 开源项目 | `Rs`<br><sub>score/noul</sub> | 数据集筛选在经济性上很合适：百万量级的逐行判断，正是廉价决策调用胜过 LLM 的那个体量。 |
| [A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)<br><sub>Flavio Copes</sub> | 技术密度最高的独立讲解：JS / Python / AI SDK 三种代码、三种应答结构、进阶模式，还诚实列出了模型的失效场景。 | 教程 | `JS` `Py` `TS`<br><sub>choice/score/noul</sub> | 想看代码的话，这是最好的单篇第三方文章。作者把算术、日期、计数列为失效场景，说明他真用过模型，而不是抄新闻稿。 |
| [jevai.org community showcase cases](https://www.jevai.org/cases) | 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。 | 开源项目 | — | `宣称未核实` 站点自己标注为「Community Inspiration」，即非官方内容，也未经 TypeSafe 审核。 |

### 总览

_介绍模型或整个领域，而非单一模式。_

| 例子 | 展示了什么 | 形态 | 代码 | 备注 |
| --- | --- | --- | --- | --- |
| [typesafe-ai/skills](https://github.com/typesafe-ai/skills) ⭐ | Claude Code 插件背后的官方技能仓库，里面的 SKILL.md 教会智能体如何使用 System One API。 | 插件 | `sh` | — |
| [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) ⭐ | 一个可直接替换 TypeSafeClient 的适配器，底层走普通 LLM API —— 没有 Jev 权限也能跑 Jev 形状的代码。 | SDK | `Py` | 「想试这些模式但还在等候名单上」的最佳解法。注意它的行为与真实模型会有差异。 |
| [@typesafe-ai/sdk (TypeScript / JavaScript)](https://github.com/typesafe-ai/typesafe-sdk-js) ⭐ | 官方 TypeScript 客户端。同时提供 ESM、CJS 和类型声明，辅助函数是小写的 choice()/score()/noul()。 | SDK | `TS` `JS`<br><sub>choice/score/noul</sub> | 需要 Node.js 20 及以上。辅助工厂函数在这里是小写函数，与 Python 的大写类不同。 |
| [typesafe-sdk (Python)](https://github.com/typesafe-ai/typesafe-sdk-python) ⭐ | 官方 Python 客户端。含同步与异步客户端、支持 retry-after 的重试策略，以及 Choice/Score/Noul 辅助类。 | SDK | `Py`<br><sub>choice/score/noul</sub> | Python 里方法名是 system_one，JavaScript 里是 systemOne。跨语言移植时很容易写错。 |
| [API reference](https://docs.typesafe.ai/api) ⭐ | 唯一的端点 POST /v1/systemone，给出三种问题类型的完整请求与应答结构。 | 官方文档 | `sh` `Py` `TS` | 接任何集成前先读这页：noul 应答不带 confidence 字段，choice 和 score 才带。 |
| [Models, pricing and limits](https://docs.typesafe.ai/models) ⭐ | 权威参数表：jev-1.13.0、输入 $0.042/Mtok 且输出免费、64k 上下文、state 加最长问题 32k、仅支持文本输入。 | 官方文档 | `sh` `Py` `TS` | 该页还说明英语是主要训练语言、中日韩文「能处理但不同等」。速率限制附有官方警告：可能随时变动。 |
| [Official agent skill for Claude Code](https://docs.typesafe.ai/agent-skill) ⭐ | 把 TypeSafe 官方技能装进 Claude Code，让智能体自己写出正确的 Jev 调用，不必每次手动贴 API 结构。 | 官方文档 | `sh` | — |
| [Primitives: Choice, Score, Noul](https://docs.typesafe.ai/primitives) ⭐ | 三个原语各自的用途与 criteria 写法，含 Choice 最多 255 个选项、Score 只能 2–10 级这些硬限制。 | 官方文档 | `Py` `TS`<br><sub>choice/score/noul</sub> | — |
| [Introducing System One models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) ⭐<br><sub>Diogo Almeida</sub> | 发布博文：什么是 System One 模型、为什么要把决策从生成里拆出来，以及厂商自报的延迟与成本数字。 | 文章 | — | `厂商自报数据` 文中所有速度与成本数字都是厂商自测。请当作宣称，而不是实测结果。 |
| [Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13) ⭐ | 厂商自己列出的失效场景：字面化理解、算术与计数、日期比较、间接指代、夹杂大量无关细节的长 state、对抗性内容。 | 官方文档 | — | 官方文档里最有用、却最少被引用的一页。它还解释了一件事：对选项做一个 Choice，和每个选项各问一个 Noul，问的根本不是同一个问题。 |
| [Use case map](https://docs.typesafe.ai/concepts/use-case-map) ⭐ | 厂商自己的分类体系：五大类、十九个行业方向、十种决策形态（从分类一直到结构化数据抽取）。 | 官方文档 | — | 用来找与你问题形状相近的用例。本目录的模式分类法与它做过交叉核对。 |
| [OpenCode Zen: Jev resale](https://github.com/anomalyco/opencode) | 一个编程智能体，其托管网关转售 Jev，还提供一个免费档位的模型 id。 | 平台集成 | `TS` | 值得知道，因为它是少数提供免费模型 id 的路径之一 —— 在早期访问仍需排队时很有用。 |
| [Opik TypeSafe tracker](https://github.com/comet-ml/opik/blob/main/sdks/python/src/opik/integrations/typesafe/opik_tracker.py) | 包装同步与异步客户端，把每次 system_one 调用记录成一个可追踪的 span。 | 开源项目 | `Py` | 要求 typesafe-sdk 0.7.0 及以上，因为响应对象在该版本换了表示方式。如果你还在用旧 SDK，这是个有用的提醒。 |
| [@effect/ai-typesafe](https://github.com/Effect-TS/effect) | 在 Jev 之上实现 Effect 的 DecisionModel 接口，并罕见地坦白说明取整行为尚未核实。 | 平台集成 | `TS`<br><sub>choice/score/noul</sub> | — |
| [rig-typesafeai](https://github.com/0xPlaygrounds/rig) | Rust 集成，选项数量在编译期检查 —— 超过 255 个选项的 Choice 会编译失败，而不是运行时才报错。 | 平台集成 | `Rs`<br><sub>choice/score/noul</sub> | 把 255 选项上限搬进类型系统，是所有集成里最漂亮的一处人机工程设计。注意它读的环境变量名和其他集成不同 —— 见 docs/compatibility.md。 |
| [Bifrost TypeSafe gateway route](https://github.com/maximhq/bifrost/tree/dev/core/providers/typesafe) | 一个 Go 网关 provider，对原生 API 做一比一透传 —— 官方 SDK 只需改 base URL 即可使用。 | 开源项目 | `Go` | — |
| [Kiln: Jev adapter](https://github.com/Kiln-AI/Kiln) | 一个接进 adapter registry 的「JSON Schema 转问题」编译器，并诚实说明了它无法支持的场景。 | 平台集成 | `Py`<br><sub>choice/score/noul</sub> | 它记录了一个真实边界：需要 token 对数概率的评判器它支持不了，因为模型不暴露这些。 |
| [ruby_llm: TypeSafe provider](https://github.com/crmne/ruby_llm) | 带专门 System One 协议的 Ruby provider，是 Ruby 侧接入 Jev 的主要路径。 | 平台集成 | `Rb`<br><sub>choice/score/noul</sub> | — |
| [SemIf](https://github.com/TheoLeeCJ/SemIf) | 一个独立的「语义 if」实现，开门见山声明与 Jev 和 TypeSafe 无隶属关系。 | Jev 替代实现 | `Py` | `并非 Jev 本身` 不是 Jev。收录是因为它的命名很容易被误认为是某种集成。 |
| [kev](https://github.com/jaredpalmer/kev)<br><sub>Jared Palmer</sub> | 一套可训练、可自托管的 Jev-like 决策模型，API 与 System One 兼容 —— 官方 SDK 可以直接指向你自己的服务。 | Jev 替代实现 | `Py`<br><sub>choice/score/noul</sub> | `并非 Jev 本身` 不是 Jev，也不是 TypeSafe 出的。收录是因为它协议兼容，本目录里的模式可以迁移过去；也因为 Jev 本身无法自托管。 |
| [NanoJev](https://github.com/TianyuCodings/NanoJev) | 自称 Jev 的「nano 复刻版」，用途是拿来读，不是拿来上生产。 | Jev 替代实现 | `Py` | `并非 Jev 本身` 不是 Jev，但它确实调用真实模型作为评测基线。它自己的兼容性审计很坦白地说明了分歧之处，包括采用 AI-SDK 的 `boolean` 拼法而非 `noul`。 |
| [jevlike](https://github.com/vinnylarouge/jevlike)<br><sub>vinnylarouge</sub> | 一个独立可训练的模型，输入输出形状与 Jev 相同：文本加 N 个选项进，每个选项一个概率出，单次前向完成。 | Jev 替代实现 | `Py` | `并非 Jev 本身` 已更正：它完全不调用 Jev API —— 已核实，52 个文件中零引用。其 README 自述「这是研究起点，不是 Jev 的复制品」，也未声称达到同等质量。视觉打分只是演示，不是主体。 |
| [simple-jev](https://github.com/featherless-ai/simple-jev) | 通过读取 next-token logits，把任意开源权重模型变成 Jev 形状的端点 —— JSON 由服务端组装，而不是模型生成。 | Jev 替代实现 | `Py` | `并非 Jev 本身` 不是 Jev。但仍值得一读：它把「在固定选项集上做受约束解码」讲得很具体 —— 而这正是整个类别赖以成立的机制。 |
| [jev-skill](https://github.com/wuyoscar/jev-skill) | 一个 agent 技能加 CLI：校验三种原语、在产生计费调用前要求明确同意、并禁止在模拟时编造输出。 | 插件 | `Py`<br><sub>choice/score/noul</sub> | 它的技能文件在这个领域里格外自律：花钱前先征得同意、未实际调用时打出明确标记，以及那句「被选中不等于被授权」。 |
| [awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects)<br><sub>logicrw</sub> | 一个同类目录，主打生态广度：来源锚定到具体 commit、四语 README、以及一个生成式站点。 | 开源项目 | `JS` | 它走的是广度，本目录走的是深度。这里缺的条目值得去它那里对一遍；它只收 issue，不收 PR。 |
| [typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) | 最适合刚拿到 API 的人。把 Jev 接进 Claude Code、Claude Desktop、Codex 和 Pi，随时做 Choice / Score / Noul。 | 插件 | `Go`<br><sub>choice/score/noul</sub> | 如果你想先上手体验这几个原语、再动手写代码，从这里开始。 |
| [awesome-jev (fatwang2)](https://github.com/fatwang2/awesome-jev)<br><sub>fatwang2</sub> | 一个同类目录，提交由 Jev 自己审核，其多语言社区客户端清单相当完整。 | 开源项目 | `JS` | 用这个模型来审核关于这个模型的列表的投稿，是个漂亮的自产自销。它的 SDK 分区是寻找官方未覆盖语言客户端的最佳去处。 |
| [OpenDecision](https://github.com/deepanwadhwa/OpenDecision)<br><sub>deepanwadhwa</sub> | 一个开源语义决策引擎，本地跑零样本模型，其 FastAPI 服务已验证与官方 SDK 协议兼容。 | Jev 替代实现 | `Py`<br><sub>choice/score/noul</sub> | `并非 Jev 本身` 不是 Jev。它的 examples 目录里有一个 demo 用真实的 typesafe-sdk 指向本地 base URL，这是「可直接替换」最干净的证明。 |
| [@ai-sdk/typesafe-ai provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai) | 直连 TypeSafe 的 AI SDK provider 包，示例覆盖三种问题类型以及嵌套的 criteria 写法。 | SDK | `TS` `JS`<br><sub>choice/score/noul</sub> | — |
| [aegis: TypeSafe as a first-class provider](https://github.com/dvjn/aegis)<br><sub>dvjn</sub> | 一个个人 Rust AI 网关，内置 TypeSafe provider，用真实响应体测试了用量提取与别名解析。 | 开源项目 | `Rs` | `代码未实测` 规模很小，但它自带的 skill 文件是一份相当准确的指南：如何把 state 写成结构化对象、以及把确定性工作留在代码里。README 提到许可，但仓库里没有 LICENSE 文件。 |
| [Build Your Own JEV Locally: Run a 100% Private AI Agent on Your Machine](https://medium.com/coding-nexus/build-your-own-jev-locally-run-a-100-private-ai-agent-on-your-machine-bb98126d394a)<br><sub>DataScience Nexus</sub> | 标题误导：它并没有在跑 Jev，而是用开源 LLM 加受约束的 next-token 打分，自己搭一个 Jev-like 决策引擎。 | Jev 替代实现 | `Py` | `并非 Jev 本身` `代码未实测` `付费墙` 收录是为了纠偏 —— 这个标题排名不低且具误导性。Jev 未公开权重、无法本地运行；任何声称能本地跑 Jev 的内容，实际讲的都是替代品。 |
| [Jev Explained: How to Add Fast, Typed Decisions to an AI Agent](https://aihubmix.com/blog/jev-explained-how-to-add-fast-typed-decisions-to-an-ai-agent) | 第三方解读文章，给了一张有用的架构草图，还罕见地诚实列出了「不该用决策模型」的场景。 | 文章 | `Py` | `代码未实测` 文中代码用关键字参数调用 LangChain 分类器，而官方签名接收的是单个 dict。读文章可以，别照抄那段代码。 |
| [jevai.org community site](https://www.jevai.org/) | 一个与官方无关的社区站：有 playground、预设决策 API、MCP 服务、可下载技能，以及一个社区应用展示廊。 | 开源项目 | `sh` | `需第三方密钥` `宣称未核实` 非官方，也不是 TypeSafe 的 API —— 它跑的是自己的端点、请求结构和密钥。其 /jev-api 页面给出的请求结构与任何一手来源都不符，不要从那里抄代码。见 docs/vetting.md。 |
| [Tracing Jev calls with Langfuse](https://langfuse.com/integrations/model-providers/typesafe) | 目前唯一有 Jev 专用可观测性的平台：一个 OpenInference instrumentor，通过 OpenTelemetry 追踪每次决策调用。 | 平台集成 | `Py`<br><sub>choice/score/noul</sub> | 因为走的是标准 OpenTelemetry，追踪数据可以发往任意 OTLP 后端；但只有 Langfuse 文档写了 Jev 专门的处理。 |
| [TypeSafe AI Jev now available on AI Gateway](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway) | Vercel 在 AI Gateway 上线 Jev 的公告，附 experimental_evaluate 示例，模型串为 typesafe-ai/jev。 | 平台集成 | `TS`<br><sub>noul</sub> | Vercel 的 evaluation API 把是非类型叫 `boolean`、返回 `.probability`，而原生 API 用 `noul`。见 docs/compatibility.md。 |
| [TypeSafe models in Pydantic AI](https://pydantic.dev/docs/ai/models/typesafe/) | Pydantic AI 的一方支持：用 typesafe:jev-latest 这个模型串、配 output_type=bool 建 Agent。 | 平台集成 | `Py` | 它给的设计建议是这个话题上最好的一句总结：每个字段问的，应该是懂行的人一秒钟就能下的判断。 |
| [TypeSafe pass-through on LiteLLM](https://docs.litellm.ai/docs/pass_through/typesafe) | 通过 LiteLLM 代理 Jev，统一密钥与成本追踪，/typesafe/ 下的任意路径都直接透传。 | 平台集成 | `sh` | 不支持流式，因为上游 API 本身不支持。成本追踪读的是 usage.input_tokens。 |
| [TypeSafe-compatible API on Vercel AI Gateway](https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe) | 只改一个 baseURL 就能把官方 TypeSafe SDK 指向 Vercel，也可以直接用 cURL 调网关的 systemone 端点。 | 平台集成 | `TS` `sh`<br><sub>noul</sub> | 兼容路径保留原生的 `noul` 命名，AI SDK 的 evaluation 路径不保留。选一条走，别混用。 |
| [typesafe-go](https://github.com/Nibir1/typesafe-go)<br><sub>Nibir1</sub> | 零依赖的社区 Go SDK，还带一个静态分析器，能在编译期指出设计不良的问题。 | SDK | `Go`<br><sub>choice/score/noul</sub> | `代码未实测` 官方没有 Go SDK，所以它填的是真实空缺。它明确声明与官方无隶属关系。成熟度未经验证，目前也还没有 star。 |
| [awesome-jev (yibie)](https://github.com/yibie/awesome-jev) | 目前这个领域里 star 数最高的同类目录。 | 开源项目 | — | `无许可证` 为完整性而收录。这个领域有数十个同类目录；本目录竞争的是核实严谨度，不是收录数量。 |
| [A new kind of AI model from a ChatGPT inventor is thrilling developers](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)<br><sub>Tim Fernholz</sub> | 唯一一篇引用了开发者一手说法（而非厂商数字）的发布报道，其中还提醒：解释阈值的责任现在落在你自己头上。 | 文章 | — | — |
| [AI model "Jev" to make machines decide faster](https://www.heise.de/en/news/AI-model-Jev-to-make-machines-decide-faster-11457071.html)<br><sub>Tomislav Bezmalinović</sub> | 重点落在可解释性的缺失 —— 模型不给出语言层面的理由 —— 以及所有已公布基准都出自厂商自己。 | 文章 | — | — |
| [Hacker News: Introducing System One Models and Jev](https://news.ycombinator.com/item?id=49717558) | 发布讨论帖，也是质疑最集中的地方：RLCD 缺乏支撑材料、延迟对比不对等、以及官方刻意不公开基准。 | 讨论 | — | 建议与发布博文对照阅读。这里也最容易找到有人讲自己实际是从什么方案迁移过来的，比如 embedding 加余弦相似度。 |
| [Jev (AI model) on Wikipedia](https://en.wikipedia.org/wiki/Jev_(AI_model)) | 最大价值在于当索引用：它的参考文献列表是找到值得读的报道的最快路径。 | 文章 | — | 使用了正确的 Choice/Score/Noul 术语，不少主流媒体没做到这点。 |
| [Jev by TypeSafe: A Decision Model for AI Agents](https://beam.ai/agentic-insights/jev-typesafe-ai-agents) | 从智能体开发者角度，讲决策模型在智能体技术栈里的位置。 | 文章 | — | `营销内容` 发在某厂商自己的 insights 博客上，读的时候要意识到它同时也是在做定位宣传。 |
| [Jev Cuts AI Decision Costs 100x And Vercel, Cloudflare Rushed To Add It](https://www.forbes.com/sites/josipamajic/2026/09/19/jev-cuts-ai-decision-costs-100x-and-vercel-cloudflare-rushed-to-add-it/)<br><sub>Josipa Majic Predin</sub> | 主流媒体对这次发布、以及各家网关上线速度的报道。 | 文章 | — | `厂商自报数据` `付费墙` 100x 这个数字来自厂商。「匆忙上线」是作者的措辞；但集成本身在本目录里已独立确认。 |
| [Jev From TypeSafe is a New Class of AI Model that is FAST and CHEAP - But There is a Caveat!](https://youtube.com/watch?v=qdji39XXgEY)<br><sub>Gary Explains</sub> | 一篇把限制直接写进标题、而不是藏在正文里的评测。 | 视频 | — | 元数据已核实；本条目未逐段核对视频内容。 |
| [Jev: System One models for Prod, not God](https://www.latent.space/p/jev)<br><sub>Latent Space</sub> | 唯一的长篇创始人访谈：为什么 RLHF 是错的优化目标、为什么不公开基准、以及全合成数据的路线。 | 讨论 | — | 约两小时十五分。YouTube 镜像的标题被改过不止一次，站内标题才是稳定的那个。 |
| [Jev: TypeSafe's System One Model Explained](https://www.datacamp.com/blog/system-one-models-jev)<br><sub>Matt Crabtree</sub> | 对架构、宣称的基准和定价的中立综述，并明确指出当时还没有出现大规模的独立复现。 | 文章 | — | 它的 SEO 标题与此处采用的页面标题不一致。 |
| [jevai.org community app gallery](https://www.jevai.org/apps) | 从社交帖子里策展的 36 个社区作品：浏览器智能体、表格工具、按意图搜邮箱、会判断的广告拦截、游戏与机器人。 | 开源项目 | — | `宣称未核实` 卡片链接的是社交帖子而非代码仓库，所以多数是演示、不是可运行代码。适合用来了解第一周大家都试了些什么。 |
| [RLCD explained: Reinforcement Learning for Calibrated Decisions](https://systemonemodels.org/guides/rlcd-explained/) | 一份独立整理，其最有价值的结论是否定性的：RLCD 没有论文、没有奖励函数、没有数据集说明、也没有可复现的评测。 | 文章 | — | 注意缩写撞车：2023 年有一篇无关论文也叫 RLCD（Reinforcement Learning from Contrastive Distillation）。任何标称「RLCD 论文」的 arXiv 链接几乎必然是那一篇，而不是这个方法。 |
| [TypeSafe AI debuts model for machines that plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711)<br><sub>Thomas Claburn</sub> | 最具怀疑视角的主流报道：它质疑「不会幻觉」的说法 —— 格式正确的答案不等于正确的答案。 | 文章 | — | 建议与发布博文对照阅读。它点出的那个区别 ——「符合 schema」不等于「正确」—— 是多数报道都跳过的。 |
| [TypeSafe on OpenRouter](https://openrouter.ai/typesafe) | OpenRouter 上的 Jev 条目，有自己的模型 id，以及「输入收费、输出免费」这种少见的定价结构。 | 平台集成 | — | 这里的模型 id 是 typesafe/jev-1.13 和 ~typesafe/jev-latest —— 注意那个波浪号。该页没有代码示例。 |

## 按资源形态

同样这些行，按你点开链接后会看到什么来分组。

- **官方文档** `31` — [API reference](https://docs.typesafe.ai/api), [Cookbook: Autoresearch feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery), [Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence), [Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages), [Cookbook: Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook), [Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check), [Cookbook: Function calling](https://docs.typesafe.ai/cookbooks/function_calling), [Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails), [Cookbook: Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification), [Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment), [Cookbook: Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find), [Cookbook: Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions), [Cookbook: Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook), [Cookbook: Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe), [Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook), [Cookbook: Self-consistency with nouls](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook), [Cookbook: Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion), [Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat), [Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade), [Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home), [Models, pricing and limits](https://docs.typesafe.ai/models), [Official agent skill for Claude Code](https://docs.typesafe.ai/agent-skill), [Pattern: Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring), [Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing), [Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing), [Pattern: Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out), [Primitives: Choice, Score, Noul](https://docs.typesafe.ai/primitives), [Quickstart](https://docs.typesafe.ai/introduction/quickstart), [Confidence](https://docs.typesafe.ai/confidence), [Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13), [Use case map](https://docs.typesafe.ai/concepts/use-case-map)
- **SDK** `5` — [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python), [@typesafe-ai/sdk (TypeScript / JavaScript)](https://github.com/typesafe-ai/typesafe-sdk-js), [typesafe-sdk (Python)](https://github.com/typesafe-ai/typesafe-sdk-python), [@ai-sdk/typesafe-ai provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai), [typesafe-go](https://github.com/Nibir1/typesafe-go)
- **平台集成** `18` — [OpenCode Zen: Jev resale](https://github.com/anomalyco/opencode), [Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html), [@langchain/typesafe](https://github.com/langchain-ai/langchainjs), [@effect/ai-typesafe](https://github.com/Effect-TS/effect), [rig-typesafeai](https://github.com/0xPlaygrounds/rig), [Kiln: Jev adapter](https://github.com/Kiln-AI/Kiln), [ruby_llm: TypeSafe provider](https://github.com/crmne/ruby_llm), [Jev on AI/ML API](https://docs.aimlapi.com/api-references/decision-models/typesafe/jev), [Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/), [Jev on Netlify AI Gateway](https://www.netlify.com/changelog/typesafe-jev-ai-gateway/), [langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe), [spring-ai-typesafe](https://spring.io/blog/2026/09/21/spring-ai-typesafe-structured-judgment), [Tracing Jev calls with Langfuse](https://langfuse.com/integrations/model-providers/typesafe), [TypeSafe AI Jev now available on AI Gateway](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway), [TypeSafe models in Pydantic AI](https://pydantic.dev/docs/ai/models/typesafe/), [TypeSafe pass-through on LiteLLM](https://docs.litellm.ai/docs/pass_through/typesafe), [TypeSafe-compatible API on Vercel AI Gateway](https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe), [TypeSafe on OpenRouter](https://openrouter.ai/typesafe)
- **代码片段** `4` — [Example: confidence-gated escalation](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-confidence-gate/main.py), [Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py), [Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py), [Example: tool selection with a none option](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/04-tool-selection/main.py)
- **开源项目** `44` — [AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe), [sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api), [OpenViking: retrieval reranking](https://github.com/volcengine/OpenViking), [Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe), [FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py), [Cua driver: jev-use example](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use), [Opik TypeSafe tracker](https://github.com/comet-ml/opik/blob/main/sdks/python/src/opik/integrations/typesafe/opik_tracker.py), [jcode: memory recall without embeddings](https://github.com/1jehuang/jcode), [json-render](https://github.com/vercel-labs/json-render), [jev-ultrafast](https://github.com/browser-use/jev-ultrafast), [Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero), [LanceDB TypeSafeReranker](https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py), [Bifrost TypeSafe gateway route](https://github.com/maximhq/bifrost/tree/dev/core/providers/typesafe), [DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat), [agentgateway: CI-validated LLM guardrail](https://github.com/agentgateway/agentgateway), [jev-trader](https://github.com/jarrodwatts/jev-trader), [agent-desktop](https://github.com/lahfir/agent-desktop), [jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis), [Jev-cu](https://github.com/Sac-Y/Jev-cu), [jev-review](https://github.com/devagrawal09/jev-review), [jev-search](https://github.com/superagents-lab/jev-search), [typesafe-mario](https://github.com/fhshaik/typesafe-mario), [awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects), [pg-jev](https://github.com/realZachi/pg-jev), [jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser), [awesome-jev (fatwang2)](https://github.com/fatwang2/awesome-jev), [hyperedit](https://github.com/kevinbadi/hyperedit), [perch: semantic code linting](https://github.com/lakeday-org/perch), [jevpilot](https://github.com/standardagents/jevpilot), [jev-drone](https://github.com/RomanSlack/jev-drone), [jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat), [neo4jev](https://github.com/jexp/neo4jev), [killmyidea](https://github.com/monteduro/killmyidea), [Prism](https://github.com/irfndi/prism-liquidity-agent), [Blink](https://github.com/ellipsis-dev/blink), [Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot), [Canny](https://github.com/qkal/Canny), [jev-curate](https://github.com/AkashPriyadarshii/jev-curate), [OneVOneJev](https://github.com/emrickgarrett/OneVOneJev), [aegis: TypeSafe as a first-class provider](https://github.com/dvjn/aegis), [jevai.org community site](https://www.jevai.org/), [awesome-jev (yibie)](https://github.com/yibie/awesome-jev), [jevai.org community app gallery](https://www.jevai.org/apps), [jevai.org community showcase cases](https://www.jevai.org/cases)
- **插件** `11` — [typesafe-ai/skills](https://github.com/typesafe-ai/skills), [claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates), [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction), [hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills), [jev-skill](https://github.com/wuyoscar/jev-skill), [jev-mcp](https://github.com/jkudish/jev-mcp), [typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp), [jev-codex-router](https://github.com/0xNatoshi/jev-codex-router), [jev-pruner](https://github.com/tamaratran/jev-pruner), [Winnow](https://github.com/GhalebDweikat/winnow), [SemDecide](https://github.com/sharziki/semdecide)
- **教程** `5` — [Real Python: hello-jev](https://github.com/realpython/materials/tree/master/hello-jev), [ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook), [A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/), [Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4), [Using TypeSafe Jev with the AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk)
- **基准测试** `6` — [Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent), [worldmonitor: news threat classification](https://github.com/koala73/worldmonitor), [no-mistakes: review context selection](https://github.com/kunchenguid/no-mistakes), [Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til), [An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/), [Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)
- **文章** `12` — [Introducing System One models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev), [Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev), [Jev Explained: How to Add Fast, Typed Decisions to an AI Agent](https://aihubmix.com/blog/jev-explained-how-to-add-fast-typed-decisions-to-an-ai-agent), [A new kind of AI model from a ChatGPT inventor is thrilling developers](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/), [AI model "Jev" to make machines decide faster](https://www.heise.de/en/news/AI-model-Jev-to-make-machines-decide-faster-11457071.html), [Jev (AI model) on Wikipedia](https://en.wikipedia.org/wiki/Jev_(AI_model)), [Jev by TypeSafe: A Decision Model for AI Agents](https://beam.ai/agentic-insights/jev-typesafe-ai-agents), [Jev Cuts AI Decision Costs 100x And Vercel, Cloudflare Rushed To Add It](https://www.forbes.com/sites/josipamajic/2026/09/19/jev-cuts-ai-decision-costs-100x-and-vercel-cloudflare-rushed-to-add-it/), [Jev: TypeSafe's System One Model Explained](https://www.datacamp.com/blog/system-one-models-jev), [RLCD explained: Reinforcement Learning for Calibrated Decisions](https://systemonemodels.org/guides/rlcd-explained/), [TypeSafe AI debuts model for machines that plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711), [TypeSafe's Jev: Can decision models replace LLM judges?](https://arize.com/blog/typesafe-jev-llm-judge/)
- **视频** `3` — [Jev (Fully Tested) + Browser Use: FASTEST AI Agent I'VE TRIED YET!](https://www.youtube.com/watch?v=SNJ3yuJ_QwY), [Jev - The Ultimate Classification Model?](https://youtube.com/watch?v=X117w2Rark8), [Jev From TypeSafe is a New Class of AI Model that is FAST and CHEAP - But There is a Caveat!](https://youtube.com/watch?v=qdji39XXgEY)
- **讨论** `2` — [Hacker News: Introducing System One Models and Jev](https://news.ycombinator.com/item?id=49717558), [Jev: System One models for Prod, not God](https://www.latent.space/p/jev)
- **Jev 替代实现** `7` — [SemIf](https://github.com/TheoLeeCJ/SemIf), [kev](https://github.com/jaredpalmer/kev), [NanoJev](https://github.com/TianyuCodings/NanoJev), [jevlike](https://github.com/vinnylarouge/jevlike), [simple-jev](https://github.com/featherless-ai/simple-jev), [OpenDecision](https://github.com/deepanwadhwa/OpenDecision), [Build Your Own JEV Locally: Run a 100% Private AI Agent on Your Machine](https://medium.com/coding-nexus/build-your-own-jev-locally-run-a-100-private-ai-agent-on-your-machine-bb98126d394a)

## 本仓库内的可运行样例

<!-- examples-table:start -->
See [`examples/README.md`](examples/README.md).
<!-- examples-table:end -->

## 生态现状

<!-- status:start -->
See [`docs/status.md`](docs/status.md).
<!-- status:end -->

## 哪些经过核实，哪些没有

- **已核实：** 该链接在 `checked` 日期返回了成功状态，并且有人打开页面、按页面实际内容写了摘要。
- **未核实：** 代码能否跑通、性能宣称是否成立、项目是否仍在维护、以及这些做法是否适合你的系统。本仓库没有做过压测或安全审计。标了 `code-untested` 的行是读过、没跑过。

## 机器可读数据

每个例子一条记录，每次推送都按 JSON Schema 校验。

- Catalog — [`catalog.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/catalog.json)
- Retired — [`retired.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/retired.json)
- Schema — [`schema/entry.schema.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/schema/entry.schema.json)
- For agents — [`llms.txt`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/llms.txt)

## 参与贡献

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [docs/method.md](docs/method.md)
- [docs/patterns.md](docs/patterns.md)
- [docs/vetting.md](docs/vetting.md)

## 许可

`scripts/`、`site/`、`examples/` 中的代码采用 [MIT](LICENSE-MIT)。目录元数据采用 [CC0-1.0](LICENSE-CC0)，标记为 `CC-BY-4.0` 的行除外 —— 其署名即该行的 `sources` 数组。被链接的作品各自保留其原许可。
