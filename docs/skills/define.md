# define

Defines a product precisely, by a long interview that settles every decision one at a time, then writes the documents that describe it. Step 2 of the chain.

## Trigger

- `/define`, or `/define <slug>` for one milestone.
- Model-invoked on an explicit ask: "définis mon produit", "fais-moi le cadrage", "on creuse mon idée", "cadre ce projet", "define this", "spec this out", "what exactly are we building".

## Input

- A milestone slug: works in `.veebee/milestones/<slug>/`, inherits everything the root settles, touches only its own folder plus the root milestone list.
- Else `.veebee/idea.md` if it exists; else the user's words.
- An existing `product.md`: fresh directory, overwrite, or resume. Nothing written before the answer.
- An existing project in the directory (README, CONTEXT.md, code) is read before round 1 and treated as facts.

## Method

The design tree of `/grill-me`, and nothing else. No topic list, no mandatory sections. The frontier is every decision whose prerequisites are settled; you ask all of it each round, and the answers redraw the tree. Done when the frontier is empty.

Three things are specific to this skill:

- **Going deep.** When an answer opens ten questions behind it, the skill asks whether to go down there rather than diving on its own. A yes means rounds of edge cases landing in `rules.md`; a no prunes the branch. The user decides where the product is precise and where it stays rough.
- **Contradictions.** A new answer that contradicts an earlier one stops the round: both sides quoted, which one gives. Never resolved by the skill. Each arbitration becomes a numbered file in `decisions/`.
- **Sizing and milestones.** See below.

Facts are the skill's job (web, filesystem, sub-agents). Stop word and a ten-round checkpoint. Asking ends the turn.

## Style

Questions read like someone talking across a table. One short sentence. Options that name the thing and stop, with no justification, reference or second sentence inside them; an option that needs explaining is two options. At most one 💡 line per question, only where it would change the pick. Concrete over abstract, always.

## Sizing

First question, always. Sketch, Product, Platform, sized by how long, how many people, how many essences. The skill says which it would pick, even when the user named one: that is its one chance to disagree. The user decides; a disagreement is written as a reserve.

## Milestones

A deliverable slice with its own essence. None in Sketch, proposed in Product when the launch list does not ship in one go, mandatory in Platform. Two to six, ordered, slug + title + one line, with an alternative cut. First one = smallest thing that proves the bet. Each gets a folder with an `idea.md` in `eureka`'s frame; `/define <slug>` writes its documents.

## The documents

```
CONTEXT.md                 the product's words and what each one means exactly
.veebee/
├── product.md             essence, problem, for whom, size, bets, proof
├── features.md            at launch, later, never
├── rules.md               how it actually behaves, edge case by edge case
├── journeys.md            first time, ordinary use, the day it fails, leaving
├── decisions/0001-*.md    one per arbitrated contradiction
└── milestones/
```

`product.md` carries a front-matter: `kind`, `title`, `lang`, `size`. Headings in the user's language, front-matter in English. `CONTEXT.md` sits at the root so the `domain-modeling` skill reads the same file. `rules.md` is usually the longest: it is where the deep dives land. Nothing about the stack. `idea.md` is never rewritten.

## Canvas

`assets/canvas.html`, `DOCS` object: the documents as cards, each filling as answers arrive, what is empty drawn as a dashed line so the road left is visible. Artifact tool when available (favicon 🚗), else chat at the checkpoint and finish, plus the page opened once in the browser.

## Finish

Empty sections are named out loud first: empty on purpose is an answer, empty by accident is a hole. Then the documents are shown, the user confirms, everything is written, and the whole project milestone tree is printed, read from disk by `scripts/milestones.py`.

```
✓ Bourg
├── ✓ 01-la-premiere-marche  La première marche
├── ○ 02-l-echelle  L'échelle   ← /define 02-l-echelle
└── ○ 03-le-bonheur  Le bonheur   ← /define 03-le-bonheur

1/3 définis   ✓ défini   ○ à définir
```

## Tests

Six prompts in `skills/define/evals/evals.json`: questions coming from answers rather than a list, the deep-dive gate, a contradiction put back in the face, the question style, the documents written, a milestone run inheriting the root.
