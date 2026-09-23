# 工具选择

<sub>[awesome-jev](../../README.zh-CN.md) · [English](tool-selection.md)</sub>

_智能体下一步该调用哪个工具或动作。_

这个决策的全部已收录例子 —— 共 148 条，官方优先，其次是含代码的，再按 star 排序。同样这些行及其警示也在[索引](../../README.zh-CN.md#工具选择)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=tool-selection&lang=zh)还能按语言、原语和形态进一步筛选。

- **[Cookbook: Function calling](https://docs.typesafe.ai/cookbooks/function_calling)** ⭐ — 把自然语言的交易请求映射到普通的类型化函数：函数名和有限取值的参数各自变成一个带置信度的问题。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion)** ⭐ — 为智能体的一轮对话从 182 个技能里最多挑一个：第一次请求给所有技能排序并顺便问「这轮到底需不需要技能」，第二次细读前三名。
  <sub>`官方文档` · `Py` · `choice` · `noul`</sub>

- **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐ — 一个可运行的智能家居助手示例，用类型化决策来解析用户请求。
  <sub>`官方文档` · `Py`</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)** — 三个可独立安装的 Claude Code 插件 —— 护栏、模型路由、技能推荐 —— 各自带 hook 和测试。
  <sub>`插件` · ★31,297 · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)** — 把工具目录编译成问题，再从答案还原出 tool call，并为「弃权」和「需确认」两种情况定义了专门的错误类型。
  <sub>`开源项目` · ★30,294 · `Py` · `choice`</sub>

- **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)** — 两段式 MCP 工具检索：先用一个宽 Choice 对整个目录粗排，再给候选短名单配完整描述，每个候选各配一个 Noul 判断它到底是否胜任。
  <sub>`开源项目` · ★27,878 · `Py` · `choice` · `noul`</sub>

- **[Cua driver: jev-use example](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use)** — Python 与 TypeScript 双实现的 computer-use 动作选择：Jev 从不可变候选集里挑下一个浏览器动作，保留 reobserve 和 abstain 两个特殊选项。
  <sub>`开源项目` · ★26,050 · `Py` · `TS` · `choice`</sub>

- **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)** — Browser Use 做的高速浏览器 Agent。Jev 每一步只判断「做什么、点哪个元素」，要打字才叫小模型。
  <sub>`开源项目` · ★18,685 · Browser Use · `Py` · `choice` · ⚠ `厂商自报数据`</sub>

- **[json-render](https://github.com/vercel-labs/json-render)** — Vercel Labs 的生成式 UI 框架。实验里 Jev 不逐 token 写 JSON，只负责选组件、属性和布局。
  <sub>`开源项目` · ★18,141 · Vercel Labs · `TS` · `choice`</sub>

- **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)** — 从三个维度审查每次工具调用：风险等级、用户是否授权、以及一个显式的提示注入压力检查。
  <sub>`开源项目` · ★6,340 · `TS` · `choice` · `noul`</sub>

