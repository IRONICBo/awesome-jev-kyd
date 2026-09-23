# 模型路由

<sub>[awesome-jev](../../README.zh-CN.md) · [English](model-routing.md)</sub>

_选择由哪个下游模型或档位处理请求。_

这个决策的全部已收录例子 —— 共 24 条，官方优先，其次是含代码的，再按 star 排序。同样这些行及其警示也在[索引](../../README.zh-CN.md#模型路由)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=model-routing&lang=zh)还能按语言、原语和形态进一步筛选。

- **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐ — 「小模型 → 校验 → 推理模型」的两段级联，用一小部分成本拿到接近大推理模型的质量。
  <sub>`官方文档` · `Py`</sub>

- **[Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing)** ⭐ — 对进来的请求做分类，路由到足够用的最便宜那个处理方：确定性代码、专用 LLM、或人。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)** — 三个可独立安装的 Claude Code 插件 —— 护栏、模型路由、技能推荐 —— 各自带 hook 和测试。
  <sub>`插件` · ★31,297 · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)** — LangChain 集成的 JavaScript 对应版本，分类器与 middleware 形状一致。
  <sub>`平台集成` · ★18,222 · `TS` · `choice` · `score` · `noul`</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** — 九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。
  <sub>`插件` · ★673 · `Py` · `choice` · `score` · `noul`</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)** — 代码审查前先过一遍 Jev，把高风险改动挑出来，再交给更贵的大模型或人。带本地看板。
  <sub>`开源项目` · ★568 · `TS` · `choice` · `score` · `noul`</sub>

- **[jev-codex-router](https://github.com/0xNatoshi/jev-codex-router)** — 先让 Jev 判断这一轮编程任务有多难，再决定模型档位、推理深度和速度模式。
  <sub>`插件` · ★242 · `JS` · `choice` · `score`</sub>

- **[jevrouter](https://github.com/BillionsBobby/JevRouter)** — 面向模型、工具和子智能体的路由器。
  <sub>`开源项目` · ★178 · billionsbobby · `TS`</sub>

- **[jev-eval-agent](https://github.com/vinilana/jev-eval-agent)** — 一个把评测工作通过类型化决策来路由的智能体。
  <sub>`开源项目` · ★105 · vinilana · `TS` · ⚠ `无许可证`</sub>

- **[jev-use](https://github.com/shitianfang/jev-use)** — 一个智能体插件：把不需要文本输出的步骤交给 Jev，而不是主模型。
  <sub>`插件` · ★22 · shitianfang · `JS`</sub>

- **[pi-jev-router](https://github.com/mejiasd3v/pi-jev-router)** — 通过 Vercel AI Gateway 为 Pi 做自动模型路由。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★13 · mejiasd3v · `JS`</sub>

- **[jev-router](https://github.com/prismhq/jev-router)** — 开源 LLM 路由器，在 LiteLLM 之上用 Jev 选模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10 · prismhq · `Py`</sub>

- **[jev-auto-router](https://github.com/miniLV/Jev-Auto-Router)** — 实验性的逐次调用 GPT 模型路由，通过 Jev 与一个本地 Rescue 层为 Codex 服务。 <sub>(机翻)</sub>
  <sub>`插件` · ★6 · minilv · `TS`</sub>

- **[jev-codex-pilot](https://github.com/Charlyhno-eng/jev-codex-pilot)** — 带 JEV 模型路由、上下文优化与看板自动化的 Codex 覆盖层。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · charlyhno-eng · `TS`</sub>

- **[jev-gate](https://github.com/MongLong0214/jev-gate)** — 不是每个编程任务都需要你最好的模型：实验性的 Jev 模型路由。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · monglong0214 · `TS` · ⚠ `无许可证`</sub>

- **[smart-switch](https://github.com/reycn/smart-switch)** — 用前沿 AI 重新想象的 macOS 窗口切换器，由 Jev 做预测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · reycn · `Swift`</sub>

- **[tiershift](https://github.com/iamvatsalpatel/tiershift)** — 把每次 LLM 调用下沉到能胜任的最便宜模型，路由由 Jev 在约 180 毫秒内决定，无需训练。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · iamvatsalpatel · `TS`</sub>

- **[janus](https://github.com/FirasSX914/Janus)** — 先在你自己的数据上衡量何时该用 Jev、何时该用别的模型，再据此路由。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · firassx914 · `Py`</sub>

- **[hermes-jev-router](https://github.com/ussyverse/hermes-jev-router)** — 实验性 Hermes 插件：带预算与能力约束的 Jev 辅助模型路由方案。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · ussyverse · `Py`</sub>

- **[jev-engineering](https://github.com/eugeniughelbur/jev-engineering)** — 面向 AI 智能体的决策层：约 400 毫秒、两百分之一美分的类型化校准决策，用于拦截工具调用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · eugeniughelbur · `Py`</sub>

- **[jev-synthetic-survey](https://github.com/jjd-lab/jev-synthetic-survey)** — 把 Jev 与 GPT-4.1 当作合成问卷受访者做对比 —— 怎么问比用哪个模型更重要。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · jjd-lab · `Py`</sub>

- **[Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)** — LangChain 的讲解兼集成实操：三种问题类型，加上模型路由、以及在高风险工具调用执行前拦截它。
  <sub>`文章` · Sydney Runkle, Hunter Lovell · `Py` · ⚠ `厂商自报数据`</sub>

- **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)** — 逐个用例走一遍 —— 智能体路由、智能体内部的决策层、工单分拣 —— 每个都给出具体的选项集和示例响应。
  <sub>`教程` · Mehul Gupta · `Py` · `choice` · ⚠ `付费墙`</sub>

- **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)** — LangChain 集成：一个分类器，外加用于模型路由、以及在高风险工具调用执行前拦截它的实验性 middleware。
  <sub>`平台集成` · `Py` · `choice` · `score` · `noul` · ⚠ `需早期访问`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件 —— 两者不一致时 CI 会失败。</sub>
