# style

Settles how a product looks, by an interview about taste, then writes the prompt to paste into a design tool. Step 3 of the chain. It draws nothing itself: the prompt is the deliverable.

## Trigger

- `/style`, or `/style <slug>` for one milestone.
- Model-invoked on an explicit ask: "design mon produit", "la direction artistique", "un prompt pour Claude Design", "à quoi ça ressemble", "design this", "art direction", "write me a design prompt".

## Input

- `.veebee/product.md`, `features.md`, `journeys.md`, `idea.md` and `CONTEXT.md` at the root; the milestone folder too on a slug run.
- No `product.md`: says `define` has not run and that the prompt will be thinner, offers to go on from the README or the user's words, and does. It never refuses.
- `.veebee/style.md` already there: read, summarised in one line, not re-interviewed unless asked.

## Two levels

A design tool keeps brand identity in a design system separate from each screen, so the skill writes two things.

- **The charter**, `.veebee/style.md`, once for the whole product. The taste, the colours, the type, the feeling.
- **One prompt per piece**, `prompt.md` beside that piece's `product.md`. It leans on the charter, so the milestones cannot drift from each other.

The charter interview runs first even when a slug was passed: a prompt written without a charter drifts from every other piece.

## The interview

Not `define`'s grill. The subjects are known in advance, because what a design tool needs to know is always the same. Six to ten questions, one or two rounds.

**Only a question whose answer changes the prompt.** What the documents already settle is stated, never asked: if `idea.md` says pixel art, the technique is settled and the pixel size is what is left.

The spine follows the `kind` written by `eureka`:

| kind | what gets settled |
|---|---|
| `product`, `service`, `skill` with an interface | the feeling · light or dark and where the colour comes from · airy or packed · typography neutral or with character · still or alive |
| `game` | technique and its constraints (pixel size, palette size) · perspective · mood and era · what the palette is built around · interface inside the world or laid over it |
| `content` | the shape on the page · typography and rhythm · images or none |

One question is asked in every run, whatever the kind: **what it must not look like**. An anti-reference cuts more than a reference. A reference the user loves is a taste signal, never a template: the skill names the part it kept and never copies a whole product into the prompt.

## The surfaces

Deduced from `journeys.md` and the launch features, proposed with one line each, validated before the prompt is written. Three to eight is a piece; over ten and the skill says the piece is too big.

Each carries its name, who is on it, what they came to do, what has to be visible. The forgotten ones are named out loud, because a design tool never invents them: the empty state, the error, the first time, the moment there is too much of everything.

For a `game` the surfaces are not screens: a tileset, a set of sprites, the HUD, one key scene.

## Style

Everything the user needs in order to answer lives inside the question card: what is being settled, what it changes on screen, then the question naming its subject in full. Options are two to five words and hold nothing else.

The suggestion is narrower than in `define`, because this skill is about their taste. 💡 only when something read points somewhere, naming what points there. Nothing points anywhere, no suggestion.

## The files

```
.veebee/
├── style.md                         the charter, written once
├── prompt.md                        the prompt, when the product has no milestones
└── milestones/<slug>/prompt.md      one per piece
```

The charter says intentions rather than values — *un fond chaud, papier, jamais blanc pur* rather than a hex — because the tool picks better values. An existing brand is the exception: exact hexes, exact fonts, taken as given.

Nothing about the stack in either file: no framework, no component library, no CSS. That is `setup`'s fight. Nothing telling the design tool how to behave either.

## Canvas

`assets/canvas.html`, `PROMPTS` object: the charter and the prompt in blocks with a copy button, the surfaces, and the tree. Clipboard API first, `execCommand` next, and the text selected when both are refused. Artifact tool when available (favicon 🎨), else opened from disk.

## Finish

The files are written, then the whole tree is printed from disk by `scripts/pieces.py`.

```
✓ Bourg   charte écrite
├── ✓ 01-poser-et-peupler  Poser et peupler
├── ○ 02-le-catalogue  Le catalogue   ← /style 02-le-catalogue
└── ◌ 03-le-bonheur  Le bonheur   ← /define 03-le-bonheur d'abord

1/3 designés   ✓ designé   ○ à designer   ◌ à définir avant
```

A piece with no `product.md` cannot be designed, and the tree points at `/define` for it instead.

## Tests

Ten prompts in `skills/style/evals/evals.json`: the charter before any piece, the charter read and not redone, only asking what changes the prompt, the spine following the kind, the anti-reference, the surfaces deduced and validated, the two files written, the narrow suggestion rule, the tree read from disk, and working without `define`.
