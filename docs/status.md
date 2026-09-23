# Ecosystem status

This page has two halves that age differently. The first is regenerated from
`catalog.json` by `scripts/build_docs.py` on every build, so it is current by
construction. The second is a dated snapshot, written at **2026-09-22** — a week
after the model entered early access on 2026-09-15 — and is meant to age; that
is the point of dating it.

## The catalogue, now

<!-- shape:start -->
|  |  |
| --- | --- |
| Entries | 805 |
| Carrying code | 781 |
| Official (TypeSafe AI's own) | 36 |
| Link answered 2xx on the last sweep (2026-09-23) | 801 |
| Rows citing a call site CI re-reads weekly | 721 |
| Patterns covered | 17 of 18 |
| Retired links | 0 |
<!-- shape:end -->

### Coverage gaps

<!-- gaps:start -->
No entries yet:

- **`recommendation`** — Choose what to surface next, fast enough for a live conversation.

Thin (fewer than 10): `retry-control` (4), `feature-extraction` (7), `support-triage` (7).
<!-- gaps:end -->

Two holes are in the research rather than the ecosystem: **Reddit** produced
nothing verifiable across four retrieval routes, and **X/Twitter** is barely
represented for the same reason. Both are gaps, not judgements.

Run `python3 scripts/counts.py` for the full breakdown by kind, language and
platform.

## Snapshot at 2026-09-22: what week one looked like

**The official material is the best material.** The cookbooks and pattern pages
in the vendor's docs are more useful than almost anything written about them,
and they are primary sources. If you only read five things, read those.

**Adoption was unusually fast.** First-class integrations landed within days
across the AI SDK, LangChain in both languages, Pydantic AI, LiteLLM, Effect,
Pydantic, Rig, ruby_llm and more, plus four or more hosted gateways. Production
integrations exist in repositories with six-figure star counts.

**Almost every number in circulation is vendor-reported.** The widely-quoted
speed and cost multiples come from the vendor's own workflow evaluations, whose
reference answers were derived from other models' judgements rather than human
ground truth. The vendor's launch post itself describes the headline figures as
an upper bound.

**Independent measurement is scarce, and the honest ones are the most useful
thing in this catalog.** A handful of projects published results that did not
flatter the model:

- A large agent framework ported the compaction approach, measured it, and
  concluded not to adopt it — recall came out below their existing summariser,
  and at a matched context budget it tied plain recency ordering.
- A news classifier found the model merely tied their incumbent on blind-judged
  headlines, and kept it in shadow mode rather than shipping it.
- A code-review tool measured materially more billed input for essentially no
  wall-clock gain, and recommended keeping the feature off by default.
- An independent tester found that reversing option order shifted a probability
  enough to cross a 0.9 threshold.

Cost was consistently the clear win. Quality was frequently a wash. Both of those
are useful to know before you build.

**A large fraction of "Jev projects" are not Jev.** Independent
reimplementations with a compatible wire format are among the most-starred
repositories mentioning the model, and are routinely miscatalogued as usage
examples. They are `kind: alternative` here with a `not-jev` flag. A compatible
API does not imply compatible calibration.

**Popularity and substance have not had time to correlate.** Four-figure star
counts sit on single commits; several notable projects declare no licence;
at least two ship the integration deliberately inert. Hence the `single-commit`,
`no-license` and `shadow-mode-only` flags.

**Nothing about the training method is published.** There is no paper, no reward
function, no dataset description and no reproducible evaluation for RLCD. An
unrelated 2023 paper abbreviates to the same four letters, which is a reliable
source of confusion.

## What to watch

- Whether independent benchmarks accumulate, and whether they keep landing on
  "cheap but comparable" rather than "better".
- Whether the option-ordering sensitivity reproduces. If it does, option order
  becomes part of everyone's prompt-freezing discipline.
- Whether a paper appears.
- Whether the alternatives converge on the wire format well enough that patterns
  really do become portable, calibration aside.
- Whether rate limits and pricing settle. The docs currently carry an explicit
  warning that limits can change without notice.
