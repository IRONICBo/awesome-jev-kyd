# MCP server

Query the catalogue from an agent instead of reading it.

A catalogue about how agents make decisions that only humans can read is a
strange artefact. This exposes it: an assistant about to wire Jev into
something can ask for examples of the exact decision it is making, on the
platform it is using, in the language it is writing.

## Install

```bash
pip install -r mcp/requirements.txt
```

Then register it. For Claude Code:

```bash
claude mcp add awesome-jev -- python3 /absolute/path/to/awesome-jev/mcp/server.py
```

Any MCP client works; it speaks stdio.

## Tools

| Tool | What it answers |
| --- | --- |
| `search_examples` | "Show me safety-gating examples in TypeScript that call `noul`." |
| `get_example` | One row in full, including its sources and its `evidence`. |
| `list_patterns` | The decision taxonomy, with how many examples exist for each. |
| `compatibility` | Model string, field names, request shape and env var per platform. |
| `check_model_string` | "Is `typesafe/jev-1` real?" — it is not, and that matters. |

## Three things it does on purpose

**Caveats are never optional.** Every result carries its flags. An agent that
got a recommendation without `not-jev` or `vendor-reported` attached would be
worse informed than one that read the README.

**Reimplementations are excluded by default.** Rows flagged `not-jev` do not
call the API and `shadow-mode-only` rows are deliberately inert; neither
answers "how do I do this". Pass `include_non_jev=True` when you want them.

**No network.** It reads this repository's own JSON, so it works offline and
cannot disagree with the published catalogue.

## Why this one file has a dependency

Everything else here is stdlib-only, so CI is `setup-python` with no install
step. Hand-rolling stdio JSON-RPC would keep that streak, but a subtly broken
MCP server is worse than a dependency, and nothing in the build pipeline
imports this module.
