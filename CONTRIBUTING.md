# Contributing

This catalog competes on verification, not on size. There are dozens of Jev
directories; the reason to use this one is that every row was opened by a person
and says what it does not know. A submission that adds a link without adding
that confidence makes the list worse, not longer.

So the bar is: **could a reader act on this row without opening the link?**

## Adding an entry

1. Add an object to `catalog.json`. Required fields: `slug`, `title`, `summary`,
   `summary_zh`, `url`, `kind`, `patterns`, `sources`, `license`.
2. Run the checks:

```bash
python3 scripts/lint.py \
  && python3 scripts/build_readme.py \
  && python3 scripts/build_assets.py
```

`build_assets.py` regenerates the README's SVG figures from the catalog. CI
fails if they are stale, because a coverage chart that disagrees with the
catalog is worse than no chart.

3. Commit `catalog.json`, both generated READMEs, **and** any changed
   `docs/assets/*.svg`. CI fails if any of them drift.

No Python dependencies are needed. The schema validator is self-contained.

## Field rules

- **`title`** — as published at the source. If the page's `<title>` and its
  on-page heading disagree, use the heading a reader sees, and say so in `notes`.
- **`summary`** — what the example _actually demonstrates_, not what its README
  claims. "Routes support tickets with a choice and a score" beats "revolutionary
  AI-powered triage".
- **`summary_zh`** — write it yourself if you can. If you machine-translated it,
  set `zh_machine: true`. The READMEs report the split; claiming hand-written
  Chinese that is not is the one thing that would quietly make the data untrue.
- **`kind`** — the form of the thing. Use `alternative` for anything that does
  not call Jev, however Jev-shaped it is.
- **`patterns`** — which decisions it demonstrates. Read
  [`docs/patterns.md`](docs/patterns.md) first. `overview` cannot be combined
  with a specific pattern; the linter enforces that.
- **`question_types`** — only the primitives the code _actually_ calls. Read the
  call site; do not infer from the README. Several projects describe "scoring"
  while using only `noul`. The primitive is `noul`, never `binary`.
- **`evidence`** — the file you read that claim in, and strings from it that
  substantiate it. This is what makes the claim re-checkable rather than
  asserted, so a weekly job can notice when it stops being true. Let the
  discoverer propose one and then check it yourself:

  ```bash
  python3 scripts/verify_claims.py --discover --only <slug>
  python3 scripts/verify_claims.py --only <slug>
  ```

  Prefer the implementation over a test file: tests get deleted while features
  stay, and a mocked string is weaker proof than a real call site. When the
  source is a docs page, a video or a paywalled post, set `evidence_none`
  instead and say which.
- **`official`** — true only for `typesafe.ai` hosts and the `typesafe-ai`
  GitHub org. A first-party integration published by another vendor is not
  official. The linter checks this.
- **`stars`**, **`repo_license`** — from the GitHub API on the date you add the
  row, not from a README badge. Several repos have a licence badge and no
  `LICENSE` file; that gets the `no-license` flag.
- **`sources`** — at least one, so the row is attributable. Name where you found
  it, not where it lives.

## Flags are the point

Use them generously. A flagged row is more useful than an unflagged one.

| Flag                                     | Use when                                        |
| ---------------------------------------- | ----------------------------------------------- |
| `vendor-reported`                        | it repeats the vendor's own performance numbers |
| `unverified-claims`                      | it makes measurement claims you could not check |
| `not-jev`                                | it does not call Jev at all                     |
| `shadow-mode-only`                       | Jev is wired in but changes no behaviour        |
| `code-untested`                          | you read the code but did not run it            |
| `single-commit`                          | one commit, so maintenance is unlikely          |
| `no-license`                             | no `LICENSE` file, whatever the README says     |
| `archived`                               | development visibly stopped                     |
| `paywalled`, `marketing`, `ai-generated` | as they say                                     |
| `early-access-required`                  | needs waitlist access to use                    |
| `third-party-api-key`                    | needs a key for a service other than TypeSafe   |

`ai-generated`, `unverified-claims` and `code-untested` require a `notes` line
saying why — a flag a reader cannot interpret is worse than no flag.

## What does not belong here

- **Anything you have not opened.** Including anything an AI tool suggested and
  you did not check. Fabricated entries are the failure mode this catalog is
  built to avoid.
- **A model string, package name or endpoint you have not seen in a primary
  source.** `typesafe/jev-1` is the canonical example: it appears in no
  documentation and keeps getting repeated.
- **Content-farm rewrites of the launch announcement.** There are hundreds. If it
  adds no observation of its own, it adds nothing here.
- **"Run Jev locally" content filed as a Jev tutorial.** There are no published
  weights. File it as `alternative` with `not-jev`.
- **Your own project, described the way you would describe it to an investor.**
  Self-submissions are welcome; marketing copy is not. Say what decision it makes
  and which primitive it uses.

## Finding things to add

```bash
python3 scripts/discover_candidates.py --top 40
```

This harvests every list in `docs/sibling-lists.txt`, ranks repositories by how
many cite each, and reads the candidate's code before reporting. A `calls-jev`
verdict means a call site was found — it is a shortlist, not a row. Read it,
write the summary yourself, and keep the evidence path the scan produced.

Know a directory we are not harvesting? Add it to `docs/sibling-lists.txt`.
That is a useful contribution on its own.

## Reporting a dead link

Open an issue with the slug. Do not delete the row — retiring an entry means
moving it to `retired.json` with a `notes` line explaining why, so the dead
reference stays searchable. `scripts/check_links.py` finds them but deliberately
never moves them; that judgement is a person's.

## Adding a pattern

A pattern earns a heading once **two independent real examples** exist. Adding
one means editing four places:

1. the enum in `schema/entry.schema.json`
2. the label table and order list in `scripts/build_readme.py`
3. the `PATTERNS` list in `scripts/build_assets.py`, which draws the figure
4. `docs/patterns.md`, with an explicit *when NOT to use this*

Both generators fail loudly on a pattern they have no label for, which is
intentional — a silent fallback to a raw slug is how a bilingual list starts
rotting.

## Adding a runnable example

See [`examples/README.md`](examples/README.md). Two patterns have no example yet
— `retry-control` and `recommendation` — and either would be a genuinely useful
contribution. Say plainly in the file whether you ran it against the live API.

## Ground rules

Be accurate, be brief, and say what you do not know. If you are not sure whether
something qualifies, open an issue and ask rather than guessing — an honest
question costs nothing and a wrong row costs a reader's trust.
