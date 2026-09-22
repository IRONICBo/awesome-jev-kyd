<!--
  This file is generated from catalog.json. Edit the catalog, then run `python3 scripts/build_readme.py`.
-->

<div align="center">

# awesome-jev

**Every public example of Jev — TypeSafe AI's System One decision model — indexed by the decision it makes, not by the blog that mentioned it.**

[![lint](https://github.com/kydlikebtc/awesome-jev/actions/workflows/lint.yml/badge.svg)](https://github.com/kydlikebtc/awesome-jev/actions/workflows/lint.yml) [![links](https://github.com/kydlikebtc/awesome-jev/actions/workflows/links.yml/badge.svg)](https://github.com/kydlikebtc/awesome-jev/actions/workflows/links.yml) [![entries](https://img.shields.io/badge/entries-404-f5a524?style=flat-square)](https://kydlikebtc.github.io/awesome-jev/) [![verified](https://img.shields.io/badge/link--verified-400-3fb950?style=flat-square)](https://kydlikebtc.github.io/awesome-jev/) [![rechecked](https://img.shields.io/badge/claims%20re--checked-320-58a6ff?style=flat-square)](https://github.com/kydlikebtc/awesome-jev/actions/workflows/claims.yml) [![data](https://img.shields.io/badge/data-CC0--1.0-8b949e?style=flat-square)](LICENSE-CC0) [![code](https://img.shields.io/badge/code-MIT-8b949e?style=flat-square)](LICENSE-MIT)

[Searchable site](https://kydlikebtc.github.io/awesome-jev/) &nbsp;·&nbsp; [中文](README.zh-CN.md) &nbsp;·&nbsp; [Patterns](docs/patterns.md) &nbsp;·&nbsp; [Compatibility](docs/compatibility.md) &nbsp;·&nbsp; [Vetting](docs/vetting.md)

<a href="https://kydlikebtc.github.io/awesome-jev/"><img src="docs/screenshots/site-desktop.png" alt="The awesome-jev site: a coverage histogram down the left acting as the pattern filter, dense entry cards on the right" width="760"></a>

<sub>Filter by clicking a bar. Two more views: <a href="https://kydlikebtc.github.io/awesome-jev/?view=prims">primitives</a> · <a href="https://kydlikebtc.github.io/awesome-jev/?view=compat">compatibility</a>. Every filter and entry is a shareable URL.</sub>

</div>

---

## What this is

- **Jev** is a decision model from TypeSafe AI. It does not write text — you hand it state plus typed questions and it returns typed answers with calibrated confidence, fast and cheap enough to sit in an agent's inner loop.
- **This repo** indexes public examples of using it, organised by the *decision* being made. The resource you read this week is disposable; the decision pattern is not.
- **Why trust it:** every row names where it came from, says which primitives the code actually calls, and flags what a reader deserves to know before clicking. There are dozens of Jev lists — this one competes on verification, not on size.

> ⚠️ Not the product, not an SDK, not affiliated with TypeSafe AI, and not a recommendation. A row means the link resolved and a person read it — nothing more. See [what is verified](#what-is-verified-and-what-is-not).

## What Jev returns

Three primitives. Every pattern below is built out of them, and the asymmetry in the last row is the single most common source of bugs.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/primitives-en-dark.svg">
  <img src="docs/assets/primitives-en-light.svg" alt="Three panels describing the choice, score and noul primitives and what each returns" width="660">
</picture>

Input is **text only** — string, JSON object, or array of text. Context is **64k** tokens per request, **32k** for the state plus the longest question. Output tokens are free. There are no published weights, so it cannot be run locally. Full cross-platform differences: [`docs/compatibility.md`](docs/compatibility.md).

## Start here

Six things in reading order. Hand-picked, because "most starred" is not the same as "read this first".

1. **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)**
   <sub>The canonical first call: one support ticket, one Choice, one Score and one Noul in a single request, in Python, JS and cURL.</sub>

2. **[Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)**
   <sub>The most useful page in the docs and the least linked. It explains, among other things, that a Choice over options and one Noul per option answer different questions.</sub>

3. **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)**
   <sub>Written from the official API reference and checked field by field against it, but not executed against the live API.</sub>

4. **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)**
   <sub>Exactly two nouls per tool call: does knowing this call happened still matter, and is the full output still needed verbatim. Despite the word "scored" in its own description, no score primitive is used.</sub>

5. **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**
   <sub>The best structured tutorial found. It states plainly that typed output does not guarantee a correct decision, lists the documented weaknesses, and qualifies its own cost illustration rather than selling it.</sub>

6. **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)**
   <sub>The single most credible row in this catalog. Recall came out below their existing summariser, and at a matched context budget it tied plain recency ordering. Cost was genuinely far lower. Publishing a negative result on a hyped model is rare.</sub>

## Coverage

Every decision pattern, sized by how many examples exist. This doubles as the index — the names link to the sections below. A zero is a research gap, not a rendering bug.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/coverage-en-dark.svg">
  <img src="docs/assets/coverage-en-light.svg" alt="Horizontal bar chart of how many catalog examples exist for each of the eighteen decision patterns" width="100%">
</picture>

Two patterns have no examples yet. Both are plausible fits nobody appears to have published — see [`docs/status.md`](docs/status.md).

## Measured, not claimed

Almost every performance number circulating about this model is the vendor's own, produced with reference answers derived from other models' judgements rather than human ground truth. These are the independent measurements in the catalog — several are **negative results**, which is exactly why they are worth reading first.

- **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)** — Ported the Jev compaction approach, measured it against their shipping summariser, and published the conclusion not to adopt it.
  <sub>`Benchmark` · ★247,881 · `Py` · `noul`</sub>
  <sub>The single most credible row in this catalog. Recall came out below their existing summariser, and at a matched context budget it tied plain recency ordering. Cost was genuinely far lower. Publishing a negative result on a hyped model is rare.</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)** — Two Choice questions over threat level and category, held in shadow mode after a blind evaluation found Jev merely tied the incumbent model.
  <sub>`Benchmark` · ★87,191 · `TS` · `choice` · ⚠ `shadow mode`</sub>
  <sub>Wired in but deliberately inert: by their own statement nothing Jev returns reaches a label, a cache row or an alert. Ships a golden fixture. A model to copy for how to trial a new model without betting production on it.</sub>

