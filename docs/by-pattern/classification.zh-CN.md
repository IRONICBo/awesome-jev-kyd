# 分类

<sub>[awesome-jev](../../README.zh-CN.md) · [English](classification.md)</sub>

_把条目归入分类体系，包括用概率遍历的深层层级。_

这个决策的全部已收录例子 —— 共 83 条，官方优先，其次是含代码的，再按 star 排序。同样这些行及其警示也在[索引](../../README.zh-CN.md#分类)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=classification&lang=zh)还能按语言、原语和形态进一步筛选。

- **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐ — 把年报分入 75 个行业组，再根据答案自身的置信度决定：报这个细分组，还是退回上一层的大类。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification)** ⭐ — 用对 Choice 概率做并行 beam search 的方式，遍历专利、零售、生物医学、源码这几套很深的分类体系。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐ — 判断两份商品目录间 450 个候选配对里哪些指的是同一个东西 —— 一个 Score 就够，它的三级正好对应三种可执行动作。
  <sub>`官方文档` · `Py` · `score`</sub>

- **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐ — 用两次请求把丢了格式的纯文本还原成 Markdown：一次把硬换行的段落重新接起来，一次给每个块分类。
  <sub>`官方文档` · `Py`</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)** — 用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。
  <sub>`基准测试` · ★87,239 · `TS` · `choice` · ⚠ `仅影子运行`</sub>

- **[json-render](https://github.com/vercel-labs/json-render)** — Vercel Labs 的生成式 UI 框架。实验里 Jev 不逐 token 写 JSON，只负责选组件、属性和布局。
  <sub>`开源项目` · ★18,113 · Vercel Labs · `TS` · `choice`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)** — 七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。
  <sub>`开源项目` · ★12,304 · `TS` · `choice` · `noul`</sub>

