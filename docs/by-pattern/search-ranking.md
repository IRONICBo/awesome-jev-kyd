# Search & ranking

<sub>[awesome-jev](../../README.md) · [中文](search-ranking.zh-CN.md)</sub>

_Score or re-rank candidates from a cheaper retrieval step._

Every catalogued example of this decision — 44 of them, official first, then rows with code, then by stars. The same rows, with caveats, are in [the index](../../README.md#search--ranking); [the site](https://kydlikebtc.github.io/awesome-jev/?p=search-ranking&lang=en) can filter them further by language, primitive and kind.

- **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐ — Scores each retrieved passage, then decides in code which reach the answering model — keeping contradictory ones flagged and dropping ones carrying prompt injection.
  <sub>`Official docs` · `Py`</sub>

- **[Cookbook: Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find)** ⭐ — Semantic search over a terms-of-service document: one request scores 218 line ids with a Choice, and a Noul checks whether the document answers at all.
  <sub>`Official docs` · `Py` · `choice` · `noul`</sub>

- **[Cookbook: Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe)** ⭐ — Re-ranks 30-passage BM25 shortlists for 40 legal queries with one question per query-candidate pair, reporting large top-1 and top-10 gains.
  <sub>`Official docs` · `Py`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)** — Seven production blocks — choice, score, yes/no, ask-many, route, pick-best, filter — with a UTF-8 byte budget, verbatim wire capture and eleven test files.
  <sub>`Project` · ★187,503 · `Py` · `choice` · `score` · `noul`</sub>

- **[OpenViking: retrieval reranking](https://github.com/volcengine/OpenViking)** — One Noul per candidate document in a single batched request, with the yes-probability used directly as the relevance score.
  <sub>`Project` · ★38,483 · `Py` · `noul`</sub>

- **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)** — Two-stage MCP tool search: a wide Choice coarse-ranks the whole catalogue, then a shortlist gets full descriptions plus one Noul each to decide whether it does the job at all.
  <sub>`Project` · ★27,873 · `Py` · `choice` · `noul`</sub>

- **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)** — Replaces the whole retrieval stack for memory recall — no embeddings, no BM25, no reranker — with one batched Noul per candidate memory.
  <sub>`Project` · ★20,038 · `Rs` · `noul`</sub>

- **[LanceDB TypeSafeReranker](https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py)** — A vector-database reranker that asks one Noul per result and uses the yes-probability as an absolute relevance score, comparable across queries.
  <sub>`Project` · ★11,505 · `Py` · `noul`</sub>