- **[jev-trader](https://github.com/jarrodwatts/jev-trader)** — 在 Monad 测试网上做高频做市。Jev 根据价差和成交方向判断下一步买还是卖。
  <sub>`开源项目` · ★2,128 · `TS` · `choice` · ⚠ `宣称未核实`</sub>

- **[agent-desktop](https://github.com/lahfir/agent-desktop)** — 桌面自动化。读系统无障碍树，判断下一步该点哪个按钮、菜单或输入框。
  <sub>`开源项目` · ★1,557 · `Rs` · `choice`</sub>

- **[typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)** — macOS 上的 computer use：OCR 屏幕、分类下一步动作、点击。每步成本不到一分钱的零头。
  <sub>`开源项目` · ★861 · awlevin · `Py`</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** — 九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。
  <sub>`插件` · ★673 · `Py` · `choice` · `score` · `noul`</sub>

- **[tiptour-macos](https://github.com/milind-soni/tiptour-macos)** — 开源的快速本地 computer use。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★654 · milind-soni · `Swift`</sub>

- **[agent](https://github.com/AgentiLoop/Agent)** — 面向 Mac 的自主智能体 harness。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★629 · agentiloop · `Swift`</sub>

- **[Jev-cu](https://github.com/Sac-Y/Jev-cu)** — 一个 computer-use 智能体：判断该对无障碍树里哪个元素操作，并单独用一个 noul 判断这个动作是否需要用户显式确认。
  <sub>`开源项目` · ★585 · `JS` · `choice` · `noul`</sub>

- **[omg.dev](https://github.com/BennyKok/omg.dev)** — 用手机远程控制各类编程智能体。 <sub>(机翻)</sub>
  <sub>`插件` · ★535 · bennykok · `TS`</sub>

- **[foreman](https://github.com/thruwire/foreman)** — 一个「软件工厂工头」，用 Jev 决定智能体流水线下一步该做什么。
  <sub>`开源项目` · ★525 · thruwire · `Py`</sub>

- **[jev-browser-use](https://github.com/wy-coliney/jev-browser-use)** — 把循环拆开：Jev 负责点击，推理模型负责思考与验证。
  <sub>`开源项目` · ★415 · wy-coliney · `JS`</sub>

- **[mobile-jev](https://github.com/droidrun/mobile-jev)** — 移动端 computer use：由 Jev 决定手机屏幕上的下一个动作。
  <sub>`开源项目` · ★362 · droidrun · `JS`</sub>

- **[typesafe-mario](https://github.com/fhshaik/typesafe-mario)** — 让 Jev 玩《超级马里奥》。不看截图，直接读模拟器 RAM 里的结构化状态，再决定跑、跳、躲。
  <sub>`开源项目` · ★361 · `Py` · `choice` · `score` · `noul` · ⚠ `代码未实测` `仅一次提交` `无许可证`</sub>

- **[wrongstack](https://github.com/WrongStack/WrongStack)** — 一个 AI 编程智能体：读代码、改文件、跑命令、推理 bug。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★334 · wrongstack · `TS`</sub>

- **[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)** — 语音驱动的浏览器控制：目标选项每次请求都按当前实时元素列表重建，并且总是包含一个 none 选项。
  <sub>`开源项目` · ★253 · `JS` · `choice` · `score` · `noul`</sub>

- **[jev-browser](https://github.com/jkudish/jev-browser)** — 浏览器自动化，下一步动作由 Jev 选择。
  <sub>`开源项目` · ★245 · jkudish · `TS`</sub>

- **[quackd](https://github.com/rokbenko/quackd)** — 统管所有机器人的 CLI：每台机器人配一个 LLM 作大脑，由 Jev 做决策。 <sub>(机翻)</sub>
  <sub>`插件` · ★229 · rokbenko · `Py`</sub>

- **[embodied-jev](https://github.com/FBddcz/embodied-jev)** — EmbodiedJev：基于 MuJoCo 的机器人决策工作台。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★210 · fbddcz · `Py`</sub>

- **[hyperedit](https://github.com/kevinbadi/hyperedit)** — 一个 AI 视频编辑器：把编辑指令路由到具体操作、目标片段和轨道，并以关键词路由作为兜底。
  <sub>`开源项目` · ★191 · `TS` · `choice` · `noul` · ⚠ `无许可证`</sub>

- **[jev-gateway](https://github.com/vinilana/jev-gateway)** — 把 Jev 接进编程智能体，用于工具调用的推理判断。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★182 · vinilana · `TS`</sub>

- **[jevpilot](https://github.com/standardagents/jevpilot)** — 驾驶模拟器的自动驾驶，每个 tick 问两个 choice；只剩单一选项的问题直接在本地短路，不花钱发出去。
  <sub>`开源项目` · ★179 · `JS` · `choice` · ⚠ `无许可证`</sub>

- **[interlinked-cli](https://github.com/QuentinCody/interlinked-cli)** — 给你的 harness 做的 harness：本地钩子、品味约束与开发者可观测性。 <sub>(机翻)</sub>
  <sub>`插件` · ★178 · quentincody · `TS`</sub>

- **[jevrouter](https://github.com/BillionsBobby/JevRouter)** — 面向模型、工具和子智能体的路由器。
  <sub>`开源项目` · ★178 · billionsbobby · `TS`</sub>

- **[jevharness](https://github.com/TianyuCodings/JevHarness)** — 由 LLM 撰写的任务专用 Jev harness，可选全轨迹奖励反思。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★155 · tianyucodings · `Py` · ⚠ `无许可证`</sub>

- **[jev-drone](https://github.com/RomanSlack/jev-drone)** — 拿 Jev 控无人机。底层飞控继续负责稳定和安全，Jev 只做爬升、刹车、穿越障碍这类上层判断。
  <sub>`开源项目` · ★145 · `Py` · `choice` · `score` · `noul` · ⚠ `宣称未核实`</sub>

- **[macbrow](https://github.com/timpratim/macbrow)** — 由 Gradium 驱动的免手操作 Mac 与浏览器控制。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★141 · timpratim · `Py`</sub>

- **[pi-jev](https://github.com/y0usaf/pi-jev)** — 给编程智能体做的决策层：一个可度量的工具调用闸门，外加一个返回校准答案的类型化提问。
  <sub>`插件` · ★140 · y0usaf · `TS`</sub>

- **[jev-dsh-decision](https://github.com/Devin-AXIS/jev-dsh-decision)** — Jev DSH 决策引擎：面向 Agent Harness 的结构化决策插件，原生支持 DeepSeek Harness。 <sub>(机翻)</sub>
  <sub>`插件` · ★129 · devin-axis · `JS` · ⚠ `无许可证`</sub>

- **[systemoneharness](https://github.com/HarnessRouter/SystemOneHarness)** — 面向 System One 模型的 harness。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★128 · harnessrouter · `Py`</sub>

- **[skillranker](https://github.com/Dicklesworthstone/skillranker)** — 用当前会话上下文给智能体的技能排序以决定下一步，带 Claude Code hook。
  <sub>`插件` · ★114 · dicklesworthstone · `Rs`</sub>

- **[neo4jev](https://github.com/jexp/neo4jev)** — 把 Jev 塞进知识图谱。每走到一个节点，判断下一条最值得走的边，再一路找下去。
  <sub>`开源项目` · ★107 · `Py` · `choice`</sub>

- **[fastbrowse](https://github.com/agent-labs-dev/fastbrowse)** — 快速浏览器智能体：Jev 从页面现有内容里挑动作，LLM 负责阅读与规划。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★98 · agent-labs-dev · `Py`</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)** — 一个完全不含语言模型的 tool calling 聊天机器人：一次请求同时问清请求类型、该调哪个工具、以及每个工具的参数。
  <sub>`开源项目` · ★91 · `TS` · `choice` · `noul`</sub>

- **[windtunnel](https://github.com/nekuda-ai/WindTunnel)** — 一个 WebMCP 基准，衡量 WebMCP 与其他浏览器智能体接口的差距。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★79 · nekuda-ai · `TS`</sub>

- **[jev-desktop](https://github.com/yikangy873-gif/jev-desktop)** — 在 Codex Computer Use 内部做动作选择。 <sub>(机翻)</sub>
  <sub>`插件` · ★63 · yikangy873-gif · `JS`</sub>

- **[jev-libero](https://github.com/Dimweaker/jev-libero)** — 精细的机器人控制，带物理预览与可配置的 LIBERO 任务。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★61 · dimweaker · `Py`</sub>

- **[jev-social](https://github.com/socai-io/jev-social)** — 只读的 Instagram、TikTok 与 LinkedIn 调研：Jev 先路由平台，再从最新浏览器证据中选择受限的 SocAI CLI 动作；代码校验目标并保留来源链接。
  <sub>`开源项目` · ★47 · socai-io · `JS` · `choice` · ⚠ `需第三方密钥`</sub>

- **[jev-mem](https://github.com/libingzheren/Jev-Mem)** — Jev-Mem：由 System One 控制的智能体记忆。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★39 · libingzheren · `Py`</sub>

- **[robojev](https://github.com/lykycy123/RoboJEV)** — 在 MuJoCo 里对 Franka Panda 做两阶段 JEV 控制。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★36 · lykycy123 · `Py`</sub>

- **[jev-reviewer](https://github.com/choxos/jev-reviewer)** — 系统综述的数据抽取：让 Jev 从论文及其补充材料里按抽取表取值，并附原文引用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★32 · choxos · `JS`</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — 给所有编程智能体做的自动模式：结合会话上下文给每次工具调用打风险分（拒绝／询问／放行）。 <sub>(机翻)</sub>
  <sub>`插件` · ★27 · leepokai · `JS`</sub>

- **[jevgpt](https://github.com/Bewinxed/jevgpt)** — 用一个不会生成文本的模型搭的聊天机器人（自回归驱动）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★26 · bewinxed · `TS`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — 只读的交易日志与复盘 harness：Jev 类型化判断、智能体集成，以及一个可复现的金融基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★26 · myc0576 · `Py`</sub>

- **[OneVOneJev](https://github.com/emrickgarrett/OneVOneJev)** — 浏览器里的 1v1 FPS。每个决策 tick 都要判断走位、视角、瞄准、开火和跳跃。
  <sub>`开源项目` · ★23 · `TS` · `choice` · ⚠ `代码未实测` `无许可证`</sub>

- **[pi-jev-auto-mode](https://github.com/jomatsu/pi-jev-auto-mode)** — 给 Pi 编程智能体做的自动模式：在语义层面自动批准 bash、写入和编辑类工具调用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★23 · jomatsu · `TS`</sub>

- **[tsai-sc](https://github.com/phyous/tsai-sc)** — 通过键鼠操作一款 90 年代即时战略游戏，并记录每次动作的概率。
  <sub>`开源项目` · ★23 · phyous · `Py`</sub>

- **[jev-use](https://github.com/shitianfang/jev-use)** — 一个智能体插件：把不需要文本输出的步骤交给 Jev，而不是主模型。
  <sub>`插件` · ★22 · shitianfang · `JS`</sub>

- **[jev-for-chrome](https://github.com/chy4pro/jev-for-chrome)** — Jev for Chrome：用亚秒级决策模型驱动你正在看的那个标签页。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★21 · chy4pro · `TS`</sub>

- **[agent-chaperone](https://github.com/agent-chaperone/agent-chaperone)** — 在智能体工具调用执行前、以及工具结果被读取前做筛查。 <sub>(机翻)</sub>
  <sub>`插件` · ★20 · agent-chaperone · `TS`</sub>

- **[jev-mac-voice](https://github.com/brudarko/jev-mac-voice)** — 面向 macOS 的英文全双工语音控制。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★20 · brudarko · `JS`</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)** — 开源的 macOS computer use 与原生 GUI 自动化，运行在 Apple 芯片上。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★20 · jcpsimmons · `JS`</sub>

- **[jcr](https://github.com/NiazMorshed2007/jcr)** — 由 Jev 驱动的解析器，帮智能体 harness 在仓库里找到确定性命令及其上下文。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★18 · niazmorshed2007 · `JS`</sub>

- **[jevalyn](https://github.com/Ray-Hughes/jevalyn)** — 给 Rails 应用的决策层：对 Jev System One API 的 Rails 原生封装。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★18 · ray-hughes · `Rb`</sub>

- **[jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab)** — 多无人机自主实验室：展示 Jev 的反射式决策，可选叠加 System 2 战略指导。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★17 · khordoo · `TS` · ⚠ `无许可证`</sub>

- **[live-jev](https://github.com/vinilana/live-jev)** — 浏览器里的 2D 自动驾驶仿真，由 Jev 决策模型驱动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★17 · vinilana · `JS` · ⚠ `无许可证`</sub>

- **[evoke](https://github.com/evoke-build/evoke)** — 反射式软件：一句话变成对一个小程序的调用，由 Jev 选择。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★14 · evoke-build · `Rs`</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — 用 Jev 给收件箱分类：打标、移动、标记、通知，全部配置驱动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★14 · parth-kp · `Py`</sub>

- **[azdaja](https://github.com/kubet/azdaja)** — 与 harness 无关的极简递归语言模型层：单个二进制。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★13 · kubet · `Py`</sub>

- **[discern](https://github.com/doeixd/discern)** — 类型安全、感知不确定性的语义模式匹配与控制流。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★12 · doeixd · `TS`</sub>

- **[jev-harness](https://github.com/AntonioCoppe/jev-harness)** — Jev 决策 harness：置信闸门、影子模式、配方与评测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★11 · antoniocoppe · `TS`</sub>

- **[jev-askable-arm](https://github.com/TarunTomar122/jev-askable-arm)** — 在仿真机械臂上执行零样本英文目标：Jev 串联写死的原语动作。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10 · taruntomar122 · `Py`</sub>

- **[jev-autopilot](https://github.com/arielweinberger/jev-autopilot)** — 这个演示用 Jev 自主驾驶无人机在随机城市里从 A 点飞到 B 点。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10 · arielweinberger · `TS` · ⚠ `无许可证`</sub>

- **[super-jev](https://github.com/Kevthetech143/super-jev)** — 小而可扩展的「决策到动作」harness。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10 · kevthetech143 · `Py`</sub>

- **[hearth-jev-rental-search](https://github.com/Nancy-Chauhan/hearth-jev-rental-search)** — 由 Jev 驱动的自主多源租房搜索。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★9 · nancy-chauhan · `JS`</sub>

- **[jev-agent-browser](https://github.com/forvela/jev-agent-browser)** — 由 Jev 驱动的快速有界浏览器智能体：类型化动作、调研、分类与安全编排。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★9 · forvela · `JS`</sub>

- **[aside-jev](https://github.com/himomohi/aside-jev)** — 让 Aside 智能体用 Jev 做决策（Choice／Score／Noul）。 <sub>(机翻)</sub>
  <sub>`SDK` · ★8 · himomohi · `Py`</sub>

- **[jev-doom-agent](https://github.com/lukaske/jev-doom-agent)** — 浏览器原生的 Doom 智能体实验，带结构化空间状态与实时决策遥测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · lukaske · `TS` · ⚠ `无许可证`</sub>

- **[jevscape](https://github.com/Skyvern-AI/jevscape)** — 给 Jev 的 RuneBench harness：有界动作目录、tick 模式控制器与实时看板。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · skyvern-ai · `TS` · ⚠ `无许可证`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — 可观测的浏览器潜行游戏：Jev 做类型化的守卫判断，确定性代码掌管世界规则。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · abdelstark · `TS`</sub>

- **[pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)** — 给 pi 编程智能体的运行时约束：每个有副作用的工具调用执行前，先对照你说过的话检查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · nyarlathoteppppp · `TS`</sub>

- **[browserclaw](https://github.com/GoldenLoaf24h/browserclaw)** — 高效率的 Chrome 浏览器自动化 MCP server。 <sub>(机翻)</sub>
  <sub>`插件` · ★6 · goldenloaf24h · `TS`</sub>

- **[gg-friggin-ez](https://github.com/ItisShikhar/gg-friggin-ez)** — 给 Node.js 的快速多语言脏话与毒性筛查器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · itisshikhar · `TS`</sub>

- **[jev-lab](https://github.com/jammaru/jev-lab)** — 100 个 AI NPC 住在一个小镇里：Jev 选择下一步动作，世界自己写故事。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · jammaru · `TS`</sub>

- **[jev-tool-router](https://github.com/jackbarunz/jev-tool-router)** — 给 Codex 的 Jev 驱动 MCP 工具路由。 <sub>(机翻)</sub>
  <sub>`插件` · ★6 · jackbarunz · `JS`</sub>

- **[typesafe-jev](https://github.com/gtaras7/typesafe-jev)** — 用 Jev 筛选一整个文件夹的简历：类型化判断、可编辑的策略、免费重新打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · gtaras7 · `TS`</sub>

- **[bicameral](https://github.com/AbdelStark/bicameral)** — 混合式编程 harness：System 2 负责写，System 1（Jev）负责反射式动作。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · abdelstark · `TS`</sub>

- **[deepseek-harness-jev-pre-compaction](https://github.com/wjw66/deepseek-harness-jev-pre-compaction)** — 给 DeepSeek Harness 的压缩前顾问，在标准压缩流程之前运行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · wjw66 · `TS`</sub>

- **[jev-usecases](https://github.com/kenhuangus/jev-usecases)** — 生产级的 Jev 用例 harness，带置信度门控的决策逻辑。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · kenhuangus · `Py`</sub>

- **[jevonly](https://github.com/buluoray/JevOnly)** — 纯 Jev 驱动的智能体：能「打字」并推进任务直至完成。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · buluoray · `Py`</sub>

- **[agi-jev-containment](https://github.com/carlosedm10/agi-jev-containment)** — 本地 AI 智能体监控：链路级恶意智能体检测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · carlosedm10 · `Py` · ⚠ `无许可证`</sub>

- **[computer-use-jev](https://github.com/paulsmith/computer-use-jev)** — 以 Jev 为决策者的 macOS computer use。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · paulsmith · `Go`</sub>

- **[ego-jev](https://github.com/jiangkoumo/ego-jev)** — 用 Jev 驱动轻量浏览器：输入一张带索引的元素表，输出一个动作。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · jiangkoumo · `JS`</sub>

- **[jev-mobile](https://github.com/Friedjof/jev-mobile)** — 结合 Mobile MCP 的快速 Android 结构化控制循环。 <sub>(机翻)</sub>
  <sub>`插件` · ★4 · friedjof · `Py`</sub>

- **[jev-model-tokengate](https://github.com/Thanh-Mathieu95/jev-model-tokengate)** — OpenAI 兼容代理，夹在你的 LLM 与用户之间，逐窗口评估输出。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · thanh-mathieu95 · `JS`</sub>

- **[jev-robotics-demo](https://github.com/FazalAAli/jev-robotics-demo)** — Jev 对比某大模型：在 MuJoCo 里驾驶仿真机械臂。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · fazalaali · `Py`</sub>

- **[jev-voice-control](https://github.com/chris-wozniczek/jev-voice-control)** — 用语音控制 Mac：语音 → Jev 类型化决策 → macOS 自动化。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · chris-wozniczek · `Swift`</sub>

- **[laya-browser-agent](https://github.com/ChenneyZhuang/laya-browser-agent)** — 本地开源的 Jev 替代：用 Laya 做浏览器智能体决策。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★4 · chenneyzhuang · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[otto](https://github.com/NobleSpartan6/otto)** — 面向 macOS 与 Windows 的开源原生 computer use：Jev 加本地 OCR。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · noblespartan6 · `TS`</sub>

- **[slidepilot](https://github.com/harshil1712/slidepilot)** — 给 Slidev 做的语音驱动语义自动翻页，由 Cloudflare Agents 与 Jev 驱动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · harshil1712 · `TS`</sub>

- **[agent-fastpath](https://github.com/abhishekswe/agent-fastpath)** — Jev MCP server：给编程智能体的决策层。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · abhishekswe · `TS`</sub>

- **[dsh-jev-prune](https://github.com/yangyu666/dsh-jev-prune)** — 给 DeepSeek Harness 的 Jev 判定式上下文压缩：语义化的工具结果裁剪。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · yangyu666 · `JS`</sub>

- **[ego-jev-ultrafast](https://github.com/shikaizhong-design/ego-jev-ultrafast)** — Jev 驱动你的轻量浏览器：每步一次类型化选择请求，单文件零依赖。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★3 · shikaizhong-design · `JS`</sub>

- **[fast-compaction-dsh](https://github.com/kolawong/fast-compaction-dsh)** — 给 DeepSeek Harness 的判定式上下文压缩，取代有损的 LLM 摘要。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · kolawong · `TS`</sub>

- **[jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study)** — 独立的 Jev 1.13.0 行为研究：报告、受控提示实验、原始结果与离线验证。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · rinnecoder · `Py`</sub>

- **[jev-browser-control](https://github.com/nexibeo/jev-browser-control)** — 让编程智能体控制你自己的 Chrome：扩展加 MCP server。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · nexibeo · `JS`</sub>

- **[jev-builder](https://github.com/collapseindex/jev-builder)** — 构建 Jev 请求的网页表单：选模板、填空、复制代码。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · collapseindex · `JS`</sub>

- **[jev-codex-pilot](https://github.com/Charlyhno-eng/jev-codex-pilot)** — 带 JEV 模型路由、上下文优化与看板自动化的 Codex 覆盖层。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · charlyhno-eng · `TS`</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — 八个最小可运行示例：把 Jev 用在机械与电气工程场景。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · foadsf · `Py`</sub>

- **[jev-ra](https://github.com/brnyxx/jev-ra)** — 给编程智能体的浏览器操作，号称比 browser-use 快 3–5 倍：每一步由 Jev 决策。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · brnyxx · `Py`</sub>

- **[jevdroid](https://github.com/antiyro/jevdroid)** — 用 Jev 通过 ADB 控制 Android 的类型化 Python 框架。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · antiyro · `Py`</sub>

- **[open-jev-approvals](https://github.com/alexj11324/open-jev-approvals)** — 给 Codex 与 Claude Code 的二值批准闸门：每次被拦截的工具调用都要审查。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★3 · alexj11324 · `Go` · ⚠ `并非 Jev 本身`</sub>

- **[jev-browser-pilot](https://github.com/aidil2105/jev-browser-pilot)** — 给浏览器与桌面自动化的有界决策层：只做决策的模型负责选择。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · aidil2105 · `Py`</sub>

- **[jev-browser-skill](https://github.com/zurfyx/jev-browser-skill)** — 让约 100 毫秒的 Jev 决策模型驱动你的浏览器 —— 给 Claude Code 和 Codex 的即插即用技能。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · zurfyx · `JS`</sub>

- **[jev-compaction](https://github.com/picaye/jev-compaction)** — 从不做摘要的 Hermes 会话上下文压缩：每次工具调用都被打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · picaye · `JS`</sub>

- **[jev-frontend-qa](https://github.com/Nainish-Rai/jev-frontend-qa)** — 证据驱动的前端 QA，构建在 Jev Ultrafast 与浏览器 harness 之上。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · nainish-rai · `Py` · ⚠ `无许可证`</sub>

- **[jev-git](https://github.com/AkashPriyadarshii/jev-git)** — 亚秒级的 Git pre-commit / pre-push 语义反射闸门。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · akashpriyadarshii · `Rs`</sub>

- **[jev-layer](https://github.com/typakon4/jev-layer)** — 可移植的 System-1 决策层，面向智能体 harness，含宿主自控路由、凭据与回放。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★2 · typakon4 · `JS`</sub>

- **[jev-physical-ai](https://github.com/robokrunch/jev-physical-ai)** — 把 Jev 用在机器人、机群与边缘硬件上 —— 附真实实测数字。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · robokrunch · `Py`</sub>

- **[jev-play-ping-pong](https://github.com/Icohen007/jev-play-ping-pong)** — 让 Jev 实时玩浏览器乒乓球：结构化遥测与类型化决策。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★2 · icohen007 · `JS`</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — 基于 Jev 的类型化、策略驱动决策工作流：置信路由、回退与评测。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · hamakyo · `TS`</sub>

- **[jev-turbo](https://github.com/sightmap/jev-turbo)** — 由 Jev 驱动的语义化浏览器操作。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · sightmap · `Go`</sub>

- **[jevarena](https://github.com/raihankhan-rk/jevarena)** — JevArena：两个 Jev 智能体在仅可点击的浏览器游戏里对决。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · raihankhan-rk · `TS`</sub>

- **[jevshield](https://github.com/lgy1027/jevshield)** — 亚 100 毫秒的智能体工具调用安全闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · lgy1027 · `Py`</sub>

- **[pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)** — 一个 pi 扩展，把 Jev 判断暴露成五个 pi 工具，让模型能做狭义的语义判断。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · legacybridge-tech · `TS`</sub>

- **[robo-harness](https://github.com/grmkris/robo-harness)** — SO-101 机械臂智能体工作台：Bun/Effect 协调器、React 工作台、Python 电机控制。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · grmkris · `TS` · ⚠ `无许可证`</sub>

- **[tsai-civ2](https://github.com/phyous/tsai-civ2)** — 让 Jev 在浏览器里玩初代《文明 II》，实时展示动作概率。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · phyous · `Py`</sub>

- **[typesafe-ai-firewall](https://github.com/AnshChoudhary/typesafe-ai-firewall)** — 智能体工具调用执行前防火墙的影子模式验证 harness。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · anshchoudhary · `Py` · ⚠ `无许可证`</sub>

- **[zerosweep](https://github.com/sysadarsh/zerosweep)** — 自主的 System-One 分拣引擎与基准，75 毫秒推理。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★2 · sysadarsh · `TS` · ⚠ `无许可证`</sub>

- **[datajev](https://github.com/zzz1YAO/DataJev)** — 用 System-1 控制 System-2：继续／切换／校验／停止。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · zzz1yao · `Py`</sub>

- **[dsh-jev-verify](https://github.com/xienda/dsh-jev-verify)** — 给 DeepSeek Harness 的 Jev 决策工具与实时验证基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · xienda · `JS`</sub>

- **[jev-engineering](https://github.com/eugeniughelbur/jev-engineering)** — 面向 AI 智能体的决策层：约 400 毫秒、两百分之一美分的类型化校准决策，用于拦截工具调用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · eugeniughelbur · `Py`</sub>

- **[jev-routing](https://github.com/nekowasabi/jev-routing)** — 给多个编程智能体的 Go 版 Jev harness，不依赖 npx，也不是 MCP server。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · nekowasabi · `Go`</sub>

- **[jevaluate](https://github.com/ElshinQ/jevaluate)** — 先评估再信任：实战笔记、可运行脚本与一个 agent 技能。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · elshinq · `JS`</sub>

- **[stepwarden](https://github.com/getexcited/stepwarden)** — 智能体的每一次工具调用在执行前都过一遍检查的 Claude Code 插件。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · getexcited · `TS`</sub>

- **[typesafe-jev-drone-demo](https://github.com/kxzk/typesafe-jev-drone-demo)** — Three.js 无人机模拟器，Python 后端加 Jev 实时导航。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · kxzk · `Py` · ⚠ `无许可证`</sub>

- **[browser-use-olympics](https://github.com/eriestra/browser-use-olympics)** — 浏览器操作奥运会：一个提示、五个项目、一块秒表。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · eriestra · `TS`</sub>

- **[casse-brique-typesafe](https://github.com/Para-FR/casse-brique-typesafe)** — 一个 Next.js 打砖块游戏，球拍由 Jev 实时控制。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · para-fr · `TS` · ⚠ `无许可证`</sub>

- **[Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py)** — 一次问清操作本身、以及每个可能操作各自的目标 —— 于是浏览器的一步永远不需要第二次往返。
  <sub>`代码片段` · `Py` · `choice` · `noul` · ⚠ `代码未实测`</sub>

- **[Example: tool selection with a none option](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/04-tool-selection/main.py)** — 把「选哪个工具」的 choice 和「到底需不需要工具」的 noul 配对使用 —— 因为这是两个不同的问题。
  <sub>`代码片段` · `Py` · `choice` · `noul` · ⚠ `代码未实测`</sub>

- **[harnessjudge](https://github.com/ndolinschi/harnessjudge)** — 评判智能体的每一步：通过／重试／升级／停止。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ndolinschi · `TS` · ⚠ `无许可证`</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — 给 AI 智能体的免费类型化判断：把分类／筛查／打分／校验卸载给 Jev。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · yuyang2230 · `Py`</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — 给 Jev 的有限样本保证：用保形风险控制把校准概率转成可证的约束。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · nikkoxgonzales · `Py`</sub>

- **[jev-llm-router-benchmark](https://github.com/erendikmenn/jev-llm-router-benchmark)** — 以基准驱动的 Jev 路由器与评判者，服务于成本可控的 LLM 编程流程。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · erendikmenn · `Py`</sub>

- **[ps2-ai-agent](https://github.com/opaielsheikh/ps2-ai-agent)** — 自主的 PS2 AI 智能体，带实时视觉遥测 HUD。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · opaielsheikh · `Py` · ⚠ `无许可证`</sub>

- **[s1s](https://github.com/cpaczek/s1s)** — System One 搜索：用类型化判断与仓库证据导航与追踪代码。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · cpaczek · `TS`</sub>

- **[snake-jev](https://github.com/siroccomask/snake-jev)** — 由并行 Jev 判断控制的贪吃蛇，每个游戏 tick 一次 API 调用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · siroccomask · `Py`</sub>

- **[swarmrouter](https://github.com/ndolinschi/swarmrouter)** — 用 Jev 把任务路由给研究／编码／浏览／客服／写作智能体。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ndolinschi · `TS` · ⚠ `无许可证`</sub>

- **[terrarium](https://github.com/TheGali/terrarium)** — 一个沙盒：System One 模型按下小生物的操控键，代码负责其余。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · thegali · `JS`</sub>

- **[Jev (Fully Tested) + Browser Use: FASTEST AI Agent I'VE TRIED YET!](https://www.youtube.com/watch?v=SNJ3yuJ_QwY)** — 把 Jev 接到 Browser Use 上，驱动一个浏览器自动化智能体。
  <sub>`视频` · AICodeKing · ⚠ `宣称未核实`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件 —— 两者不一致时 CI 会失败。</sub>
