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

Define defines, it never plans. Nothing in the interview is about building: not how long it takes, not what gets done first, not what ships when. A word like *livrer*, *sprint* or *soirées* in a question is the signal the skill has drifted.

The design tree of `/grill-me`, and nothing else. No topic list, no mandatory sections. The frontier is every decision whose prerequisites are settled; you ask all of it each round, and the answers redraw the tree. Done when the frontier is empty.

Three things are specific to this skill:

- **Going deep.** When an answer opens ten questions behind it, the skill asks whether to go down there rather than diving on its own. A yes means rounds of edge cases landing in `rules.md`; a no prunes the branch. The user decides where the product is precise and where it stays rough.
- **Contradictions.** A new answer that contradicts an earlier one stops the round: both sides quoted, which one gives. Never resolved by the skill. Each arbitration becomes a numbered file in `decisions/`.
- **Sizing and milestones.** See below.

Facts are the skill's job (web, filesystem, sub-agents). Stop word and a ten-round checkpoint. Asking ends the turn.

## Style

Everything the user needs in order to answer lives inside the question itself, so a card read alone is answerable: what is being settled, why it matters and what changes downstream, what bothers the skill in what they said, then the question naming its subject in full. Three or four sentences. The chat around it stays light, a transition at most; the reasoning is never there.

Options are two to five words, in the user's language, and hold nothing but the option. No "(Recommandé)", no "(exclusifs)", no parenthesis bolted onto the question. The skill's opinion closes the question, in the first person. The sizes are said as *un week-end*, *un mois de soirées*, *plusieurs mois*; `sketch`, `product` and `platform` are internal names for the documents, never spoken.

## Sizing

First question, always, asked as *how many independent pieces does this product hold*, never as *how long will you spend on it*. One piece defined in one go is `sketch`; one product made of several pieces is `product`; several products that would live apart is `platform`. The skill gives its own reading first, in the first person: that is its one chance to disagree. The user decides; a disagreement is written as a reserve.

## Milestones

A piece of the product with its own essence, never a date and never a sprint. None for a `sketch`, proposed for a `product` whose launch list holds more than one essence, mandatory for a `platform`. Two to six, slug + title + one line, ordered by dependency and said to be a reading order rather than a schedule. First one = the piece that carries the bet. Each gets a folder with an `idea.md` in `eureka`'s frame; `/define <slug>` writes its documents.

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
