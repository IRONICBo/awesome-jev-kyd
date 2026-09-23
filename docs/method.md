# Data and method

How the first build of this catalog was produced, what was checked, and where it
is weakest. If you want to reproduce or audit it, this is the page.

## Pipeline

1. **Establish the primary facts first.** The official docs serve raw Markdown at
   `<page>.md`, so the API reference, primitives, confidence, models and
   limitations pages were fetched and read directly rather than summarised. Every
   claim about the model in this repo traces to one of those.
2. **Sweep in parallel, along four axes.** Official sources; platform and
   framework integrations; open-source projects and packages; articles, videos
   and discussion. Four passes, each required to cite a URL per claim and to mark
   anything it could not confirm.
3. **Verify code entries at the call site.** For every row claiming code, the
   actual calling file was read to confirm which primitives are used. This is
   where README descriptions and reality diverge most often.
4. **Verify repository metadata from the API.** Stars, licence, creation date and
   last push came from the GitHub API on 2026-09-22, not from badges.
5. **Reject aggressively.** See "What was excluded".
6. **Write both summaries by hand**, English and Chinese, from what the page
   actually said.
7. **Validate and generate.** `scripts/lint.py` then `scripts/build_readme.py`.

## What the first build checked, and what it found

- **148 entries**, 124 carrying code, 36 official.
- **Two agent reports contradicted each other twice**, and both conflicts were
  resolved by direct inspection rather than by majority:
  - A Discord moderation bot was called a name collision by one pass. Reading
    `moderator.py` showed a real `typesafe` import and `jev-latest` default. It
    stayed in.
  - A widely-starred repository was catalogued by the community site as a visual
    inference tool using Jev. Scanning all 52 of its files found **zero**
    references to the API. Its own README says it is a research starter, not a
    copy. It was reclassified as `alternative` with a `not-jev` flag.
- **A fabricated integration was found and excluded**: a skills repository
  documenting a Jev API that does not exist, with primitives' meanings inverted,
  linking to a repository that returns 404.
- **The linter caught a bug in its own rule.** The `official` check originally
  accepted only `typesafe.ai` hosts, which wrongly rejected the vendor's own
  GitHub org. The rule was widened to the org and no further.

## Claims are re-checked, not just asserted

A row carrying `question_types` asserts which primitives a project's code calls.
That was true when a person read the call site, and nothing stopped it going
stale — an upstream refactor could remove the integration entirely and this
catalog would keep claiming it.

So every such row records `evidence`: the file the claim was read in, and
strings from that file that substantiate it. `scripts/verify_claims.py` fetches
each one from the repository's default branch and asserts those strings are
still there. A scheduled job runs it weekly and opens an issue on failure,
rather than failing the build — an upstream rename is a false positive, and a
permanently red repo teaches people to ignore the signal.

Deliberately unpinned to a commit. Pinning would verify a historical snapshot
forever and never notice a removal, which defeats the purpose.

The first backfill was machine-assisted and human-reviewed: a `--discover` mode
reads each repository and proposes a path, then a person checks it. That review
mattered — the discoverer favoured test files over implementations in seven
cases, and proposed the same file for all four of this repo's own examples. It
also caught a mistake in the review itself: one hand-written override cited a
file that did not contain the strings claimed, and the verifier failed it on the
first real run.

Rows whose source is not a readable repository file — a docs page, a video, a
paywalled article — carry `evidence_none` saying which, rather than a fabricated
citation.

## Discovery is crowdsourced, verification is not

There are dozens of Jev directories. Each is a different person's sweep of the
same ecosystem, so their union is a far better discovery surface than any single
one — including this one. `docs/sibling-lists.txt` names them, and
`scripts/discover_candidates.py` harvests them, ranks repositories by how many
cite each, and then reads the candidate's own code looking for a call site.

The two halves matter separately. Crowd agreement finds things: a repository
cited by twenty lists is worth looking at. Crowd agreement does not verify
anything: these lists copy from each other, so one miscataloguing propagates
everywhere. The most-starred "Jev visual inference tool" in this ecosystem
contains zero references to the API and is listed as a Jev project almost
universally.

So the script emits a shortlist with a verdict per candidate — `calls-jev` with
the file and strings that prove it, `mentions-only` when the README claims what
the code does not, or `no-signal`. A `calls-jev` verdict is not a catalog row.
Someone still reads it and writes the summary.

The first aggregation run harvested 32 lists, found 1,885 distinct repositories
cited, verified the 45 most-cited that were missing here, and added 34. Six were
`mentions-only` — including one cited by twenty lists — and four were dropped
because their only Jev reference was in a fixture named `fake_jev`, which proves
the request shape and nothing else.

Sibling lists that ship no licence can be used as pointers but not as prose: a
URL is a fact, a description is someone's writing. Rows discovered that way were
re-read at the call site and summarised independently.

### The bulk pass, and what it cost

A second aggregation run verified the 320 most-cited repositories missing here
and added 223. At that volume two standards had to bend, and both are recorded
in the data rather than hidden:

- **Summaries are the project's own description**, normalised, rather than a
  sentence written after reading the code. What _was_ read is the call site,
  and `evidence` on every row proves it.
- **Chinese is bulk-translated**, so those rows carry `zh_machine: true`. The
  counts script reports the split — 183 of 404 hand-written at the time of
  writing — because a catalogue that claimed all of them were would be lying
  about the one thing it sells.