- **[no-mistakes: review context selection](https://github.com/kunchenguid/no-mistakes)** — One Score per candidate file to pick review context, with a measured outcome: materially more billed input for essentially no wall-clock gain.
  <sub>`Benchmark` · ★8,598 · `Go` · `score`</sub>
  <sub>Their own recommendation was to keep the feature opt-in, off by default, and ship no savings claim. That is what an honest measurement looks like.</sub>

- **[hippo-memory](https://github.com/kitfunso/hippo-memory)** — Biologically-inspired memory for AI agents. Decay, retrieval strengthening, consolidation. Zero runtime deps, SQLite, MCP. Benchmarked retrieval with an opt-in TypeSafe Jev reranker.
  <sub>`Benchmark` · ★752 · kitfunso · `TS`</sub>

- **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)** — Independent Korean-language notes reporting that reversing the order of options shifted a probability enough to flip a 0.9 threshold.
  <sub>`Benchmark` · ★190 · `Py` · ⚠ `no licence` `unverified`</sub>
  <sub>The most actionable engineering caveat found anywhere: if option order alone can move a probability past your threshold, your threshold is not as stable as it looks. Independent and unreplicated, so treat the magnitude as indicative.</sub>

- **[windtunnel](https://github.com/nekuda-ai/WindTunnel)** — A WebMCP benchmark, measures WebMCP against other browser-agent interfaces.
  <sub>`Benchmark` · ★76 · nekuda-ai · `TS`</sub>

- **[jevbench](https://github.com/fstandhartinger/jevbench)** — JevBench v1 - a benchmark for Jev-class typed decision models: smart, cheap, fast, reliable, open.
  <sub>`Benchmark` · ★71 · fstandhartinger · `Py`</sub>

- **[typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark)** — A gateway that mimics the structured-output shape, used to benchmark against it.
  <sub>`Benchmark` · ★37 · iammrduncan · `TS`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — Read-only trading journal and review harness: Jev typed judgments, agent integration, and a reproducible finance benchmark. No orders, no advice.
  <sub>`Benchmark` · ★26 · myc0576 · `Py`</sub>

- **[jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas)** — Independent, evidence-based map of when TypeSafe's Jev actually holds up vs. breaks down — real API-call receipts, not a leaderboard. 中文為主的雙語 repo。
  <sub>`Benchmark` · ★24 · zaious · `Py`</sub>

- **[jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)** — Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks.
  <sub>`Benchmark` · ★17 · abdelstark · `Py`</sub>

- **[jev-benchmark](https://github.com/wondertwins/jev-benchmark)** — Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs
  <sub>`Benchmark` · ★6 · wondertwins · `Py`</sub>

- **[jev-korean-benchmark](https://github.com/mahlernim/jev-korean-benchmark)** — Reproducible early-access evaluation of Jev on Korean understanding and medical text, with runtime and cost evidence
  <sub>`Benchmark` · ★6 · mahlernim · `Py` · ⚠ `no licence`</sub>

- **[jev-little-airways](https://github.com/lbotinelly/jev-little-airways)** — A show-and-tell capability study for Jev, TypeSafe's System One decision model.
  <sub>`Benchmark` · ★5 · lbotinelly · `TS`</sub>

- **[jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench)** — An independent head-to-head against dedicated rerankers across fourteen datasets.
  <sub>`Benchmark` · ★5 · anessbelbati · `Py`</sub>
  <sub>An independent measurement rather than a vendor figure, and a direct comparison against purpose-built rerankers — the comparison that matters for the search-ranking pattern.</sub>

- **[legalforecastbench](https://github.com/johnhughes3/LegalForecastBench)** — LegalForecast-MTD benchmark alpha and official evaluation workflows
  <sub>`Benchmark` · ★5 · johnhughes3 · `Py`</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — Independent calibration test of TypeSafe's Jev on a task it cannot have seen: 900 rule-generated support tickets (choice / score / boolean) plus 3 public benchmarks via Vercel AI Gateway. Raw responses, ECE with noise floor, temperature refit, per-type sign of miscalibration. Reproducible for ~
  <sub>`Benchmark` · ★4 · scienthoon · `Py`</sub>

- **[jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab)** — Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows
  <sub>`Benchmark` · ★3 · jmanhype · `Py`</sub>

- **[jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench)** — Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark.
  <sub>`Benchmark` · ★3 · anisselbd · `Py` · ⚠ `no licence`</sub>

- **[jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark)** — Benchmarking Jev (Typesafe.ai) against a strong LLM on the Who&When Pro agent-failure-attribution benchmark (text subset).
  <sub>`Benchmark` · ★2 · tokentrim · `Py`</sub>

- **[jev-eval](https://github.com/4esv/jev-eval)** — Benchmark TypeSafe Jev against any OpenRouter model on your own labelled classification data: accuracy, calibration, latency, cost
  <sub>`Benchmark` · ★1 · 4esv · `Py` · ⚠ `no licence`</sub>

- **[padflow-jev-evals](https://github.com/zsavage8/padflow-jev-evals)** — Typed-decision benchmark from PadFlow (land development SaaS): schemas, anonymized labeled rows, and a runner for confidence-calibrated models like TypeSafe Jev.
  <sub>`Benchmark` · ★1 · zsavage8 · `Py`</sub>

- **[jev-calibration-audit](https://github.com/jujumilk3/jev-calibration-audit)** — Independent API-only calibration audit of TypeSafe AI's Jev decision model
  <sub>`Benchmark` · ★0 · jujumilk3 · `Py`</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — Finite-sample guarantees for Jev (TypeSafe's System One). Conformal risk control turns calibrated probabilities into certified routing thresholds; prediction-powered inference audits them. 2,412 decisions on CLINC150 for $0.23 — including the shift and prevalence cases where the guarantee break
  <sub>`Benchmark` · ★0 · nikkoxgonzales · `Py`</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and invariant measurements of TypeSafe AI's Jev: passes six pre-registered gates on 360 labeled rows, fails four of six on graded product relevance.
  <sub>`Benchmark` · ★0 · yodablocks · `Py`</sub>

- **[jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)** — Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets
  <sub>`Benchmark` · ★0 · teyhouse · `Py` · ⚠ `no licence`</sub>

- **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)** — The best independent test found: 24 Norwegian documents on one pinned model version, opening with a case the model got wrong while correctly reporting low confidence.
  <sub>`Benchmark` · Lindfors</sub>
  <sub>Methodology is stated cleanly and scoped honestly as a single-day snapshot. Leading with a failure case is what makes it a real calibration test rather than a testimonial.</sub>

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)** — The only three-way head-to-head found, with each model's prompt tuned separately and the scope limited to one task rather than a general ranking.
  <sub>`Benchmark` · Near Here</sub>
  <sub>Self-limits correctly: a use-case study, not a model leaderboard. That restraint is rarer than the numbers.</sub>

## By decision pattern

The primary index. Each heading is a decision an agent has to make; the rows are examples of making it. Caveats appear as short tags — the full note for each row is in [`catalog.json`](catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/).

### Tool selection

_Which tool or action the agent should call next._

- **[Cookbook: Function calling](https://docs.typesafe.ai/cookbooks/function_calling)** ⭐ — Maps natural-language trading requests onto ordinary typed functions by turning function names and closed-set arguments into confidence-aware questions.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion)** ⭐ — Picks at most one skill out of 182 for an agent turn: one request ranks every skill and asks whether the turn needs one at all, a second reads the top three.
  <sub>`Official docs` · `Py` · `choice` · `noul`</sub>

- **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐ — Runnable demo code for a smart home assistant that evaluates user requests with typed decisions.
  <sub>`Official docs` · `Py`</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)** — Three independently installable Claude Code plugins — guardrails, model router and skill suggestion — each with its own hooks and tests.
  <sub>`Plugin` · ★30,899 · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)** — Compiles a tool catalogue into questions and reconstructs tool calls from the answers, with typed errors for abstention and confirmation-required cases.
  <sub>`Project` · ★30,279 · `Py` · `choice`</sub>

- **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)** — Two-stage MCP tool search: a wide Choice coarse-ranks the whole catalogue, then a shortlist gets full descriptions plus one Noul each to decide whether it does the job at all.
  <sub>`Project` · ★27,855 · `Py` · `choice` · `noul`</sub>

- **[Cua driver: jev-use example](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use)** — Computer-use action selection in Python and TypeScript: Jev picks the next browser action from an immutable candidate set, with reobserve and abstain as reserved options.
  <sub>`Project` · ★25,834 · `Py` · `TS` · `choice`</sub>

- **[json-render](https://github.com/vercel-labs/json-render)** — Vercel Labs' generative UI framework. In its Jev experiment the model does not write JSON token by token — it only picks components, props and layout.
  <sub>`Project` · ★17,994 · Vercel Labs · `TS` · `choice`</sub>

- **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)** — A high-speed browser agent from Browser Use: Jev decides the operation and which element to act on, and a small LLM is called only when text must be typed.
  <sub>`Project` · ★16,758 · Browser Use · `Py` · `choice` · ⚠ `vendor numbers`</sub>

- **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)** — Reviews each tool call on three axes — risk level, whether the user authorised it, and an explicit prompt-injection pressure check.
  <sub>`Project` · ★6,338 · `TS` · `choice` · `noul`</sub>

- **[jev-trader](https://github.com/jarrodwatts/jev-trader)** — High-frequency market making on a test network, deciding buy or sell from spread and trade direction.
  <sub>`Project` · ★1,911 · `TS` · `choice` · ⚠ `unverified`</sub>

- **[agent-desktop](https://github.com/lahfir/agent-desktop)** — Desktop automation that reads the system accessibility tree and decides which button, menu or field to act on next.
  <sub>`Project` · ★1,449 · `Rs` · `choice`</sub>

- **[typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)** — Computer use on macOS: OCR the screen, classify the next action, click. Costs a fraction of a cent per step.
  <sub>`Project` · ★775 · awlevin · `Py`</sub>

- **[tiptour-macos](https://github.com/milind-soni/tiptour-macos)** — Open-Source fast local computer use
  <sub>`Project` · ★644 · milind-soni · `Swift` · ⚠ `no licence`</sub>

- **[Jev-cu](https://github.com/Sac-Y/Jev-cu)** — A computer-use agent that asks which accessibility-tree element to act on, plus a separate noul for whether the action needs explicit user confirmation.
  <sub>`Project` · ★557 · `JS` · `choice` · `noul`</sub>

- **[foreman](https://github.com/thruwire/foreman)** — A software-factory foreman that uses Jev to decide what an agent pipeline should do next.
  <sub>`Project` · ★482 · thruwire · `Py`</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** — Nine agent skills plus a CLI covering model routing, memory filtering, turn retention, one-of-many skill selection and next-action choice.
  <sub>`Plugin` · ★408 · `Py` · `choice` · `score` · `noul`</sub>

- **[jev-browser-use](https://github.com/wy-coliney/jev-browser-use)** — Splits the loop: Jev clicks, a reasoning model thinks and verifies.
  <sub>`Project` · ★341 · wy-coliney · `JS`</sub>

- **[typesafe-mario](https://github.com/fhshaik/typesafe-mario)** — Plays Super Mario Bros. from structured emulator RAM rather than screenshots, deciding run, jump and dodge.
  <sub>`Project` · ★340 · `Py` · `choice` · `score` · `noul` · ⚠ `code untested` `one commit` `no licence`</sub>

- **[mobile-jev](https://github.com/droidrun/mobile-jev)** — Mobile computer use: Jev picks the next on-screen action on a phone.
  <sub>`Project` · ★336 · droidrun · `JS`</sub>

- **[jev-browser](https://github.com/jkudish/jev-browser)** — Browser automation where Jev chooses the next action.
  <sub>`Project` · ★235 · jkudish · `TS`</sub>

- **[quackd](https://github.com/rokbenko/quackd)** — One CLI for all your robots. Connect them, command them, and let them work together, each with an LLM for a brain, Jev for cheaper steps. Microduck, Open Duck Mini, LeRobot, XLeRobot, AlohaMini, ToddlerBot or any ROS base. Claude, OpenAI, Gemini, Grok, or local via Ollama or vLLM. Simulator, .d
  <sub>`Plugin` · ★228 · rokbenko · `Py`</sub>

- **[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)** — Voice-driven browser control where target criteria are rebuilt per request from the live element list, always including a none option.
  <sub>`Project` · ★222 · `JS` · `choice` · `score` · `noul`</sub>

- **[hyperedit](https://github.com/kevinbadi/hyperedit)** — An AI video editor routing an editing instruction to an operation, a target clip and a track, with a keyword router as fallback.
  <sub>`Project` · ★179 · `TS` · `choice` · `noul` · ⚠ `no licence`</sub>

- **[embodied-jev](https://github.com/FBddcz/embodied-jev)** — EmbodiedJev: MuJoCo robot decision workbench with MiniCPM5-2B, Jev and compatible model APIs
  <sub>`Project` · ★167 · fbddcz · `Py`</sub>

- **[jevpilot](https://github.com/standardagents/jevpilot)** — A driving simulator autopilot asking two choices per tick, which short-circuits single-option questions locally instead of paying to send them.
  <sub>`Project` · ★162 · `JS` · `choice` · ⚠ `no licence`</sub>

- **[jevrouter](https://github.com/BillionsBobby/JevRouter)** — A router for models, tools and subagents.
  <sub>`Project` · ★151 · billionsbobby · `TS`</sub>

- **[pi-jev](https://github.com/y0usaf/pi-jev)** — A decision layer for a coding agent: a measured tool-call gate plus a typed ask for calibrated answers.
  <sub>`Plugin` · ★135 · y0usaf · `TS`</sub>

- **[jev-drone](https://github.com/RomanSlack/jev-drone)** — Camera-only simulated drone where Jev makes tactical judgements at a low rate while stabilisation and safety reflexes stay in ordinary fast code.
  <sub>`Project` · ★121 · `Py` · `choice` · `score` · `noul` · ⚠ `unverified`</sub>

- **[jev-gateway](https://github.com/vinilana/jev-gateway)** — An easy way to use jev with your coding agent for tool calling reasoning
  <sub>`Project` · ★121 · vinilana · `TS`</sub>

- **[skillranker](https://github.com/Dicklesworthstone/skillranker)** — Ranks an agent's skills for the next step using live session context, with Claude Code hooks.
  <sub>`Plugin` · ★110 · dicklesworthstone · `Rs` · ⚠ `no licence`</sub>

- **[fastbrowse](https://github.com/agent-labs-dev/fastbrowse)** — A fast browser agent: Jev picks each action from what is on the page, an LLM reads and plans, and every claim in an answer cites a quote from the page.
  <sub>`Project` · ★94 · agent-labs-dev · `Py`</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)** — A chat bot that does tool calling with no language model anywhere: one request asks the request kind, the tool, and every tool's arguments at once.
  <sub>`Project` · ★86 · `TS` · `choice` · `noul`</sub>

- **[jev-dsh-decision](https://github.com/Devin-AXIS/jev-dsh-decision)** — Jev DSH 决策引擎｜面向 Agent Harness 的结构化决策插件。原生支持 DeepSeek Harness，通过 iPolloWork 支持 OpenCode、Codex Harness。
  <sub>`Plugin` · ★85 · devin-axis · `JS` · ⚠ `no licence`</sub>

- **[neo4jev](https://github.com/jexp/neo4jev)** — Puts Jev inside a knowledge graph traversal: at each node it decides which edge is most worth following.
  <sub>`Project` · ★83 · `Py` · `choice`</sub>

- **[windtunnel](https://github.com/nekuda-ai/WindTunnel)** — A WebMCP benchmark, measures WebMCP against other browser-agent interfaces.
  <sub>`Benchmark` · ★76 · nekuda-ai · `TS`</sub>

- **[jev-desktop](https://github.com/yikangy873-gif/jev-desktop)** — TypeSafe Jev action selection inside Codex Computer Use
  <sub>`Plugin` · ★60 · yikangy873-gif · `JS`</sub>

- **[jev-libero](https://github.com/Dimweaker/jev-libero)** — Fine-grained robot control with Jev, physics previews, and configurable LIBERO tasks.
  <sub>`Project` · ★52 · dimweaker · `Py`</sub>

- **[jev-reviewer](https://github.com/choxos/jev-reviewer)** — Data extraction for systematic reviews, quoted from the papers. Ask a trial report and its supplements your extraction form or a RoB 2, ROBINS-I, QUADAS-2 or TIDieR template; Jev points at the lines, every answer is a verbatim quote with its page, you check it and export the table. Files stay i
  <sub>`Project` · ★32 · choxos · `JS`</sub>

- **[robojev](https://github.com/lykycy123/RoboJEV)** — Two-stage JEV control of a Franka Panda in MuJoCo
  <sub>`Project` · ★29 · lykycy123 · `Py`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — Read-only trading journal and review harness: Jev typed judgments, agent integration, and a reproducible finance benchmark. No orders, no advice.
  <sub>`Benchmark` · ★26 · myc0576 · `Py`</sub>

- **[pi-jev-auto-mode](https://github.com/jomatsu/pi-jev-auto-mode)** — Jev (TypeSafe System One) backed auto mode for the Pi coding agent: semantically auto-approves bash, write, and edit tool calls and fails closed when a decision cannot be made.
  <sub>`Project` · ★23 · jomatsu · `TS`</sub>

- **[tsai-sc](https://github.com/phyous/tsai-sc)** — Drives a 1990s real-time strategy game through keyboard and mouse, recording the action probabilities.
  <sub>`Project` · ★22 · phyous · `Py`</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — Auto mode for every coding agent, built on Jev: risk-scores every tool call with session context (deny / ask / allow), flags prompt injection in results, checks skills and plugins. Claude Code, Codex, Copilot, Gemini, Cursor, pi, OpenCode, ACP.
  <sub>`Plugin` · ★21 · leepokai · `JS`</sub>

- **[OneVOneJev](https://github.com/emrickgarrett/OneVOneJev)** — A browser 1v1 FPS where every decision tick judges movement, view angle, aim, fire and jump.
  <sub>`Project` · ★20 · `TS` · `choice` · ⚠ `code untested` `no licence`</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)** — Open-source macOS AI computer use and native GUI automation on Apple silicon. Jev + OmniParser CoreML + Apple Vision OCR. Bring your own OpenRouter, Vercel AI Gateway, or TypesafeAI token.
  <sub>`Project` · ★19 · jcpsimmons · `JS`</sub>

- **[jevalyn](https://github.com/Ray-Hughes/jevalyn)** — The decision layer for your Rails app. A Rails-native wrapper around TypeSafe's Jev System One API: typed, calibrated decisions in your control flow.
  <sub>`Project` · ★17 · ray-hughes · `Rb`</sub>

- **[jev-for-chrome](https://github.com/chy4pro/jev-for-chrome)** — Jev for Chrome: drives the tab you are looking at with TypeSafe Jev, a sub-second decision model. Community port of browser-use/jev-ultrafast, not affiliated with TypeSafe.
  <sub>`Project` · ★16 · chy4pro · `TS`</sub>

- **[jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab)** — Multi-drone autonomy lab demonstrating TypeSafe Jev reflex decisions with optional System 2 strategy guidance.
  <sub>`Project` · ★15 · khordoo · `TS` · ⚠ `no licence`</sub>

- **[jev-use](https://github.com/shitianfang/jev-use)** — An agent plugin that hands steps needing no text output to Jev instead of the main model.
  <sub>`Plugin` · ★15 · shitianfang · `JS`</sub>

- **[live-jev](https://github.com/vinilana/live-jev)** — 2D autonomous car simulation in the browser, driven by TypeSafe's Jev decision model
  <sub>`Project` · ★15 · vinilana · `JS` · ⚠ `no licence`</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — Classify your inbox with Jev (TypeSafe's System One model) — tag, move, flag, and notify, all config-driven.
  <sub>`Project` · ★14 · parth-kp · `Py`</sub>

- **[evoke](https://github.com/evoke-build/evoke)** — Software, by reflex. A sentence becomes a call of a small program, chosen by Jev, TypeSafe AI's classifier, and run only when it is sure enough. Reflexes are recipes anyone can write, share and improve. A CLI you talk to, a package manager for reflexes from git, and a TypeScript SDK.
  <sub>`Project` · ★10 · evoke-build · `Rs`</sub>

- **[jev-askable-arm](https://github.com/TarunTomar122/jev-askable-arm)** — Zero-shot English goals on a sim Franka. Jev chains hardcoded primitives.
  <sub>`Project` · ★10 · taruntomar122 · `Py`</sub>

- **[jev-harness](https://github.com/AntonioCoppe/jev-harness)** — Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job.
  <sub>`Project` · ★9 · antoniocoppe · `TS`</sub>

- **[super-jev](https://github.com/Kevthetech143/super-jev)** — A small, extensible decision-to-action harness for TypeSafe Jev
  <sub>`Project` · ★8 · kevthetech143 · `Py`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — Observable browser stealth game: Jev makes typed guard judgments while deterministic code owns the world.
  <sub>`Project` · ★7 · abdelstark · `TS`</sub>

- **[jev-doom-agent](https://github.com/lukaske/jev-doom-agent)** — A browser-native Doom agent experiment with structured spatial state, composable AI controls, live decision telemetry, and a Chocolate Doom WebAssembly runtime.
  <sub>`Project` · ★7 · lukaske · `TS` · ⚠ `no licence`</sub>

- **[pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)** — Runtime constraints for the pi coding agent: checks every side-effecting tool call against what you said, before it runs. Powered by TypeSafe Jev.
  <sub>`Project` · ★7 · nyarlathoteppppp · `TS`</sub>

- **[jev-agent-browser](https://github.com/forvela/jev-agent-browser)** — Fast, bounded browser agents powered by Jev and agent-browser — typed actions, research, classification, and safe orchestration.
  <sub>`Project` · ★6 · forvela · `JS`</sub>

- **[bicameral](https://github.com/AbdelStark/bicameral)** — Hybrid coding harness: System 2 writes, System 1 (Jev) runs reflexes.
  <sub>`Project` · ★5 · abdelstark · `TS`</sub>

- **[slidepilot](https://github.com/harshil1712/slidepilot)** — Voice-driven semantic auto-advance for Slidev, powered by Cloudflare Agents and TypeSafe AI Jev
  <sub>`Project` · ★4 · harshil1712 · `TS`</sub>

- **[typesafe-jev](https://github.com/gtaras7/typesafe-jev)** — Screen a folder of CVs with the TypeSafe Jev decision model: typed judgments, an editable policy, free re-scoring.
  <sub>`Project` · ★4 · gtaras7 · `TS`</sub>

- **[jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study)** — Independent Jev 1.13.0 behavior study: report, controlled prompt experiments, raw results, and offline verification.
  <sub>`Project` · ★3 · rinnecoder · `Py`</sub>

- **[jev-mobile](https://github.com/Friedjof/jev-mobile)** — Fast structured Android control loops with TypeSafe Jev and Mobile MCP
  <sub>`Plugin` · ★3 · friedjof · `Py`</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies.
  <sub>`Project` · ★2 · foadsf · `Py`</sub>

- **[jev-git](https://github.com/AkashPriyadarshii/jev-git)** — Sub-second Git pre-commit & pre-push semantic reflex gate powered by TypeSafe AI Jev
  <sub>`Plugin` · ★2 · akashpriyadarshii · `Rs`</sub>

- **[jev-ra](https://github.com/brnyxx/jev-ra)** — Browser use for coding agents, 3-5x faster than browser-use. MCP server + CLI; TypeSafe Jev decides every step in ~300 ms.
  <sub>`Plugin` · ★2 · brnyxx · `Py`</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps.
  <sub>`Plugin` · ★2 · hamakyo · `TS`</sub>

- **[pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)** — A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions.
  <sub>`Plugin` · ★2 · legacybridge-tech · `TS` · ⚠ `no licence`</sub>

- **[tsai-civ2](https://github.com/phyous/tsai-civ2)** — TypeSafe Jev plays original Civilization II in a browser, with live action probabilities. Experimental full-game harness.
  <sub>`Project` · ★2 · phyous · `Py` · ⚠ `no licence`</sub>

- **[jev-browser-skill](https://github.com/zurfyx/jev-browser-skill)** — Let Jev, TypeSafe's ~100ms decision model, drive your browser. A plug-and-play skill for Claude Code and Codex.
  <sub>`Plugin` · ★1 · zurfyx · `JS`</sub>

- **[jev-engineering](https://github.com/eugeniughelbur/jev-engineering)** — The decision layer for AI agents. Typed, calibrated decisions in ~400ms for two hundredths of a cent: gate tool calls, route models, rank options. With the 300-call injection test that found what breaks.
  <sub>`Project` · ★1 · eugeniughelbur · `Py`</sub>

- **[Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py)** — Asks for an operation plus a target for each operation it might have picked, so a browser step never needs a second round trip.
  <sub>`Snippet` · `Py` · `choice` · `noul` · ⚠ `code untested`</sub>

- **[Example: tool selection with a none option](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/04-tool-selection/main.py)** — Pairs a choice over tools with a separate noul on whether a tool is needed at all, because those are different questions.
  <sub>`Snippet` · `Py` · `choice` · `noul` · ⚠ `code untested`</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — Free typed judgments for AI agents: offload classify/screen/score/verify to Jev (TypeSafe System One) via OpenCode Zen. Claude Code / ZCode skill. 给AI代理省token的免费决策分流技能
  <sub>`Plugin` · ★0 · yuyang2230 · `Py`</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — Finite-sample guarantees for Jev (TypeSafe's System One). Conformal risk control turns calibrated probabilities into certified routing thresholds; prediction-powered inference audits them. 2,412 decisions on CLINC150 for $0.23 — including the shift and prevalence cases where the guarantee break
  <sub>`Benchmark` · ★0 · nikkoxgonzales · `Py`</sub>

- **[snake-jev](https://github.com/siroccomask/snake-jev)** — Snake controlled by parallel Jev assessments, with one API call per game tick.
  <sub>`Project` · ★0 · siroccomask · `Py`</sub>

- **[Jev (Fully Tested) + Browser Use: FASTEST AI Agent I'VE TRIED YET!](https://www.youtube.com/watch?v=SNJ3yuJ_QwY)** — Wires Jev into Browser Use to drive a browser automation agent.
  <sub>`Video` · AICodeKing · ⚠ `unverified`</sub>

### Intent routing

_Classify what the user wants and send the request down the right branch._

- **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐ — Runnable demo code for a smart home assistant that evaluates user requests with typed decisions.
  <sub>`Official docs` · `Py`</sub>

- **[Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing)** ⭐ — Treat confidence as a second axis: the answer tells you what, the confidence tells you whether to act on it.
  <sub>`Official docs` · `Py`</sub>

- **[Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing)** ⭐ — Classify an incoming request and route it to the cheapest adequate handler: deterministic code, a specialist LLM, or a person.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files.
  <sub>`Project` · ★187,482 · `Py` · `choice` · `score` · `noul`</sub>

- **[Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html)** — Turns downstream task ids into a choice option set, with a minimum-confidence gate that routes uncertain runs to a human.
  <sub>`Integration` · ★46,934 · `Py` · `choice`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)** — Seven distinct email decisions, each with its own separately chosen threshold, falling back to the normal LLM on any error.
  <sub>`Project` · ★12,278 · `TS` · `choice` · `noul`</sub>

- **[Real Python: hello-jev](https://github.com/realpython/materials/tree/master/hello-jev)** — A teaching example with a deliberate control group: the same station-enquiry task written in plain Python that only accepts Y/N, next to a Noul that reads intent.
  <sub>`Tutorial` · ★5,205 · Real Python · `Py` · `noul`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — A graded course from a first call through each primitive, state shapes and criteria, to ticket triage and a multi-step workflow, mirroring all four official patterns.
  <sub>`Tutorial` · ★4,559 · `Py` · `choice` · `score` · `noul`</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** — An Android reply co-pilot that judges intent, timing and risk from on-screen text, while separate models handle OCR and drafting.
  <sub>`Project` · ★1,950 · `Java` · `choice` · `score` · `noul`</sub>

- **[foreman](https://github.com/thruwire/foreman)** — A software-factory foreman that uses Jev to decide what an agent pipeline should do next.
  <sub>`Project` · ★482 · thruwire · `Py`</sub>

- **[jev-search](https://github.com/superagents-lab/jev-search)** — Jev-driven web search: chooses the recency window and the best query rewrite, then reranks results in batches with one noul each.
  <sub>`Project` · ★390 · `TS` · `choice` · `noul`</sub>

- **[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)** — Voice-driven browser control where target criteria are rebuilt per request from the live element list, always including a none option.
  <sub>`Project` · ★222 · `JS` · `choice` · `score` · `noul`</sub>

- **[hyperedit](https://github.com/kevinbadi/hyperedit)** — An AI video editor routing an editing instruction to an operation, a target clip and a track, with a keyword router as fallback.
  <sub>`Project` · ★179 · `TS` · `choice` · `noul` · ⚠ `no licence`</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)** — A chat bot that does tool calling with no language model anywhere: one request asks the request kind, the tool, and every tool's arguments at once.
  <sub>`Project` · ★86 · `TS` · `choice` · `noul`</sub>

- **[jev-social](https://github.com/socai-io/jev-social)** — Social-platform research with typed routing and browser evidence.
  <sub>`Project` · ★46 · socai-io · `JS`</sub>

- **[ha-jev](https://github.com/AboveColin/HA-Jev)** — A Home Assistant integration: typed answers as sensors, with actions for automations.
  <sub>`Integration` · ★45 · abovecolin · `Py`</sub>

- **[hono-jev-router](https://github.com/yusukebe/hono-jev-router)** — Routes HTTP requests by meaning — a semantic router for a web framework.
  <sub>`Project` · ★45 · yusukebe · `TS`</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — Classify your inbox with Jev (TypeSafe's System One model) — tag, move, flag, and notify, all config-driven.
  <sub>`Project` · ★14 · parth-kp · `Py`</sub>

- **[jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench)** — Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark.
  <sub>`Benchmark` · ★3 · anisselbd · `Py` · ⚠ `no licence`</sub>

- **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)** — The densest independent explainer: code in JS, Python and the AI SDK, all three answer shapes, the advanced patterns, and an honest list of where the model fails.
  <sub>`Tutorial` · Flavio Copes · `JS` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Example: confidence-gated escalation](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-confidence-gate/main.py)** — Routing with an act-or-escalate gate, where the policy function is deliberately left unimplemented because the thresholds are yours to choose.
  <sub>`Snippet` · `Py` · `choice` · ⚠ `code untested`</sub>

- **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)** — Walks through use case after use case — agent routing, an in-agent decision layer, ticket triage — each with a concrete option set and a sample response.
  <sub>`Tutorial` · Mehul Gupta · `Py` · `choice` · ⚠ `paywall`</sub>

- **[Jev on Netlify AI Gateway](https://www.netlify.com/changelog/typesafe-jev-ai-gateway/)** — Zero-config access from a Netlify function: use the official SDK with no API key, base URL or provider setup, billed through Netlify credits.
  <sub>`Integration` · `TS` · `choice`</sub>

- **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)** — The LangChain integration: a classifier plus experimental middleware for model routing and for gating risky tool calls before they run.
  <sub>`Integration` · `Py` · `choice` · `score` · `noul` · ⚠ `early access`</sub>

- **[Using TypeSafe Jev with the AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk)** — The richest Vercel walkthrough: single and multi-question calls, probability-threshold routing, and unit tests with a mock evaluation model.
  <sub>`Tutorial` · `TS` · `noul` · `choice` · `score`</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — Nine worked community scenarios: intent routing, invoice classification, news filtering, product tagging, moderation, claim verification, CSV validation and more.
  <sub>`Project` · ⚠ `unverified`</sub>

### Context compaction

_Decide which tool calls and results still matter so stale context can be dropped._

- **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)** — Ported the Jev compaction approach, measured it against their shipping summariser, and published the conclusion not to adopt it.
  <sub>`Benchmark` · ★247,881 · `Py` · `noul`</sub>

- **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)** — Replaces the whole retrieval stack for memory recall — no embeddings, no BM25, no reranker — with one batched Noul per candidate memory.
  <sub>`Project` · ★19,996 · `Rs` · `noul`</sub>

- **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** — A Claude Code plugin that replaces the compaction summary with per-item decisions: stale tool calls are dropped or truncated, everything kept stays verbatim.
  <sub>`Plugin` · ★6,090 · tamaratran · `TS` · `noul`</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** — Nine agent skills plus a CLI covering model routing, memory filtering, turn retention, one-of-many skill selection and next-action choice.
  <sub>`Plugin` · ★408 · `Py` · `choice` · `score` · `noul`</sub>

- **[compact-adviser](https://github.com/kunchenguid/compact-adviser)** — "Work appears completed or recorded. Run /compact to save tokens."
  <sub>`Project` · ★174 · kunchenguid · `TS`</sub>

- **[jev-pruner](https://github.com/tamaratran/jev-pruner)** — Trims long shell output before the model sees it, asking one Noul per chunk.
  <sub>`Plugin` · ★137 · tamaratran · `TS` · `noul`</sub>

- **[Winnow](https://github.com/GhalebDweikat/winnow)** — Context garbage collection for Claude Code: when Read, Bash or Grep dump a wall of output, each chunk is judged for relevance to the current task.
  <sub>`Plugin` · ★59 · `Py` · `noul`</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy
  <sub>`Plugin` · ★22 · compozy · `TS`</sub>

- **[omp-jev-compaction](https://github.com/jerryfane/omp-jev-compaction)** — Verbatim Jev-scored context reduction for omp, over TypeSafe or OpenRouter
  <sub>`Project` · ★8 · jerryfane · `TS`</sub>

- **[pi-jev-context](https://github.com/Nyarlathoteppppp/pi-jev-context)** — Model performance first. Token savings second. A Pi extension with freshness-aware read dedupe, Jev log filtering, and searchable verbatim recall. Keeps existing message history intact.
  <sub>`Plugin` · ★6 · nyarlathoteppppp · `TS`</sub>

- **[jselect](https://github.com/keltokhy/jselect)** — Useful evidence for your AI, within a token budget. A fast, source-linked context selector for files, records, and agents.
  <sub>`Project` · ★3 · keltokhy · `Py`</sub>

### Safety gating

_Decide whether an action is safe to run. Defence in depth, never a security boundary._

- **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐ — Scores each retrieved passage, then decides in code which reach the answering model — keeping contradictory ones flagged and dropping ones carrying prompt injection.
  <sub>`Official docs` · `Py`</sub>

- **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐ — Screens every message in and out of an LLM app in one request, naming hazards and scoring how much harm complying would do.
  <sub>`Official docs` · `Py` · `noul` · `score`</sub>

- **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)** — Drops in as a moderation API by asking many parallel Noul questions in one request, one per hazard category, with an anti-injection prefix on every instruction.
  <sub>`Project` · ★42,345 · `Go` · `noul`</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)** — Three independently installable Claude Code plugins — guardrails, model router and skill suggestion — each with its own hooks and tests.
  <sub>`Plugin` · ★30,899 · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)** — The JavaScript counterpart of the LangChain integration, with the same classifier and middleware shapes.
  <sub>`Integration` · ★18,214 · `TS` · `choice` · `score` · `noul`</sub>

- **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)** — Reviews each tool call on three axes — risk level, whether the user authorised it, and an explicit prompt-injection pressure check.
  <sub>`Project` · ★6,338 · `TS` · `choice` · `noul`</sub>

- **[agentgateway: CI-validated LLM guardrail](https://github.com/agentgateway/agentgateway)** — Three Score questions on a shared severity scale, blocking the request when two or more cross the line, and failing closed.
  <sub>`Project` · ★4,971 · `Rs` · `score`</sub>

- **[Jev-cu](https://github.com/Sac-Y/Jev-cu)** — A computer-use agent that asks which accessibility-tree element to act on, plus a separate noul for whether the action needs explicit user confirmation.
  <sub>`Project` · ★557 · `JS` · `choice` · `noul`</sub>

- **[vexjoy-agent](https://github.com/notque/vexjoy-agent)** — VexJoy AI Agent with Jev Intelligent Routing - /do routes plain-English requests to the right specialist agent and gates the work with reviews, tests, and a learning loop.
  <sub>`Project` · ★423 · notque · `Py`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools.
  <sub>`Plugin` · ★253 · `JS` · `choice` · `score` · `noul`</sub>

- **[quackd](https://github.com/rokbenko/quackd)** — One CLI for all your robots. Connect them, command them, and let them work together, each with an LLM for a brain, Jev for cheaper steps. Microduck, Open Duck Mini, LeRobot, XLeRobot, AlohaMini, ToddlerBot or any ROS base. Claude, OpenAI, Gemini, Grok, or local via Ollama or vLLM. Simulator, .d
  <sub>`Plugin` · ★228 · rokbenko · `Py`</sub>

- **[pi-jev](https://github.com/y0usaf/pi-jev)** — A decision layer for a coding agent: a measured tool-call gate plus a typed ask for calibrated answers.
  <sub>`Plugin` · ★135 · y0usaf · `TS`</sub>

- **[jev-drone](https://github.com/RomanSlack/jev-drone)** — Camera-only simulated drone where Jev makes tactical judgements at a low rate while stabilisation and safety reflexes stay in ordinary fast code.
  <sub>`Project` · ★121 · `Py` · `choice` · `score` · `noul` · ⚠ `unverified`</sub>

- **[jev-gateway](https://github.com/vinilana/jev-gateway)** — An easy way to use jev with your coding agent for tool calling reasoning
  <sub>`Project` · ★121 · vinilana · `TS`</sub>

- **[youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection)** — Detect youtube sponsor segment with live audio and transcript powered by Jev
  <sub>`Project` · ★81 · trungdq88 · `JS` · ⚠ `no licence`</sub>

- **[grok-bot-jev](https://github.com/Bodila51/grok-bot-jev)** — Connect TypeSafe Jev to Grok Bot as a cheap decision layer - usage gates, skill template, examples
  <sub>`Plugin` · ★74 · bodila51 · `Py`</sub>

- **[jevals](https://github.com/openlayer-ai/jevals)** — Agent evals and guardrails as Jev decisions: one request per trace, a fraction of a cent, fast enough for the agent loop. Runs locally with Kev or Laya.
  <sub>`Project` · ★53 · openlayer-ai · `Py`</sub>

- **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)** — A Discord moderation bot: a Choice tiers each message while a Noul carries ban urgency, and an admin pardon is fed back as a safe precedent in later requests.
  <sub>`Project` · ★41 · brainstormity · `Py` · `choice` · `noul`</sub>

- **[is-malicious](https://github.com/luantak/is-malicious)** — A codebase scanner that helps you not run malicous code
  <sub>`Project` · ★22 · luantak · `TS`</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — Auto mode for every coding agent, built on Jev: risk-scores every tool call with session context (deny / ask / allow), flags prompt injection in results, checks skills and plugins. Claude Code, Codex, Copilot, Gemini, Cursor, pi, OpenCode, ACP.
  <sub>`Plugin` · ★21 · leepokai · `JS`</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)** — Open-source macOS AI computer use and native GUI automation on Apple silicon. Jev + OmniParser CoreML + Apple Vision OCR. Bring your own OpenRouter, Vercel AI Gateway, or TypesafeAI token.
  <sub>`Project` · ★19 · jcpsimmons · `JS`</sub>

- **[jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)** — Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks.
  <sub>`Benchmark` · ★17 · abdelstark · `Py`</sub>

- **[patdown](https://github.com/tyler-dot-earth/patdown)** — Block, steer, and "fuzzy lint" with Jev to make agents follow your rules and conventions. CLI, github action, pi package, and more. Built with Effect.
  <sub>`Project` · ★14 · tyler-dot-earth · `TS` · ⚠ `no licence`</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-jev)** — Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.
  <sub>`Project` · ★12 · keeltrace · `Py`</sub>

- **[pi-jev-router](https://github.com/mejiasd3v/pi-jev-router)** — Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway
  <sub>`Project` · ★12 · mejiasd3v · `JS`</sub>

- **[jev-harness](https://github.com/AntonioCoppe/jev-harness)** — Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job.
  <sub>`Project` · ★9 · antoniocoppe · `TS`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — Observable browser stealth game: Jev makes typed guard judgments while deterministic code owns the world.
  <sub>`Project` · ★7 · abdelstark · `TS`</sub>

- **[augustus](https://github.com/24601/Augustus)** — Agent skill for the decision-model class (classifiers, encoders/decoders, specialized AR heads, System One). TypeSafe Jev is the dominant exemplar. Composition algebra, question design, validation gates. MIT.
  <sub>`Plugin` · ★6 · 24601 · `Py`</sub>

- **[daf-jev](https://github.com/docxology/daf-jev)** — daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confidence gates, evaluator, calibration, CLI, MCP server, agent skill
  <sub>`Plugin` · ★5 · docxology · `Py`</sub>

- **[diffjury](https://github.com/raihankhan-rk/diffjury)** — DiffJury — TypeSafe Jev PR risk router + code review coach
  <sub>`Project` · ★5 · raihankhan-rk · `TS` · ⚠ `no licence`</sub>

- **[jev-block-android-ad](https://github.com/ufec/jev-block-android-ad)** — JevNoiseGate filters unwanted notifications and SMS on Android. Rather than matching keywords, an LLM decides what's noise — and only what it explicitly flags is blocked. Verification codes are matched on-device and never uploaded; anything uncertain passes through.
  <sub>`Project` · ★5 · ufec · `Kt`</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — Independent calibration test of TypeSafe's Jev on a task it cannot have seen: 900 rule-generated support tickets (choice / score / boolean) plus 3 public benchmarks via Vercel AI Gateway. Raw responses, ECE with noise floor, temperature refit, per-type sign of miscalibration. Reproducible for ~
  <sub>`Benchmark` · ★4 · scienthoon · `Py`</sub>

- **[jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab)** — Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows
  <sub>`Benchmark` · ★3 · jmanhype · `Py`</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — Cut Claude Code's skill manifest by ~75% with TypeSafe Jev. Scores every installed skill for relevance and hides the rest via skillOverrides — 12,750 → 3,185 tokens on a 217-skill install, for $0.0009 a session.
  <sub>`Plugin` · ★3 · shivampansuriya · `JS`</sub>

- **[jev-web-analyzer](https://github.com/replynodes/jev-web-analyzer)** — See what Jev thinks about your SaaS website — powered by ReplyNodes web context and Vercel AI Gateway.
  <sub>`Project` · ★3 · replynodes · `TS`</sub>

- **[jev-audio-beeper](https://github.com/santos-sanz/jev-audio-beeper)** — Low-latency audio censorship POC using Jev typed decisions and ffmpeg.
  <sub>`Project` · ★2 · santos-sanz · `TS` · ⚠ `no licence`</sub>

- **[jev-git](https://github.com/AkashPriyadarshii/jev-git)** — Sub-second Git pre-commit & pre-push semantic reflex gate powered by TypeSafe AI Jev
  <sub>`Plugin` · ★2 · akashpriyadarshii · `Rs`</sub>

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)** — Non-blocking Spring Boot Starter for Spring WebFlux that implements a Semantic Circuit Breaker to detect silent HTTP 200 failures using TypeSafe Jev.
  <sub>`Plugin` · ★2 · vicente-md · `Java` · ⚠ `no licence`</sub>

- **[jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)** — Jev decides whether a batch of logs is worth acting on. Typed questions, confidence gates, nothing executed.
  <sub>`Project` · ★1 · jyatesdotdev · `Py`</sub>

- **[assay-001](https://github.com/jourdanlabs/assay-001)** — ASSAY-001: independent, pre-registered verification of TypeSafe Jev's calibration and type-safety claims. Split verdict, published in full.
  <sub>`Project` · ★0 · jourdanlabs · `Py` · ⚠ `no licence`</sub>

- **[Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)** — LangChain's explainer and integration walkthrough: the three question types, plus model routing and gating risky tool calls before they run.
  <sub>`Article` · Sydney Runkle, Hunter Lovell · `Py` · ⚠ `vendor numbers`</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — Finite-sample guarantees for Jev (TypeSafe's System One). Conformal risk control turns calibrated probabilities into certified routing thresholds; prediction-powered inference audits them. 2,412 decisions on CLINC150 for $0.23 — including the shift and prevalence cases where the guarantee break
  <sub>`Benchmark` · ★0 · nikkoxgonzales · `Py`</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and invariant measurements of TypeSafe AI's Jev: passes six pre-registered gates on 360 labeled rows, fails four of six on graded product relevance.
  <sub>`Benchmark` · ★0 · yodablocks · `Py`</sub>

- **[jev-packs](https://github.com/dtduc-git/jev-packs)** — Evidence-gated registry of Jev question packs — curated questions, golden cases and measured evidence for Jev-compatible decision endpoints
  <sub>`Project` · ★0 · dtduc-git · `Py`</sub>

- **[jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)** — Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets
  <sub>`Benchmark` · ★0 · teyhouse · `Py` · ⚠ `no licence`</sub>

- **[jev-spam-eval](https://github.com/bitnovus/jev-spam-eval)** — Zero-shot spam filtering with TypeSafe Jev Noul questions, compared with TF-IDF baselines
  <sub>`Project` · ★0 · bitnovus · `Py`</sub>

- **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)** — The LangChain integration: a classifier plus experimental middleware for model routing and for gating risky tool calls before they run.
  <sub>`Integration` · `Py` · `choice` · `score` · `noul` · ⚠ `early access`</sub>

- **[openclaw-typesafe-ai](https://github.com/Olli0103/openclaw-typesafe-ai)** — Optional typed TypeSafe AI Jev decisions for OpenClaw, with SecretRef credentials and strict API validation.
  <sub>`Project` · ★0 · olli0103 · `TS`</sub>

- **[progressgate](https://github.com/AshutoshVJTI/progressgate)** — Detect semantic stagnation in AI agent loops
  <sub>`Project` · ★0 · ashutoshvjti · `TS`</sub>

- **[wakegate](https://github.com/shitianfang/wakegate)** — Ask Jev whether a sleeping agent's wakeup is worth a full LLM turn before you resume it. A fail-open wake gate for long-running agents on Workers, Durable Objects and Node.
  <sub>`Project` · ★0 · shitianfang · `TS`</sub>

### Output validation

_Check a model's output against a rubric before it reaches a user._

- **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐ — Catches wrong or invented citations against the source document with one Choice, using its confidence to flag borderline cases for review.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐ — Screens every message in and out of an LLM app in one request, naming hazards and scoring how much harm complying would do.
  <sub>`Official docs` · `Py` · `noul` · `score`</sub>

- **[vexjoy-agent](https://github.com/notque/vexjoy-agent)** — VexJoy AI Agent with Jev Intelligent Routing - /do routes plain-English requests to the right specialist agent and gates the work with reviews, tests, and a learning loop.
  <sub>`Project` · ★423 · notque · `Py`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools.
  <sub>`Plugin` · ★253 · `JS` · `choice` · `score` · `noul`</sub>

- **[jev-review](https://github.com/NiazMorshed2007/jev-review)** — A local-first MCP plugin for continuous code-quality review by coding agents.
  <sub>`Plugin` · ★198 · niazmorshed2007 · `TS`</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — Tree-sitter finds and ranks methods, then user-authored YAML rules compile into nouls, with severity read as the rubric's expected value rather than the top band.
  <sub>`Project` · ★168 · `JS` · `choice` · `score` · `noul`</sub>

- **[jev-eval-agent](https://github.com/vinilana/jev-eval-agent)** — An agent that routes evaluation work through typed decisions.
  <sub>`Project` · ★103 · vinilana · `TS` · ⚠ `no licence`</sub>

- **[formanator](https://github.com/timrogers/formanator)** — Submit Forma <https://joinforma.com> benefit claims from the command line and Model Context Protocol (MCP) clients, with support for AI-powered receipt analysis with an LLM or Jev
  <sub>`Plugin` · ★99 · timrogers · `Rs`</sub>

- **[supercov](https://github.com/supercorp-ai/supercov)** — Code quality and coverage judgements for coding agents, in Rust.
  <sub>`Project` · ★95 · supercorp-ai · `Rs`</sub>

- **[fastbrowse](https://github.com/agent-labs-dev/fastbrowse)** — A fast browser agent: Jev picks each action from what is on the page, an LLM reads and plans, and every claim in an answer cites a quote from the page.
  <sub>`Project` · ★94 · agent-labs-dev · `Py`</sub>

- **[jev-lint](https://github.com/mizchi/jev-lint)** — lint text in code by jev scorerer
  <sub>`Project` · ★70 · mizchi · `TS`</sub>

- **[jev-libero](https://github.com/Dimweaker/jev-libero)** — Fine-grained robot control with Jev, physics previews, and configurable LIBERO tasks.
  <sub>`Project` · ★52 · dimweaker · `Py`</sub>

- **[vibecheck](https://github.com/RafalWilinski/vibecheck)** — Chrome extension: vibe-check your X posts with TypeSafe's Jev before you hit Post
  <sub>`Plugin` · ★47 · rafalwilinski · `JS` · ⚠ `no licence`</sub>

- **[jev-reviewer](https://github.com/choxos/jev-reviewer)** — Data extraction for systematic reviews, quoted from the papers. Ask a trial report and its supplements your extraction form or a RoB 2, ROBINS-I, QUADAS-2 or TIDieR template; Jev points at the lines, every answer is a verbatim quote with its page, you check it and export the table. Files stay i
  <sub>`Project` · ★32 · choxos · `JS`</sub>

- **[Canny](https://github.com/qkal/Canny)** — Guards against a coding agent claiming it finished: reads tool output, the diff and test results, then judges whether the completion claim holds.
  <sub>`Project` · ★31 · `TS` · `noul` · `score`</sub>

- **[snifftest](https://github.com/DanRWilloughby/snifftest)** — A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model.
  <sub>`Project` · ★27 · danrwilloughby · `TS`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — Read-only trading journal and review harness: Jev typed judgments, agent integration, and a reproducible finance benchmark. No orders, no advice.
  <sub>`Benchmark` · ★26 · myc0576 · `Py`</sub>

- **[jev-column-race](https://github.com/goodrahstar/jev-column-race)** — Jev vs Gemini 3.8 Flash: labelling 1,000 app reviews, 4.1× faster and 7× cheaper
  <sub>`Project` · ★22 · goodrahstar · `JS`</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy
  <sub>`Plugin` · ★22 · compozy · `TS`</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — Auto mode for every coding agent, built on Jev: risk-scores every tool call with session context (deny / ask / allow), flags prompt injection in results, checks skills and plugins. Claude Code, Codex, Copilot, Gemini, Cursor, pi, OpenCode, ACP.
  <sub>`Plugin` · ★21 · leepokai · `JS`</sub>

- **[invalidate](https://github.com/chopratejas/invalidate)** — The invalidation layer for AI memory. Every fact gets a lease; new evidence ends it. Built on TypeSafe Jev.
  <sub>`Project` · ★15 · chopratejas · `Py`</sub>

- **[patdown](https://github.com/tyler-dot-earth/patdown)** — Block, steer, and "fuzzy lint" with Jev to make agents follow your rules and conventions. CLI, github action, pi package, and more. Built with Effect.
  <sub>`Project` · ★14 · tyler-dot-earth · `TS` · ⚠ `no licence`</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-jev)** — Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.
  <sub>`Project` · ★12 · keeltrace · `Py`</sub>

- **[jevlint](https://github.com/iamtoomas/JevLint)** — Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin.
  <sub>`Plugin` · ★11 · huntedman · `TS`</sub>

- **[jev-commit](https://github.com/valentynkit/jev-commit)** — A pre-commit hook: one call judges whether the commit message matches the diff.
  <sub>`Project` · ★9 · valentynkit · `Py`</sub>

- **[jev-feels](https://github.com/Qew7/jev-feels)** — Semantic decisions as ordinary Ruby — feels?, decide, score, Rails validations and pattern matching powered by Jev
  <sub>`Project` · ★8 · qew7 · `Rb`</sub>

- **[pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)** — Runtime constraints for the pi coding agent: checks every side-effecting tool call against what you said, before it runs. Powered by TypeSafe Jev.
  <sub>`Project` · ★7 · nyarlathoteppppp · `TS`</sub>

- **[augustus](https://github.com/24601/Augustus)** — Agent skill for the decision-model class (classifiers, encoders/decoders, specialized AR heads, System One). TypeSafe Jev is the dominant exemplar. Composition algebra, question design, validation gates. MIT.
  <sub>`Plugin` · ★6 · 24601 · `Py`</sub>

- **[riff](https://github.com/scale-venture-partners/riff)** — A small, fast prose linter: ruff-style rule codes for writing, backed by TypeSafe's Jev model
  <sub>`Project` · ★6 · scale-venture-partners · `Py`</sub>

- **[citation-verifier](https://github.com/MarissaFamularo/citation-verifier)** — Check whether each cited paper supports the sentence citing it. Claude proves the quote, TypeSafe's Jev scores it, a human decides.
  <sub>`Project` · ★5 · marissafamularo · `JS`</sub>

- **[diffjury](https://github.com/raihankhan-rk/diffjury)** — DiffJury — TypeSafe Jev PR risk router + code review coach
  <sub>`Project` · ★5 · raihankhan-rk · `TS` · ⚠ `no licence`</sub>

- **[jev-block-android-ad](https://github.com/ufec/jev-block-android-ad)** — JevNoiseGate filters unwanted notifications and SMS on Android. Rather than matching keywords, an LLM decides what's noise — and only what it explicitly flags is blocked. Verification codes are matched on-device and never uploaded; anything uncertain passes through.
  <sub>`Project` · ★5 · ufec · `Kt`</sub>

- **[jev-oas-sentinel](https://github.com/ShuhanSun/jev-oas-sentinel)** — Catch breaking API behavior hidden in OpenAPI prose with deterministic checks and TypeSafe JEV System One semantic review.
  <sub>`Project` · ★4 · shuhansun · `Py`</sub>

- **[jev-pref](https://github.com/doeixd/jev-pref)** — Turn your AGENTS.md preferences into a fast, Jev-powered AI linter.
  <sub>`Project` · ★4 · doeixd · `JS`</sub>

- **[jev-spec](https://github.com/nozomi-koborinai/jev-spec)** — ⚡ Catch spec drift on every commit: check your code against your Markdown specs with TypeSafe AI's Jev model.
  <sub>`Project` · ★4 · nozomi-koborinai · `TS`</sub>

- **[hermes-jev-plugin](https://github.com/ajensenwaud/hermes-jev-plugin)** — TypeSafe Jev (System One) decision tools for Hermes Agent: jev_check / jev_route / jev_score / jev_evaluate
  <sub>`Plugin` · ★3 · ajensenwaud · `Py`</sub>

- **[jev-auto-router](https://github.com/miniLV/Jev-Auto-Router)** — Jev Auto Router (Jev Router): experimental per-call GPT model routing for Codex via TypeSafe Jev and a local Responses proxy, with independent task verification.
  <sub>`Plugin` · ★3 · minilv · `TS`</sub>

- **[jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study)** — Independent Jev 1.13.0 behavior study: report, controlled prompt experiments, raw results, and offline verification.
  <sub>`Project` · ★3 · rinnecoder · `Py`</sub>

- **[jevkit](https://github.com/ariel-frischer/jevkit)** — Fast Rust CLI for TypeSafe Jev: typed decisions, offline linting before you pay
  <sub>`Project` · ★3 · ariel-frischer · `Rs`</sub>

- **[jod](https://github.com/mateonunez/jod)** — Semantic schemas over TypeSafe's Jev — validate the state locally, then project typed answers.
  <sub>`Project` · ★3 · mateonunez · `TS`</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies.
  <sub>`Project` · ★2 · foadsf · `Py`</sub>

- **[jev-scout](https://github.com/AkashPriyadarshii/jev-scout)** — Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring
  <sub>`Project` · ★2 · akashpriyadarshii · `Rs`</sub>

- **[limpet](https://github.com/noplan-inc/limpet)** — A Stop hook that stops your coding agent from stopping too early. Plain-language rules, judged by jev.
  <sub>`Plugin` · ★2 · noplan-inc · `Py`</sub>

- **[tripwire](https://github.com/noelzappy/tripwire)** — Judge every LLM response before the user sees it. AI SDK middleware and OpenAI-compatible proxy.
  <sub>`Integration` · ★2 · noelzappy · `TS`</sub>

- **[jev-review-action](https://github.com/fatwang2/jev-review-action)** — Configurable GitHub submission review and PR classification with TypeSafe Jev. No text-generation model.
  <sub>`Project` · ★1 · fatwang2 · `JS`</sub>

- **[assay-001](https://github.com/jourdanlabs/assay-001)** — ASSAY-001: independent, pre-registered verification of TypeSafe Jev's calibration and type-safety claims. Split verdict, published in full.
  <sub>`Project` · ★0 · jourdanlabs · `Py` · ⚠ `no licence`</sub>

- **[human-compiler](https://github.com/asfarsadewa/human-compiler)** — A compiler for human language. Paste text, get diagnostics. Measured by TypeSafe Jev.
  <sub>`Project` · ★0 · asfarsadewa · `TS`</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — Free typed judgments for AI agents: offload classify/screen/score/verify to Jev (TypeSafe System One) via OpenCode Zen. Claude Code / ZCode skill. 给AI代理省token的免费决策分流技能
  <sub>`Plugin` · ★0 · yuyang2230 · `Py`</sub>

- **[openclaw-typesafe-ai](https://github.com/Olli0103/openclaw-typesafe-ai)** — Optional typed TypeSafe AI Jev decisions for OpenClaw, with SecretRef credentials and strict API validation.
  <sub>`Project` · ★0 · olli0103 · `TS`</sub>

- **[plotveil](https://github.com/Dearest/plotveil)** — A quiet spoiler blocker for YouTube comments. One typed Jev (TypeSafe System One) Noul decision per comment; covered while checked, still covered if the check fails.
  <sub>`Project` · ★0 · dearest · `TS`</sub>

- **[pytest-jev](https://github.com/allebee/pytest-jev)** — Semantic assertions for pytest: test what your LLM app's output means, judged by TypeSafe's Jev.
  <sub>`Plugin` · ★0 · allebee · `Py`</sub>

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)** — The only three-way head-to-head found, with each model's prompt tuned separately and the scope limited to one task rather than a general ranking.
  <sub>`Benchmark` · Near Here</sub>

- **[TypeSafe's Jev: Can decision models replace LLM judges?](https://arize.com/blog/typesafe-jev-llm-judge/)** — Collects the third-party evaluations that exist so far and frames the question of where a decision model can stand in for an LLM judge.
  <sub>`Article` · Laurie Voss</sub>

### Retry control

_Decide whether a failed step is worth retrying._

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)** — Non-blocking Spring Boot Starter for Spring WebFlux that implements a Semantic Circuit Breaker to detect silent HTTP 200 failures using TypeSafe Jev.
  <sub>`Plugin` · ★2 · vicente-md · `Java` · ⚠ `no licence`</sub>

### Human escalation

_Use calibrated confidence to decide what a person must see._

- **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐ — Classifies annual reports into 75 industry groups, then reads the answer's own confidence to decide whether to report that group or the broader division above it.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐ — Catches wrong or invented citations against the source document with one Choice, using its confidence to flag borderline cases for review.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐ — Decides which of 450 candidate pairs from two product catalogues describe the same thing, with one Score whose three levels are the three available actions.
  <sub>`Official docs` · `Py` · `score`</sub>

- **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐ — Adds an explicit "uncertain" outcome to moderation decisions and measures label agreement against the share of actions taken automatically.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Self-consistency with nouls](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook)** ⭐ — Routes uncertain probabilities to human review while keeping the underlying noul values visible rather than collapsing them to a label.
  <sub>`Official docs` · `Py` · `noul`</sub>

- **[Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing)** ⭐ — Treat confidence as a second axis: the answer tells you what, the confidence tells you whether to act on it.
  <sub>`Official docs` · `Py`</sub>

- **[Confidence](https://docs.typesafe.ai/confidence)** ⭐ — How confidence is derived from the probability distribution, and why a threshold tuned on one question type does not transfer to another.
  <sub>`Official docs`</sub>

- **[Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html)** — Turns downstream task ids into a choice option set, with a minimum-confidence gate that routes uncertain runs to a human.
  <sub>`Integration` · ★46,934 · `Py` · `choice`</sub>

- **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)** — Compiles a tool catalogue into questions and reconstructs tool calls from the answers, with typed errors for abstention and confirmation-required cases.
  <sub>`Project` · ★30,279 · `Py` · `choice`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)** — Seven distinct email decisions, each with its own separately chosen threshold, falling back to the normal LLM on any error.
  <sub>`Project` · ★12,278 · `TS` · `choice` · `noul`</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)** — Pre-screens code review with Jev to surface high-risk changes for a more expensive model or a person, with a local dashboard.
  <sub>`Project` · ★510 · `TS` · `choice` · `score` · `noul`</sub>

- **[jev-align](https://github.com/sutro-sh/jev-align)** — Builds calibrated decision functions from human feedback.
  <sub>`Project` · ★271 · sutro-sh · `Py`</sub>

- **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)** — Independent Korean-language notes reporting that reversing the order of options shifted a probability enough to flip a 0.9 threshold.
  <sub>`Benchmark` · ★190 · `Py` · ⚠ `no licence` `unverified`</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — One TypeScript interface for 40 AI providers across three inference types — generate, stream, and decide. Decide returns typed, calibrated judgments (boolean/choice/score) via TypeSafe Jev, not text. MCP-native, voice (TTS/STT/realtime), RAG, memory, file processors. Powers Tara, Yama and Clair
  <sub>`Plugin` · ★137 · juspay · `TS`</sub>

- **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)** — A Discord moderation bot: a Choice tiers each message while a Noul carries ban urgency, and an admin pardon is fed back as a safe precedent in later requests.
  <sub>`Project` · ★41 · brainstormity · `Py` · `choice` · `noul`</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — Calibrate Jev questions against your own labels: tune criteria on labelled examples, confirm on a held-out set, get a verdict per question. Unofficial.
  <sub>`Project` · ★31 · smkrv · `TS`</sub>

- **[jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)** — Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks.
  <sub>`Benchmark` · ★17 · abdelstark · `Py`</sub>

- **[jevalyn](https://github.com/Ray-Hughes/jevalyn)** — The decision layer for your Rails app. A Rails-native wrapper around TypeSafe's Jev System One API: typed, calibrated decisions in your control flow.
  <sub>`Project` · ★17 · ray-hughes · `Rb`</sub>

- **[jevwire](https://github.com/Brainwires/jevwire)** — Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code plugin (TypeSafe AI's Jev)
  <sub>`Plugin` · ★15 · brainwires · `TS`</sub>

- **[jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router)** — Typed, confidence-aware agent skill routing with TypeSafe Jev.
  <sub>`Plugin` · ★13 · godsboy · `Py`</sub>

- **[jev-forge](https://github.com/zwliJay/jev-forge)** — An open training and inference stack for Jev-style decision models. Train models to score dynamic candidate branches from a shared prefix, with support for high-cardinality choice, calibration, and fast batched inference.
  <sub>`Jev-like alternative` · ★11 · zwlijay · `Py` · ⚠ `not Jev` `no licence`</sub>

- **[jevcal](https://github.com/abhixhek/jevcal)** — Calibrate, threshold and drift-check a decision model against an LLM teacher instead of guessing a cutoff.
  <sub>`Project` · ★10 · abhixhek · `Py`</sub>

- **[jev-harness](https://github.com/AntonioCoppe/jev-harness)** — Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job.
  <sub>`Project` · ★9 · antoniocoppe · `TS`</sub>

- **[daf-jev](https://github.com/docxology/daf-jev)** — daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confidence gates, evaluator, calibration, CLI, MCP server, agent skill
  <sub>`Plugin` · ★5 · docxology · `Py`</sub>

- **[jev-block-android-ad](https://github.com/ufec/jev-block-android-ad)** — JevNoiseGate filters unwanted notifications and SMS on Android. Rather than matching keywords, an LLM decides what's noise — and only what it explicitly flags is blocked. Verification codes are matched on-device and never uploaded; anything uncertain passes through.
  <sub>`Project` · ★5 · ufec · `Kt`</sub>

- **[poorjev](https://github.com/rupeshpoojary9/poorjev)** — Open-source, local Jev alternative: a System One decision layer with provably calibrated confidence (ECE 0.170→0.071). Typed decisions, runs offline, no API key, no waitlist.
  <sub>`Jev-like alternative` · ★5 · rupeshpoojary9 · `Py` · ⚠ `not Jev`</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — Independent calibration test of TypeSafe's Jev on a task it cannot have seen: 900 rule-generated support tickets (choice / score / boolean) plus 3 public benchmarks via Vercel AI Gateway. Raw responses, ECE with noise floor, temperature refit, per-type sign of miscalibration. Reproducible for ~
  <sub>`Benchmark` · ★4 · scienthoon · `Py`</sub>

- **[qwen-rlcd](https://github.com/shamazharikh/qwen-rlcd)** — Jev-style calibrated decision model (Choice/Score/Noul) on Qwen3.5-0.8B
  <sub>`Jev-like alternative` · ★4 · shamazharikh · `Py` · ⚠ `not Jev` `no licence`</sub>

- **[jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab)** — Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows
  <sub>`Benchmark` · ★3 · jmanhype · `Py`</sub>

- **[jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench)** — Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark.
  <sub>`Benchmark` · ★3 · anisselbd · `Py` · ⚠ `no licence`</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps.
  <sub>`Plugin` · ★2 · hamakyo · `TS`</sub>

- **[pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)** — A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions.
  <sub>`Plugin` · ★2 · legacybridge-tech · `TS` · ⚠ `no licence`</sub>

- **[jev-eval](https://github.com/4esv/jev-eval)** — Benchmark TypeSafe Jev against any OpenRouter model on your own labelled classification data: accuracy, calibration, latency, cost
  <sub>`Benchmark` · ★1 · 4esv · `Py` · ⚠ `no licence`</sub>

- **[jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)** — Jev decides whether a batch of logs is worth acting on. Typed questions, confidence gates, nothing executed.
  <sub>`Project` · ★1 · jyatesdotdev · `Py`</sub>

- **[padflow-jev-evals](https://github.com/zsavage8/padflow-jev-evals)** — Typed-decision benchmark from PadFlow (land development SaaS): schemas, anonymized labeled rows, and a runner for confidence-calibrated models like TypeSafe Jev.
  <sub>`Benchmark` · ★1 · zsavage8 · `Py`</sub>

- **[assay-001](https://github.com/jourdanlabs/assay-001)** — ASSAY-001: independent, pre-registered verification of TypeSafe Jev's calibration and type-safety claims. Split verdict, published in full.
  <sub>`Project` · ★0 · jourdanlabs · `Py` · ⚠ `no licence`</sub>

- **[Example: confidence-gated escalation](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-confidence-gate/main.py)** — Routing with an act-or-escalate gate, where the policy function is deliberately left unimplemented because the thresholds are yours to choose.
  <sub>`Snippet` · `Py` · `choice` · ⚠ `code untested`</sub>

- **[jev-calibration-audit](https://github.com/jujumilk3/jev-calibration-audit)** — Independent API-only calibration audit of TypeSafe AI's Jev decision model
  <sub>`Benchmark` · ★0 · jujumilk3 · `Py`</sub>

- **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)** — The best independent test found: 24 Norwegian documents on one pinned model version, opening with a case the model got wrong while correctly reporting low confidence.
  <sub>`Benchmark` · Lindfors</sub>

### Model routing

_Pick which downstream model or tier should handle a request._

- **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐ — A two-stage mini-then-verify-then-reasoning cascade that reaches most of a big reasoning model's quality at a fraction of the cost.
  <sub>`Official docs` · `Py`</sub>

- **[Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing)** ⭐ — Classify an incoming request and route it to the cheapest adequate handler: deterministic code, a specialist LLM, or a person.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)** — Three independently installable Claude Code plugins — guardrails, model router and skill suggestion — each with its own hooks and tests.
  <sub>`Plugin` · ★30,899 · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)** — The JavaScript counterpart of the LangChain integration, with the same classifier and middleware shapes.
  <sub>`Integration` · ★18,214 · `TS` · `choice` · `score` · `noul`</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)** — Pre-screens code review with Jev to surface high-risk changes for a more expensive model or a person, with a local dashboard.
  <sub>`Project` · ★510 · `TS` · `choice` · `score` · `noul`</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** — Nine agent skills plus a CLI covering model routing, memory filtering, turn retention, one-of-many skill selection and next-action choice.
  <sub>`Plugin` · ★408 · `Py` · `choice` · `score` · `noul`</sub>

- **[jev-codex-router](https://github.com/0xNatoshi/jev-codex-router)** — Judges how hard a coding turn is, then picks the model tier, reasoning depth and speed mode to match.
  <sub>`Plugin` · ★188 · `JS` · `choice` · `score`</sub>

- **[jevrouter](https://github.com/BillionsBobby/JevRouter)** — A router for models, tools and subagents.
  <sub>`Project` · ★151 · billionsbobby · `TS`</sub>

- **[jev-eval-agent](https://github.com/vinilana/jev-eval-agent)** — An agent that routes evaluation work through typed decisions.
  <sub>`Project` · ★103 · vinilana · `TS` · ⚠ `no licence`</sub>

- **[jev-use](https://github.com/shitianfang/jev-use)** — An agent plugin that hands steps needing no text output to Jev instead of the main model.
  <sub>`Plugin` · ★15 · shitianfang · `JS`</sub>

- **[pi-jev-router](https://github.com/mejiasd3v/pi-jev-router)** — Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway
  <sub>`Project` · ★12 · mejiasd3v · `JS`</sub>

- **[jev-router](https://github.com/prismhq/jev-router)** — Open-source LLM router that uses TypeSafe's Jev to pick a model, on top of LiteLLM
  <sub>`Project` · ★7 · prismhq · `Py`</sub>

- **[jev-auto-router](https://github.com/miniLV/Jev-Auto-Router)** — Jev Auto Router (Jev Router): experimental per-call GPT model routing for Codex via TypeSafe Jev and a local Responses proxy, with independent task verification.
  <sub>`Plugin` · ★3 · minilv · `TS`</sub>

- **[tiershift](https://github.com/iamvatsalpatel/tiershift)** — Shift every LLM call to the cheapest model that can handle it. Routing decided by TypeSafe Jev in ~180 ms. No training data. Policy in plain YAML. TypeScript and Python.
  <sub>`Project` · ★3 · iamvatsalpatel · `TS`</sub>

- **[janus](https://github.com/FirasSX914/Janus)** — Measure when to use Jev and other models on your data, then route accordingly.
  <sub>`Project` · ★2 · firassx914 · `Py`</sub>

- **[jev-engineering](https://github.com/eugeniughelbur/jev-engineering)** — The decision layer for AI agents. Typed, calibrated decisions in ~400ms for two hundredths of a cent: gate tool calls, route models, rank options. With the 300-call injection test that found what breaks.
  <sub>`Project` · ★1 · eugeniughelbur · `Py`</sub>

- **[Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)** — LangChain's explainer and integration walkthrough: the three question types, plus model routing and gating risky tool calls before they run.
  <sub>`Article` · Sydney Runkle, Hunter Lovell · `Py` · ⚠ `vendor numbers`</sub>

- **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)** — Walks through use case after use case — agent routing, an in-agent decision layer, ticket triage — each with a concrete option set and a sample response.
  <sub>`Tutorial` · Mehul Gupta · `Py` · `choice` · ⚠ `paywall`</sub>

- **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)** — The LangChain integration: a classifier plus experimental middleware for model routing and for gating risky tool calls before they run.
  <sub>`Integration` · `Py` · `choice` · `score` · `noul` · ⚠ `early access`</sub>

### Speculative fan-out

_Pack many questions — including speculative ones — into one request and let code pick what mattered._

- **[Cookbook: Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions)** ⭐ — A 13-question regulatory briefing over one long article, showing that batching every question into one call is far cheaper and faster with no change in answers.
  <sub>`Official docs` · `Py`</sub>

- **[Pattern: Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out)** ⭐ — Pack many questions, including ones you may not need, into a single request and let your code decide afterwards what was relevant.
  <sub>`Official docs` · `Py`</sub>

- **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐ — The canonical first call: one support ticket, one Choice, one Score and one Noul in a single request, in Python, JS and cURL.
  <sub>`Official docs` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files.
  <sub>`Project` · ★187,482 · `Py` · `choice` · `score` · `noul`</sub>

- **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)** — Drops in as a moderation API by asking many parallel Noul questions in one request, one per hazard category, with an anti-injection prefix on every instruction.
  <sub>`Project` · ★42,345 · `Go` · `noul`</sub>

- **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)** — A high-speed browser agent from Browser Use: Jev decides the operation and which element to act on, and a small LLM is called only when text must be typed.
  <sub>`Project` · ★16,758 · Browser Use · `Py` · `choice` · ⚠ `vendor numbers`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — A graded course from a first call through each primitive, state shapes and criteria, to ticket triage and a multi-step workflow, mirroring all four official patterns.
  <sub>`Tutorial` · ★4,559 · `Py` · `choice` · `score` · `noul`</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)** — A chat bot that does tool calling with no language model anywhere: one request asks the request kind, the tool, and every tool's arguments at once.
  <sub>`Project` · ★86 · `TS` · `choice` · `noul`</sub>

- **[jev-sift](https://github.com/kbhuw/jev-sift)** — Classify first. Read selectively. A portable agent plugin and MCP tool for batch text classification.
  <sub>`Plugin` · ★45 · kbhuw · `JS` · ⚠ `no licence`</sub>

- **[pi-typesafe](https://github.com/DevMortimer/pi-typesafe)** — TypeSafe decisions for Pi: batched evaluation tool, terminal playground, and typed API for extension authors
  <sub>`Plugin` · ★40 · devmortimer · `TS`</sub>

- **[OneVOneJev](https://github.com/emrickgarrett/OneVOneJev)** — A browser 1v1 FPS where every decision tick judges movement, view angle, aim, fire and jump.
  <sub>`Project` · ★20 · `TS` · `choice` · ⚠ `code untested` `no licence`</sub>

- **[slop-grader](https://github.com/lukstei/slop-grader)** — Jev-powered, rule-based grader for text files. Runs every rule against every line in parallel. No skimming, no missed lines.
  <sub>`Project` · ★13 · lukstei · `TS`</sub>

- **[jev-forge](https://github.com/zwliJay/jev-forge)** — An open training and inference stack for Jev-style decision models. Train models to score dynamic candidate branches from a shared prefix, with support for high-cardinality choice, calibration, and fast batched inference.
  <sub>`Jev-like alternative` · ★11 · zwlijay · `Py` · ⚠ `not Jev` `no licence`</sub>

- **[duckdb-jev](https://github.com/prasanthj/duckdb-jev)** — High-throughput, robust native DuckDB extension for batched and streaming TypeSafe/Jev classification, scoring, and semantic predicates from SQL.
  <sub>`Plugin` · ★3 · prasanthj · `C++`</sub>

- **[jev-tree](https://github.com/reachjalil/jev-tree)** — Recursive Jev choice over a taxonomy. Select from more than 255 options without breaking TypeSafe Jev's choice cap.
  <sub>`Project` · ★3 · reachjalil · `TS`</sub>

- **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)** — The densest independent explainer: code in JS, Python and the AI SDK, all three answer shapes, the advanced patterns, and an honest list of where the model fails.
  <sub>`Tutorial` · Flavio Copes · `JS` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py)** — Asks for an operation plus a target for each operation it might have picked, so a browser step never needs a second round trip.
  <sub>`Snippet` · `Py` · `choice` · `noul` · ⚠ `code untested`</sub>

- **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)** — A minimal first call asking a choice, a score and a noul together, annotated with the asymmetries that catch people out.
  <sub>`Snippet` · `Py` · `choice` · `score` · `noul` · ⚠ `code untested`</sub>

- **[Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/)** — Workers AI binding and REST samples asking a noul, a choice and a score in one call, with the full response including per-answer confidence.
  <sub>`Integration` · `TS` · `sh` · `noul` · `choice` · `score`</sub>

- **[snake-jev](https://github.com/siroccomask/snake-jev)** — Snake controlled by parallel Jev assessments, with one API call per game tick.
  <sub>`Project` · ★0 · siroccomask · `Py`</sub>

- **[Using TypeSafe Jev with the AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk)** — The richest Vercel walkthrough: single and multi-question calls, probability-threshold routing, and unit tests with a mock evaluation model.
  <sub>`Tutorial` · `TS` · `noul` · `choice` · `score`</sub>

### Search & ranking

_Score or re-rank candidates from a cheaper retrieval step._

- **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐ — Scores each retrieved passage, then decides in code which reach the answering model — keeping contradictory ones flagged and dropping ones carrying prompt injection.
  <sub>`Official docs` · `Py`</sub>

- **[Cookbook: Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find)** ⭐ — Semantic search over a terms-of-service document: one request scores 218 line ids with a Choice, and a Noul checks whether the document answers at all.
  <sub>`Official docs` · `Py` · `choice` · `noul`</sub>

- **[Cookbook: Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe)** ⭐ — Re-ranks 30-passage BM25 shortlists for 40 legal queries with one question per query-candidate pair, reporting large top-1 and top-10 gains.
  <sub>`Official docs` · `Py`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files.
  <sub>`Project` · ★187,482 · `Py` · `choice` · `score` · `noul`</sub>

- **[OpenViking: retrieval reranking](https://github.com/volcengine/OpenViking)** — One Noul per candidate document in a single batched request, with the yes-probability used directly as the relevance score.
  <sub>`Project` · ★38,384 · `Py` · `noul`</sub>

- **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)** — Two-stage MCP tool search: a wide Choice coarse-ranks the whole catalogue, then a shortlist gets full descriptions plus one Noul each to decide whether it does the job at all.
  <sub>`Project` · ★27,855 · `Py` · `choice` · `noul`</sub>

- **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)** — Replaces the whole retrieval stack for memory recall — no embeddings, no BM25, no reranker — with one batched Noul per candidate memory.
  <sub>`Project` · ★19,996 · `Rs` · `noul`</sub>

- **[LanceDB TypeSafeReranker](https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py)** — A vector-database reranker that asks one Noul per result and uses the yes-probability as an absolute relevance score, comparable across queries.
  <sub>`Project` · ★11,496 · `Py` · `noul`</sub>

- **[no-mistakes: review context selection](https://github.com/kunchenguid/no-mistakes)** — One Score per candidate file to pick review context, with a measured outcome: materially more billed input for essentially no wall-clock gain.
  <sub>`Benchmark` · ★8,598 · `Go` · `score`</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** — An Android reply co-pilot that judges intent, timing and risk from on-screen text, while separate models handle OCR and drafting.
  <sub>`Project` · ★1,950 · `Java` · `choice` · `score` · `noul`</sub>

- **[hippo-memory](https://github.com/kitfunso/hippo-memory)** — Biologically-inspired memory for AI agents. Decay, retrieval strengthening, consolidation. Zero runtime deps, SQLite, MCP. Benchmarked retrieval with an opt-in TypeSafe Jev reranker.
  <sub>`Benchmark` · ★752 · kitfunso · `TS`</sub>

- **[jev-search](https://github.com/superagents-lab/jev-search)** — Jev-driven web search: chooses the recency window and the best query rewrite, then reranks results in batches with one noul each.
  <sub>`Project` · ★390 · `TS` · `choice` · `noul`</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — A real PostgreSQL extension exposing the primitives as SQL functions, so a semantic decision can appear in a WHERE clause over any row type.
  <sub>`Project` · ★291 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools.
  <sub>`Plugin` · ★253 · `JS` · `choice` · `score` · `noul`</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — One TypeScript interface for 40 AI providers across three inference types — generate, stream, and decide. Decide returns typed, calibrated judgments (boolean/choice/score) via TypeSafe Jev, not text. MCP-native, voice (TTS/STT/realtime), RAG, memory, file processors. Powers Tara, Yama and Clair
  <sub>`Plugin` · ★137 · juspay · `TS`</sub>

- **[jev-semgrep](https://github.com/uehaj/jev-semgrep)** — grep by meaning, across languages. TypeSafe Jev scores every line against a meaning; combine meanings with AND/OR/NOT. 意味で探す grep。日本語で英語を、英語で日本語を検索できる
  <sub>`Project` · ★125 · uehaj · `JS` · ⚠ `no licence`</sub>

- **[skillranker](https://github.com/Dicklesworthstone/skillranker)** — Ranks an agent's skills for the next step using live session context, with Claude Code hooks.
  <sub>`Plugin` · ★110 · dicklesworthstone · `Rs` · ⚠ `no licence`</sub>

- **[jev-shell-history](https://github.com/mrnugget/jev-shell-history)** — Fish-style zsh history autosuggestions, ranked by Jev rather than by recency.
  <sub>`Project` · ★96 · mrnugget · `TS` · ⚠ `no licence`</sub>

- **[neo4jev](https://github.com/jexp/neo4jev)** — Puts Jev inside a knowledge graph traversal: at each node it decides which edge is most worth following.
  <sub>`Project` · ★83 · `Py` · `choice`</sub>

- **[jegrep](https://github.com/can1357/jegrep)** — Semantic grep: find code by describing what you're looking for, powered by Jev.
  <sub>`Project` · ★76 · can1357 · `Rs`</sub>

- **[Blink](https://github.com/ellipsis-dev/blink)** — Uses Jev as a codebase navigator: at each directory level it decides which files are most relevant to the question, then descends.
  <sub>`Project` · ★56 · `TS` · `choice` · ⚠ `no licence`</sub>

- **[jev-social](https://github.com/socai-io/jev-social)** — Social-platform research with typed routing and browser evidence.
  <sub>`Project` · ★46 · socai-io · `JS`</sub>

- **[jgrep](https://github.com/keltokhy/jgrep)** — grep, but the pattern is a description. Filters lines by meaning with TypeSafe's Jev decision model: ~200 ms and a thousandth of a cent per line.
  <sub>`Project` · ★17 · keltokhy · `Py`</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-jev)** — Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.
  <sub>`Project` · ★12 · keeltrace · `Py`</sub>

- **[jevql](https://github.com/kylemclaren/jevql)** — Semantic SQL for Postgres, powered by Jev
  <sub>`Project` · ★11 · kylemclaren · `Go`</sub>

- **[every](https://github.com/sufianetaouil/every)** — Ask a yes/no question of every function in a codebase. Ranked answers in seconds, for cents. Grep whose pattern is a question, powered by TypeSafe Jev.
  <sub>`Project` · ★5 · sufianetaouil · `Py`</sub>

- **[jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench)** — An independent head-to-head against dedicated rerankers across fourteen datasets.
  <sub>`Benchmark` · ★5 · anessbelbati · `Py`</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — Cut Claude Code's skill manifest by ~75% with TypeSafe Jev. Scores every installed skill for relevance and hides the rest via skillOverrides — 12,750 → 3,185 tokens on a 217-skill install, for $0.0009 a session.
  <sub>`Plugin` · ★3 · shivampansuriya · `JS`</sub>

- **[llama-index-jev](https://github.com/WiktorB2004/llama-index-jev)** — LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge.
  <sub>`Project` · ★3 · wiktorb2004 · `Py`</sub>

- **[jev-reranker](https://github.com/shinpr/jev-reranker)** — Rerank, filter, and compress JSON search results with TypeSafe AI's Jev.
  <sub>`Project` · ★2 · shinpr · `Rs`</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps.
  <sub>`Plugin` · ★2 · hamakyo · `TS`</sub>

- **[jev-engineering](https://github.com/eugeniughelbur/jev-engineering)** — The decision layer for AI agents. Typed, calibrated decisions in ~400ms for two hundredths of a cent: gate tool calls, route models, rank options. With the 300-call injection test that found what breaks.
  <sub>`Project` · ★1 · eugeniughelbur · `Py`</sub>

- **[jev-bfs](https://github.com/komikat/jev-bfs)** — Wikipedia link races with direct Jev ranking and a live terminal display.
  <sub>`Project` · ★0 · komikat · `Py`</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and invariant measurements of TypeSafe AI's Jev: passes six pre-registered gates on 360 labeled rows, fails four of six on graded product relevance.
  <sub>`Benchmark` · ★0 · yodablocks · `Py`</sub>

- **[jevgrep](https://github.com/allebee/jevgrep)** — grep by meaning: pipe in any text, ask a yes/no question in plain English, get only the matching lines. Works behind tail -f, about $0.004 per 1,000 lines, powered by TypeSafe's Jev.
  <sub>`Project` · ★0 · allebee · `Py`</sub>

### Structured extraction

_Pull typed fields out of messy text by choosing among candidates rather than generating them._

- **[Cookbook: Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook)** ⭐ — Extracts absolute and relative dates by asking for the parts a document names, then resolving and validating them in code with confidence-based review.
  <sub>`Official docs` · `Py`</sub>

- **[Cookbook: Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook)** ⭐ — Regexes find candidate emails, phone numbers and amounts; the model selects the requested span so code can normalise a verbatim value.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐ — Reconstructs Markdown from plain text that lost its formatting, in two requests: one restitches hard-wrapped lines, one classifies every block.
  <sub>`Official docs` · `Py`</sub>

- **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐ — A two-stage mini-then-verify-then-reasoning cascade that reaches most of a big reasoning model's quality at a fraction of the cost.
  <sub>`Official docs` · `Py`</sub>

- **[jev-reviewer](https://github.com/choxos/jev-reviewer)** — Data extraction for systematic reviews, quoted from the papers. Ask a trial report and its supplements your extraction form or a RoB 2, ROBINS-I, QUADAS-2 or TIDieR template; Jev points at the lines, every answer is a verbatim quote with its page, you check it and export the table. Files stay i
  <sub>`Project` · ★32 · choxos · `JS`</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)** — Open-source macOS AI computer use and native GUI automation on Apple silicon. Jev + OmniParser CoreML + Apple Vision OCR. Bring your own OpenRouter, Vercel AI Gateway, or TypesafeAI token.
  <sub>`Project` · ★19 · jcpsimmons · `JS`</sub>

### Classification

_Put an item into a taxonomy, including deep hierarchies walked with probabilities._

- **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐ — Classifies annual reports into 75 industry groups, then reads the answer's own confidence to decide whether to report that group or the broader division above it.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification)** ⭐ — Walks deep patent, retail, biomedical and source-code taxonomies with a parallel beam search over Choice probabilities.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐ — Decides which of 450 candidate pairs from two product catalogues describe the same thing, with one Score whose three levels are the three available actions.
  <sub>`Official docs` · `Py` · `score`</sub>

- **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐ — Reconstructs Markdown from plain text that lost its formatting, in two requests: one restitches hard-wrapped lines, one classifies every block.
  <sub>`Official docs` · `Py`</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)** — Two Choice questions over threat level and category, held in shadow mode after a blind evaluation found Jev merely tied the incumbent model.
  <sub>`Benchmark` · ★87,191 · `TS` · `choice` · ⚠ `shadow mode`</sub>

- **[json-render](https://github.com/vercel-labs/json-render)** — Vercel Labs' generative UI framework. In its Jev experiment the model does not write JSON token by token — it only picks components, props and layout.
  <sub>`Project` · ★17,994 · Vercel Labs · `TS` · `choice`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)** — Seven distinct email decisions, each with its own separately chosen threshold, falling back to the normal LLM on any error.
  <sub>`Project` · ★12,278 · `TS` · `choice` · `noul`</sub>

- **[tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier)** — Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per page.
  <sub>`Project` · ★361 · kyotofin · `TS`</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — A real PostgreSQL extension exposing the primitives as SQL functions, so a semantic decision can appear in a WHERE clause over any row type.
  <sub>`Project` · ★291 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools.
  <sub>`Plugin` · ★253 · `JS` · `choice` · `score` · `noul`</sub>

- **[docjev](https://github.com/jerryjliu/docjev)** — A very fast document classifier/splitter using Jev
  <sub>`Project` · ★207 · jerryjliu · `Py`</sub>

- **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)** — Independent Korean-language notes reporting that reversing the order of options shifted a probability enough to flip a 0.9 threshold.
  <sub>`Benchmark` · ★190 · `Py` · ⚠ `no licence` `unverified`</sub>

- **[unclutter](https://github.com/kitze/unclutter)** — A browser extension that removes page clutter, with reusable template rules.
  <sub>`Project` · ★181 · kitze · `TS`</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — Tree-sitter finds and ranks methods, then user-authored YAML rules compile into nouls, with severity read as the rubric's expected value rather than the top band.
  <sub>`Project` · ★168 · `JS` · `choice` · `score` · `noul`</sub>

- **[pg_typesafe](https://github.com/giuliosmall/pg_typesafe)** — Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification
  <sub>`Plugin` · ★81 · giuliosmall · `C`</sub>

- **[youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection)** — Detect youtube sponsor segment with live audio and transcript powered by Jev
  <sub>`Project` · ★81 · trungdq88 · `JS` · ⚠ `no licence`</sub>

- **[Prism](https://github.com/irfndi/prism-liquidity-agent)** — Does not place orders. It judges market conditions such as toxic flow and mean reversion, and hands the assessment to the existing strategy.
  <sub>`Project` · ★71 · `TS` · `choice` · `score`</sub>

- **[typesafe-adblock](https://github.com/realZachi/typesafe-adblock)** — A Chrome extension that asks whether a DOM element is an advert.
  <sub>`Project` · ★68 · realzachi · `JS`</sub>

- **[Blink](https://github.com/ellipsis-dev/blink)** — Uses Jev as a codebase navigator: at each directory level it decides which files are most relevant to the question, then descends.
  <sub>`Project` · ★56 · `TS` · `choice` · ⚠ `no licence`</sub>

- **[ha-jev](https://github.com/AboveColin/HA-Jev)** — A Home Assistant integration: typed answers as sensors, with actions for automations.
  <sub>`Integration` · ★45 · abovecolin · `Py`</sub>

- **[jev-sift](https://github.com/kbhuw/jev-sift)** — Classify first. Read selectively. A portable agent plugin and MCP tool for batch text classification.
  <sub>`Plugin` · ★45 · kbhuw · `JS` · ⚠ `no licence`</sub>

- **[commit-miner](https://github.com/devanshbatham/commit-miner)** — Classify Git commit diffs and messages with Jev. Bug fixes, security fixes/CWEs, and change types.
  <sub>`Project` · ★33 · devanshbatham · `Rs` · ⚠ `no licence`</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — Calibrate Jev questions against your own labels: tune criteria on labelled examples, confirm on a held-out set, get a verdict per question. Unofficial.
  <sub>`Project` · ★31 · smkrv · `TS`</sub>

- **[SemDecide](https://github.com/sharziki/semdecide)** — Jev as a command-line tool: classify, score and filter straight from a shell, for crawlers, CI and data pipelines.
  <sub>`Plugin` · ★31 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[jev-column-race](https://github.com/goodrahstar/jev-column-race)** — Jev vs Gemini 3.8 Flash: labelling 1,000 app reviews, 4.1× faster and 7× cheaper
  <sub>`Project` · ★22 · goodrahstar · `JS`</sub>

- **[jev-mcp](https://github.com/blakestone-x/jev-mcp)** — An MCP server exposing classify, score, check, match and screen to any agent.
  <sub>`Plugin` · ★18 · blakestone-x · `Py`</sub>

- **[jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier)** — Classify your inbox with Jev (TypeSafe's System One model) — tag, move, flag, and notify, all config-driven.
  <sub>`Project` · ★14 · parth-kp · `Py`</sub>

- **[jevframe](https://github.com/ktaletsk/jevframe)** — Semantic AI for pandas and Polars: classify text, analyze sentiment, and score DataFrame rows with natural-language questions and full probabilities using TypeSafe Jev.
  <sub>`Project` · ★12 · ktaletsk · `Py`</sub>

- **[evoke](https://github.com/evoke-build/evoke)** — Software, by reflex. A sentence becomes a call of a small program, chosen by Jev, TypeSafe AI's classifier, and run only when it is sure enough. Reflexes are recipes anyone can write, share and improve. A CLI you talk to, a package manager for reflexes from git, and a TypeScript SDK.
  <sub>`Project` · ★10 · evoke-build · `Rs`</sub>

- **[jevlogs](https://github.com/reachjalil/jevlogs)** — Open-source Jev log triage for OpenTelemetry. Score the signal before expensive LLM analysis.
  <sub>`Project` · ★9 · reachjalil · `JS`</sub>

- **[jev-dsl](https://github.com/inanna-malick/jev-dsl)** — Agent-first Haskell DSL for TypeSafe's Jev judgment model: typed packets, inferred types, answers under the same labels
  <sub>`Project` · ★7 · inanna-malick · `Hs`</sub>

- **[augustus](https://github.com/24601/Augustus)** — Agent skill for the decision-model class (classifiers, encoders/decoders, specialized AR heads, System One). TypeSafe Jev is the dominant exemplar. Composition algebra, question design, validation gates. MIT.
  <sub>`Plugin` · ★6 · 24601 · `Py`</sub>

- **[jev-agent-browser](https://github.com/forvela/jev-agent-browser)** — Fast, bounded browser agents powered by Jev and agent-browser — typed actions, research, classification, and safe orchestration.
  <sub>`Project` · ★6 · forvela · `JS`</sub>

- **[duckdb-jev](https://github.com/prasanthj/duckdb-jev)** — High-throughput, robust native DuckDB extension for batched and streaming TypeSafe/Jev classification, scoring, and semantic predicates from SQL.
  <sub>`Plugin` · ★3 · prasanthj · `C++`</sub>

- **[jev-document-classification](https://github.com/Charlyhno-eng/jev-document-classification)** — JEV Document Classification enables the rapid and cost-effective classification of text-based documents using AI, leveraging TypeSafe's "System One" model.
  <sub>`Project` · ★3 · charlyhno-eng · `TS`</sub>

- **[jev-skip](https://github.com/valentynkit/jev-skip)** — Skips video sponsor segments by reading the captions and deciding at watch time.
  <sub>`Project` · ★3 · valentynkit · `TS`</sub>

- **[jev-tree](https://github.com/reachjalil/jev-tree)** — Recursive Jev choice over a taxonomy. Select from more than 255 options without breaking TypeSafe Jev's choice cap.
  <sub>`Project` · ★3 · reachjalil · `TS`</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies.
  <sub>`Project` · ★2 · foadsf · `Py`</sub>

- **[jev-ids](https://github.com/jev-ids/jev-ids)** — Blazing-Fast Token-Efficient Intrusion Detection System (IDS) based on TypeSafe's Jev
  <sub>`Project` · ★2 · jev-ids · `Py`</sub>

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)** — Non-blocking Spring Boot Starter for Spring WebFlux that implements a Semantic Circuit Breaker to detect silent HTTP 200 failures using TypeSafe Jev.
  <sub>`Plugin` · ★2 · vicente-md · `Java` · ⚠ `no licence`</sub>

- **[jev-eval](https://github.com/4esv/jev-eval)** — Benchmark TypeSafe Jev against any OpenRouter model on your own labelled classification data: accuracy, calibration, latency, cost
  <sub>`Benchmark` · ★1 · 4esv · `Py` · ⚠ `no licence`</sub>

- **[jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)** — Jev decides whether a batch of logs is worth acting on. Typed questions, confidence gates, nothing executed.
  <sub>`Project` · ★1 · jyatesdotdev · `Py`</sub>

- **[jev-review-action](https://github.com/fatwang2/jev-review-action)** — Configurable GitHub submission review and PR classification with TypeSafe Jev. No text-generation model.
  <sub>`Project` · ★1 · fatwang2 · `JS`</sub>

- **[jev-triage](https://github.com/cephalization/jev-triage)** — Uses typeful jev, zero sync to pull and sync large repositories for issue triage
  <sub>`Project` · ★1 · cephalization · `TS`</sub>

- **[discoprint](https://github.com/lirantal/discoprint)** — Classify an artist's discography by theme, mood, and lyrical complexity with Jev (TypeSafe AI), and view it as a colorful terminal dashboard
  <sub>`Project` · ★0 · lirantal · `JS`</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — Free typed judgments for AI agents: offload classify/screen/score/verify to Jev (TypeSafe System One) via OpenCode Zen. Claude Code / ZCode skill. 给AI代理省token的免费决策分流技能
  <sub>`Plugin` · ★0 · yuyang2230 · `Py`</sub>

- **[jev-secret-detection](https://github.com/teyhouse/jev-secret-detection)** — Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets
  <sub>`Benchmark` · ★0 · teyhouse · `Py` · ⚠ `no licence`</sub>

- **[progressgate](https://github.com/AshutoshVJTI/progressgate)** — Detect semantic stagnation in AI agent loops
  <sub>`Project` · ★0 · ashutoshvjti · `TS`</sub>

- **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)** — The best independent test found: 24 Norwegian documents on one pinned model version, opening with a case the model got wrong while correctly reporting low confidence.
  <sub>`Benchmark` · Lindfors</sub>

- **[Jev - The Ultimate Classification Model?](https://youtube.com/watch?v=X117w2Rark8)** — An ML engineer's walkthrough from the classification-task angle, which is the framing closest to what the model actually does.
  <sub>`Video` · Sam Witteveen</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — Nine worked community scenarios: intent routing, invoice classification, news filtering, product tagging, moderation, claim verification, CSV validation and more.
  <sub>`Project` · ⚠ `unverified`</sub>

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)** — The only three-way head-to-head found, with each model's prompt tuned separately and the scope limited to one task rather than a general ranking.
  <sub>`Benchmark` · Near Here</sub>

### ML feature extraction

_Turn free text into numeric features for a classical downstream model._

- **[Cookbook: Autoresearch feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery)** ⭐ — An autoresearch loop that proposes questions, turns free text into numeric features, and uses model error to improve a supervised gradient-boosting regressor.
  <sub>`Official docs` · `Py`</sub>

- **[nimble](https://github.com/bespokelabsai/nimble)** — Local typed decisions, contrastive data curation, and model evaluation.
  <sub>`Project` · ★1,543 · bespokelabsai · `Py` · ⚠ `no licence`</sub>

- **[jev-align](https://github.com/sutro-sh/jev-align)** — Builds calibrated decision functions from human feedback.
  <sub>`Project` · ★271 · sutro-sh · `Py`</sub>

- **[Prism](https://github.com/irfndi/prism-liquidity-agent)** — Does not place orders. It judges market conditions such as toxic flow and mean reversion, and hands the assessment to the existing strategy.
  <sub>`Project` · ★71 · `TS` · `choice` · `score`</sub>

- **[jev-curate](https://github.com/AkashPriyadarshii/jev-curate)** — Curates training data: JSONL and Parquet rows are judged on quality, relevance and risk before deciding what reaches downstream training.
  <sub>`Project` · ★21 · `Rs` · `score` · `noul`</sub>

- **[tiershift](https://github.com/iamvatsalpatel/tiershift)** — Shift every LLM call to the cheapest model that can handle it. Routing decided by TypeSafe Jev in ~180 ms. No training data. Policy in plain YAML. TypeScript and Python.
  <sub>`Project` · ★3 · iamvatsalpatel · `TS`</sub>

### Document triage

_Classify and route incoming documents, invoices and forms._

- **[tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier)** — Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per page.
  <sub>`Project` · ★361 · kyotofin · `TS`</sub>

- **[docjev](https://github.com/jerryjliu/docjev)** — A very fast document classifier/splitter using Jev
  <sub>`Project` · ★207 · jerryjliu · `Py`</sub>

- **[formanator](https://github.com/timrogers/formanator)** — Submit Forma <https://joinforma.com> benefit claims from the command line and Model Context Protocol (MCP) clients, with support for AI-powered receipt analysis with an LLM or Jev
  <sub>`Plugin` · ★99 · timrogers · `Rs`</sub>

- **[jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas)** — Independent, evidence-based map of when TypeSafe's Jev actually holds up vs. breaks down — real API-call receipts, not a leaderboard. 中文為主的雙語 repo。
  <sub>`Benchmark` · ★24 · zaious · `Py`</sub>

- **[jev-document-classification](https://github.com/Charlyhno-eng/jev-document-classification)** — JEV Document Classification enables the rapid and cost-effective classification of text-based documents using AI, leveraging TypeSafe's "System One" model.
  <sub>`Project` · ★3 · charlyhno-eng · `TS`</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — Nine worked community scenarios: intent routing, invoice classification, news filtering, product tagging, moderation, claim verification, CSV validation and more.
  <sub>`Project` · ⚠ `unverified`</sub>

### Support triage

_Route support tickets and conversations by intent and urgency._

- **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐ — The canonical first call: one support ticket, one Choice, one Score and one Noul in a single request, in Python, JS and cURL.
  <sub>`Official docs` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — A graded course from a first call through each primitive, state shapes and criteria, to ticket triage and a multi-step workflow, mirroring all four official patterns.
  <sub>`Tutorial` · ★4,559 · `Py` · `choice` · `score` · `noul`</sub>

- **[spring-ai-typesafe](https://spring.io/blog/2026/09/21/spring-ai-typesafe-structured-judgment)** — A community Spring AI starter bringing typed decisions to Java, with a builder API over the three question types.
  <sub>`Integration` · ★19 · `Java` · `choice` · `score` · `noul`</sub>

- **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)** — A minimal first call asking a choice, a score and a noul together, annotated with the asymmetries that catch people out.
  <sub>`Snippet` · `Py` · `choice` · `score` · `noul` · ⚠ `code untested`</sub>

- **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)** — Walks through use case after use case — agent routing, an in-agent decision layer, ticket triage — each with a concrete option set and a sample response.
  <sub>`Tutorial` · Mehul Gupta · `Py` · `choice` · ⚠ `paywall`</sub>

- **[Jev on AI/ML API](https://docs.aimlapi.com/api-references/decision-models/typesafe/jev)** — Another gateway route, notable because its endpoint path and request envelope differ again from both the native API and Cloudflare's.
  <sub>`Integration` · `Py` · `noul` · `choice` · `score`</sub>

- **[Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/)** — Workers AI binding and REST samples asking a noul, a choice and a score in one call, with the full response including per-answer confidence.
  <sub>`Integration` · `TS` · `sh` · `noul` · `choice` · `score`</sub>

### Content scoring

_Score quality, risk or relevance on an ordered scale._

- **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐ — Adds an explicit "uncertain" outcome to moderation decisions and measures label agreement against the share of actions taken automatically.
  <sub>`Official docs` · `Py` · `choice`</sub>

- **[Pattern: Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring)** ⭐ — Break one broad judgement into atomic scores and combine them with weights that live in your code, not in the prompt.
  <sub>`Official docs` · `Py` · `score`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files.
  <sub>`Project` · ★187,482 · `Py` · `choice` · `score` · `noul`</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)** — Two Choice questions over threat level and category, held in shadow mode after a blind evaluation found Jev merely tied the incumbent model.
  <sub>`Benchmark` · ★87,191 · `TS` · `choice` · ⚠ `shadow mode`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — A graded course from a first call through each primitive, state shapes and criteria, to ticket triage and a multi-step workflow, mirroring all four official patterns.
  <sub>`Tutorial` · ★4,559 · `Py` · `choice` · `score` · `noul`</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** — An Android reply co-pilot that judges intent, timing and risk from on-screen text, while separate models handle OCR and drafting.
  <sub>`Project` · ★1,950 · `Java` · `choice` · `score` · `noul`</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)** — Pre-screens code review with Jev to surface high-risk changes for a more expensive model or a person, with a local dashboard.
  <sub>`Project` · ★510 · `TS` · `choice` · `score` · `noul`</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — A real PostgreSQL extension exposing the primitives as SQL functions, so a semantic decision can appear in a WHERE clause over any row type.
  <sub>`Project` · ★291 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[jev-review](https://github.com/NiazMorshed2007/jev-review)** — A local-first MCP plugin for continuous code-quality review by coding agents.
  <sub>`Plugin` · ★198 · niazmorshed2007 · `TS`</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — Tree-sitter finds and ranks methods, then user-authored YAML rules compile into nouls, with severity read as the rubric's expected value rather than the top band.
  <sub>`Project` · ★168 · `JS` · `choice` · `score` · `noul`</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — One TypeScript interface for 40 AI providers across three inference types — generate, stream, and decide. Decide returns typed, calibrated judgments (boolean/choice/score) via TypeSafe Jev, not text. MCP-native, voice (TTS/STT/realtime), RAG, memory, file processors. Powers Tara, Yama and Clair
  <sub>`Plugin` · ★137 · juspay · `TS`</sub>

- **[llm2jev](https://github.com/Yinsongxu/LLM2Jev)** — Adapt local language models into Jev-compatible structured decision engines with Choice, Score, and Noul outputs powered by prefill-only binary inference.
  <sub>`Project` · ★127 · yinsongxu · `Py`</sub>

- **[jev-semgrep](https://github.com/uehaj/jev-semgrep)** — grep by meaning, across languages. TypeSafe Jev scores every line against a meaning; combine meanings with AND/OR/NOT. 意味で探す grep。日本語で英語を、英語で日本語を検索できる
  <sub>`Project` · ★125 · uehaj · `JS` · ⚠ `no licence`</sub>

- **[supercov](https://github.com/supercorp-ai/supercov)** — Code quality and coverage judgements for coding agents, in Rust.
  <sub>`Project` · ★95 · supercorp-ai · `Rs`</sub>

- **[jevmeter](https://github.com/ChetasLua/jevmeter)** — Scores every sentence of a video and renders the result as a live meter.
  <sub>`Project` · ★81 · chetaslua · `Py`</sub>

- **[killmyidea](https://github.com/monteduro/killmyidea)** — Scores a startup idea across several dimensions and returns a verdict of kill, fix or ship.
  <sub>`Project` · ★78 · `TS` · `score` · `choice` · ⚠ `no licence`</sub>

- **[jev-lint](https://github.com/mizchi/jev-lint)** — lint text in code by jev scorerer
  <sub>`Project` · ★70 · mizchi · `TS`</sub>

- **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)** — A Discord moderation bot: a Choice tiers each message while a Noul carries ban urgency, and an admin pardon is fed back as a safe precedent in later requests.
  <sub>`Project` · ★41 · brainstormity · `Py` · `choice` · `noul`</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — Calibrate Jev questions against your own labels: tune criteria on labelled examples, confirm on a held-out set, get a verdict per question. Unofficial.
  <sub>`Project` · ★31 · smkrv · `TS`</sub>

- **[SemDecide](https://github.com/sharziki/semdecide)** — Jev as a command-line tool: classify, score and filter straight from a shell, for crawlers, CI and data pipelines.
  <sub>`Plugin` · ★31 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[snifftest](https://github.com/DanRWilloughby/snifftest)** — A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model.
  <sub>`Project` · ★27 · danrwilloughby · `TS`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — Read-only trading journal and review harness: Jev typed judgments, agent integration, and a reproducible finance benchmark. No orders, no advice.
  <sub>`Benchmark` · ★26 · myc0576 · `Py`</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy
  <sub>`Plugin` · ★22 · compozy · `TS`</sub>

- **[jev-curate](https://github.com/AkashPriyadarshii/jev-curate)** — Curates training data: JSONL and Parquet rows are judged on quality, relevance and risk before deciding what reaches downstream training.
  <sub>`Project` · ★21 · `Rs` · `score` · `noul`</sub>

- **[jev-mcp](https://github.com/blakestone-x/jev-mcp)** — An MCP server exposing classify, score, check, match and screen to any agent.
  <sub>`Plugin` · ★18 · blakestone-x · `Py`</sub>

- **[jevalyn](https://github.com/Ray-Hughes/jevalyn)** — The decision layer for your Rails app. A Rails-native wrapper around TypeSafe's Jev System One API: typed, calibrated decisions in your control flow.
  <sub>`Project` · ★17 · ray-hughes · `Rb`</sub>

- **[slop-grader](https://github.com/lukstei/slop-grader)** — Jev-powered, rule-based grader for text files. Runs every rule against every line in parallel. No skimming, no missed lines.
  <sub>`Project` · ★13 · lukstei · `TS`</sub>

- **[jevframe](https://github.com/ktaletsk/jevframe)** — Semantic AI for pandas and Polars: classify text, analyze sentiment, and score DataFrame rows with natural-language questions and full probabilities using TypeSafe Jev.
  <sub>`Project` · ★12 · ktaletsk · `Py`</sub>

- **[jev-forge](https://github.com/zwliJay/jev-forge)** — An open training and inference stack for Jev-style decision models. Train models to score dynamic candidate branches from a shared prefix, with support for high-cardinality choice, calibration, and fast batched inference.
  <sub>`Jev-like alternative` · ★11 · zwlijay · `Py` · ⚠ `not Jev` `no licence`</sub>

- **[jevlint](https://github.com/iamtoomas/JevLint)** — Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin.
  <sub>`Plugin` · ★11 · huntedman · `TS`</sub>

- **[jevlogs](https://github.com/reachjalil/jevlogs)** — Open-source Jev log triage for OpenTelemetry. Score the signal before expensive LLM analysis.
  <sub>`Project` · ★9 · reachjalil · `JS`</sub>

- **[jev-feels](https://github.com/Qew7/jev-feels)** — Semantic decisions as ordinary Ruby — feels?, decide, score, Rails validations and pattern matching powered by Jev
  <sub>`Project` · ★8 · qew7 · `Rb`</sub>

- **[omp-jev-compaction](https://github.com/jerryfane/omp-jev-compaction)** — Verbatim Jev-scored context reduction for omp, over TypeSafe or OpenRouter
  <sub>`Project` · ★8 · jerryfane · `TS`</sub>

- **[heist-one](https://github.com/AbdelStark/heist-one)** — Observable browser stealth game: Jev makes typed guard judgments while deterministic code owns the world.
  <sub>`Project` · ★7 · abdelstark · `TS`</sub>

- **[jev-dsl](https://github.com/inanna-malick/jev-dsl)** — Agent-first Haskell DSL for TypeSafe's Jev judgment model: typed packets, inferred types, answers under the same labels
  <sub>`Project` · ★7 · inanna-malick · `Hs`</sub>

- **[a0-typesafe-ai](https://github.com/3clyp50/a0-typesafe-ai)** — TypeSafe AI Jev judgments for Agent Zero, with typed tools and probability cards.
  <sub>`Project` · ★5 · 3clyp50 · `Py`</sub>

- **[citation-verifier](https://github.com/MarissaFamularo/citation-verifier)** — Check whether each cited paper supports the sentence citing it. Claude proves the quote, TypeSafe's Jev scores it, a human decides.
  <sub>`Project` · ★5 · marissafamularo · `JS`</sub>

- **[poorjev](https://github.com/rupeshpoojary9/poorjev)** — Open-source, local Jev alternative: a System One decision layer with provably calibrated confidence (ECE 0.170→0.071). Typed decisions, runs offline, no API key, no waitlist.
  <sub>`Jev-like alternative` · ★5 · rupeshpoojary9 · `Py` · ⚠ `not Jev`</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — Independent calibration test of TypeSafe's Jev on a task it cannot have seen: 900 rule-generated support tickets (choice / score / boolean) plus 3 public benchmarks via Vercel AI Gateway. Raw responses, ECE with noise floor, temperature refit, per-type sign of miscalibration. Reproducible for ~
  <sub>`Benchmark` · ★4 · scienthoon · `Py`</sub>

- **[qwen-rlcd](https://github.com/shamazharikh/qwen-rlcd)** — Jev-style calibrated decision model (Choice/Score/Noul) on Qwen3.5-0.8B
  <sub>`Jev-like alternative` · ★4 · shamazharikh · `Py` · ⚠ `not Jev` `no licence`</sub>

- **[typesafe-cli](https://github.com/y0usaf/typesafe-cli)** — Ask Jev typed questions from the shell: noul, choice, and score answers as numbers, not prose
  <sub>`Project` · ★4 · y0usaf · `TS`</sub>

- **[typesafe-jev](https://github.com/gtaras7/typesafe-jev)** — Screen a folder of CVs with the TypeSafe Jev decision model: typed judgments, an editable policy, free re-scoring.
  <sub>`Project` · ★4 · gtaras7 · `TS`</sub>

- **[dsh-jev](https://github.com/noetion/dsh-jev)** — DSH bundle that registers jev_ask for TypeSafe Jev noul, choice, and score answers.
  <sub>`Project` · ★3 · noetion · `TS`</sub>

- **[jev-judgment](https://github.com/HyunjunJeon/jev-judgment)** — Agent Skill: send closed coding-agent judgments to TypeSafe Jev
  <sub>`Plugin` · ★3 · hyunjunjeon · `Py`</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — Cut Claude Code's skill manifest by ~75% with TypeSafe Jev. Scores every installed skill for relevance and hides the rest via skillOverrides — 12,750 → 3,185 tokens on a 217-skill install, for $0.0009 a session.
  <sub>`Plugin` · ★3 · shivampansuriya · `JS`</sub>

- **[jevchess](https://github.com/choxos/jevchess)** — Jev, TypeSafe's System One model, plays chess against any OpenRouter LLM, Stockfish and you. One-page web app with live moves, Jev's move probabilities, saved games and win rates.
  <sub>`Project` · ★3 · choxos · `JS`</sub>

- **[llama-index-jev](https://github.com/WiktorB2004/llama-index-jev)** — LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge.
  <sub>`Project` · ★3 · wiktorb2004 · `Py`</sub>

- **[pagegrade](https://github.com/kitze/pagegrade)** — Grade page sections for clarity, writing and on-page SEO. WXT + TypeSafe AI Jev.
  <sub>`Project` · ★3 · kitze · `TS`</sub>

- **[prompt2jev](https://github.com/sumleo/prompt2jev)** — Agent skill and CLI that turn natural language, an LLM prompt, or the code that runs one into a TypeSafe Jev decision: typed state, Choice/Score/Noul questions, and a runnable script
  <sub>`Plugin` · ★3 · sumleo · `Py`</sub>

- **[vgi-typesafe](https://github.com/Query-farm/vgi-typesafe)** — A VGI worker exposing TypeSafe System One questions (choice, noul, score) to DuckDB/SQL as LATERAL-joinable table functions
  <sub>`Project` · ★3 · query-farm · `Py`</sub>

- **[jev-scout](https://github.com/AkashPriyadarshii/jev-scout)** — Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring
  <sub>`Project` · ★2 · akashpriyadarshii · `Rs`</sub>

- **[limpet](https://github.com/noplan-inc/limpet)** — A Stop hook that stops your coding agent from stopping too early. Plain-language rules, judged by jev.
  <sub>`Plugin` · ★2 · noplan-inc · `Py`</sub>

- **[pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)** — A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions.
  <sub>`Plugin` · ★2 · legacybridge-tech · `TS` · ⚠ `no licence`</sub>

- **[tripwire](https://github.com/noelzappy/tripwire)** — Judge every LLM response before the user sees it. AI SDK middleware and OpenAI-compatible proxy.
  <sub>`Integration` · ★2 · noelzappy · `TS`</sub>

- **[gpt-vs-jev](https://github.com/TanayPadar/gpt-vs-jev)** — Compare GPT generated language with JEV structured Noul decisions on the same input.
  <sub>`Project` · ★1 · tanaypadar · `TS`</sub>

- **[jev-wrapped](https://github.com/gaborishka/jev-wrapped)** — Telegram channel X-ray: Jev judges a year of posts, you get a card. One Cloudflare Worker.
  <sub>`Project` · ★1 · gaborishka · `JS`</sub>

- **[padflow-jev-evals](https://github.com/zsavage8/padflow-jev-evals)** — Typed-decision benchmark from PadFlow (land development SaaS): schemas, anonymized labeled rows, and a runner for confidence-calibrated models like TypeSafe Jev.
  <sub>`Benchmark` · ★1 · zsavage8 · `Py`</sub>

- **[s1-rs](https://github.com/AbdelStark/s1-rs)** — Typed System One layer for Rust (Choice/Score/Noul).
  <sub>`Project` · ★1 · abdelstark · `Rs`</sub>

- **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)** — The densest independent explainer: code in JS, Python and the AI SDK, all three answer shapes, the advanced patterns, and an honest list of where the model fails.
  <sub>`Tutorial` · Flavio Copes · `JS` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[jev-certify](https://github.com/nikkoxgonzales/jev-certify)** — Finite-sample guarantees for Jev (TypeSafe's System One). Conformal risk control turns calibrated probabilities into certified routing thresholds; prediction-powered inference audits them. 2,412 decisions on CLINC150 for $0.23 — including the shift and prevalence cases where the guarantee break
  <sub>`Benchmark` · ★0 · nikkoxgonzales · `Py`</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and invariant measurements of TypeSafe AI's Jev: passes six pre-registered gates on 360 labeled rows, fails four of six on graded product relevance.
  <sub>`Benchmark` · ★0 · yodablocks · `Py`</sub>

- **[jev-packs](https://github.com/dtduc-git/jev-packs)** — Evidence-gated registry of Jev question packs — curated questions, golden cases and measured evidence for Jev-compatible decision endpoints
  <sub>`Project` · ★0 · dtduc-git · `Py`</sub>

- **[pytest-jev](https://github.com/allebee/pytest-jev)** — Semantic assertions for pytest: test what your LLM app's output means, judged by TypeSafe's Jev.
  <sub>`Plugin` · ★0 · allebee · `Py`</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — Nine worked community scenarios: intent routing, invoice classification, news filtering, product tagging, moderation, claim verification, CSV validation and more.
  <sub>`Project` · ⚠ `unverified`</sub>

### Overview

_Surveys the model or the space rather than one pattern._

<details>
<summary><b>128</b> rows — click to expand</summary>

- **[Official agent skill for Claude Code](https://docs.typesafe.ai/agent-skill)** ⭐ — Installs a TypeSafe skill into Claude Code so an agent can write correct Jev calls without you pasting the API shape each time.
  <sub>`Official docs` · ★1,645 · `sh`</sub>

- **[typesafe-ai/skills](https://github.com/typesafe-ai/skills)** ⭐ — The official agent-skills repository behind the Claude Code plugin, holding the SKILL.md that teaches an agent the System One API.
  <sub>`Plugin` · ★1,645 · `sh`</sub>

- **[system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python)** ⭐ — A drop-in TypeSafeClient replacement backed by ordinary LLM APIs, so you can run Jev-shaped code without Jev access.
  <sub>`SDK` · ★249 · `Py`</sub>

- **[@typesafe-ai/sdk (TypeScript / JavaScript)](https://github.com/typesafe-ai/typesafe-sdk-js)** ⭐ — The official TypeScript client. Ships ESM, CJS and type declarations, with lowercase choice()/score()/noul() helper factories.
  <sub>`SDK` · ★218 · `TS` · `JS` · `choice` · `score` · `noul`</sub>

- **[typesafe-sdk (Python)](https://github.com/typesafe-ai/typesafe-sdk-python)** ⭐ — The official Python client. Sync and async clients, retry policy with retry-after support, and Choice/Score/Noul helper classes.
  <sub>`SDK` · ★194 · `Py` · `choice` · `score` · `noul`</sub>

- **[API reference](https://docs.typesafe.ai/api)** ⭐ — The one endpoint, POST /v1/systemone, with the exact request and answer shapes for all three question types.
  <sub>`Official docs` · `sh` · `Py` · `TS`</sub>

- **[Models, pricing and limits](https://docs.typesafe.ai/models)** ⭐ — The authoritative sheet: jev-1.13.0, $0.042 per Mtok input with output free, 64k context, 32k for state plus the longest question, text input only.
  <sub>`Official docs` · `sh` · `Py` · `TS`</sub>

- **[Primitives: Choice, Score, Noul](https://docs.typesafe.ai/primitives)** ⭐ — What each primitive is for and how to write criteria, including the 255-option cap on Choice and the 2-10 level range on Score.
  <sub>`Official docs` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Introducing System One models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)** ⭐ — The launch post: what a System One model is, why decisions were split from generation, and the vendor's latency and cost claims.
  <sub>`Article` · Diogo Almeida · ⚠ `vendor numbers`</sub>

- **[Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)** ⭐ — The vendor's own list of where the model fails: literal reading, arithmetic and counting, date comparison, indirection, large noisy states, adversarial content.
  <sub>`Official docs`</sub>

- **[Use case map](https://docs.typesafe.ai/concepts/use-case-map)** ⭐ — The vendor's own taxonomy: five headline categories, nineteen industry groups, and ten decision shapes from classification through to structured data extraction.
  <sub>`Official docs`</sub>

- **[OpenCode Zen: Jev resale](https://github.com/anomalyco/opencode)** — A coding agent whose hosted gateway resells Jev, including a free tier model id.
  <sub>`Integration` · ★209,234 · `TS`</sub>

- **[litellm](https://github.com/BerriAI/litellm)** — The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (or native) format with cost tracking, guardrails, load balancing, and logging [Bedrock, Azure, OpenAI, Anthropic, OpenAI, VertexAI, vLLM, Nvidia NIM]
  <sub>`Integration` · ★59,374 · berriai · `Py` · ⚠ `no licence`</sub>

- **[oh-my-pi](https://github.com/can1357/oh-my-pi)** — ⌥ Coding agent with the IDE wired in
  <sub>`Project` · ★32,448 · can1357 · `TS`</sub>

- **[openwork](https://github.com/different-ai/openwork)** — The open-source alternative to Claude Cowork (powered by opencode)
  <sub>`Jev-like alternative` · ★23,687 · different-ai · `TS` · ⚠ `not Jev` `no licence`</sub>

- **[Opik TypeSafe tracker](https://github.com/comet-ml/opik/blob/main/sdks/python/src/opik/integrations/typesafe/opik_tracker.py)** — Wraps the sync and async clients so every system_one call is recorded as a traced span.
  <sub>`Project` · ★22,188 · `Py`</sub>

- **[@effect/ai-typesafe](https://github.com/Effect-TS/effect)** — Implements Effect's DecisionModel interface over Jev, with an unusually candid caveat about unverified rounding behaviour.
  <sub>`Integration` · ★16,167 · `TS` · `choice` · `score` · `noul`</sub>

- **[rig-typesafeai](https://github.com/0xPlaygrounds/rig)** — A Rust integration with compile-time-checked option counts, so an over-255 Choice fails to build rather than at runtime.
  <sub>`Integration` · ★8,693 · `Rs` · `choice` · `score` · `noul`</sub>

- **[Bifrost TypeSafe gateway route](https://github.com/maximhq/bifrost/tree/dev/core/providers/typesafe)** — A Go gateway provider that passes the native API through one-to-one, so the official SDKs work by changing only the base URL.
  <sub>`Project` · ★8,230 · `Go`</sub>

- **[Kiln: Jev adapter](https://github.com/Kiln-AI/Kiln)** — A JSON-Schema-to-question compiler wired into the adapter registry, with an honest note on what it cannot serve.
  <sub>`Integration` · ★5,078 · `Py` · `choice` · `score` · `noul`</sub>

- **[laya-mlx](https://github.com/mizorewww/laya-mlx)** — Native MLX runtime for Laya typed decision models — 7–14 ms short decisions on M3 Max. No text generation, PyTorch, or cloud API.
  <sub>`Project` · ★4,500 · mizorewww · `Py`</sub>

- **[ruby_llm: TypeSafe provider](https://github.com/crmne/ruby_llm)** — A Ruby provider with a dedicated System One protocol, the main route into Jev from Ruby.
  <sub>`Integration` · ★4,396 · `Rb` · `choice` · `score` · `noul`</sub>

- **[SemIf](https://github.com/TheoLeeCJ/SemIf)** — An independent semantic-if implementation that states up front it is unaffiliated with Jev or TypeSafe.
  <sub>`Jev-like alternative` · ★3,427 · `Py` · ⚠ `not Jev`</sub>

- **[kev](https://github.com/jaredpalmer/kev)** — A trainable, self-hostable family of Jev-like decision models with a System One compatible API, so the official SDK can point at your own server.
  <sub>`Jev-like alternative` · ★2,764 · Jared Palmer · `Py` · `choice` · `score` · `noul` · ⚠ `not Jev`</sub>

- **[NanoJev](https://github.com/TianyuCodings/NanoJev)** — A self-described nano replica of Jev, for reading rather than for production.
  <sub>`Jev-like alternative` · ★1,887 · `Py` · ⚠ `not Jev`</sub>

- **[jevlike](https://github.com/vinnylarouge/jevlike)** — An independent, trainable model with the same input and output shape as Jev: text plus N options in, one probability per option out, in a single pass.
  <sub>`Jev-like alternative` · ★1,183 · vinnylarouge · `Py` · ⚠ `not Jev`</sub>

- **[celesto](https://github.com/CelestoAI/celesto)** — Secure and persistent computer for AI agents -- build your own Grokbot, and Muse.
  <sub>`Project` · ★959 · celestoai · `Py`</sub>

- **[distill](https://github.com/samuelfaj/distill)** — Get FAR MORE done with FAR FEWER tokens 🔥
  <sub>`Project` · ★682 · samuelfaj · `Rs`</sub>

- **[aiavatarkit](https://github.com/uezo/aiavatarkit)** — 🥰 Building AI-based conversational avatars lightning fast ⚡️💬
  <sub>`Project` · ★678 · uezo · `Py`</sub>

- **[simple-jev](https://github.com/featherless-ai/simple-jev)** — Turns any open-weights model into a Jev-shaped endpoint by reading next-token logits, with the server constructing the JSON rather than the model generating it.
  <sub>`Jev-like alternative` · ★462 · `Py` · ⚠ `not Jev`</sub>

- **[jev-skill](https://github.com/wuyoscar/jev-skill)** — An agent skill plus CLI that validates all three primitives, requires explicit consent before a billed call, and forbids inventing output when simulating.
  <sub>`Plugin` · ★395 · `Py` · `choice` · `score` · `noul`</sub>

- **[awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects)** — A sibling directory aiming at ecosystem breadth with commit-pinned sources, four README languages and a generated site.
  <sub>`Project` · ★339 · logicrw · `JS`</sub>

- **[openjev](https://github.com/razorback16/openjev)** — A Jev-compatible decision server on an open diffusion model.
  <sub>`Jev-like alternative` · ★288 · razorback16 · `Py` · ⚠ `not Jev`</sub>

- **[decider](https://github.com/Mapika/decider)** — A family of System One-style models fine-tuned from an open base for one-pass typed decisions.
  <sub>`Jev-like alternative` · ★287 · mapika · `Py` · ⚠ `not Jev`</sub>

- **[rizzo-flow](https://github.com/Rizzo-AI-Academy/rizzo-flow)** — The open, local take on Jev: typed decisions from an LLM, without generating a single token
  <sub>`Jev-like alternative` · ★261 · rizzo-ai-academy · `Py` · ⚠ `not Jev`</sub>

- **[openjev-sglang](https://github.com/ekzhang/openjev-sglang)** — A Jev-compatible endpoint served from open models, prefill only.
  <sub>`Jev-like alternative` · ★259 · ekzhang · `Py` · ⚠ `not Jev` `no licence`</sub>

- **[awesome-jev (heyjunpenn)](https://github.com/heyjunpenn/awesome-jev)** — The broadest sibling directory: hundreds of projects in six languages, with a README that is itself the parsed data source.
  <sub>`Project` · ★256 · heyjunpenn · `TS` · ⚠ `no licence`</sub>

- **[typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp)** — The easiest first step once you have a key: registers Jev into Claude Code, Claude Desktop, Codex and Pi with one command.
  <sub>`Plugin` · ★234 · `Go` · `choice` · `score` · `noul`</sub>

- **[laya](https://github.com/receptron/laya)** — Run Laya, the open-source Jev-compatible System-1 decision model, from Node.js / TypeScript via ONNX Runtime
  <sub>`Project` · ★216 · receptron · `TS`</sub>

- **[jeff](https://github.com/logan-markewich/jeff)** — A self-hosted drop-in replacement for TypeSafe's jev, powered by GliFormer.
  <sub>`Jev-like alternative` · ★207 · logan-markewich · `Py` · ⚠ `not Jev`</sub>

- **[awesome-jev (fatwang2)](https://github.com/fatwang2/awesome-jev)** — A sibling directory whose submissions are reviewed by Jev itself, with a notably thorough list of multi-language community clients.
  <sub>`Project` · ★187 · fatwang2 · `JS`</sub>

- **[djev-spark](https://github.com/mmastrac/djev-spark)** — DiffusionGemma NVFP4 structured decisions on a DGX Spark: container recipe
  <sub>`Project` · ★170 · mmastrac · `TS` · ⚠ `no licence`</sub>

- **[stanley-code](https://github.com/devagrawal09/stanley-code)** — Bounded TypeSafe Jev workflows for coding agents.
  <sub>`Project` · ★111 · devagrawal09 · `TS`</sub>

- **[open-jev](https://github.com/daseinlabs/open-jev)** — Open Jev implementation with custom finetuning
  <sub>`Jev-like alternative` · ★95 · daseinlabs · `Py` · ⚠ `not Jev` `no licence`</sub>

- **[advocaat](https://github.com/pithings/advocaat)** — A small typed client for asking questions about your own data.
  <sub>`SDK` · ★89 · pithings · `TS`</sub>

- **[jevbench](https://github.com/fstandhartinger/jevbench)** — JevBench v1 - a benchmark for Jev-class typed decision models: smart, cheap, fast, reliable, open.
  <sub>`Benchmark` · ★71 · fstandhartinger · `Py`</sub>

- **[jev-voice](https://github.com/kevinbadi/jev-voice)** — Talk to your Mac. Local whisper.cpp + one Jev (TypeSafe) call per command + macOS automation.
  <sub>`Project` · ★68 · kevinbadi · `Py`</sub>

- **[agent-router](https://github.com/nidhi-singh02/agent-router)** — CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr
  <sub>`Plugin` · ★63 · nidhi-singh02 · `TS`</sub>

- **[OpenDecision](https://github.com/deepanwadhwa/OpenDecision)** — An open-source semantic decision engine running a local zero-shot model, with a FastAPI server proven wire-compatible with the official SDK.
  <sub>`Jev-like alternative` · ★52 · deepanwadhwa · `Py` · `choice` · `score` · `noul` · ⚠ `not Jev`</sub>

- **[ruby_decision_model](https://github.com/obie/ruby_decision_model)** — Ruby client for decision models such as Typesafe Jev
  <sub>`SDK` · ★49 · obie · `Rb`</sub>

- **[jev-rules](https://github.com/EliaAlberti/jev-rules)** — Jev picks which of your rules apply to each prompt, so Claude only sees the ones that matter.
  <sub>`Project` · ★46 · eliaalberti · `JS`</sub>

- **[litjev](https://github.com/zhengxuyu/litjev)** — Turn any off-the-shelf LLM into a Jev -like decision layer
  <sub>`Jev-like alternative` · ★38 · zhengxuyu · `Py` · ⚠ `not Jev`</sub>

- **[openthai-systemone](https://github.com/iapp-technology/openthai-systemone)** — OpenThai-SystemOne: open Thai + English System One decision model (0.8B, 256-way slot head, Apache-2.0)
  <sub>`Project` · ★38 · iapp-technology · `Py`</sub>

- **[ask-jev-skill](https://github.com/shantanugoel/ask-jev-skill)** — Skill for Hermes, and other agents, to ask typesafe's jev
  <sub>`Plugin` · ★37 · shantanugoel · `Py`</sub>

- **[typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark)** — A gateway that mimics the structured-output shape, used to benchmark against it.
  <sub>`Benchmark` · ★37 · iammrduncan · `TS`</sub>

- **[jev-seo](https://github.com/AkashPriyadarshii/jev-seo)** — 100% free ₹0 agent-first SEO & GEO CLI suite and MCP server in Rust replacing Semrush and OpenSEO via DuckDuckGo and TypeSafe Jev System One https://akashpriyadarshii.github.io/jev-seo/
  <sub>`Plugin` · ★32 · akashpriyadarshii · `Rs`</sub>

- **[jev (Elixir/OTP)](https://github.com/dannote/jev)** — Jev as an OTP process: reply from a GenServer and pattern match on the answer.
  <sub>`SDK` · ★28 · dannote · `Ex`</sub>

- **[refgarden](https://github.com/AlbionaHoti/refgarden)** — A spatial reference explorer for creators. Local Jev query choices, metadata highlights and source-linked collections.
  <sub>`Jev-like alternative` · ★27 · albionahoti · `TS` · ⚠ `not Jev`</sub>

- **[jev-trades](https://github.com/zadescoxp/Jev-Trades)** — Trading bot with the all new TypeSafe AI's first system one model named as Jev
  <sub>`Project` · ★24 · zadescoxp · `Py`</sub>

- **[jevify](https://github.com/altryne/jevify)** — An agent skill to discover TypeSafe Jev opportunities, design typed questions, and learn from recent community experiments.
  <sub>`Plugin` · ★21 · altryne · `Py`</sub>

- **[ruby_llm-typesafe](https://github.com/kieranklaassen/ruby_llm-typesafe)** — A structured-output provider for a Ruby LLM library.
  <sub>`Integration` · ★18 · kieranklaassen · `Rb`</sub>

- **[jevocks](https://github.com/unicodeveloper/jevocks)** — Everyday Stocks Status with Jev
  <sub>`Project` · ★16 · unicodeveloper · `TS` · ⚠ `no licence`</sub>

- **[swift-typesafe](https://github.com/ainame/swift-typesafe)** — Unofficial Swift SDK for TypeSafe
  <sub>`SDK` · ★14 · ainame · `Swift`</sub>

- **[jev](https://github.com/BorisLeMeec/jev)** — A claude code plugin for jev
  <sub>`Plugin` · ★13 · borislemeec · `Go`</sub>

- **[jev-foundation-models](https://github.com/peterfriese/jev-foundation-models)** — A lightweight, native Swift 6 bridge integrating TypeSafe AI's Jev System One decision model into Apple's Foundation Models framework.
  <sub>`Project` · ★13 · peterfriese · `Swift`</sub>

- **[jev-cli](https://github.com/tumf/jev-cli)** — Small dependency-free CLI for TypeSafe Jev
  <sub>`SDK` · ★12 · tumf · `Py`</sub>

- **[jev_stock](https://github.com/sosopop/jev_stock)** — An experimental JEV-powered framework for forecasting short-term stock price direction from structured market data.
  <sub>`Project` · ★12 · sosopop · `Py` · ⚠ `no licence`</sub>

- **[typesafe-skill-router](https://github.com/DECRUX9812/typesafe-skill-router)** — TypeSafe (Jev) skill routing for Hermes Agent: names the one skill worth loading, before the model call. Opt-in, stdlib only, ~$0.001 per routed turn.
  <sub>`Plugin` · ★12 · decrux9812 · `Py`</sub>

- **[typesafe-ai](https://github.com/Twister915/typesafe-ai)** — Typed TypeSafe AI clients for Rust, with async and blocking backends and observable retries.
  <sub>`SDK` · ★11 · twister915 · `Rs`</sub>

- **[typesafe-playground](https://github.com/kavehmz/typesafe-playground)** — Interactive experiments with TypeSafe Jev, from support routing to 3D driving simulations with real AI decisions and visible sensor inputs.
  <sub>`Project` · ★11 · kavehmz · `JS` · ⚠ `no licence`</sub>

- **[pi-quiet-ask](https://github.com/HyunjunJeon/pi-quiet-ask)** — TypeSafe Jev as the pi coding agent's quiet decision layer
  <sub>`Project` · ★10 · hyunjunjeon · `TS`</sub>

- **[xtags](https://github.com/manifoldor/xtags)** — 在 X 的时间线上，给每条帖子标出它想让你干什么。判断来自 Jev，一个只返回概率、不生成文本的模型。
  <sub>`Project` · ★10 · manifoldor · `JS`</sub>

- **[typesafe-sdk-go](https://github.com/Tangerg/typesafe-sdk-go)** — Go SDK for the TypeSafe AI API — typed questions in, probability distributions out.
  <sub>`SDK` · ★9 · tangerg · `Go`</sub>

- **[jev-benchmark](https://github.com/wondertwins/jev-benchmark)** — Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs
  <sub>`Benchmark` · ★6 · wondertwins · `Py`</sub>

- **[jev-korean-benchmark](https://github.com/mahlernim/jev-korean-benchmark)** — Reproducible early-access evaluation of Jev on Korean understanding and medical text, with runtime and cost evidence
  <sub>`Benchmark` · ★6 · mahlernim · `Py` · ⚠ `no licence`</sub>

- **[typesafe-sdk](https://github.com/joshmn/typesafe-sdk)** — Ruby client for typesafe.ai
  <sub>`SDK` · ★6 · joshmn · `Rb`</sub>

- **[typesafeai-dotnet-sdk](https://github.com/saibimajdi/typesafeai-dotnet-sdk)** — Community .NET SDK for the TypeSafe AI System One API — typed noul, choice, and score questions with structured, confidence-scored answers. Not affiliated with TypeSafe AI.
  <sub>`SDK` · ★6 · saibimajdi · `C#`</sub>

- **[jev-little-airways](https://github.com/lbotinelly/jev-little-airways)** — A show-and-tell capability study for Jev, TypeSafe's System One decision model.
  <sub>`Benchmark` · ★5 · lbotinelly · `TS`</sub>

- **[legalforecastbench](https://github.com/johnhughes3/LegalForecastBench)** — LegalForecast-MTD benchmark alpha and official evaluation workflows
  <sub>`Benchmark` · ★5 · johnhughes3 · `Py`</sub>

- **[typesafe_sdk (Elixir)](https://github.com/nshkrdotcom/typesafe_sdk)** — An Elixir port of the official SDK.
  <sub>`SDK` · ★5 · nshkrdotcom · `Ex`</sub>

- **[jev-system-one](https://github.com/haseeb-heaven/jev-system-one)** — A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports
  <sub>`Project` · ★4 · haseeb-heaven · `Py`</sub>

- **[typesafe-ai-rs](https://github.com/gilljon/typesafe-ai-rs)** — Independent async and blocking Rust SDK for the TypeSafe AI System One API
  <sub>`SDK` · ★4 · gilljon · `Rs`</sub>

- **[typesafe-sdk-swift](https://github.com/alterhq/typesafe-sdk-swift)** — Unofficial Swift library for the TypeSafe API
  <sub>`SDK` · ★4 · alterhq · `Swift`</sub>

- **[jcm-router](https://github.com/adarshmishra07/jcm-router)** — Local proxy that picks the Claude model and effort per message using TypeSafe Jev. Routes subagents, leaves your cached main chat alone.
  <sub>`Project` · ★3 · adarshmishra07 · `TS`</sub>

- **[new-api-plugin-typesafe](https://github.com/FFatTiger/new-api-plugin-typesafe)** — TypeSafe AI System One (Jev) task plugin for QuantumNous/new-api — native /v1/systemone, synchronous evaluation, token billing
  <sub>`Plugin` · ★3 · ffattiger · `JS`</sub>

- **[soupbase](https://github.com/spoonnotfound/soupbase)** — Jev x 海龟汤
  <sub>`Project` · ★3 · spoonnotfound · `TS`</sub>

- **[switchboard](https://github.com/ruban-24/switchboard)** — An open-source, model-agnostic decision router for Claude Code and Codex.
  <sub>`Plugin` · ★3 · ruban-24 · `TS`</sub>

- **[typesafe-sdk-java](https://github.com/Premo-Cloud/typesafe-sdk-java)** — Community Java client for the TypeSafe System One API (unofficial)
  <sub>`SDK` · ★3 · premo-cloud · `Java`</sub>

- **[got-jev](https://github.com/phureewat29/jev-got)** — Jev (TypeSafe AI) PoC through Game of Thrones
  <sub>`Project` · ★2 · phureewat29 · `TS` · ⚠ `no licence`</sub>

- **[jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark)** — Benchmarking Jev (Typesafe.ai) against a strong LLM on the Who&When Pro agent-failure-attribution benchmark (text subset).
  <sub>`Benchmark` · ★2 · tokentrim · `Py`</sub>

- **[jev-canvas](https://github.com/gaborishka/jev-canvas)** — Draw on a tldraw canvas with your voice and a pointing finger. Jev (TypeSafe System One) decides action, target and place in ~350 ms per spoken word.
  <sub>`Project` · ★2 · gaborishka · `JS`</sub>

- **[jevclient](https://github.com/AboveColin/jevclient)** — Async Python client for TypeSafe Jev. Typed questions in, probabilities and choices out, no prose to parse.
  <sub>`SDK` · ★2 · abovecolin · `Py`</sub>

- **[jevgo](https://github.com/fgn/jevgo)** — Go client for TypeSafe AI's System One API (Jev), with optional Langfuse instrumentation
  <sub>`SDK` · ★2 · fgn · `Go`</sub>

- **[jevtown](https://github.com/gaborishka/jevtown)** — Jevtown: a social network where people write and 10,000 AI personas react
  <sub>`Project` · ★2 · gaborishka · `JS`</sub>

- **[typesafeai.net](https://github.com/Hawxy/TypeSafeAI.Net)** — .NET SDK for the TypeSafe AI platform
  <sub>`SDK` · ★2 · hawxy · `C#`</sub>

- **[askjev](https://github.com/pZacca/askjev)** — Unofficial MCP server for Jev (Typesafe AI)
  <sub>`Plugin` · ★1 · pzacca · `TS`</sub>

- **[jev-skill-router](https://github.com/shimo4228/jev-skill-router)** — Claude Code plugin: asks TypeSafe Jev which installed skill fits each prompt and logs the answer (shadow-first). A working reference for the skill-suggestion cookbook on Claude Code — the README records why it is unlikely to help a strong model as a router.
  <sub>`Plugin` · ★1 · shimo4228 · `Py`</sub>

- **[typesafe-ai-playground](https://github.com/markjaquith/typesafe-ai-playground)** — A playground for experiments around Jev, TypeSafe's System One model.
  <sub>`Project` · ★1 · markjaquith · `Rs`</sub>

- **[typesafe-go](https://github.com/zhirschtritt/typesafe-go)** — Idiomatic Go SDK for the TypeSafe AI API
  <sub>`SDK` · ★1 · zhirschtritt · `Go`</sub>

- **[typesafe-rs](https://github.com/AbdelStark/typesafe-rs)** — Latency-first Rust SDK for TypeSafe System One.
  <sub>`SDK` · ★1 · abdelstark · `Rs`</sub>

- **[@ai-sdk/typesafe-ai provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai)** — The AI SDK provider package for calling TypeSafe directly, with a sample covering all three question types and nested criteria shapes.
  <sub>`SDK` · `TS` · `JS` · `choice` · `score` · `noul`</sub>

- **[aegis: TypeSafe as a first-class provider](https://github.com/dvjn/aegis)** — A personal Rust AI gateway with a TypeSafe provider, usage extraction and alias resolution tested against real response bodies.
  <sub>`Project` · ★0 · dvjn · `Rs` · ⚠ `code untested` `no licence`</sub>

- **[Build Your Own JEV Locally: Run a 100% Private AI Agent on Your Machine](https://medium.com/coding-nexus/build-your-own-jev-locally-run-a-100-private-ai-agent-on-your-machine-bb98126d394a)** — Despite the title, this does not run Jev. It builds a Jev-like decision engine from an open LLM using constrained next-token scoring.
  <sub>`Jev-like alternative` · DataScience Nexus · `Py` · ⚠ `not Jev` `code untested` `paywall`</sub>

- **[Jev Explained: How to Add Fast, Typed Decisions to an AI Agent](https://aihubmix.com/blog/jev-explained-how-to-add-fast-typed-decisions-to-an-ai-agent)** — A third-party explainer with a useful architecture sketch and an unusually honest list of cases where you should not use a decision model.
  <sub>`Article` · `Py` · ⚠ `code untested`</sub>

- **[jev-t-rex-runner](https://github.com/joshlarsen/jev-t-rex-runner)** — Chrome dino game played by Typesafe AI Jev model
  <sub>`Project` · ★0 · joshlarsen · `JS`</sub>

- **[jevai.org community site](https://www.jevai.org/)** — An unaffiliated community site with a playground, a preset decision API, an MCP server, downloadable skills and a gallery of community apps.
  <sub>`Project` · `sh` · ⚠ `3rd-party key` `unverified`</sub>

- **[kunobi-jev](https://github.com/kunobi-ninja/kunobi-jev)** — Rust client for the TypeSafe System One API (Jev)
  <sub>`SDK` · ★0 · kunobi-ninja · `Rs`</sub>

- **[labs](https://github.com/kiarina/labs)** — Small, independent projects for experiments, research, and investigations.
  <sub>`Project` · ★0 · kiarina · `Py`</sub>

- **[Tracing Jev calls with Langfuse](https://langfuse.com/integrations/model-providers/typesafe)** — The only platform with dedicated Jev observability: an OpenInference instrumentor that traces every decision call over OpenTelemetry.
  <sub>`Integration` · `Py` · `choice` · `score` · `noul`</sub>

- **[TypeSafe AI Jev now available on AI Gateway](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway)** — Vercel's launch note for Jev on AI Gateway, with an experimental_evaluate sample using the model string typesafe-ai/jev.
  <sub>`Integration` · `TS` · `noul`</sub>

- **[TypeSafe models in Pydantic AI](https://pydantic.dev/docs/ai/models/typesafe/)** — First-party Pydantic AI support: an Agent with output_type=bool over the typesafe:jev-latest model string.
  <sub>`Integration` · `Py`</sub>

- **[TypeSafe pass-through on LiteLLM](https://docs.litellm.ai/docs/pass_through/typesafe)** — Proxy Jev through LiteLLM for unified keys and cost tracking, with any path under /typesafe/ passed straight through.
  <sub>`Integration` · `sh`</sub>

- **[TypeSafe-compatible API on Vercel AI Gateway](https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe)** — Point the official TypeSafe SDK at Vercel by changing one baseURL, or call the gateway's systemone endpoint directly with cURL.
  <sub>`Integration` · `TS` · `sh` · `noul`</sub>

- **[typesafe-go](https://github.com/Nibir1/typesafe-go)** — A zero-dependency community Go SDK, including a static analyser that flags poorly designed questions at compile time.
  <sub>`SDK` · ★0 · Nibir1 · `Go` · `choice` · `score` · `noul` · ⚠ `code untested`</sub>

- **[awesome-jev (yibie)](https://github.com/yibie/awesome-jev)** — Currently the most-starred sibling directory in this space.
  <sub>`Project` · ★1,094 · ⚠ `no licence`</sub>

- **[A new kind of AI model from a ChatGPT inventor is thrilling developers](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)** — The only launch coverage with first-hand developer quotes rather than vendor figures, including a caution that interpreting the thresholds is now your job.
  <sub>`Article` · Tim Fernholz</sub>

- **[AI model "Jev" to make machines decide faster](https://www.heise.de/en/news/AI-model-Jev-to-make-machines-decide-faster-11457071.html)** — Focuses on the missing explainability — the model returns no reasoning in language — and on every published benchmark coming from the vendor.
  <sub>`Article` · Tomislav Bezmalinović</sub>

- **[Hacker News: Introducing System One Models and Jev](https://news.ycombinator.com/item?id=49717558)** — The launch thread, and the densest single collection of scepticism: unsupported RLCD claims, apples-to-oranges latency comparisons, and the deliberate absence of public benchmarks.
  <sub>`Discussion`</sub>

- **[Jev (AI model) on Wikipedia](https://en.wikipedia.org/wiki/Jev_(AI_model))** — Most useful as an index: its reference list is a fast route to the coverage worth reading.
  <sub>`Article`</sub>

- **[Jev by TypeSafe: A Decision Model for AI Agents](https://beam.ai/agentic-insights/jev-typesafe-ai-agents)** — An agent-builder's framing of where a decision model sits in an agent stack.
  <sub>`Article` · ⚠ `marketing`</sub>

- **[Jev Cuts AI Decision Costs 100x And Vercel, Cloudflare Rushed To Add It](https://www.forbes.com/sites/josipamajic/2026/09/19/jev-cuts-ai-decision-costs-100x-and-vercel-cloudflare-rushed-to-add-it/)** — Mainstream coverage of the launch and the speed with which gateways added support.
  <sub>`Article` · Josipa Majic Predin · ⚠ `vendor numbers` `paywall`</sub>

- **[Jev From TypeSafe is a New Class of AI Model that is FAST and CHEAP - But There is a Caveat!](https://youtube.com/watch?v=qdji39XXgEY)** — A review that puts the limitation in the title rather than burying it.
  <sub>`Video` · Gary Explains</sub>

- **[Jev: System One models for Prod, not God](https://www.latent.space/p/jev)** — The only long-form founder interview: why RLHF was the wrong optimisation target, why public benchmarks were withheld, and the all-synthetic data approach.
  <sub>`Discussion` · Latent Space</sub>

- **[Jev: TypeSafe's System One Model Explained](https://www.datacamp.com/blog/system-one-models-jev)** — A neutral survey of the architecture, the claimed benchmarks and the pricing, which states plainly that no large independent reproduction had surfaced.
  <sub>`Article` · Matt Crabtree</sub>

- **[jevai.org community app gallery](https://www.jevai.org/apps)** — Thirty-six community builds curated from social posts: browser agents, spreadsheet tooling, inbox search by intent, ad blocking with judgement, games and robotics.
  <sub>`Project` · ⚠ `unverified`</sub>

- **[RLCD explained: Reinforcement Learning for Calibrated Decisions](https://systemonemodels.org/guides/rlcd-explained/)** — An independent write-up whose most useful finding is a negative one: there is no paper, no reward function, no dataset description and no reproducible evaluation for RLCD.
  <sub>`Article`</sub>

- **[TypeSafe AI debuts model for machines that plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711)** — The most sceptical mainstream piece: it challenges the no-hallucination framing on the grounds that a well-formed answer is not the same as a correct one.
  <sub>`Article` · Thomas Claburn</sub>

- **[TypeSafe on OpenRouter](https://openrouter.ai/typesafe)** — OpenRouter's listing for Jev, with its own model ids and the unusual pricing shape of paid input and free output.
  <sub>`Integration`</sub>

</details>

## By resource kind

The same rows grouped by what you will find when you open the link.

| Kind | Examples | What you will find |
| --- | :-- | --- |
| **Official docs** | `31` ██▌ | Vendor documentation, cookbooks and pattern pages. |
| **SDK** | `24` ██ | Client libraries, official and community. |
| **Integration** | `22` █▉ | A gateway, framework or platform route to the model. |
| **Snippet** | ` 4` ▍ | Small runnable examples in this repository. |
| **Project** | `194` ████████████████ | An application or library that calls Jev in anger. |
| **Plugin** | `60` █████ | Editor, agent and MCP integrations you can install. |
| **Tutorial** | ` 5` ▍ | Step-by-step material with code. |
| **Benchmark** | `28` ██▎ | Measurement. Check whether it is independent or vendor-reported. |
| **Article** | `12` █ | Explainers, analysis and launch coverage. |
| **Video** | ` 3` ▎ | Walkthroughs and reviews. |
| **Discussion** | ` 2` ▏ | Threads worth reading, including the sceptical ones. |
| **Jev-like alternative** | `19` █▋ | Independent reimplementations. These do NOT call Jev. |

## Also in this repo

The parts that are not the catalog.

| File | What it is |
| --- | --- |
| [`docs/patterns.md`](docs/patterns.md) | Every pattern defined, each with an explicit *when NOT to use this*. |
| [`docs/compatibility.md`](docs/compatibility.md) | Model string, field names, request shape, endpoint and env var differ per platform. This is that table. |
| [`docs/vetting.md`](docs/vetting.md) | What to check before trusting a row, and the one mistake most people make. |
| [`docs/status.md`](docs/status.md) | What week one of this ecosystem actually looked like, gaps included. |
| [`docs/method.md`](docs/method.md) | How the catalog was built, what was excluded, and where it is weakest. |
| [`docs/sources.md`](docs/sources.md) | Where every row came from, and the licence position. |
| [`examples/`](examples/) | Four runnable examples. One deliberately leaves the threshold policy to you. |
| [`schema/entry.schema.json`](schema/entry.schema.json) | What a catalog entry may contain. |
| [`mcp/`](mcp/) | An MCP server, so an agent can query the catalogue instead of reading it. Caveats travel with every result. |
| [`SKILL.md`](SKILL.md) | An agent skill: the facts that generated Jev code most often gets wrong, and the design rules worth following. |
| [`scripts/verify_claims.py`](scripts/verify_claims.py) | Re-reads every cited call site weekly, so a primitive claim is checkable rather than asserted. |
| [`scripts/refresh_metadata.py`](scripts/refresh_metadata.py) | Re-reads stars, licences and archive status from the GitHub API and opens a PR. |

## What is verified, and what is not

- ✅ **Verified** — the URL returned a success status on the date in `checked`; a person opened it and wrote the summary from what was there; for code rows the call site was read to confirm which primitives are used; stars and licences came from the GitHub API.
- 🔁 **Re-checked weekly** — 320 rows record the file their primitive claim was read in. A scheduled job re-reads each one from the repository's default branch and opens an issue if the claim stopped holding, so an upstream removal cannot leave a false claim sitting here. Deliberately unpinned to a commit: pinning would verify a historical snapshot forever.
- ❌ **Not verified** — whether the code runs, whether any performance claim holds, whether a project is maintained, or whether any of this suits your system. Nothing here has been executed, load-tested or security-reviewed.

### What the tags mean

| Tag | Means |
| --- | --- |
| `not Jev` | Does not call Jev at all. A compatible API does not imply compatible calibration, so thresholds do not transfer. |
| `shadow mode` | Wired in but deliberately inert — nothing it returns reaches a user-visible decision. |
| `early access` | Needs waitlist access to run. |
| `code untested` | The code was read, not executed. |
| `one commit` | One commit, so maintenance is unlikely. |
| `no licence` | No LICENSE file, whatever a README badge claims. A blocker for reuse. |
| `3rd-party key` | Needs a key for a service other than TypeSafe. |
| `vendor numbers` | Repeats the vendor's own benchmarks rather than an independent measurement. |
| `unverified` | Makes measurement claims that could not be checked. |
| `marketing` | Published to sell something as much as to explain. |
| `paywall` | Behind a paywall or a metered reader. |

## Machine-readable data

One entry per example, validated against a JSON Schema on every push.

| File | What it is |
| --- | --- |
| [`catalog.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/catalog.json) | 404 entries |
| [`retired.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/retired.json) | 0 retired |
| [`compat.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/compat.json) | The platform matrix behind `docs/compatibility.md` |
| [`patterns.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/patterns.json) | The decision taxonomy both generators and the MCP server read |
| [`schema/entry.schema.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/schema/entry.schema.json) | One entry's shape |
| [`llms.txt`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/llms.txt) | For agents, with the caveats spelled out |

## Contributing and licence

Corrections take priority over additions — a wrong row costs more than a missing one. See [CONTRIBUTING.md](CONTRIBUTING.md); the bar is *could a reader act on this row without opening the link?*

Code in `scripts/`, `site/` and `examples/` is [MIT](LICENSE-MIT). Catalog metadata is [CC0-1.0](LICENSE-CC0), with a per-row `license` field. Linked works keep their own licences — `repo_license` records what each declares.