- **[no-mistakes: review context selection](https://github.com/kunchenguid/no-mistakes)** — One Score per candidate file to pick review context, with a measured outcome: materially more billed input for essentially no wall-clock gain.
  <sub>`Benchmark` · ★8,609 · `Go` · `score`</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** — An Android reply co-pilot that judges intent, timing and risk from on-screen text, while separate models handle OCR and drafting.
  <sub>`Project` · ★4,213 · `Java` · `choice` · `score` · `noul`</sub>

- **[hippo-memory](https://github.com/kitfunso/hippo-memory)** — Biologically-inspired memory for AI agents. Decay, retrieval strengthening, consolidation. Zero runtime deps, SQLite, MCP. Benchmarked retrieval with an opt-in TypeSafe Jev reranker.
  <sub>`Benchmark` · ★756 · kitfunso · `TS`</sub>

- **[jev-search](https://github.com/superagents-lab/jev-search)** — Jev-driven web search: chooses the recency window and the best query rewrite, then reranks results in batches with one noul each.
  <sub>`Project` · ★417 · `TS` · `choice` · `noul`</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)** — A real PostgreSQL extension exposing the primitives as SQL functions, so a semantic decision can appear in a WHERE clause over any row type.
  <sub>`Project` · ★315 · `Py` · `sh` · `choice` · `score` · `noul`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — A ready-made judgement toolbox for agents: fact verification, content screening, semantic ranking, classification and extraction as separate tools.
  <sub>`Plugin` · ★290 · `JS` · `choice` · `score` · `noul`</sub>

- **[vector-graph-rag](https://github.com/zilliztech/vector-graph-rag)** — Graph RAG with pure vector search, achieving SOTA performance in multi-hop reasoning scenarios.
  <sub>`Project` · ★246 · zilliztech · `Py`</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — The pipe layer of an AI nervous system: one interface connecting provider neurons to an application, across three inference types — generate, stream, and decide. Decide returns typed, calibrated judgments (boolean/choice/score) via TypeSafe Jev, not text.
  <sub>`Plugin` · ★138 · juspay · `TS`</sub>

- **[jev-semgrep](https://github.com/uehaj/jev-semgrep)** — grep by meaning, across languages. TypeSafe Jev scores every line against a meaning; combine meanings with AND/OR/NOT. 意味で探す grep。日本語で英語を、英語で日本語を検索できる
  <sub>`Project` · ★130 · uehaj · `JS`</sub>

- **[skillranker](https://github.com/Dicklesworthstone/skillranker)** — Ranks an agent's skills for the next step using live session context, with Claude Code hooks.
  <sub>`Plugin` · ★114 · dicklesworthstone · `Rs`</sub>

- **[jev-shell-history](https://github.com/mrnugget/jev-shell-history)** — Fish-style zsh history autosuggestions, ranked by Jev rather than by recency.
  <sub>`Project` · ★104 · mrnugget · `TS` · ⚠ `no licence`</sub>

- **[neo4jev](https://github.com/jexp/neo4jev)** — Puts Jev inside a knowledge graph traversal: at each node it decides which edge is most worth following.
  <sub>`Project` · ★100 · `Py` · `choice`</sub>

- **[jegrep](https://github.com/can1357/jegrep)** — Semantic grep: find code by describing what you're looking for, powered by Jev.
  <sub>`Project` · ★83 · can1357 · `Rs`</sub>

- **[Blink](https://github.com/ellipsis-dev/blink)** — Uses Jev as a codebase navigator: at each directory level it decides which files are most relevant to the question, then descends.
  <sub>`Project` · ★65 · `TS` · `choice` · ⚠ `no licence`</sub>

- **[jev-social](https://github.com/socai-io/jev-social)** — Social-platform research with typed routing and browser evidence.
  <sub>`Project` · ★47 · socai-io · `JS`</sub>

- **[jev-recall](https://github.com/samdotmak/jev-recall)** — Retrieve by relevance, not resemblance: filter an AI assistant's memories with TypeSafe's Jev
  <sub>`Project` · ★32 · samdotmak · `TS`</sub>

- **[pi-jev-skill-picker](https://github.com/safzanpirani/pi-jev-skill-picker)** — Rank Pi Agent Skills for the current task with TypeSafe Jev
  <sub>`Plugin` · ★29 · safzanpirani · `TS`</sub>

- **[jgrep](https://github.com/keltokhy/jgrep)** — grep, but the pattern is a description. Filters lines by meaning with TypeSafe's Jev decision model: ~200 ms and a thousandth of a cent per line.
  <sub>`Project` · ★21 · keltokhy · `Py`</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-jev)** — Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.
  <sub>`Project` · ★17 · keeltrace · `Py`</sub>

- **[jgrep (npm: jevgrep)](https://github.com/kyu1204/jgrep)** — grep for what code does: one Noul per code chunk, diff hunk or CSV row, printed as file:line hits with probabilities. --diff gates a PR in CI on a rule written in English (exit 0 match / 1 clean / 2 error); --tests lists the test files a diff can affect.
  <sub>`Project` · ★16 · kyu1204 · `TS` · `noul` · `choice` · `score`</sub>

- **[jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark)** — Reproducible benchmark for measuring Jev reranking quality, latency, and cost in RAG
  <sub>`Benchmark` · ★14 · erendikmenn · `Py`</sub>

- **[jevql](https://github.com/kylemclaren/jevql)** — Semantic SQL for Postgres, powered by Jev
  <sub>`Project` · ★12 · kylemclaren · `Go`</sub>

- **[every](https://github.com/sufianetaouil/every)** — Ask a yes/no question of every function in a codebase. Ranked answers in seconds, for cents. Grep whose pattern is a question, powered by TypeSafe Jev.
  <sub>`Project` · ★7 · sufianetaouil · `Py`</sub>

- **[jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench)** — An independent head-to-head against dedicated rerankers across fourteen datasets.
  <sub>`Benchmark` · ★6 · anessbelbati · `Py`</sub>

- **[jev-nlgrep](https://github.com/YehuiTang0316/jev-nlgrep)** — Search code and text by meaning with natural-language grep, powered by Jev.
  <sub>`Project` · ★4 · yehuitang0316 · `TS`</sub>

- **[jev-reranker](https://github.com/shinpr/jev-reranker)** — Rerank, filter, and compress JSON search results with TypeSafe AI's Jev.
  <sub>`Project` · ★4 · shinpr · `Rs`</sub>

- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** — Cut Claude Code's skill manifest by ~75% with TypeSafe Jev. Scores every installed skill for relevance and hides the rest via skillOverrides — 12,750 → 3,185 tokens on a 217-skill install, for $0.0009 a session.
  <sub>`Plugin` · ★4 · shivampansuriya · `JS`</sub>

- **[llama-index-jev](https://github.com/WiktorB2004/llama-index-jev)** — LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge.
  <sub>`Project` · ★4 · wiktorb2004 · `Py`</sub>

- **[jev-assist](https://github.com/glud123/jev-assist)** — Don't burn your expensive main model on grep-and-guess grunt work — let jev rank the whole repo, and save the main model for reading the right files and writing the right code.
  <sub>`Project` · ★3 · glud123 · `JS`</sub>

- **[typesafe-mod](https://github.com/BeLazy167/typesafe-mod)** — Claude Code mod that routes decisions to TypeSafe's Jev model: ranks installed skills per prompt, and answers the agent's own this-or-that questions when confident.
  <sub>`Plugin` · ★3 · belazy167 · `TS`</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps.
  <sub>`Plugin` · ★2 · hamakyo · `TS`</sub>

- **[typesafe-as-a-judge](https://github.com/E-FL/typesafe-as-a-judge)** — Unofficial community MCP plugin for Codex and Claude Code using TypeSafe Jev for bounded routing, ranking, extraction, verification, and escalation
  <sub>`Plugin` · ★2 · e-fl · `JS`</sub>

- **[jev-engineering](https://github.com/eugeniughelbur/jev-engineering)** — The decision layer for AI agents. Typed, calibrated decisions in ~400ms for two hundredths of a cent: gate tool calls, route models, rank options. With the 300-call injection test that found what breaks.
  <sub>`Project` · ★1 · eugeniughelbur · `Py`</sub>

- **[jevgrep](https://github.com/allebee/jevgrep)** — grep by meaning: pipe in any text, ask a yes/no question in plain English, get only the matching lines. Works behind tail -f, about $0.004 per 1,000 lines, powered by TypeSafe's Jev.
  <sub>`Project` · ★1 · allebee · `Py`</sub>

- **[jev-bfs](https://github.com/komikat/jev-bfs)** — Wikipedia link races with direct Jev ranking and a live terminal display.
  <sub>`Project` · ★0 · komikat · `Py`</sub>

- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** — Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and invariant measurements of TypeSafe AI's Jev: passes six pre-registered gates on 360 labeled rows, fails four of six on graded product relevance.
  <sub>`Benchmark` · ★0 · yodablocks · `Py`</sub>

---

<sub>Generated from `catalog.json` by `scripts/build_readme.py`. Edit the catalogue, not this file — CI fails if the two disagree.</sub>