Patterns were suggested by keyword rules over the description and then
reviewed. The review caught eight errors in 223, almost all of the same shape:
an SDK picking up a behavioural pattern from words describing its own API.
"Typed noul, choice and score" is an API surface, not content scoring;
"observable retries" is an HTTP client, not a retry decision. One was a plain
regex bug — `form\b` with no leading boundary matched "platform" and filed a
.NET SDK under document triage.

`retry-control` went from zero to one genuine example, a semantic circuit
breaker that asks whether an HTTP 200 is a silent failure. The other apparent
matches were false positives and were removed. `recommendation` is still empty
across 32 lists and 1,887 repositories, which is now a reasonably strong claim
that nobody has published one.

### The long tail, 2026-09-22

A third run took the next 700 most-cited repositories and added 401, taking the
catalogue from 404 to 805. The median candidate was cited by two lists and had
two stars, so this pass is mostly the long tail rather than anything popular.
The same two concessions apply, and the same `zh_machine` flag records them.

Running at this size broke three things that had worked at 400 rows, all of
them in the machinery that keeps the catalogue honest rather than in the data:

- Two of the first three `path-gone` verdicts were transient fetch failures, not
  deleted files. The raw-file fetch now retries once before believing a miss.
- Scraping github.com HTML for link status hit its rate limit a few dozen rows
  in, so most GitHub rows never got stamped. Bare repository URLs now go through
  the authenticated API; paths inside a repository still go through HTTP,
  because the API answering for the repository says nothing about one file.
- The published repository description still said 148. It is the one claim
  that lives in GitHub's database rather than in git, so no build had ever
  checked it. It is checked now.

`recommendation` is still empty.

## Why a status code is not a verdict

Every row's `link_status` says the URL answered. That is all it says. It does not
mean the code runs, the project is maintained, the benchmark is sound, or the
approach suits your system.

The distinction matters more here than in most catalogs, because this ecosystem
is days old. A repository can have four figures of stars, one commit, no licence
and a description written for a launch-week audience. Popularity and substance
have not had time to correlate. That is why `stars` is documented in the schema
as "a popularity signal, not a quality verdict", and why `single-commit`,
`no-license`, `archived` and `shadow-mode-only` exist as flags.

## Field precedence

When sources disagree:

1. The official raw Markdown docs win on anything about the model.
2. A platform's own docs win on how to reach the model through that platform.
3. The code at the call site wins over any prose describing it, including the
   project's own README.
4. The GitHub API wins over README badges.
5. Where a page's `<title>` and on-page heading differ, the heading a reader sees
   is used, and `notes` records the discrepancy.

## What was excluded

- **Content-farm and SEO rewrites of the launch announcement.** Dozens exist.
  Exclusion criterion: adds no observation of its own.
- **Press-release redistributions.** Many outlets carried the same wire copy.
- **Fabricated API documentation**, including the community site's own `/jev-api`
  page, whose request shape matches neither the official API nor that same
  site's other documentation.
- **Name collisions.** "JEV" is also Japanese encephalitis virus, a person's
  name, an Eve Online asset manager, a smart-camera vision framework, a Joomla
  component and several car models. Every candidate was checked for whether it
  genuinely concerns TypeSafe's model. All searching used qualifying terms;
  bare "JEV" returns mostly noise.
- **Claimed research papers.** There is no published paper for the training
  method. An unrelated 2023 paper abbreviates to the same four letters, and an
  arXiv link labelled as "the paper" is almost certainly that one.

## Known limits

- **No code was executed and the live API was never called.** Early access is
  gated. Every row with code was read, not run. The in-repo examples carry
  `code-untested` for the same reason.
- **Performance claims were not reproduced.** Rows repeating vendor benchmarks
  carry `vendor-reported`. The independent measurements catalogued here are few,
  and that ratio is itself a finding.
- **Reddit produced nothing verifiable.** Four retrieval routes failed. There is
  no Reddit row, which is a gap rather than a judgement that none exists.
- **X/Twitter is barely represented**, for the same reason.
- **Video content was verified by metadata only.** Channel, title and existence
  were confirmed; the demonstrations inside were not reviewed, and the rows say
  so.
- **The ecosystem is far larger than this catalog.** Searching for the model
  alongside the vendor name returns repositories in the thousands. This is a
  curated subset chosen for being verifiable, not an enumeration. Nobody can
  enumerate it at this growth rate.
- **Star counts move hourly** and were true on 2026-09-22.

## Reproducing it

```bash
git clone https://github.com/kydlikebtc/awesome-jev
cd awesome-jev

python3 scripts/lint.py          # schema plus cross-entry invariants
python3 scripts/build_readme.py  # regenerate both READMEs
python3 scripts/counts.py        # coverage, with gaps marked
python3 scripts/check_links.py   # sweep every URL, report only
python3 scripts/verify_claims.py # re-read every cited call site
python3 scripts/build_assets.py  # regenerate the README figures
python3 scripts/build_compat.py  # regenerate the compatibility tables
```

`verify_claims.py` needs `GITHUB_TOKEN` set — unauthenticated GitHub is 60
requests an hour, which will not cover a full sweep. `--discover` proposes
evidence for a row that has none; the proposal is a starting point for a
person, never written automatically.

`check_links.py --write` stamps `checked` and `link_status` on rows that
answered. It never retires a row: that needs a human-written reason.

## Kept current

- `lint` runs on every push and pull request, and fails if the generated READMEs
  drift from `catalog.json`.
- `links` sweeps every URL weekly and opens a red build on a dead link, rather
  than silently rewriting data.
- `pages` republishes the searchable site when the catalog or site changes.