- **[classifier-dev](https://github.com/mrmps/classifier-dev)** — 基于纯 HTTP 的零样本文本分类 —— 不需要密钥、不需要账号，一个 Cloudflare Worker。 <sub>(机翻)</sub>
  <sub>`插件` · ★411 · mrmps · `TS`</sub>

- **[tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier)** — 基于 Jev 决策的税务文档分页分类器，在 261 种 IRS 表单上达到严格全对，每页约 $0.001。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★399 · kyotofin · `TS`</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — 一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。
  <sub>`开源项目` · ★315 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[docjev](https://github.com/jerryjliu/docjev)** — 非常快的文档分类与切分器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★292 · jerryjliu · `Py`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。
  <sub>`插件` · ★290 · `JS` · `choice` · `score` · `noul`</sub>

- **[unclutter](https://github.com/kitze/unclutter)** — 一个浏览器扩展，用可复用的模板规则清除页面杂物。
  <sub>`开源项目` · ★203 · kitze · `TS`</sub>

- **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)** — 独立的韩语实测笔记，报告仅仅把选项顺序倒过来，就能让概率移动到足以翻转 0.9 阈值的程度。
  <sub>`基准测试` · ★190 · `Py` · ⚠ `无许可证` `宣称未核实`</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — 先用 tree-sitter 找出并排序方法，再把用户自写的 YAML 规则编译成 noul；严重度取评分量表的期望值，而不是概率最高的那一档。
  <sub>`开源项目` · ★170 · `JS` · `choice` · `score` · `noul`</sub>

- **[taskuary](https://github.com/ldbumble/taskuary)** — 本地优先的 AI 任务中枢：把邮件、Teams、Slack 与报表汇成一条时间线。 <sub>(机翻)</sub>
  <sub>`插件` · ★118 · ldbumble · `Py`</sub>

- **[youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection)** — 结合实时音频与字幕检测 YouTube 视频里的赞助片段。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★91 · trungdq88 · `JS` · ⚠ `无许可证`</sub>

- **[pg_typesafe](https://github.com/giuliosmall/pg_typesafe)** — 用于 Jev 分类决策的 PostgreSQL 扩展（预 alpha）。 <sub>(机翻)</sub>
  <sub>`插件` · ★82 · giuliosmall · `C`</sub>

- **[Prism](https://github.com/irfndi/prism-liquidity-agent)** — 不直接让 Jev 下单。它判断 toxic flow、市场压力、均值回归之类的状态，再交给原来的策略。
  <sub>`开源项目` · ★79 · `TS` · `choice` · `score`</sub>

- **[typesafe-adblock](https://github.com/realZachi/typesafe-adblock)** — 一个 Chrome 扩展，逐个询问 DOM 元素是不是广告。
  <sub>`开源项目` · ★71 · realzachi · `JS`</sub>

- **[Blink](https://github.com/ellipsis-dev/blink)** — 把 Jev 当代码库导航器。每走到一层目录，就判断哪些文件和当前问题最相关，再继续往下找。
  <sub>`开源项目` · ★65 · `TS` · `choice` · ⚠ `无许可证`</sub>

- **[ha-jev](https://github.com/AboveColin/HA-Jev)** — 一个 Home Assistant 集成：把类型化答案变成传感器，并提供可用于自动化的动作。
  <sub>`平台集成` · ★50 · abovecolin · `Py`</sub>

- **[jev-sift](https://github.com/kbhuw/jev-sift)** — 先分类，再选择性阅读：可移植的批量文本分类插件与 MCP 工具。 <sub>(机翻)</sub>
  <sub>`插件` · ★45 · kbhuw · `JS` · ⚠ `无许可证`</sub>

- **[SemDecide](https://github.com/sharziki/semdecide)** — 把 Jev 做成命令行。Shell 里直接分类、打分、过滤，适合接爬虫、CI 和数据流水线。
  <sub>`插件` · ★38 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[commit-miner](https://github.com/devanshbatham/commit-miner)** — 用 Jev 对 Git 提交的 diff 与信息做分类：缺陷修复、安全修复、变更类型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★36 · devanshbatham · `Rs` · ⚠ `无许可证`</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — 用你自己的标注数据校准 Jev 的问题：在标注样本上调 criteria，在留出集上确认。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★31 · smkrv · `TS`</sub>

- **[jev-column-race](https://github.com/goodrahstar/jev-column-race)** — Jev 对比一个轻量 LLM：标注 1000 条应用评论，快 4.1 倍、便宜 7 倍。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★22 · goodrahstar · `JS`</sub>

- **[jev-mcp](https://github.com/blakestone-x/jev-mcp)** — 一个 MCP server，把分类、打分、检查、匹配、筛选暴露给任意智能体。
  <sub>`插件` · ★21 · blakestone-x · `Py`</sub>

- **[jgrep (npm: jevgrep)](https://github.com/kyu1204/jgrep)** — 按代码的作用来 grep：对每个代码块、diff 块或 CSV 行问一个 Noul，输出带概率的 file:line 命中。--diff 用一条英文规则在 CI 里为 PR 把关（退出码 0 命中 / 1 干净 / 2 出错）；--tests 列出一次 diff 可能影响的测试文件。
  <sub>`开源项目` · ★16 · kyu1204 · `TS` · `noul` · `choice` · `score`</sub>

- **[x-scanner](https://github.com/oso95/x-scanner)** — Chrome 扩展：给你在 X 上滑过的每条帖子打上类型化 Jev 判断与实时评分。 <sub>(机翻)</sub>
  <sub>`插件` · ★16 · oso95 · `TS`</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — 用 Jev 给收件箱分类：打标、移动、标记、通知，全部配置驱动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★14 · parth-kp · `Py`</sub>

- **[jevframe](https://github.com/ktaletsk/jevframe)** — 给 pandas 和 Polars 的语义 AI：用自然语言问题对 DataFrame 的行做分类、情感分析与打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★13 · ktaletsk · `Py`</sub>

- **[jev-code](https://github.com/FrancoisChastel/jev-code)** — 把 Jev 作为工具接入多个编程智能体。 <sub>(机翻)</sub>
  <sub>`插件` · ★12 · francoischastel · `TS`</sub>

- **[evoke](https://github.com/evoke-build/evoke)** — 反射式软件：一句话变成对一个小程序的调用，由 Jev 选择。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★11 · evoke-build · `Rs`</sub>

- **[jevlogs](https://github.com/reachjalil/jevlogs)** — 面向 OpenTelemetry 的开源 Jev 日志分拣：在昂贵的 LLM 分析之前先给信号打分。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10 · reachjalil · `JS`</sub>

- **[sift](https://github.com/bohutang/sift)** — Chrome 扩展：给 X 上的每条帖子打标（干货／幽默／闲聊／推广／垃圾／AI 生成）。 <sub>(机翻)</sub>
  <sub>`插件` · ★10 · bohutang · `JS`</sub>

- **[jev-agent-browser](https://github.com/forvela/jev-agent-browser)** — 由 Jev 驱动的快速有界浏览器智能体：类型化动作、调研、分类与安全编排。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · forvela · `JS`</sub>

- **[jev-dsl](https://github.com/inanna-malick/jev-dsl)** — 面向智能体的 Haskell DSL：类型化数据包、类型推断，答案与问题同构。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · inanna-malick · `Hs`</sub>

- **[augustus](https://github.com/24601/Augustus)** — 面向决策模型这一类别的 agent 技能：分类器、编解码器、专用 AR 头、System One。 <sub>(机翻)</sub>
  <sub>`插件` · ★6 · 24601 · `Py`</sub>

- **[one-system](https://github.com/rawwerks/one-system)** — 通过统一接口使用本地与托管的分类器（即决策模型）。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★6 · rawwerks · `TS` · ⚠ `并非 Jev 本身`</sub>

- **[jev-tree](https://github.com/reachjalil/jev-tree)** — 在分类体系上做递归 Jev choice —— 在不突破 255 选项上限的前提下，从更多选项中做选择。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · reachjalil · `TS`</sub>

- **[agi-jev-containment](https://github.com/carlosedm10/agi-jev-containment)** — 本地 AI 智能体监控：链路级恶意智能体检测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · carlosedm10 · `Py` · ⚠ `无许可证`</sub>

- **[jev-document-classification](https://github.com/Charlyhno-eng/jev-document-classification)** — 对文本文档做快速且低成本的分类。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · charlyhno-eng · `TS`</sub>

- **[jeveryword](https://github.com/jkrup/jeveryword)** — 用 Jev 做文本抽取：字段抽取、PII 检测与逐字引文。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · jkrup · `JS`</sub>

- **[agent-fastpath](https://github.com/abhishekswe/agent-fastpath)** — Jev MCP server：给编程智能体的决策层。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · abhishekswe · `TS`</sub>

- **[duckdb-jev](https://github.com/prasanthj/duckdb-jev)** — 高吞吐的原生 DuckDB 扩展，支持批量与流式的分类、打分与筛选。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · prasanthj · `C++`</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — 八个最小可运行示例：把 Jev 用在机械与电气工程场景。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · foadsf · `Py`</sub>

- **[jev-ids](https://github.com/jev-ids/jev-ids)** — 基于 Jev 的高速、省 token 的入侵检测系统。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · jev-ids · `Py`</sub>

- **[jev-skip](https://github.com/valentynkit/jev-skip)** — 读字幕、在观看时判断，从而跳过视频里的赞助段落。
  <sub>`开源项目` · ★3 · valentynkit · `TS`</sub>

- **[local-jev](https://github.com/amithgc/local-jev)** — 本地离线的 System One 服务，兼容 Jev API，回答类型化的是非问题。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · amithgc · `Py`</sub>

- **[dsh-jev-decide](https://github.com/nanami-0713/dsh-jev-decide)** — DSH 插件：把 Jev 注册成一个智能体工具。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · nanami-0713 · `JS`</sub>

- **[hush](https://github.com/emreozyoruk/hush)** — 不确定时保持沉默的 issue 分拣：校准过的标签，含垃圾与重复检测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · emreozyoruk · `JS`</sub>

- **[jev-chess](https://github.com/hemanth/jev-chess)** — 用 Jev 做国际象棋的着法、局面评估、人格对手与棋局分类。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · hemanth · `TS` · ⚠ `无许可证`</sub>

- **[jev-mcp-server](https://github.com/wangkuangkuang/jev-mcp-server)** — Jev 的 MCP server：提供官方三种问题类型。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · wangkuangkuang · `Py`</sub>

- **[jev-mode](https://github.com/ddfeyes/jev-mode)** — 编程智能体总在不难的决策上烧上下文 —— 分拣 400 条工单之类的活儿不该这么贵。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · ddfeyes · `Py`</sub>

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)** — 给 Spring WebFlux 的非阻塞 Starter，实现一个语义熔断器来检测静默故障。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · vicente-md · `Java` · ⚠ `无许可证`</sub>

- **[watfile](https://github.com/jexp/watfile)** — 用 Jev 或本地校准决策模型给文本与 PDF 分类归档。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · jexp · `Py` · ⚠ `无许可证`</sub>

- **[zerosweep](https://github.com/sysadarsh/zerosweep)** — 自主的 System-One 分拣引擎与基准，75 毫秒推理。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★2 · sysadarsh · `TS` · ⚠ `无许可证`</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — 十个可运行的 JavaScript 智能体决策，一个文件一个：新记忆与旧记忆冲突时该改还是该留、工具返回 200 是否真的完成了任务、写入超时后该重试还是该对账、上下文分块在预算内如何取舍、压缩后的交接是否丢掉了某条禁令。Jev 只回答带类型的问题，阈值和最终提案由普通代码决定。
  <sub>`开源项目` · ★1 · Really Artificial · `JS` · `choice` · `score` · `noul` · ⚠ `仅一次提交` `疑似 AI 生成`</sub>

- **[jev-eval](https://github.com/4esv/jev-eval)** — 在你自己的标注分类数据上，把 Jev 与任意 OpenRouter 模型做基准对比：准确率与校准度。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · 4esv · `Py` · ⚠ `无许可证`</sub>

- **[jev-issue-radar](https://github.com/Patrick-SCH03/jev-issue-radar)** — 带并排证据的 GitHub issue 分拣，可免配置试用公开样例。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · patrick-sch03 · `JS`</sub>

- **[jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)** — 由 Jev 判断一批日志是否值得处理：类型化问题、置信闸门，不执行任何动作。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · jyatesdotdev · `Py`</sub>

- **[jev-playwright-mcp](https://github.com/krw82/jev-playwright-mcp)** — Jev 增强的 Playwright MCP 代理：页面状态分拣与提示注入防护。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · krw82 · `TS`</sub>

- **[jev-review-action](https://github.com/fatwang2/jev-review-action)** — 可配置的 GitHub 提交审查与 PR 分类，不使用任何文本生成模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · fatwang2 · `JS`</sub>

- **[jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)** — 衡量 Jev 在文件片段中识别真实密钥凭据的能力。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · teyhouse · `Py` · ⚠ `无许可证`</sub>

- **[jev-triage](https://github.com/cephalization/jev-triage)** — 拉取并同步大型仓库以做 issue 分拣。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · cephalization · `TS`</sub>

- **[jevticktrouter](https://github.com/GhrezaKh74/JevTicktRouter)** — 用 .NET 10 与 React 19 做的快速结构化工单分拣。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · ghrezakh74 · `C#` · ⚠ `无许可证`</sub>

- **[metis](https://github.com/Ayush0054/metis)** — Metis：由 Jev 驱动的 GitHub issue 自动分拣，可复用的 GitHub Action。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · ayush0054 · `Py`</sub>

- **[n8n-nodes-jev-classification](https://github.com/khmuhtadin/n8n-nodes-jev-classification)** — Jev 的 n8n 社区节点：带校准概率的文本分类、打分与检查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · khmuhtadin · `TS`</sub>

- **[triagedy](https://github.com/m0rphtail/triagedy)** — 把告警分拣做成 UNIX 过滤器：JSONL 安全告警进，类型化决策出。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · m0rphtail · `Rs`</sub>

- **[discoprint](https://github.com/lirantal/discoprint)** — 用 Jev 按主题、情绪与歌词复杂度给一位艺人的全部作品分类，并可视化呈现。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · lirantal · `JS`</sub>

- **[github-issue-classification-using-jev](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev)** — 基于 Jev 的 GitHub issue 分类器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · kalyanm45 · `Py`</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — 给 AI 智能体的免费类型化判断：把分类／筛查／打分／校验卸载给 Jev。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · yuyang2230 · `Py`</sub>

- **[jev-trace-classifier](https://github.com/sypherin/jev-trace-classifier)** — 把 Jev 的 noul 原语应用到一个共谋语料库上。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · sypherin · `Py`</sub>

- **[omp-jevens-classifier](https://github.com/STRML/omp-jevens-classifier)** — 给 OMP 的模型裁决式权限闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · strml · `TS` · ⚠ `已归档`</sub>

- **[progressgate](https://github.com/AshutoshVJTI/progressgate)** — 检测 AI 智能体循环中的语义停滞。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ashutoshvjti · `TS`</sub>

- **[pulselane](https://github.com/ndolinschi/pulselane)** — PulseLane：诊所分诊决策。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ndolinschi · `TS` · ⚠ `无许可证`</sub>

- **[typesafe-image-diffusion](https://github.com/Wizhill05/typesafe-image-diffusion)** — 用通用分类器做扩散风格像素画：256 个并行像素问题。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · wizhill05 · `TS` · ⚠ `无许可证`</sub>

- **[typesafe-triage-guard](https://github.com/shivam2003-dev/typesafe-triage-guard)** — 基于 Jev 的三条可组合判断流水线：工单分拣、可观测性等。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · shivam2003-dev · `Py`</sub>

- **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)** — 找到的最好的独立实测：固定单一模型版本、24 份挪威语文档，开篇就展示了一个模型答错、但同时正确报出低置信度的案例。
  <sub>`基准测试` · Lindfors</sub>

- **[Jev - The Ultimate Classification Model?](https://youtube.com/watch?v=X117w2Rark8)** — 一位 ML 工程师从分类任务角度做的讲解 —— 这个切入角度最贴近模型的实际能力。
  <sub>`视频` · Sam Witteveen</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。
  <sub>`开源项目` · ⚠ `宣称未核实`</sub>

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)** — 找到的唯一三方横评，每个模型分别调过提示词，且明确把范围限定在单一任务上、不做通用排名。
  <sub>`基准测试` · Near Here</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件 —— 两者不一致时 CI 会失败。</sub>
