# crash-test

`/grill-me` for a product: interviews the user about their Idea in rounds until nothing is left open, sizes it, splits it into milestones when it is too big, and writes the Product Brief. Step 2 of the chain.

## Trigger

- `/crash-test`, or `/crash-test <slug>` to crash-test one milestone.
- Model-invoked on "challenge mon idée", "est-ce que ça tient", "j'ai une idée de produit", "découpe mon projet", "I have an idea for", "does this hold up", "size this project".

## Input

- A milestone slug: works in `.veebee/milestones/<slug>/`, reads the root Brief for context and the milestone's `idea.md`.
- Else `.veebee/idea.md` if it exists; else the user's words.
- An existing `product.md`: fresh directory, overwrite, or resume (existing Brief taken as settled answers). Nothing written before the answer.

## Method

- The design tree and rounds of `/grill-me`: the whole frontier per round, up to fifteen questions, ❓ title and body with a/ b/ c/ choices, ➡️ recommendation on every question, drawn from this interview only.
- Facts are the skill's job (web, filesystem, sub-agents); decisions are the user's.
- Stop word, ten-round checkpoint, asking ends the turn.
- Branches the tree must visit: essence, problem, for whom, level, features (launch, later, never), journeys, risks and bets, proof, milestones. Free angles per kind on top.
- A loved reference is a taste signal, not a template.

## Exigence Level

First question of round 1. Sketch, Product, Platform. The skill proposes with a reason; the user decides; a disagreement is written as a reserve in the Brief. Never blocks.

## Milestones

A deliverable slice with its own essence. Never in Sketch, proposed in Product when the launch list does not ship in one go, mandatory in Platform. Proposed as a question: two to six milestones, ordered, slug + title + one-line essence, with an alternative cut when there is one. First milestone = smallest thing that proves the bet.

Tree, same shape at every depth:

```
.veebee/
├── idea.md
├── product.md
└── milestones/
    └── 01-<slug>/
        ├── idea.md        written by the root crash-test (Eureka's frame, kind inherited)
        ├── product.md     written by /crash-test 01-<slug>
        └── milestones/    only if still too big
```

Milestones are crash-tested at Product level by default.

## Canvas

`assets/canvas.html`, `BRIEF` object. Every section visible from the first turn, empty; fills as answers arrive; the milestones tree is the last section. Artifact tool when available (favicon 🚗), else chat at checkpoint and finish, and the page opened once in the browser.

## Output

`.veebee/product.md` (or the milestone's): front-matter `kind`, `title`, `lang`, `level`; sections Essence, Problem, For whom, Exigence Level (with reserve), Features (At launch / Later / Never), Journeys, Risks and bets, Proof, Open questions, Milestones. Headings in the user's language. Nothing about the stack. `idea.md` never rewritten.

Finish: show the Brief, ask "does it say it right?", write `product.md` then one `idea.md` per milestone, one sentence pointing to the file and to `/crash-test <first slug>` when there are milestones.

## Tests

Five prompts in `skills/crash-test/evals/evals.json`: Sketch game from an idea file, Product from a loose idea, Platform that splits, level disagreement, existing product.md.
