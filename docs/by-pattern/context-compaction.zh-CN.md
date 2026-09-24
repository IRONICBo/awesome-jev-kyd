# 上下文压缩

<sub>[awesome-jev](../../README.zh-CN.md) · [English](context-compaction.md)</sub>

_判断哪些工具调用和结果仍然相关，从而丢弃过期上下文。_

这个决策的全部已收录例子 —— 共 22 条，官方优先，其次是含代码的，再按 star 排序。同样这些行及其警示也在[索引](../../README.zh-CN.md#上下文压缩)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=context-compaction&lang=zh)还能按语言、原语和形态进一步筛选。

- **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)** — 把 Jev 压缩方案移植过来，与自家在用的摘要器对比实测，最后公开结论：不采用。
  <sub>`基准测试` · ★248,479 · `Py` · `noul`</sub>

- **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)** — 把记忆召回的整套检索栈替换掉 —— 不用 embedding、不用 BM25、不用重排器 —— 改为对每条候选记忆批量问一个 Noul。
  <sub>`开源项目` · ★20,069 · `Rs` · `noul`</sub>

- **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** — 一个 Claude Code 插件，用逐条决策取代压缩式摘要：过期的工具调用被丢弃或截断，保留下来的全部逐字不变。
  <sub>`插件` · ★6,616 · tamaratran · `TS` · `noul`</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** — 九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。
  <sub>`插件` · ★718 · `Py` · `choice` · `score` · `noul`</sub>

- **[compact-adviser](https://github.com/kunchenguid/compact-adviser)** — 判断工作是否已完成或已记录，据此提示运行上下文压缩。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★183 · kunchenguid · `TS`</sub>

- **[jev-pruner](https://github.com/tamaratran/jev-pruner)** — 在模型看到之前先修剪冗长的 shell 输出，每个片段问一个 Noul。
  <sub>`插件` · ★144 · tamaratran · `TS` · `noul`</sub>

- **[Winnow](https://github.com/GhalebDweikat/winnow)** — 给 Claude Code 做上下文垃圾回收。Read / Bash / Grep 吐一大堆时，Jev 先判断哪些真和当前任务有关。
  <sub>`插件` · ★79 · `Py` · `noul`</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — 给 Claude Code 和 Codex 做的上下文裁剪代理：由 Jev 判断哪些历史还需要 —— 实测而非宣称。 <sub>(机翻)</sub>
  <sub>`插件` · ★25 · compozy · `TS`</sub>

- **[claude-jev](https://github.com/0x7067/claude-jev)** — Claude Code 插件：Jev 负责规则检查、逐字压缩与提示路由。 <sub>(机翻)</sub>
  <sub>`插件` · ★12 · 0x7067 · `Py`</sub>

- **[omp-jev-compaction](https://github.com/jerryfane/omp-jev-compaction)** — 给 omp 做的逐字保留式 Jev 打分上下文削减。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · jerryfane · `TS`</sub>

- **[pi-jev-context](https://github.com/Nyarlathoteppppp/pi-jev-context)** — 一个 Pi 扩展：感知新鲜度的读取去重、Jev 日志过滤，模型表现优先、省 token 其次。 <sub>(机翻)</sub>
  <sub>`插件` · ★7 · nyarlathoteppppp · `TS`</sub>

- **[deepseek-harness-jev-pre-compaction](https://github.com/wjw66/deepseek-harness-jev-pre-compaction)** — 给 DeepSeek Harness 的压缩前顾问，在标准压缩流程之前运行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · wjw66 · `TS`</sub>

- **[fast-dev-compaction](https://github.com/leonaaardob/fast-dev-compaction)** — Codex 插件：在会话压缩前后，由 Jev 引导逐字恢复上下文。移植自 tamaratran/fast-jev-compaction，适配 Codex 的生命周期钩子。 <sub>(机翻)</sub>
  <sub>`插件` · ★5 · leonaaardob · `TS`</sub>

- **[dsh-jev-prune](https://github.com/yangyu666/dsh-jev-prune)** — 给 DeepSeek Harness 的 Jev 判定式上下文压缩：语义化的工具结果裁剪。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · yangyu666 · `JS`</sub>

- **[fast-compaction-dsh](https://github.com/kolawong/fast-compaction-dsh)** — 给 DeepSeek Harness 的判定式上下文压缩，取代有损的 LLM 摘要。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · kolawong · `TS`</sub>

- **[jev-compaction](https://github.com/picaye/jev-compaction)** — 从不做摘要的 Hermes 会话上下文压缩：每次工具调用都被打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · picaye · `JS`</sub>

- **[jselect](https://github.com/keltokhy/jselect)** — 在 token 预算内给 AI 挑出有用证据：快速、带来源链接的上下文选择器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · keltokhy · `Py`</sub>

- **[pi-jev-compaction](https://github.com/nourhelmi/pi-jev-compaction)** — 为 Pi 自动清理 Jev 上下文：保留对话，修剪过期的工具输出，无需重跑命令即可取回原始内容。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · nourhelmi · `TS`</sub>

- **[jev-docs](https://github.com/chenrui333/jev-docs)** — 社区维护的 Jev／System One API、SDK 与智能体指南的变更史。 <sub>(机翻)</sub>
  <sub>`SDK` · ★2 · chenrui333 · `Py`</sub>

- **[pi-fast-jev-compaction](https://github.com/KamilPostrozny/pi-fast-jev-compaction)** — 给 pi 的快速 JEV 压缩扩展。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · kamilpostrozny · `TS`</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — 十个可运行的 JavaScript 智能体决策，一个文件一个：新记忆与旧记忆冲突时该改还是该留、工具返回 200 是否真的完成了任务、写入超时后该重试还是该对账、上下文分块在预算内如何取舍、压缩后的交接是否丢掉了某条禁令。Jev 只回答带类型的问题，阈值和最终提案由普通代码决定。
  <sub>`开源项目` · ★1 · Really Artificial · `JS` · `choice` · `score` · `noul` · ⚠ `仅一次提交` `疑似 AI 生成`</sub>

- **[smoking-extraction-benchmark](https://github.com/vclic/smoking-extraction-benchmark)** — 合成的吸烟史抽取基准：对比 Jev 与 OpenAI 结构化输出。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · vclic · `Py` · ⚠ `无许可证`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件 —— 两者不一致时 CI 会失败。</sub>
