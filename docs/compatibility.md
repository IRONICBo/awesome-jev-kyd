# Cross-platform compatibility

One model, many front doors — and the front doors do not agree. The same request
needs a different model string, a different field name for the yes/no type, a
different request envelope and a different environment variable depending on how
you reach it. Porting code between gateways is not a URL swap.

This page exists because that is the single most expensive thing to discover by
debugging.

> **Provenance.** The native API row was read directly from the official raw
> Markdown docs. Every other row was read from that platform's own
> documentation, cited in the catalog rows for that platform. Both this page and
> the platform docs move fast — **open the linked doc before you ship**. Where a
> detail could not be confirmed from a primary source, it is left out rather than
> guessed.

---

## Model string

There is no portable model string. This is the most common porting bug.

| How you reach it               | String to send                                                |
| ------------------------------ | ------------------------------------------------------------- |
| TypeSafe API directly          | `jev-latest` · `jev-preview` · `jev-1.13.0`                   |
| Vercel AI Gateway              | `typesafe-ai/jev`                                             |
| Cloudflare Workers AI          | `typesafe/jev`                                                |
| OpenRouter                     | `typesafe/jev-1.13` · `~typesafe/jev-latest` (note the tilde) |
| AI/ML API                      | `typesafe/jev`                                                |
| Pydantic AI                    | `typesafe:jev-latest`                                         |
| `@ai-sdk/typesafe-ai` (direct) | `jev-latest`                                                  |

**Pin a version rather than an alias** once you have tuned any threshold. An
alias moves when a release ships, and the answers behind it can change with no
change on your side. The response reports the versioned ID that actually
answered, so log it.

---

## The yes/no primitive is named twice

This one silently changes your code, not just your config.

| Surface                                  | Type name | Read the answer from |
| ---------------------------------------- | --------- | -------------------- |
| Native API, Cloudflare, LiteLLM, Bifrost | `noul`    | `.noul`              |
| Vercel AI SDK evaluation API             | `boolean` | `.probability`       |

Both are the same primitive. If you move from the AI SDK evaluation path to the
native path, every `type: 'boolean'` becomes `type: 'noul'` and every
`.probability` becomes `.noul`.

Note also that **Vercel's TypeSafe-compatible route keeps the native `noul`
naming**, while its evaluation API does not. Two routes on the same gateway,
two spellings. Pick one route and stay on it.

---

## Where confidence lives

| Surface                      | Confidence for `choice` / `score`        |
| ---------------------------- | ---------------------------------------- |
| Native API                   | on the answer object                     |
| Cloudflare Workers AI        | on the answer object                     |
| Vercel AI SDK evaluation API | on `providerMetadata`, not on the answer |

And on every surface: **`noul` answers carry no confidence at all.** The
probability is the answer. Do not write a helper that reads `.confidence`
uniformly across all three types — it will return `undefined` for a third of
your questions.

---

## Request envelope

| Surface                      | Shape                                      |
| ---------------------------- | ------------------------------------------ |
| Native API                   | `state` and `questions` at the top level   |
| Cloudflare Workers AI        | `state` and `questions` wrapped in `input` |
| Vercel (TypeSafe-compatible) | top level, like native                     |

A client written against the native shape will not work on Cloudflare by
changing the base URL alone.

---

## Endpoint path

| Surface                              | Path                                                    |
| ------------------------------------ | ------------------------------------------------------- |
| Native API                           | `POST /v1/systemone`                                    |
| Vercel AI Gateway (compatible route) | `POST /typesafe/v1/systemone`                           |
| LiteLLM pass-through                 | `POST /typesafe/v1/systemone`                           |
| Bifrost                              | `POST /typesafe/v1/systemone`                           |
| AI/ML API                            | `POST /v1/decisions`                                    |
| OpenRouter                           | a decisions endpoint distinct from its chat API         |
| Cloudflare                           | through the Workers AI binding or its own REST run path |

The gateways that expose `/typesafe/v1/systemone` are the ones where the official
SDK works by changing only the base URL. That is the cheapest migration path if
you expect to move.

---

## Environment variable

| Surface                                  | Variable                                        |
| ---------------------------------------- | ----------------------------------------------- |
| Most integrations, and the official SDKs | `TYPESAFE_API_KEY`                              |
| `@ai-sdk/typesafe-ai`                    | `TYPESAFE_AI_API_KEY`                           |
| `rig` (Rust)                             | `JEV_TOKEN`                                     |
| Vercel AI Gateway                        | the gateway's own key                           |
| Netlify AI Gateway                       | none — zero-config, billed through the platform |
| Self-hosted compatible servers           | `TYPESAFE_API_KEY` plus a base-URL override     |

Three different names for the same secret is a real source of "it works locally
but not in CI".

---

## SDK naming, Python versus JavaScript

|                  | Python                             | JavaScript                                 |
| ---------------- | ---------------------------------- | ------------------------------------------ |
| Package          | `typesafe-sdk`                     | `@typesafe-ai/sdk`                         |
| Method           | `client.system_one(...)`           | `client.systemOne(...)`                    |
| Question helpers | classes: `Choice`, `Score`, `Noul` | functions: `choice()`, `score()`, `noul()` |

Two answer-access patterns also appear across published examples:
`response.answers["key"]` and `response.nouls["key"]` / `.choices` / `.scores`.
Follow whichever your own SDK version's docs show and do not mix them.

---

## Hard limits, from the official docs

These are properties of the model, so they hold on every surface.

|                  | Limit                                                                            |
| ---------------- | -------------------------------------------------------------------------------- |
| `choice` options | max **255**                                                                      |
| `score` levels   | **2 to 10**, 0-indexed, ordered low to high                                      |
| Context          | **64k** tokens per request; **32k** for `state` plus the single longest question |
| Input            | **text only** — string, JSON object, or array of text                            |
| Output tokens    | free; the model does not generate text                                           |

There is no published tokenizer, which is why at least one production integration
budgets in UTF-8 bytes with headroom rather than counting tokens.

---

## Things that are not portable at all

- **Streaming.** The upstream API does not stream, so no gateway can offer it.
- **Self-hosting.** There are no published weights. Anything that runs locally is
  a different model with a compatible wire format — see the `alternative` rows in
  the catalog, and note that a compatible API does not imply compatible
  calibration, so **thresholds do not transfer**.
- **Thresholds across question types.** A cutoff tuned on a `noul` probability is
  not a `choice` confidence. The vendor's own limitations doc makes this point.
- **Thresholds across model versions.** Pin the version if you have tuned any.
- **Option ordering.** One independent report found that reversing option order
  moved a probability enough to cross a 0.9 threshold. If that reproduces for
  your workload, treat option order as part of your prompt and freeze it.

---

## Corrections this page exists to prevent

Claims that circulate but are wrong, each verified against a primary source:

- **`typesafe/jev-1` is not a model string.** It appears in no documentation. The
  versioned ID is `jev-1.13.0`.
- **The yes/no type is not called "Binary".** It is `noul`. Several mainstream
  outlets wrote "Boolean", which matches one SDK's spelling but not the model's.
- **`jevai.org` is not official.** It is an unaffiliated community site running
  its own separate API with a different endpoint, request shape and keys. Its
  `/jev-api` page in particular documents a request shape matching no primary
  source — do not copy code from it.
- **You cannot run Jev locally.** No weights are published. Content titled "run
  Jev locally" describes a substitute.
