# Before you trust an entry

A row in this catalog means a link resolved and a person read it. It does not
mean the code runs, the numbers hold, or the design suits you. Here is what to
check, roughly in order of how often it bites.

## The one thing most people get wrong

**A probabilistic gate is not a security boundary.**

It is genuinely useful in front of a shell command, a write, a spend or a send —
it catches carelessness cheaply. But an attacker chooses the input, and a model
that is right 99% of the time is a model an attacker will probe for the other 1%.
The vendor's own limitations page names adversarial content as a known weak spot.

Anything destructive or irreversible needs a deterministic rule, a permission
system, or a person. Several catalogued projects get this right: they use the
model to _flag_ and keep the decision in code. At least one gate in this catalog
deliberately fails closed. Copy that shape, not the shape that trusts the score.

## Checklist

- [ ] **Is it actually Jev?** Check for the `not-jev` flag. Some of the
      most-starred repositories mentioning Jev never call it — they are
      independent reimplementations with a compatible wire format. Compatible
      does not mean calibrated, so **thresholds do not transfer**.
- [ ] **Does Jev do anything?** Check for `shadow-mode-only`. More than one
      well-known project has it wired in and deliberately inert, with nothing it
      returns reaching a user-visible decision. That is a good engineering
      practice and a bad thing to misread as a production endorsement.
- [ ] **Are the numbers measured or repeated?** `vendor-reported` means the row
      carries the vendor's own benchmark figures. Those were produced with
      reference answers derived from other models' judgements rather than human
      ground truth. Independent measurements are `kind: benchmark` without that
      flag, and there are only a handful.
- [ ] **Was the code run?** `code-untested` means read, not executed — including
      for the examples in this repository.
- [ ] **Is it maintained?** `single-commit` and `archived` exist because this
      ecosystem is days old and a four-figure star count can sit on top of one
      commit. Check the last push date yourself.
- [ ] **Can you legally use it?** `no-license` means no `LICENSE` file, whatever
      a README badge claims. `repo_license` records what the repository actually
      declares. Several otherwise good projects ship none.
- [ ] **What will it cost you?** `third-party-api-key` means a service other than
      TypeSafe. `early-access-required` means a waitlist.
- [ ] **Does it send your data somewhere?** Some catalogued projects read screen
      contents, mailbox contents or source trees. That is inherent to what they
      do; decide whether you are comfortable before running one.

## Things worth knowing about the model itself

These come from the vendor's own docs and shape what any entry can deliver.

- **Text only.** No image, audio or video input. Pre-process to text.
- **64k tokens per request**, and **32k** for the state plus the longest single
  question.
- **`choice` caps at 255 options**; **`score` takes 2 to 10 levels**.
- **A `score` is probability-weighted and lands between levels.** Do not assume
  an integer.
- **`noul` answers carry no confidence field.** The probability is the answer. A
  helper that reads `.confidence` uniformly will return nothing for those.
- **A threshold tuned on one question type does not transfer to another**, and
  one tuned on one model version does not survive an alias moving. Pin the
  version once you have tuned anything.
- **English is the primary training language.** The docs state CJK scripts are
  handled but not equally well — worth testing before you rely on it.
- **Rate limits can change without notice**, per an explicit warning in the docs.
- **Known weak spots**, per the vendor: literal reading, arithmetic and counting,
  date comparison, indirection, large states full of irrelevant detail, and
  adversarial content. Do not design around any of those without reading
  [the limitations page](https://docs.typesafe.ai/model-jaggedness/jev-1.13).

## One independent finding worth acting on

An independent test reported that **reversing the order of a question's options
moved a probability enough to cross a 0.9 threshold.** It is unreplicated, so
treat the magnitude as indicative rather than settled. But the implication is
cheap to act on: if option order can move your answer past your cutoff, freeze
the order and treat it as part of your prompt.

## What a green link proves

That the URL answered on the date in `checked`. Nothing else. Do not present any
row here as vetted, recommended, or safe.

## Reporting a problem

Open an issue with the slug. Corrections are the most valuable contribution to
this repository — a wrong row costs more than a missing one. If a row
mischaracterises your own project, say so and it will be fixed or removed.
