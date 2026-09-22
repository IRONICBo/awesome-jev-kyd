<!--
  This file is generated from catalog.json. Edit the catalog, then run `python3 scripts/build_readme.py`.
-->

# awesome-jev

[![lint](https://github.com/kydlikebtc/awesome-jev/actions/workflows/lint.yml/badge.svg)](https://github.com/kydlikebtc/awesome-jev/actions/workflows/lint.yml) [![links](https://github.com/kydlikebtc/awesome-jev/actions/workflows/links.yml/badge.svg)](https://github.com/kydlikebtc/awesome-jev/actions/workflows/links.yml) [![entries](https://img.shields.io/badge/entries-148-f5a524)](https://kydlikebtc.github.io/awesome-jev/) [![data: CC0-1.0](https://img.shields.io/badge/data-CC0--1.0-4ec97a)](LICENSE-CC0) [![code: MIT](https://img.shields.io/badge/code-MIT-5fb3d9)](LICENSE-MIT)

> Every public example of Jev — TypeSafe AI's System One decision model — indexed by the decision it makes, not by the blog that mentioned it.

**中文** · [README.zh-CN.md](README.zh-CN.md) &nbsp;·&nbsp; **Searchable site** · [kydlikebtc.github.io/awesome-jev/](https://kydlikebtc.github.io/awesome-jev/)

`148` entries &nbsp;·&nbsp; `124` with code &nbsp;·&nbsp; `36` official &nbsp;·&nbsp; `144` link-verified &nbsp;·&nbsp; `16/18` patterns &nbsp;·&nbsp; `0` retired &nbsp;·&nbsp; `2026-09-22`

<a href="https://kydlikebtc.github.io/awesome-jev/"><img src="docs/screenshots/site-desktop.png" alt="The awesome-jev site: a coverage histogram down the left acting as the pattern filter, dense entry cards on the right" width="100%"></a>

<sub>The histogram down the left of the site is the filter — each bar is a decision pattern, sized by how many examples exist for it. The site also carries two reference views: <a href="https://kydlikebtc.github.io/awesome-jev/?view=prims">the three primitives</a> and <a href="https://kydlikebtc.github.io/awesome-jev/?view=compat">the cross-platform matrix</a>. Any filter, view or single entry is a shareable URL.</sub>

---

## What this is

- **Jev** is a decision model from TypeSafe AI. It does not write text — you hand it state plus typed questions and it returns typed answers with calibrated confidence, fast and cheap enough to sit in an agent's inner loop.
- **This repo** indexes public examples of using it, organised by the *decision* being made. The resource you read this week is disposable; the decision pattern is not.
- **Why trust it:** every row names where it came from, says which primitives the code actually calls, and flags what a reader deserves to know before clicking. There are dozens of Jev lists — this one competes on verification, not on size.

> ⚠️ Not the product, not an SDK, not affiliated with TypeSafe AI, and not a recommendation. A row means the link resolved and a person read it — nothing more. See [what is verified](#what-is-verified-and-what-is-not).

## What Jev returns

Three primitives. Every pattern below is built out of them, and the asymmetry in the last row is the single most common source of bugs.

| | Primitive | Returns | Limits | Used for |
| :-: | --- | --- | --- | --- |
| ◆ | **`choice`** | one option, plus `probabilities` and `confidence` | up to **255** options | pick a tool, a route, a label |
| ▮ | **`score`** | a number, plus `legend`, `probabilities` and `confidence` | **2–10** ordered levels, 0-indexed | rank quality, risk, urgency |
| ◐ | **`noul`** | a 0–1 probability in `.noul` — **and no `confidence`** | not called "binary" or "boolean" | gate an action, keep or drop an item |

Input is **text only** — string, JSON object, or array of text. Context is **64k** tokens per request, **32k** for the state plus the longest question. Output tokens are free. There are no published weights, so it cannot be run locally. Full cross-platform differences: [`docs/compatibility.md`](docs/compatibility.md).

## Start here

Six things in reading order. Hand-picked, because "most starred" is not the same as "read this first".

| | Example | Why this one |
| :-: | --- | --- |
| `1` | **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** | The canonical first call: one support ticket, one Choice, one Score and one Noul in a single request, in Python, JS and cURL. |
| `2` | **[Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)** | The most useful page in the docs and the least linked. It explains, among other things, that a Choice over options and one Noul per option answer different questions. |
| `3` | **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)** | Written from the official API reference and checked field by field against it, but not executed against the live API. |
| `4` | **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Exactly two nouls per tool call: does knowing this call happened still matter, and is the full output still needed verbatim. Despite the word "scored" in its own description, no score primitive is used. |
| `5` | **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** | The best structured tutorial found. It states plainly that typed output does not guarantee a correct decision, lists the documented weaknesses, and qualifies its own cost illustration rather than selling it. |
| `6` | **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)** | The single most credible row in this catalog. Recall came out below their existing summariser, and at a matched context budget it tied plain recency ordering. Cost was genuinely far lower. Publishing a negative result on a hyped model is rare. |

## Coverage

Every decision pattern, sized by how many examples exist. This doubles as the index — the names link to the sections below. A zero is a research gap, not a rendering bug.

| Pattern | Examples | What it shows |
| --- | :-- | --- |
| **[Tool selection](#tool-selection)** | `25` ███████▌ | Which tool or action the agent should call next. |
| **[Intent routing](#intent-routing)** | `20` ██████ | Classify what the user wants and send the request down the right branch. |
| **[Context compaction](#context-compaction)** | ` 6` █▊ | Decide which tool calls and results still matter so stale context can be dropped. |
| **[Safety gating](#safety-gating)** | `13` ███▉ | Decide whether an action is safe to run. Defence in depth, never a security boundary. |
| **[Output validation](#output-validation)** | ` 7` ██▏ | Check a model's output against a rubric before it reaches a user. |
| Retry control | `0` &nbsp;·&nbsp; _no examples yet_ | Decide whether a failed step is worth retrying. |
| **[Human escalation](#human-escalation)** | `15` ████▌ | Use calibrated confidence to decide what a person must see. |
| **[Model routing](#model-routing)** | `10` ███ | Pick which downstream model or tier should handle a request. |
| **[Speculative fan-out](#speculative-fan-out)** | `14` ████▎ | Pack many questions — including speculative ones — into one request and let code pick what mattered. |
| **[Search & ranking](#search--ranking)** | `15` ████▌ | Score or re-rank candidates from a cheaper retrieval step. |
| **[Structured extraction](#structured-extraction)** | ` 4` █▎ | Pull typed fields out of messy text by choosing among candidates rather than generating them. |
| **[Classification](#classification)** | `18` █████▍ | Put an item into a taxonomy, including deep hierarchies walked with probabilities. |
| **[ML feature extraction](#ml-feature-extraction)** | ` 3` ▉ | Turn free text into numeric features for a classical downstream model. |
| **[Document triage](#document-triage)** | ` 1` ▎ | Classify and route incoming documents, invoices and forms. |
| **[Support triage](#support-triage)** | ` 7` ██▏ | Route support tickets and conversations by intent and urgency. |
| **[Content scoring](#content-scoring)** | `15` ████▌ | Score quality, risk or relevance on an ordered scale. |
| Recommendation | `0` &nbsp;·&nbsp; _no examples yet_ | Choose what to surface next, fast enough for a live conversation. |
| **[Overview](#overview)** | `53` ████████████████ | Surveys the model or the space rather than one pattern. |

## Measured, not claimed

Almost every performance number circulating about this model is the vendor's own, produced with reference answers derived from other models' judgements rather than human ground truth. These are the independent measurements in the catalog — several are **negative results**, which is exactly why they are worth reading first.

| Example | What it shows | Code | Caveats |
| --- | --- | :-- | :-- |
| **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)**<br><sub>Benchmark · ★247,803</sub> | Ported the Jev compaction approach, measured it against their shipping summariser, and published the conclusion not to adopt it.<br><sub>The single most credible row in this catalog. Recall came out below their existing summariser, and at a matched context budget it tied plain recency ordering. Cost was genuinely far lower. Publishing a negative result on a hyped model is rare.</sub> | `Py`<br><sub>noul</sub> | — |
| **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)**<br><sub>Benchmark · ★87,175</sub> | Two Choice questions over threat level and category, held in shadow mode after a blind evaluation found Jev merely tied the incumbent model.<br><sub>Wired in but deliberately inert: by their own statement nothing Jev returns reaches a label, a cache row or an alert. Ships a golden fixture. A model to copy for how to trial a new model without betting production on it.</sub> | `TS`<br><sub>choice</sub> | `shadow mode` |
| **[no-mistakes: review context selection](https://github.com/kunchenguid/no-mistakes)**<br><sub>Benchmark · ★8,595</sub> | One Score per candidate file to pick review context, with a measured outcome: materially more billed input for essentially no wall-clock gain.<br><sub>Their own recommendation was to keep the feature opt-in, off by default, and ship no savings claim. That is what an honest measurement looks like.</sub> | `Go`<br><sub>score</sub> | — |
| **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)**<br><sub>Benchmark · ★190</sub> | Independent Korean-language notes reporting that reversing the order of options shifted a probability enough to flip a 0.9 threshold.<br><sub>The most actionable engineering caveat found anywhere: if option order alone can move a probability past your threshold, your threshold is not as stable as it looks. Independent and unreplicated, so treat the magnitude as indicative.</sub> | `Py` | `no licence` `unverified` |
| **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)**<br><sub>Benchmark · Lindfors</sub> | The best independent test found: 24 Norwegian documents on one pinned model version, opening with a case the model got wrong while correctly reporting low confidence.<br><sub>Methodology is stated cleanly and scoped honestly as a single-day snapshot. Leading with a failure case is what makes it a real calibration test rather than a testimonial.</sub> | — | — |
| **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)**<br><sub>Benchmark · Near Here</sub> | The only three-way head-to-head found, with each model's prompt tuned separately and the scope limited to one task rather than a general ranking.<br><sub>Self-limits correctly: a use-case study, not a model leaderboard. That restraint is rarer than the numbers.</sub> | — | — |

## By decision pattern

The primary index. Each heading is a decision an agent has to make; the rows are examples of making it. Caveats appear as short tags — the full note for each row is in [`catalog.json`](catalog.json) and on [the site](https://kydlikebtc.github.io/awesome-jev/).

### Tool selection

_Which tool or action the agent should call next._

| Example | What it shows | Code | Caveats |
| --- | --- | :-- | :-- |
| **[Cookbook: Function calling](https://docs.typesafe.ai/cookbooks/function_calling)** ⭐<br><sub>Official docs</sub> | Maps natural-language trading requests onto ordinary typed functions by turning function names and closed-set arguments into confidence-aware questions. | `Py`<br><sub>choice</sub> | — |
| **[Cookbook: Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion)** ⭐<br><sub>Official docs</sub> | Picks at most one skill out of 182 for an agent turn: one request ranks every skill and asks whether the turn needs one at all, a second reads the top three. | `Py`<br><sub>choice noul</sub> | — |
| **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐<br><sub>Official docs</sub> | Runnable demo code for a smart home assistant that evaluates user requests with typed decisions. | `Py` | — |
| **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)**<br><sub>Plugin · ★30,896</sub> | Three independently installable Claude Code plugins — guardrails, model router and skill suggestion — each with its own hooks and tests. | `Py` `TS`<br><sub>choice score noul</sub> | — |
| **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)**<br><sub>Project · ★30,278</sub> | Compiles a tool catalogue into questions and reconstructs tool calls from the answers, with typed errors for abstention and confirmation-required cases. | `Py`<br><sub>choice</sub> | — |
| **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)**<br><sub>Project · ★27,847</sub> | Two-stage MCP tool search: a wide Choice coarse-ranks the whole catalogue, then a shortlist gets full descriptions plus one Noul each to decide whether it does the job at all. | `Py`<br><sub>choice noul</sub> | — |
| **[Cua driver: jev-use example](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use)**<br><sub>Project · ★25,737</sub> | Computer-use action selection in Python and TypeScript: Jev picks the next browser action from an immutable candidate set, with reobserve and abstain as reserved options. | `Py` `TS`<br><sub>choice</sub> | — |
| **[json-render](https://github.com/vercel-labs/json-render)**<br><sub>Project · ★17,964 · Vercel Labs</sub> | Vercel Labs' generative UI framework. In its Jev experiment the model does not write JSON token by token — it only picks components, props and layout. | `TS`<br><sub>choice</sub> | — |
| **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)**<br><sub>Project · ★16,069 · Browser Use</sub> | A high-speed browser agent from Browser Use: Jev decides the operation and which element to act on, and a small LLM is called only when text must be typed. | `Py`<br><sub>choice</sub> | `vendor numbers` |
| **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)**<br><sub>Project · ★6,338</sub> | Reviews each tool call on three axes — risk level, whether the user authorised it, and an explicit prompt-injection pressure check. | `TS`<br><sub>choice noul</sub> | — |
| **[jev-trader](https://github.com/jarrodwatts/jev-trader)**<br><sub>Project · ★1,871</sub> | High-frequency market making on a test network, deciding buy or sell from spread and trade direction. | `TS`<br><sub>choice</sub> | `unverified` |
| **[agent-desktop](https://github.com/lahfir/agent-desktop)**<br><sub>Project · ★1,436</sub> | Desktop automation that reads the system accessibility tree and decides which button, menu or field to act on next. | `Rs`<br><sub>choice</sub> | — |
| **[Jev-cu](https://github.com/Sac-Y/Jev-cu)**<br><sub>Project · ★547</sub> | A computer-use agent that asks which accessibility-tree element to act on, plus a separate noul for whether the action needs explicit user confirmation. | `JS`<br><sub>choice noul</sub> | `no licence` |
| **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)**<br><sub>Plugin · ★398</sub> | Nine agent skills plus a CLI covering model routing, memory filtering, turn retention, one-of-many skill selection and next-action choice. | `Py`<br><sub>choice score noul</sub> | — |
| **[typesafe-mario](https://github.com/fhshaik/typesafe-mario)**<br><sub>Project · ★336</sub> | Plays Super Mario Bros. from structured emulator RAM rather than screenshots, deciding run, jump and dodge. | `Py`<br><sub>choice score noul</sub> | `code untested` `one commit` `no licence` |
| **[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)**<br><sub>Project · ★212</sub> | Voice-driven browser control where target criteria are rebuilt per request from the live element list, always including a none option. | `JS`<br><sub>choice score noul</sub> | — |
| **[hyperedit](https://github.com/kevinbadi/hyperedit)**<br><sub>Project · ★173</sub> | An AI video editor routing an editing instruction to an operation, a target clip and a track, with a keyword router as fallback. | `TS`<br><sub>choice noul</sub> | `no licence` |
| **[jevpilot](https://github.com/standardagents/jevpilot)**<br><sub>Project · ★152</sub> | A driving simulator autopilot asking two choices per tick, which short-circuits single-option questions locally instead of paying to send them. | `JS`<br><sub>choice</sub> | `no licence` |
| **[jev-drone](https://github.com/RomanSlack/jev-drone)**<br><sub>Project · ★117</sub> | Camera-only simulated drone where Jev makes tactical judgements at a low rate while stabilisation and safety reflexes stay in ordinary fast code. | `Py`<br><sub>choice score noul</sub> | `unverified` |
| **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)**<br><sub>Project · ★83</sub> | A chat bot that does tool calling with no language model anywhere: one request asks the request kind, the tool, and every tool's arguments at once. | `TS`<br><sub>choice noul</sub> | — |
| **[neo4jev](https://github.com/jexp/neo4jev)**<br><sub>Project · ★79</sub> | Puts Jev inside a knowledge graph traversal: at each node it decides which edge is most worth following. | `Py`<br><sub>choice</sub> | — |
| **[OneVOneJev](https://github.com/emrickgarrett/OneVOneJev)**<br><sub>Project · ★18</sub> | A browser 1v1 FPS where every decision tick judges movement, view angle, aim, fire and jump. | `TS`<br><sub>choice</sub> | `code untested` `no licence` |
| **[Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py)**<br><sub>Snippet</sub> | Asks for an operation plus a target for each operation it might have picked, so a browser step never needs a second round trip. | `Py`<br><sub>choice noul</sub> | `code untested` |
| **[Example: tool selection with a none option](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/04-tool-selection/main.py)**<br><sub>Snippet</sub> | Pairs a choice over tools with a separate noul on whether a tool is needed at all, because those are different questions. | `Py`<br><sub>choice noul</sub> | `code untested` |
| **[Jev (Fully Tested) + Browser Use: FASTEST AI Agent I'VE TRIED YET!](https://www.youtube.com/watch?v=SNJ3yuJ_QwY)**<br><sub>Video · AICodeKing</sub> | Wires Jev into Browser Use to drive a browser automation agent. | — | `unverified` |

### Intent routing

_Classify what the user wants and send the request down the right branch._

| Example | What it shows | Code | Caveats |
| --- | --- | :-- | :-- |
| **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐<br><sub>Official docs</sub> | Runnable demo code for a smart home assistant that evaluates user requests with typed decisions. | `Py` | — |
| **[Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing)** ⭐<br><sub>Official docs</sub> | Treat confidence as a second axis: the answer tells you what, the confidence tells you whether to act on it. | `Py` | — |
| **[Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing)** ⭐<br><sub>Official docs</sub> | Classify an incoming request and route it to the cheapest adequate handler: deterministic code, a specialist LLM, or a person. | `Py`<br><sub>choice</sub> | — |
| **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)**<br><sub>Project · ★187,483</sub> | Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files. | `Py`<br><sub>choice score noul</sub> | — |
| **[Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html)**<br><sub>Integration · ★46,932</sub> | Turns downstream task ids into a choice option set, with a minimum-confidence gate that routes uncertain runs to a human. | `Py`<br><sub>choice</sub> | — |
| **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)**<br><sub>Project · ★12,276</sub> | Seven distinct email decisions, each with its own separately chosen threshold, falling back to the normal LLM on any error. | `TS`<br><sub>choice noul</sub> | — |
| **[Real Python: hello-jev](https://github.com/realpython/materials/tree/master/hello-jev)**<br><sub>Tutorial · ★5,205 · Real Python</sub> | A teaching example with a deliberate control group: the same station-enquiry task written in plain Python that only accepts Y/N, next to a Noul that reads intent. | `Py`<br><sub>noul</sub> | — |
| **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br><sub>Tutorial · ★4,554</sub> | A graded course from a first call through each primitive, state shapes and criteria, to ticket triage and a multi-step workflow, mirroring all four official patterns. | `Py`<br><sub>choice score noul</sub> | — |
| **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)**<br><sub>Project · ★1,340</sub> | An Android reply co-pilot that judges intent, timing and risk from on-screen text, while separate models handle OCR and drafting. | `Java`<br><sub>choice score noul</sub> | — |
| **[jev-search](https://github.com/superagents-lab/jev-search)**<br><sub>Project · ★382</sub> | Jev-driven web search: chooses the recency window and the best query rewrite, then reranks results in batches with one noul each. | `TS`<br><sub>choice noul</sub> | — |
| **[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)**<br><sub>Project · ★212</sub> | Voice-driven browser control where target criteria are rebuilt per request from the live element list, always including a none option. | `JS`<br><sub>choice score noul</sub> | — |
| **[hyperedit](https://github.com/kevinbadi/hyperedit)**<br><sub>Project · ★173</sub> | An AI video editor routing an editing instruction to an operation, a target clip and a track, with a keyword router as fallback. | `TS`<br><sub>choice noul</sub> | `no licence` |
| **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)**<br><sub>Project · ★83</sub> | A chat bot that does tool calling with no language model anywhere: one request asks the request kind, the tool, and every tool's arguments at once. | `TS`<br><sub>choice noul</sub> | — |
| **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)**<br><sub>Tutorial · Flavio Copes</sub> | The densest independent explainer: code in JS, Python and the AI SDK, all three answer shapes, the advanced patterns, and an honest list of where the model fails. | `JS` `Py` `TS`<br><sub>choice score noul</sub> | — |
| **[Example: confidence-gated escalation](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-confidence-gate/main.py)**<br><sub>Snippet</sub> | Routing with an act-or-escalate gate, where the policy function is deliberately left unimplemented because the thresholds are yours to choose. | `Py`<br><sub>choice</sub> | `code untested` |
| **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)**<br><sub>Tutorial · Mehul Gupta</sub> | Walks through use case after use case — agent routing, an in-agent decision layer, ticket triage — each with a concrete option set and a sample response. | `Py`<br><sub>choice</sub> | `paywall` |
| **[Jev on Netlify AI Gateway](https://www.netlify.com/changelog/typesafe-jev-ai-gateway/)**<br><sub>Integration</sub> | Zero-config access from a Netlify function: use the official SDK with no API key, base URL or provider setup, billed through Netlify credits. | `TS`<br><sub>choice</sub> | — |
| **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)**<br><sub>Integration</sub> | The LangChain integration: a classifier plus experimental middleware for model routing and for gating risky tool calls before they run. | `Py`<br><sub>choice score noul</sub> | `early access` |
| **[Using TypeSafe Jev with the AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk)**<br><sub>Tutorial</sub> | The richest Vercel walkthrough: single and multi-question calls, probability-threshold routing, and unit tests with a mock evaluation model. | `TS`<br><sub>noul choice score</sub> | — |
| **[jevai.org community showcase cases](https://www.jevai.org/cases)**<br><sub>Project</sub> | Nine worked community scenarios: intent routing, invoice classification, news filtering, product tagging, moderation, claim verification, CSV validation and more. | — | `unverified` |

### Context compaction

_Decide which tool calls and results still matter so stale context can be dropped._

| Example | What it shows | Code | Caveats |
| --- | --- | :-- | :-- |
| **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)**<br><sub>Benchmark · ★247,803</sub> | Ported the Jev compaction approach, measured it against their shipping summariser, and published the conclusion not to adopt it. | `Py`<br><sub>noul</sub> | — |
| **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)**<br><sub>Project · ★19,990</sub> | Replaces the whole retrieval stack for memory recall — no embeddings, no BM25, no reranker — with one batched Noul per candidate memory. | `Rs`<br><sub>noul</sub> | — |
| **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)**<br><sub>Plugin · ★6,005 · tamaratran</sub> | A Claude Code plugin that replaces the compaction summary with per-item decisions: stale tool calls are dropped or truncated, everything kept stays verbatim. | `TS`<br><sub>noul</sub> | — |
| **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)**<br><sub>Plugin · ★398</sub> | Nine agent skills plus a CLI covering model routing, memory filtering, turn retention, one-of-many skill selection and next-action choice. | `Py`<br><sub>choice score noul</sub> | — |
| **[jev-pruner](https://github.com/tamaratran/jev-pruner)**<br><sub>Plugin · ★134 · tamaratran</sub> | Trims long shell output before the model sees it, asking one Noul per chunk. | `TS`<br><sub>noul</sub> | — |
| **[Winnow](https://github.com/GhalebDweikat/winnow)**<br><sub>Plugin · ★54</sub> | Context garbage collection for Claude Code: when Read, Bash or Grep dump a wall of output, each chunk is judged for relevance to the current task. | `Py`<br><sub>noul</sub> | — |

### Safety gating

_Decide whether an action is safe to run. Defence in depth, never a security boundary._

| Example | What it shows | Code | Caveats |
| --- | --- | :-- | :-- |
| **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐<br><sub>Official docs</sub> | Scores each retrieved passage, then decides in code which reach the answering model — keeping contradictory ones flagged and dropping ones carrying prompt injection. | `Py` | — |
| **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐<br><sub>Official docs</sub> | Screens every message in and out of an LLM app in one request, naming hazards and scoring how much harm complying would do. | `Py`<br><sub>noul score</sub> | — |
| **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)**<br><sub>Project · ★42,304</sub> | Drops in as a moderation API by asking many parallel Noul questions in one request, one per hazard category, with an anti-injection prefix on every instruction. | `Go`<br><sub>noul</sub> | — |
| **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)**<br><sub>Plugin · ★30,896</sub> | Three independently installable Claude Code plugins — guardrails, model router and skill suggestion — each with its own hooks and tests. | `Py` `TS`<br><sub>choice score noul</sub> | — |
| **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)**<br><sub>Integration · ★18,214</sub> | The JavaScript counterpart of the LangChain integration, with the same classifier and middleware shapes. | `TS`<br><sub>choice score noul</sub> | — |
| **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)**<br><sub>Project · ★6,338</sub> | Reviews each tool call on three axes — risk level, whether the user authorised it, and an explicit prompt-injection pressure check. | `TS`<br><sub>choice noul</sub> | — |
| **[agentgateway: CI-validated LLM guardrail](https://github.com/agentgateway/agentgateway)**<br><sub>Project · ★4,969</sub> | Three Score questions on a shared severity scale, blocking the request when two or more cross the line, and failing closed. | `Rs`<br><sub>score</sub> | — |
| **[Jev-cu](https://github.com/Sac-Y/Jev-cu)**<br><sub>Project · ★547</sub> | A computer-use agent that asks which accessibility-tree element to act on, plus a separate noul for whether the action needs explicit user confirmation. | `JS`<br><sub>choice noul</sub> | `no licence` |
| **[jev-mcp](https://github.com/jkudish/jev-mcp)**<br><sub>Plugin · ★240</sub> | A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools. | `JS`<br><sub>choice score noul</sub> | — |
| **[jev-drone](https://github.com/RomanSlack/jev-drone)**<br><sub>Project · ★117</sub> | Camera-only simulated drone where Jev makes tactical judgements at a low rate while stabilisation and safety reflexes stay in ordinary fast code. | `Py`<br><sub>choice score noul</sub> | `unverified` |
| **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)**<br><sub>Project · ★42 · brainstormity</sub> | A Discord moderation bot: a Choice tiers each message while a Noul carries ban urgency, and an admin pardon is fed back as a safe precedent in later requests. | `Py`<br><sub>choice noul</sub> | — |
| **[Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)**<br><sub>Article · Sydney Runkle, Hunter Lovell</sub> | LangChain's explainer and integration walkthrough: the three question types, plus model routing and gating risky tool calls before they run. | `Py` | `vendor numbers` |
| **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)**<br><sub>Integration</sub> | The LangChain integration: a classifier plus experimental middleware for model routing and for gating risky tool calls before they run. | `Py`<br><sub>choice score noul</sub> | `early access` |

### Output validation

_Check a model's output against a rubric before it reaches a user._

| Example | What it shows | Code | Caveats |
| --- | --- | :-- | :-- |
| **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐<br><sub>Official docs</sub> | Catches wrong or invented citations against the source document with one Choice, using its confidence to flag borderline cases for review. | `Py`<br><sub>choice</sub> | — |
| **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐<br><sub>Official docs</sub> | Screens every message in and out of an LLM app in one request, naming hazards and scoring how much harm complying would do. | `Py`<br><sub>noul score</sub> | — |
| **[jev-mcp](https://github.com/jkudish/jev-mcp)**<br><sub>Plugin · ★240</sub> | A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools. | `JS`<br><sub>choice score noul</sub> | — |
| **[perch: semantic code linting](https://github.com/lakeday-org/perch)**<br><sub>Project · ★167</sub> | Tree-sitter finds and ranks methods, then user-authored YAML rules compile into nouls, with severity read as the rubric's expected value rather than the top band. | `JS`<br><sub>choice score noul</sub> | — |
| **[Canny](https://github.com/qkal/Canny)**<br><sub>Project · ★28</sub> | Guards against a coding agent claiming it finished: reads tool output, the diff and test results, then judges whether the completion claim holds. | `TS`<br><sub>noul score</sub> | — |
| **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)**<br><sub>Benchmark · Near Here</sub> | The only three-way head-to-head found, with each model's prompt tuned separately and the scope limited to one task rather than a general ranking. | — | — |
| **[TypeSafe's Jev: Can decision models replace LLM judges?](https://arize.com/blog/typesafe-jev-llm-judge/)**<br><sub>Article · Laurie Voss</sub> | Collects the third-party evaluations that exist so far and frames the question of where a decision model can stand in for an LLM judge. | — | — |

### Human escalation

_Use calibrated confidence to decide what a person must see._

| Example | What it shows | Code | Caveats |
| --- | --- | :-- | :-- |
| **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐<br><sub>Official docs</sub> | Classifies annual reports into 75 industry groups, then reads the answer's own confidence to decide whether to report that group or the broader division above it. | `Py`<br><sub>choice</sub> | — |
| **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐<br><sub>Official docs</sub> | Catches wrong or invented citations against the source document with one Choice, using its confidence to flag borderline cases for review. | `Py`<br><sub>choice</sub> | — |
| **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐<br><sub>Official docs</sub> | Decides which of 450 candidate pairs from two product catalogues describe the same thing, with one Score whose three levels are the three available actions. | `Py`<br><sub>score</sub> | — |
| **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐<br><sub>Official docs</sub> | Adds an explicit "uncertain" outcome to moderation decisions and measures label agreement against the share of actions taken automatically. | `Py`<br><sub>choice</sub> | — |
| **[Cookbook: Self-consistency with nouls](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook)** ⭐<br><sub>Official docs</sub> | Routes uncertain probabilities to human review while keeping the underlying noul values visible rather than collapsing them to a label. | `Py`<br><sub>noul</sub> | — |
| **[Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing)** ⭐<br><sub>Official docs</sub> | Treat confidence as a second axis: the answer tells you what, the confidence tells you whether to act on it. | `Py` | — |
| **[Confidence](https://docs.typesafe.ai/confidence)** ⭐<br><sub>Official docs</sub> | How confidence is derived from the probability distribution, and why a threshold tuned on one question type does not transfer to another. | — | — |
| **[Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html)**<br><sub>Integration · ★46,932</sub> | Turns downstream task ids into a choice option set, with a minimum-confidence gate that routes uncertain runs to a human. | `Py`<br><sub>choice</sub> | — |
| **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)**<br><sub>Project · ★30,278</sub> | Compiles a tool catalogue into questions and reconstructs tool calls from the answers, with typed errors for abstention and confirmation-required cases. | `Py`<br><sub>choice</sub> | — |
| **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)**<br><sub>Project · ★12,276</sub> | Seven distinct email decisions, each with its own separately chosen threshold, falling back to the normal LLM on any error. | `TS`<br><sub>choice noul</sub> | — |
| **[jev-review](https://github.com/devagrawal09/jev-review)**<br><sub>Project · ★495</sub> | Pre-screens code review with Jev to surface high-risk changes for a more expensive model or a person, with a local dashboard. | `TS`<br><sub>choice score noul</sub> | `archived` |
| **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)**<br><sub>Benchmark · ★190</sub> | Independent Korean-language notes reporting that reversing the order of options shifted a probability enough to flip a 0.9 threshold. | `Py` | `no licence` `unverified` |
| **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)**<br><sub>Project · ★42 · brainstormity</sub> | A Discord moderation bot: a Choice tiers each message while a Noul carries ban urgency, and an admin pardon is fed back as a safe precedent in later requests. | `Py`<br><sub>choice noul</sub> | — |
| **[Example: confidence-gated escalation](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-confidence-gate/main.py)**<br><sub>Snippet</sub> | Routing with an act-or-escalate gate, where the policy function is deliberately left unimplemented because the thresholds are yours to choose. | `Py`<br><sub>choice</sub> | `code untested` |
| **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)**<br><sub>Benchmark · Lindfors</sub> | The best independent test found: 24 Norwegian documents on one pinned model version, opening with a case the model got wrong while correctly reporting low confidence. | — | — |

### Model routing

_Pick which downstream model or tier should handle a request._

| Example | What it shows | Code | Caveats |
| --- | --- | :-- | :-- |
| **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐<br><sub>Official docs</sub> | A two-stage mini-then-verify-then-reasoning cascade that reaches most of a big reasoning model's quality at a fraction of the cost. | `Py` | — |
| **[Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing)** ⭐<br><sub>Official docs</sub> | Classify an incoming request and route it to the cheapest adequate handler: deterministic code, a specialist LLM, or a person. | `Py`<br><sub>choice</sub> | — |
| **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)**<br><sub>Plugin · ★30,896</sub> | Three independently installable Claude Code plugins — guardrails, model router and skill suggestion — each with its own hooks and tests. | `Py` `TS`<br><sub>choice score noul</sub> | — |
| **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)**<br><sub>Integration · ★18,214</sub> | The JavaScript counterpart of the LangChain integration, with the same classifier and middleware shapes. | `TS`<br><sub>choice score noul</sub> | — |
| **[jev-review](https://github.com/devagrawal09/jev-review)**<br><sub>Project · ★495</sub> | Pre-screens code review with Jev to surface high-risk changes for a more expensive model or a person, with a local dashboard. | `TS`<br><sub>choice score noul</sub> | `archived` |
| **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)**<br><sub>Plugin · ★398</sub> | Nine agent skills plus a CLI covering model routing, memory filtering, turn retention, one-of-many skill selection and next-action choice. | `Py`<br><sub>choice score noul</sub> | — |
| **[jev-codex-router](https://github.com/0xNatoshi/jev-codex-router)**<br><sub>Plugin · ★177</sub> | Judges how hard a coding turn is, then picks the model tier, reasoning depth and speed mode to match. | `JS`<br><sub>choice score</sub> | — |
| **[Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)**<br><sub>Article · Sydney Runkle, Hunter Lovell</sub> | LangChain's explainer and integration walkthrough: the three question types, plus model routing and gating risky tool calls before they run. | `Py` | `vendor numbers` |
| **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)**<br><sub>Tutorial · Mehul Gupta</sub> | Walks through use case after use case — agent routing, an in-agent decision layer, ticket triage — each with a concrete option set and a sample response. | `Py`<br><sub>choice</sub> | `paywall` |
| **[langchain-typesafe](https://docs.langchain.com/oss/python/integrations/providers/typesafe)**<br><sub>Integration</sub> | The LangChain integration: a classifier plus experimental middleware for model routing and for gating risky tool calls before they run. | `Py`<br><sub>choice score noul</sub> | `early access` |

### Speculative fan-out

_Pack many questions — including speculative ones — into one request and let code pick what mattered._

| Example | What it shows | Code | Caveats |
| --- | --- | :-- | :-- |
| **[Cookbook: Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions)** ⭐<br><sub>Official docs</sub> | A 13-question regulatory briefing over one long article, showing that batching every question into one call is far cheaper and faster with no change in answers. | `Py` | — |
| **[Pattern: Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out)** ⭐<br><sub>Official docs</sub> | Pack many questions, including ones you may not need, into a single request and let your code decide afterwards what was relevant. | `Py` | — |
| **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐<br><sub>Official docs</sub> | The canonical first call: one support ticket, one Choice, one Score and one Noul in a single request, in Python, JS and cURL. | `Py` `TS` `sh`<br><sub>choice score noul</sub> | — |
| **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)**<br><sub>Project · ★187,483</sub> | Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files. | `Py`<br><sub>choice score noul</sub> | — |
| **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)**<br><sub>Project · ★42,304</sub> | Drops in as a moderation API by asking many parallel Noul questions in one request, one per hazard category, with an anti-injection prefix on every instruction. | `Go`<br><sub>noul</sub> | — |
| **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)**<br><sub>Project · ★16,069 · Browser Use</sub> | A high-speed browser agent from Browser Use: Jev decides the operation and which element to act on, and a small LLM is called only when text must be typed. | `Py`<br><sub>choice</sub> | `vendor numbers` |
| **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br><sub>Tutorial · ★4,554</sub> | A graded course from a first call through each primitive, state shapes and criteria, to ticket triage and a multi-step workflow, mirroring all four official patterns. | `Py`<br><sub>choice score noul</sub> | — |
| **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)**<br><sub>Project · ★83</sub> | A chat bot that does tool calling with no language model anywhere: one request asks the request kind, the tool, and every tool's arguments at once. | `TS`<br><sub>choice noul</sub> | — |
| **[OneVOneJev](https://github.com/emrickgarrett/OneVOneJev)**<br><sub>Project · ★18</sub> | A browser 1v1 FPS where every decision tick judges movement, view angle, aim, fire and jump. | `TS`<br><sub>choice</sub> | `code untested` `no licence` |
| **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)**<br><sub>Tutorial · Flavio Copes</sub> | The densest independent explainer: code in JS, Python and the AI SDK, all three answer shapes, the advanced patterns, and an honest list of where the model fails. | `JS` `Py` `TS`<br><sub>choice score noul</sub> | — |
| **[Example: speculative fan-out](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/03-fan-out/main.py)**<br><sub>Snippet</sub> | Asks for an operation plus a target for each operation it might have picked, so a browser step never needs a second round trip. | `Py`<br><sub>choice noul</sub> | `code untested` |
| **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)**<br><sub>Snippet</sub> | A minimal first call asking a choice, a score and a noul together, annotated with the asymmetries that catch people out. | `Py`<br><sub>choice score noul</sub> | `code untested` |
| **[Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/)**<br><sub>Integration</sub> | Workers AI binding and REST samples asking a noul, a choice and a score in one call, with the full response including per-answer confidence. | `TS` `sh`<br><sub>noul choice score</sub> | — |
| **[Using TypeSafe Jev with the AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk)**<br><sub>Tutorial</sub> | The richest Vercel walkthrough: single and multi-question calls, probability-threshold routing, and unit tests with a mock evaluation model. | `TS`<br><sub>noul choice score</sub> | — |

### Search & ranking

_Score or re-rank candidates from a cheaper retrieval step._

| Example | What it shows | Code | Caveats |
| --- | --- | :-- | :-- |
| **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐<br><sub>Official docs</sub> | Scores each retrieved passage, then decides in code which reach the answering model — keeping contradictory ones flagged and dropping ones carrying prompt injection. | `Py` | — |
| **[Cookbook: Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find)** ⭐<br><sub>Official docs</sub> | Semantic search over a terms-of-service document: one request scores 218 line ids with a Choice, and a Noul checks whether the document answers at all. | `Py`<br><sub>choice noul</sub> | — |
| **[Cookbook: Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe)** ⭐<br><sub>Official docs</sub> | Re-ranks 30-passage BM25 shortlists for 40 legal queries with one question per query-candidate pair, reporting large top-1 and top-10 gains. | `Py` | — |
| **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)**<br><sub>Project · ★187,483</sub> | Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files. | `Py`<br><sub>choice score noul</sub> | — |
| **[OpenViking: retrieval reranking](https://github.com/volcengine/OpenViking)**<br><sub>Project · ★38,359</sub> | One Noul per candidate document in a single batched request, with the yes-probability used directly as the relevance score. | `Py`<br><sub>noul</sub> | — |
| **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)**<br><sub>Project · ★27,847</sub> | Two-stage MCP tool search: a wide Choice coarse-ranks the whole catalogue, then a shortlist gets full descriptions plus one Noul each to decide whether it does the job at all. | `Py`<br><sub>choice noul</sub> | — |
| **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)**<br><sub>Project · ★19,990</sub> | Replaces the whole retrieval stack for memory recall — no embeddings, no BM25, no reranker — with one batched Noul per candidate memory. | `Rs`<br><sub>noul</sub> | — |
| **[LanceDB TypeSafeReranker](https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py)**<br><sub>Project · ★11,494</sub> | A vector-database reranker that asks one Noul per result and uses the yes-probability as an absolute relevance score, comparable across queries. | `Py`<br><sub>noul</sub> | — |
| **[no-mistakes: review context selection](https://github.com/kunchenguid/no-mistakes)**<br><sub>Benchmark · ★8,595</sub> | One Score per candidate file to pick review context, with a measured outcome: materially more billed input for essentially no wall-clock gain. | `Go`<br><sub>score</sub> | — |
| **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)**<br><sub>Project · ★1,340</sub> | An Android reply co-pilot that judges intent, timing and risk from on-screen text, while separate models handle OCR and drafting. | `Java`<br><sub>choice score noul</sub> | — |
| **[jev-search](https://github.com/superagents-lab/jev-search)**<br><sub>Project · ★382</sub> | Jev-driven web search: chooses the recency window and the best query rewrite, then reranks results in batches with one noul each. | `TS`<br><sub>choice noul</sub> | — |
| **[pg-jev](https://github.com/realZachi/pg-jev)**<br><sub>Project · ★284</sub> | A real PostgreSQL extension exposing the primitives as SQL functions, so a semantic decision can appear in a WHERE clause over any row type. | `Py` `sh`<br><sub>choice score noul</sub> | — |
| **[jev-mcp](https://github.com/jkudish/jev-mcp)**<br><sub>Plugin · ★240</sub> | A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools. | `JS`<br><sub>choice score noul</sub> | — |
| **[neo4jev](https://github.com/jexp/neo4jev)**<br><sub>Project · ★79</sub> | Puts Jev inside a knowledge graph traversal: at each node it decides which edge is most worth following. | `Py`<br><sub>choice</sub> | — |
| **[Blink](https://github.com/ellipsis-dev/blink)**<br><sub>Project · ★50</sub> | Uses Jev as a codebase navigator: at each directory level it decides which files are most relevant to the question, then descends. | `TS`<br><sub>choice</sub> | `no licence` |

### Structured extraction

_Pull typed fields out of messy text by choosing among candidates rather than generating them._

| Example | What it shows | Code | Caveats |
| --- | --- | :-- | :-- |
| **[Cookbook: Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook)** ⭐<br><sub>Official docs</sub> | Extracts absolute and relative dates by asking for the parts a document names, then resolving and validating them in code with confidence-based review. | `Py` | — |
| **[Cookbook: Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook)** ⭐<br><sub>Official docs</sub> | Regexes find candidate emails, phone numbers and amounts; the model selects the requested span so code can normalise a verbatim value. | `Py`<br><sub>choice</sub> | — |
| **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐<br><sub>Official docs</sub> | Reconstructs Markdown from plain text that lost its formatting, in two requests: one restitches hard-wrapped lines, one classifies every block. | `Py` | — |
| **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐<br><sub>Official docs</sub> | A two-stage mini-then-verify-then-reasoning cascade that reaches most of a big reasoning model's quality at a fraction of the cost. | `Py` | — |

### Classification

_Put an item into a taxonomy, including deep hierarchies walked with probabilities._

| Example | What it shows | Code | Caveats |
| --- | --- | :-- | :-- |
| **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐<br><sub>Official docs</sub> | Classifies annual reports into 75 industry groups, then reads the answer's own confidence to decide whether to report that group or the broader division above it. | `Py`<br><sub>choice</sub> | — |
| **[Cookbook: Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification)** ⭐<br><sub>Official docs</sub> | Walks deep patent, retail, biomedical and source-code taxonomies with a parallel beam search over Choice probabilities. | `Py`<br><sub>choice</sub> | — |
| **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐<br><sub>Official docs</sub> | Decides which of 450 candidate pairs from two product catalogues describe the same thing, with one Score whose three levels are the three available actions. | `Py`<br><sub>score</sub> | — |
| **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐<br><sub>Official docs</sub> | Reconstructs Markdown from plain text that lost its formatting, in two requests: one restitches hard-wrapped lines, one classifies every block. | `Py` | — |
| **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)**<br><sub>Benchmark · ★87,175</sub> | Two Choice questions over threat level and category, held in shadow mode after a blind evaluation found Jev merely tied the incumbent model. | `TS`<br><sub>choice</sub> | `shadow mode` |
| **[json-render](https://github.com/vercel-labs/json-render)**<br><sub>Project · ★17,964 · Vercel Labs</sub> | Vercel Labs' generative UI framework. In its Jev experiment the model does not write JSON token by token — it only picks components, props and layout. | `TS`<br><sub>choice</sub> | — |
| **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)**<br><sub>Project · ★12,276</sub> | Seven distinct email decisions, each with its own separately chosen threshold, falling back to the normal LLM on any error. | `TS`<br><sub>choice noul</sub> | — |
| **[pg-jev](https://github.com/realZachi/pg-jev)**<br><sub>Project · ★284</sub> | A real PostgreSQL extension exposing the primitives as SQL functions, so a semantic decision can appear in a WHERE clause over any row type. | `Py` `sh`<br><sub>choice score noul</sub> | — |
| **[jev-mcp](https://github.com/jkudish/jev-mcp)**<br><sub>Plugin · ★240</sub> | A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools. | `JS`<br><sub>choice score noul</sub> | — |
| **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)**<br><sub>Benchmark · ★190</sub> | Independent Korean-language notes reporting that reversing the order of options shifted a probability enough to flip a 0.9 threshold. | `Py` | `no licence` `unverified` |
| **[perch: semantic code linting](https://github.com/lakeday-org/perch)**<br><sub>Project · ★167</sub> | Tree-sitter finds and ranks methods, then user-authored YAML rules compile into nouls, with severity read as the rubric's expected value rather than the top band. | `JS`<br><sub>choice score noul</sub> | — |
| **[Prism](https://github.com/irfndi/prism-liquidity-agent)**<br><sub>Project · ★68</sub> | Does not place orders. It judges market conditions such as toxic flow and mean reversion, and hands the assessment to the existing strategy. | `TS`<br><sub>choice score</sub> | — |
| **[Blink](https://github.com/ellipsis-dev/blink)**<br><sub>Project · ★50</sub> | Uses Jev as a codebase navigator: at each directory level it decides which files are most relevant to the question, then descends. | `TS`<br><sub>choice</sub> | `no licence` |
| **[SemDecide](https://github.com/sharziki/semdecide)**<br><sub>Plugin · ★27</sub> | Jev as a command-line tool: classify, score and filter straight from a shell, for crawlers, CI and data pipelines. | `Py` `sh`<br><sub>choice score noul</sub> | — |
| **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)**<br><sub>Benchmark · Lindfors</sub> | The best independent test found: 24 Norwegian documents on one pinned model version, opening with a case the model got wrong while correctly reporting low confidence. | — | — |
| **[Jev - The Ultimate Classification Model?](https://youtube.com/watch?v=X117w2Rark8)**<br><sub>Video · Sam Witteveen</sub> | An ML engineer's walkthrough from the classification-task angle, which is the framing closest to what the model actually does. | — | — |
| **[jevai.org community showcase cases](https://www.jevai.org/cases)**<br><sub>Project</sub> | Nine worked community scenarios: intent routing, invoice classification, news filtering, product tagging, moderation, claim verification, CSV validation and more. | — | `unverified` |
| **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)**<br><sub>Benchmark · Near Here</sub> | The only three-way head-to-head found, with each model's prompt tuned separately and the scope limited to one task rather than a general ranking. | — | — |

### ML feature extraction

_Turn free text into numeric features for a classical downstream model._

| Example | What it shows | Code | Caveats |
| --- | --- | :-- | :-- |
| **[Cookbook: Autoresearch feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery)** ⭐<br><sub>Official docs</sub> | An autoresearch loop that proposes questions, turns free text into numeric features, and uses model error to improve a supervised gradient-boosting regressor. | `Py` | — |
| **[Prism](https://github.com/irfndi/prism-liquidity-agent)**<br><sub>Project · ★68</sub> | Does not place orders. It judges market conditions such as toxic flow and mean reversion, and hands the assessment to the existing strategy. | `TS`<br><sub>choice score</sub> | — |
| **[jev-curate](https://github.com/AkashPriyadarshii/jev-curate)**<br><sub>Project · ★18</sub> | Curates training data: JSONL and Parquet rows are judged on quality, relevance and risk before deciding what reaches downstream training. | `Rs`<br><sub>score noul</sub> | — |

### Document triage

_Classify and route incoming documents, invoices and forms._

| Example | What it shows | Code | Caveats |
| --- | --- | :-- | :-- |
| **[jevai.org community showcase cases](https://www.jevai.org/cases)**<br><sub>Project</sub> | Nine worked community scenarios: intent routing, invoice classification, news filtering, product tagging, moderation, claim verification, CSV validation and more. | — | `unverified` |

### Support triage

_Route support tickets and conversations by intent and urgency._

| Example | What it shows | Code | Caveats |
| --- | --- | :-- | :-- |
| **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐<br><sub>Official docs</sub> | The canonical first call: one support ticket, one Choice, one Score and one Noul in a single request, in Python, JS and cURL. | `Py` `TS` `sh`<br><sub>choice score noul</sub> | — |
| **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br><sub>Tutorial · ★4,554</sub> | A graded course from a first call through each primitive, state shapes and criteria, to ticket triage and a multi-step workflow, mirroring all four official patterns. | `Py`<br><sub>choice score noul</sub> | — |
| **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)**<br><sub>Snippet</sub> | A minimal first call asking a choice, a score and a noul together, annotated with the asymmetries that catch people out. | `Py`<br><sub>choice score noul</sub> | `code untested` |
| **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)**<br><sub>Tutorial · Mehul Gupta</sub> | Walks through use case after use case — agent routing, an in-agent decision layer, ticket triage — each with a concrete option set and a sample response. | `Py`<br><sub>choice</sub> | `paywall` |
| **[Jev on AI/ML API](https://docs.aimlapi.com/api-references/decision-models/typesafe/jev)**<br><sub>Integration</sub> | Another gateway route, notable because its endpoint path and request envelope differ again from both the native API and Cloudflare's. | `Py`<br><sub>noul choice score</sub> | — |
| **[Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/)**<br><sub>Integration</sub> | Workers AI binding and REST samples asking a noul, a choice and a score in one call, with the full response including per-answer confidence. | `TS` `sh`<br><sub>noul choice score</sub> | — |
| **[spring-ai-typesafe](https://spring.io/blog/2026/09/21/spring-ai-typesafe-structured-judgment)**<br><sub>Integration</sub> | A community Spring AI starter bringing typed decisions to Java, with a builder API over the three question types. | `Java`<br><sub>choice score noul</sub> | — |

### Content scoring

_Score quality, risk or relevance on an ordered scale._

| Example | What it shows | Code | Caveats |
| --- | --- | :-- | :-- |
| **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐<br><sub>Official docs</sub> | Adds an explicit "uncertain" outcome to moderation decisions and measures label agreement against the share of actions taken automatically. | `Py`<br><sub>choice</sub> | — |
| **[Pattern: Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring)** ⭐<br><sub>Official docs</sub> | Break one broad judgement into atomic scores and combine them with weights that live in your code, not in the prompt. | `Py`<br><sub>score</sub> | — |
| **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)**<br><sub>Project · ★187,483</sub> | Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files. | `Py`<br><sub>choice score noul</sub> | — |
| **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)**<br><sub>Benchmark · ★87,175</sub> | Two Choice questions over threat level and category, held in shadow mode after a blind evaluation found Jev merely tied the incumbent model. | `TS`<br><sub>choice</sub> | `shadow mode` |
| **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br><sub>Tutorial · ★4,554</sub> | A graded course from a first call through each primitive, state shapes and criteria, to ticket triage and a multi-step workflow, mirroring all four official patterns. | `Py`<br><sub>choice score noul</sub> | — |
| **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)**<br><sub>Project · ★1,340</sub> | An Android reply co-pilot that judges intent, timing and risk from on-screen text, while separate models handle OCR and drafting. | `Java`<br><sub>choice score noul</sub> | — |
| **[jev-review](https://github.com/devagrawal09/jev-review)**<br><sub>Project · ★495</sub> | Pre-screens code review with Jev to surface high-risk changes for a more expensive model or a person, with a local dashboard. | `TS`<br><sub>choice score noul</sub> | `archived` |
| **[pg-jev](https://github.com/realZachi/pg-jev)**<br><sub>Project · ★284</sub> | A real PostgreSQL extension exposing the primitives as SQL functions, so a semantic decision can appear in a WHERE clause over any row type. | `Py` `sh`<br><sub>choice score noul</sub> | — |
| **[perch: semantic code linting](https://github.com/lakeday-org/perch)**<br><sub>Project · ★167</sub> | Tree-sitter finds and ranks methods, then user-authored YAML rules compile into nouls, with severity read as the rubric's expected value rather than the top band. | `JS`<br><sub>choice score noul</sub> | — |
| **[killmyidea](https://github.com/monteduro/killmyidea)**<br><sub>Project · ★73</sub> | Scores a startup idea across several dimensions and returns a verdict of kill, fix or ship. | `TS`<br><sub>score choice</sub> | `no licence` |
| **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)**<br><sub>Project · ★42 · brainstormity</sub> | A Discord moderation bot: a Choice tiers each message while a Noul carries ban urgency, and an admin pardon is fed back as a safe precedent in later requests. | `Py`<br><sub>choice noul</sub> | — |
| **[SemDecide](https://github.com/sharziki/semdecide)**<br><sub>Plugin · ★27</sub> | Jev as a command-line tool: classify, score and filter straight from a shell, for crawlers, CI and data pipelines. | `Py` `sh`<br><sub>choice score noul</sub> | — |
| **[jev-curate](https://github.com/AkashPriyadarshii/jev-curate)**<br><sub>Project · ★18</sub> | Curates training data: JSONL and Parquet rows are judged on quality, relevance and risk before deciding what reaches downstream training. | `Rs`<br><sub>score noul</sub> | — |
| **[A deep dive into Jev, TypeSafe's System One model](https://flaviocopes.com/jev/)**<br><sub>Tutorial · Flavio Copes</sub> | The densest independent explainer: code in JS, Python and the AI SDK, all three answer shapes, the advanced patterns, and an honest list of where the model fails. | `JS` `Py` `TS`<br><sub>choice score noul</sub> | — |
| **[jevai.org community showcase cases](https://www.jevai.org/cases)**<br><sub>Project</sub> | Nine worked community scenarios: intent routing, invoice classification, news filtering, product tagging, moderation, claim verification, CSV validation and more. | — | `unverified` |

### Overview

_Surveys the model or the space rather than one pattern._

<details>
<summary><b>53</b> rows — click to expand</summary>

| Example | What it shows | Code | Caveats |
| --- | --- | :-- | :-- |
| **[typesafe-ai/skills](https://github.com/typesafe-ai/skills)** ⭐<br><sub>Plugin · ★1,565</sub> | The official agent-skills repository behind the Claude Code plugin, holding the SKILL.md that teaches an agent the System One API. | `sh` | — |
| **[system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python)** ⭐<br><sub>SDK · ★241</sub> | A drop-in TypeSafeClient replacement backed by ordinary LLM APIs, so you can run Jev-shaped code without Jev access. | `Py` | — |
| **[@typesafe-ai/sdk (TypeScript / JavaScript)](https://github.com/typesafe-ai/typesafe-sdk-js)** ⭐<br><sub>SDK · ★214</sub> | The official TypeScript client. Ships ESM, CJS and type declarations, with lowercase choice()/score()/noul() helper factories. | `TS` `JS`<br><sub>choice score noul</sub> | — |
| **[typesafe-sdk (Python)](https://github.com/typesafe-ai/typesafe-sdk-python)** ⭐<br><sub>SDK · ★186</sub> | The official Python client. Sync and async clients, retry policy with retry-after support, and Choice/Score/Noul helper classes. | `Py`<br><sub>choice score noul</sub> | — |
| **[API reference](https://docs.typesafe.ai/api)** ⭐<br><sub>Official docs</sub> | The one endpoint, POST /v1/systemone, with the exact request and answer shapes for all three question types. | `sh` `Py` `TS` | — |
| **[Models, pricing and limits](https://docs.typesafe.ai/models)** ⭐<br><sub>Official docs</sub> | The authoritative sheet: jev-1.13.0, $0.042 per Mtok input with output free, 64k context, 32k for state plus the longest question, text input only. | `sh` `Py` `TS` | — |
| **[Official agent skill for Claude Code](https://docs.typesafe.ai/agent-skill)** ⭐<br><sub>Official docs</sub> | Installs a TypeSafe skill into Claude Code so an agent can write correct Jev calls without you pasting the API shape each time. | `sh` | — |
| **[Primitives: Choice, Score, Noul](https://docs.typesafe.ai/primitives)** ⭐<br><sub>Official docs</sub> | What each primitive is for and how to write criteria, including the 255-option cap on Choice and the 2-10 level range on Score. | `Py` `TS`<br><sub>choice score noul</sub> | — |
| **[Introducing System One models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)** ⭐<br><sub>Article · Diogo Almeida</sub> | The launch post: what a System One model is, why decisions were split from generation, and the vendor's latency and cost claims. | — | `vendor numbers` |
| **[Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)** ⭐<br><sub>Official docs</sub> | The vendor's own list of where the model fails: literal reading, arithmetic and counting, date comparison, indirection, large noisy states, adversarial content. | — | — |
| **[Use case map](https://docs.typesafe.ai/concepts/use-case-map)** ⭐<br><sub>Official docs</sub> | The vendor's own taxonomy: five headline categories, nineteen industry groups, and ten decision shapes from classification through to structured data extraction. | — | — |
| **[OpenCode Zen: Jev resale](https://github.com/anomalyco/opencode)**<br><sub>Integration · ★209,172</sub> | A coding agent whose hosted gateway resells Jev, including a free tier model id. | `TS` | — |
| **[Opik TypeSafe tracker](https://github.com/comet-ml/opik/blob/main/sdks/python/src/opik/integrations/typesafe/opik_tracker.py)**<br><sub>Project · ★22,187</sub> | Wraps the sync and async clients so every system_one call is recorded as a traced span. | `Py` | — |
| **[@effect/ai-typesafe](https://github.com/Effect-TS/effect)**<br><sub>Integration · ★16,165</sub> | Implements Effect's DecisionModel interface over Jev, with an unusually candid caveat about unverified rounding behaviour. | `TS`<br><sub>choice score noul</sub> | — |
| **[rig-typesafeai](https://github.com/0xPlaygrounds/rig)**<br><sub>Integration · ★8,692</sub> | A Rust integration with compile-time-checked option counts, so an over-255 Choice fails to build rather than at runtime. | `Rs`<br><sub>choice score noul</sub> | — |
| **[Bifrost TypeSafe gateway route](https://github.com/maximhq/bifrost/tree/dev/core/providers/typesafe)**<br><sub>Project · ★8,222</sub> | A Go gateway provider that passes the native API through one-to-one, so the official SDKs work by changing only the base URL. | `Go` | — |
| **[Kiln: Jev adapter](https://github.com/Kiln-AI/Kiln)**<br><sub>Integration · ★5,078</sub> | A JSON-Schema-to-question compiler wired into the adapter registry, with an honest note on what it cannot serve. | `Py`<br><sub>choice score noul</sub> | — |
| **[ruby_llm: TypeSafe provider](https://github.com/crmne/ruby_llm)**<br><sub>Integration · ★4,396</sub> | A Ruby provider with a dedicated System One protocol, the main route into Jev from Ruby. | `Rb`<br><sub>choice score noul</sub> | — |
| **[SemIf](https://github.com/TheoLeeCJ/SemIf)**<br><sub>Jev-like alternative · ★3,312</sub> | An independent semantic-if implementation that states up front it is unaffiliated with Jev or TypeSafe. | `Py` | `not Jev` |
| **[kev](https://github.com/jaredpalmer/kev)**<br><sub>Jev-like alternative · ★2,544 · Jared Palmer</sub> | A trainable, self-hostable family of Jev-like decision models with a System One compatible API, so the official SDK can point at your own server. | `Py`<br><sub>choice score noul</sub> | `not Jev` |
| **[NanoJev](https://github.com/TianyuCodings/NanoJev)**<br><sub>Jev-like alternative · ★1,830</sub> | A self-described nano replica of Jev, for reading rather than for production. | `Py` | `not Jev` |
| **[jevlike](https://github.com/vinnylarouge/jevlike)**<br><sub>Jev-like alternative · ★1,169 · vinnylarouge</sub> | An independent, trainable model with the same input and output shape as Jev: text plus N options in, one probability per option out, in a single pass. | `Py` | `not Jev` |
| **[simple-jev](https://github.com/featherless-ai/simple-jev)**<br><sub>Jev-like alternative · ★455</sub> | Turns any open-weights model into a Jev-shaped endpoint by reading next-token logits, with the server constructing the JSON rather than the model generating it. | `Py` | `not Jev` |
| **[jev-skill](https://github.com/wuyoscar/jev-skill)**<br><sub>Plugin · ★372</sub> | An agent skill plus CLI that validates all three primitives, requires explicit consent before a billed call, and forbids inventing output when simulating. | `Py`<br><sub>choice score noul</sub> | — |
| **[awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects)**<br><sub>Project · ★326 · logicrw</sub> | A sibling directory aiming at ecosystem breadth with commit-pinned sources, four README languages and a generated site. | `JS` | — |
| **[typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp)**<br><sub>Plugin · ★225</sub> | The easiest first step once you have a key: registers Jev into Claude Code, Claude Desktop, Codex and Pi with one command. | `Go`<br><sub>choice score noul</sub> | — |
| **[awesome-jev (fatwang2)](https://github.com/fatwang2/awesome-jev)**<br><sub>Project · ★187 · fatwang2</sub> | A sibling directory whose submissions are reviewed by Jev itself, with a notably thorough list of multi-language community clients. | `JS` | — |
| **[OpenDecision](https://github.com/deepanwadhwa/OpenDecision)**<br><sub>Jev-like alternative · ★51 · deepanwadhwa</sub> | An open-source semantic decision engine running a local zero-shot model, with a FastAPI server proven wire-compatible with the official SDK. | `Py`<br><sub>choice score noul</sub> | `not Jev` |
| **[@ai-sdk/typesafe-ai provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai)**<br><sub>SDK</sub> | The AI SDK provider package for calling TypeSafe directly, with a sample covering all three question types and nested criteria shapes. | `TS` `JS`<br><sub>choice score noul</sub> | — |
| **[aegis: TypeSafe as a first-class provider](https://github.com/dvjn/aegis)**<br><sub>Project · ★0 · dvjn</sub> | A personal Rust AI gateway with a TypeSafe provider, usage extraction and alias resolution tested against real response bodies. | `Rs` | `code untested` |
| **[Build Your Own JEV Locally: Run a 100% Private AI Agent on Your Machine](https://medium.com/coding-nexus/build-your-own-jev-locally-run-a-100-private-ai-agent-on-your-machine-bb98126d394a)**<br><sub>Jev-like alternative · DataScience Nexus</sub> | Despite the title, this does not run Jev. It builds a Jev-like decision engine from an open LLM using constrained next-token scoring. | `Py` | `not Jev` `code untested` `paywall` |
| **[Jev Explained: How to Add Fast, Typed Decisions to an AI Agent](https://aihubmix.com/blog/jev-explained-how-to-add-fast-typed-decisions-to-an-ai-agent)**<br><sub>Article</sub> | A third-party explainer with a useful architecture sketch and an unusually honest list of cases where you should not use a decision model. | `Py` | `code untested` |
| **[jevai.org community site](https://www.jevai.org/)**<br><sub>Project</sub> | An unaffiliated community site with a playground, a preset decision API, an MCP server, downloadable skills and a gallery of community apps. | `sh` | `3rd-party key` `unverified` |
| **[Tracing Jev calls with Langfuse](https://langfuse.com/integrations/model-providers/typesafe)**<br><sub>Integration</sub> | The only platform with dedicated Jev observability: an OpenInference instrumentor that traces every decision call over OpenTelemetry. | `Py`<br><sub>choice score noul</sub> | — |
| **[TypeSafe AI Jev now available on AI Gateway](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway)**<br><sub>Integration</sub> | Vercel's launch note for Jev on AI Gateway, with an experimental_evaluate sample using the model string typesafe-ai/jev. | `TS`<br><sub>noul</sub> | — |
| **[TypeSafe models in Pydantic AI](https://pydantic.dev/docs/ai/models/typesafe/)**<br><sub>Integration</sub> | First-party Pydantic AI support: an Agent with output_type=bool over the typesafe:jev-latest model string. | `Py` | — |
| **[TypeSafe pass-through on LiteLLM](https://docs.litellm.ai/docs/pass_through/typesafe)**<br><sub>Integration</sub> | Proxy Jev through LiteLLM for unified keys and cost tracking, with any path under /typesafe/ passed straight through. | `sh` | — |
| **[TypeSafe-compatible API on Vercel AI Gateway](https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe)**<br><sub>Integration</sub> | Point the official TypeSafe SDK at Vercel by changing one baseURL, or call the gateway's systemone endpoint directly with cURL. | `TS` `sh`<br><sub>noul</sub> | — |
| **[typesafe-go](https://github.com/Nibir1/typesafe-go)**<br><sub>SDK · ★0 · Nibir1</sub> | A zero-dependency community Go SDK, including a static analyser that flags poorly designed questions at compile time. | `Go`<br><sub>choice score noul</sub> | `code untested` |
| **[awesome-jev (yibie)](https://github.com/yibie/awesome-jev)**<br><sub>Project · ★1,010</sub> | Currently the most-starred sibling directory in this space. | — | `no licence` |
| **[A new kind of AI model from a ChatGPT inventor is thrilling developers](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)**<br><sub>Article · Tim Fernholz</sub> | The only launch coverage with first-hand developer quotes rather than vendor figures, including a caution that interpreting the thresholds is now your job. | — | — |
| **[AI model "Jev" to make machines decide faster](https://www.heise.de/en/news/AI-model-Jev-to-make-machines-decide-faster-11457071.html)**<br><sub>Article · Tomislav Bezmalinović</sub> | Focuses on the missing explainability — the model returns no reasoning in language — and on every published benchmark coming from the vendor. | — | — |
| **[Hacker News: Introducing System One Models and Jev](https://news.ycombinator.com/item?id=49717558)**<br><sub>Discussion</sub> | The launch thread, and the densest single collection of scepticism: unsupported RLCD claims, apples-to-oranges latency comparisons, and the deliberate absence of public benchmarks. | — | — |
| **[Jev (AI model) on Wikipedia](https://en.wikipedia.org/wiki/Jev_(AI_model))**<br><sub>Article</sub> | Most useful as an index: its reference list is a fast route to the coverage worth reading. | — | — |
| **[Jev by TypeSafe: A Decision Model for AI Agents](https://beam.ai/agentic-insights/jev-typesafe-ai-agents)**<br><sub>Article</sub> | An agent-builder's framing of where a decision model sits in an agent stack. | — | `marketing` |
| **[Jev Cuts AI Decision Costs 100x And Vercel, Cloudflare Rushed To Add It](https://www.forbes.com/sites/josipamajic/2026/09/19/jev-cuts-ai-decision-costs-100x-and-vercel-cloudflare-rushed-to-add-it/)**<br><sub>Article · Josipa Majic Predin</sub> | Mainstream coverage of the launch and the speed with which gateways added support. | — | `vendor numbers` `paywall` |
| **[Jev From TypeSafe is a New Class of AI Model that is FAST and CHEAP - But There is a Caveat!](https://youtube.com/watch?v=qdji39XXgEY)**<br><sub>Video · Gary Explains</sub> | A review that puts the limitation in the title rather than burying it. | — | — |
| **[Jev: System One models for Prod, not God](https://www.latent.space/p/jev)**<br><sub>Discussion · Latent Space</sub> | The only long-form founder interview: why RLHF was the wrong optimisation target, why public benchmarks were withheld, and the all-synthetic data approach. | — | — |
| **[Jev: TypeSafe's System One Model Explained](https://www.datacamp.com/blog/system-one-models-jev)**<br><sub>Article · Matt Crabtree</sub> | A neutral survey of the architecture, the claimed benchmarks and the pricing, which states plainly that no large independent reproduction had surfaced. | — | — |
| **[jevai.org community app gallery](https://www.jevai.org/apps)**<br><sub>Project</sub> | Thirty-six community builds curated from social posts: browser agents, spreadsheet tooling, inbox search by intent, ad blocking with judgement, games and robotics. | — | `unverified` |
| **[RLCD explained: Reinforcement Learning for Calibrated Decisions](https://systemonemodels.org/guides/rlcd-explained/)**<br><sub>Article</sub> | An independent write-up whose most useful finding is a negative one: there is no paper, no reward function, no dataset description and no reproducible evaluation for RLCD. | — | — |
| **[TypeSafe AI debuts model for machines that plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711)**<br><sub>Article · Thomas Claburn</sub> | The most sceptical mainstream piece: it challenges the no-hallucination framing on the grounds that a well-formed answer is not the same as a correct one. | — | — |
| **[TypeSafe on OpenRouter](https://openrouter.ai/typesafe)**<br><sub>Integration</sub> | OpenRouter's listing for Jev, with its own model ids and the unusual pricing shape of paid input and free output. | — | — |

</details>

## By resource kind

The same rows grouped by what you will find when you open the link.

| Kind | Examples | What you will find |
| --- | :-- | --- |
| **Official docs** | `31` ███████████▎ | Vendor documentation, cookbooks and pattern pages. |
| **SDK** | ` 5` █▉ | Client libraries, official and community. |
| **Integration** | `18` ██████▌ | A gateway, framework or platform route to the model. |
| **Snippet** | ` 4` █▌ | Small runnable examples in this repository. |
| **Project** | `44` ████████████████ | An application or library that calls Jev in anger. |
| **Plugin** | `11` ████ | Editor, agent and MCP integrations you can install. |
| **Tutorial** | ` 5` █▉ | Step-by-step material with code. |
| **Benchmark** | ` 6` ██▏ | Measurement. Check whether it is independent or vendor-reported. |
| **Article** | `12` ████▍ | Explainers, analysis and launch coverage. |
| **Video** | ` 3` █▏ | Walkthroughs and reviews. |
| **Discussion** | ` 2` ▊ | Threads worth reading, including the sceptical ones. |
| **Jev-like alternative** | ` 7` ██▌ | Independent reimplementations. These do NOT call Jev. |

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

## What is verified, and what is not

- ✅ **Verified** — the URL returned a success status on the date in `checked`; a person opened it and wrote the summary from what was there; for code rows the call site was read to confirm which primitives are used; stars and licences came from the GitHub API.
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
| `archived` | Development has visibly stopped. |

## Machine-readable data

One entry per example, validated against a JSON Schema on every push.

| File | What it is |
| --- | --- |
| [`catalog.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/catalog.json) | 148 entries |
| [`retired.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/retired.json) | 0 retired |
| [`compat.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/compat.json) | The platform matrix behind `docs/compatibility.md` |
| [`schema/entry.schema.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/schema/entry.schema.json) | One entry's shape |
| [`llms.txt`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/llms.txt) | For agents, with the caveats spelled out |

## Contributing and licence

Corrections take priority over additions — a wrong row costs more than a missing one. See [CONTRIBUTING.md](CONTRIBUTING.md); the bar is *could a reader act on this row without opening the link?*

Code in `scripts/`, `site/` and `examples/` is [MIT](LICENSE-MIT). Catalog metadata is [CC0-1.0](LICENSE-CC0), with a per-row `license` field. Linked works keep their own licences — `repo_license` records what each declares.
