# Sources and licences

Every row in `catalog.json` carries a `sources` array naming where it was found,
so the catalog is auditable rather than asserted. This page aggregates that
array and states the licence position.

## Where the first build's rows came from

Counts as of 2026-09-22, 148 entries. A row can cite more than one source.

| Source                                | URL                                                                                                   | Rows |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------- | ---- |
| GitHub code search                    | <https://github.com/search>                                                                           | 51   |
| TypeSafe AI docs index                | <https://docs.typesafe.ai/llms.txt>                                                                   | 36   |
| Maintainer submission                 | <https://github.com/kydlikebtc/awesome-jev>                                                           | 19   |
| jevai.org community site              | <https://www.jevai.org/>                                                                              | 5    |
| This repository (`examples/`)         | <https://github.com/kydlikebtc/awesome-jev>                                                           | 4    |
| YouTube search                        | <https://www.youtube.com/>                                                                            | 3    |
| Hacker News                           | <https://news.ycombinator.com/>                                                                       | 5    |
| Web search — news and analysis        | various                                                                                               | 11   |
| Platform documentation and changelogs | Vercel, Cloudflare, LangChain, Pydantic AI, LiteLLM, OpenRouter, Netlify, AI/ML API, Langfuse, Spring | 11   |

The official docs index is the single largest source, and deliberately so: the
18 official cookbooks and 4 official pattern pages are the most directly useful
usage examples that exist, and they are primary material.

## Licences

This repository separates code from data, following the convention the reference
repository established.

| What                                      | Licence                   |
| ----------------------------------------- | ------------------------- |
| `scripts/`, `site/`, `examples/`          | [MIT](../LICENSE-MIT)     |
| `catalog.json`, `retired.json`, `schema/` | [CC0-1.0](../LICENSE-CC0) |
| `docs/`, `README*.md`                     | CC0-1.0                   |

Every row in the current build is `CC0-1.0`, meaning no descriptive text was
inherited from a source that requires attribution. If a future row does inherit
text from a CC BY 4.0 catalog, it gets `license: "CC-BY-4.0"` and the attribution
is that row's `sources` array.

**Linked works keep their own licences.** The `repo_license` field on a row
records what the linked project declares, which is not always what its README
badge claims — `no-license` flags the cases where a repository ships no `LICENSE`
file at all.

Declared licences across the catalog's linked repositories:

| Licence                          | Repositories |
| -------------------------------- | ------------ |
| MIT                              | 42           |
| Apache-2.0                       | 13           |
| None declared                    | 14           |
| NOASSERTION (non-standard terms) | 4            |
| AGPL-3.0                         | 2            |
| LGPL-3.0                         | 1            |

Fourteen linked projects declare no licence. If you plan to reuse code from one,
that is a blocker, not a detail — check before you copy.

## Relationship to TypeSafe AI

None. This is an unaffiliated community index. "Jev", "TypeSafe" and "System
One" are used descriptively to refer to the vendor's product. No endorsement is
claimed or implied, and no row here should be read as a recommendation.

## Relationship to other Jev directories

There are dozens. Several are catalogued in this repository as rows of their own,
including the largest ones, because pretending otherwise would be silly. They
compete on coverage; this one competes on verification. If you are looking for a
project and cannot find it here, they are worth checking — and if you find a real
one that is missing here, [please add it](../CONTRIBUTING.md).

## Corrections

If a row misattributes your work, mischaracterises your project, or you want it
removed, open an issue. Correction requests take priority over additions.
