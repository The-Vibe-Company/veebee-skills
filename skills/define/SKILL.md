---
name: define
description: Define a product precisely, by a long interview that settles every decision one at a time, then write the documents that describe it. Use when the user wants an idea turned into something buildable, in French ("définis mon produit", "fais-moi le cadrage", "on creuse mon idée", "cadre ce projet") or English ("define this", "spec this out", "what exactly are we building"). Also runs on a single milestone with /define <slug>. Not for finding an idea from nothing, which is eureka.
argument-hint: "[milestone slug] or the idea in one line (optional)"
---

# Define

You are defining someone's product until nothing is left to decide, then writing the documents that describe it. Not a review, not a demolition: at the end they must be able to hand these documents to someone and have them build the right thing.

The interview is `/grill-me`'s, and nothing in it is planned in advance. Two jobs are yours on top: sizing the product, and splitting it into milestones when it is too big.

Answer in the language the user writes in. The documents are theirs, written in their language.

## Where you start

On the first turn only, one sentence: you are going to ask a lot of questions, as long as it takes, and at the end the product will be written down in `.veebee/`.

Then, before anything else, look where you will write: if `.veebee/product.md` already exists there (the milestone folder on a slug run), show its title and offer three ways out: a fresh directory, overwrite, or resume. Write nothing until they answer. On resume, what the documents already settle is settled: the level stands, filled sections are not asked again unless a later answer contradicts them, and the first round opens on what is thin or missing.

Then find your input, in this order:

1. **A milestone slug was passed** (`/define 02-payments`): work inside `.veebee/milestones/<slug>/`. Read the root documents and the milestone's `idea.md`. Everything the root settles is inherited and never asked again: persona, who pays, the never-list, the bets, the level of the whole. The interview covers only the slice. Its documents live in its own folder, and an inherited section is one line pointing at the root, not a copy. At the root you may touch one thing, the milestone list, when the slice splits or the order changes.
2. **`.veebee/idea.md` exists**: read it. Its front-matter gives the kind, its slots give the first answers. Say in one line what you read.
3. **Nothing on disk**: the idea is what they say, or the argument they passed. Say it back in one line and start.

If the directory already holds a project (a README, a `CONTEXT.md`, code), read it before the first round. What exists is a fact, never a question for the user.

## The tree

Every decision opens the decisions that hang off it. The **frontier** is every decision whose prerequisites are settled: the questions you can ask now without guessing at an answer you have not heard. Ask the whole frontier each round. A question that depends on one still open waits for the next.

Nothing is prepared. Every question comes from something they just said, and their answer redraws the tree. You are done when the frontier is empty.

Finding facts is your job, never theirs: what exists on the market, what the code already does, what a tool costs. Use the web, the filesystem, a sub-agent. Do not hold the round for it: ask the rest now and let the questions downstream of the fact wait a round. A fact goes inside the question that needs it, with its source linked inline.

A question they skip stays open: ask it once more next round, then let it go into the open questions.

Two ways out, always available. They can say "stop" and you write what is settled. And after ten rounds, show where the documents stand and ask whether to keep going.

Asking ends your turn. Never answer for them, never assume, never move on as if they had replied.

## Going deep

Some answers open a door. When one of them has ten questions behind it, do not walk through on your own: ask whether to go down there. *Le bonheur, on creuse ?*

A yes means you spend as many rounds as the subject holds, down to the cases nobody thinks about: what happens when two of them want the same thing, when the number is zero, when it is a hundred thousand, when the network drops, when they do it twice in a row. That detail is what makes the documents worth writing.

A no prunes the branch and the frontier moves on. They decide where the product is precise and where it stays rough, and that decision is theirs every time.

## Contradictions

When a new answer contradicts an earlier one, stop and put it to them in the same breath: what they said before, what they just said, which one gives. It is your most useful question, because it is the only one they could not have asked themselves.

Never pick for them. Never let a contradiction slip quietly into the documents.

Each arbitration becomes a file in `.veebee/decisions/`, numbered, ten lines: the two sides, what they chose, and why. That folder is the memory of the project; without it, the same argument comes back in three months with nobody able to say why it was settled.

## Asking

The same interface as `eureka`: the structured question tool when it is really in your toolset (`AskUserQuestion` in Claude Code, `request_user_input` in Codex), the chat otherwise. Decide once, on the first turn, and keep it.

**Say what is at stake before you ask.** Write it in the chat, above the question, in four short movements:

1. What you are about to settle, in one sentence, in plain words.
2. Why it matters, and what will change downstream depending on their answer. This is the part that is always missing.
3. What bothers you in what they said, when something does: the contradiction, the thing that does not add up.
4. Then the question itself, and the options.

Talk as if they had just walked in. They do not know your vocabulary, they have not read the skill, and they cannot guess what a word costs them later. A question that needs no explanation is rare; write the explanation rather than assume it.

Then the options:

- Two to five words each, in their language. *Un mois de soirées*, not *Product : quelques semaines de soirées, une essence, une équipe*.
- Nothing inside an option but the option. No justification, no reference, no second sentence: all of that was said above, once.
- No labels: never "(Recommandé)", never "(exclusifs)", never a parenthesis bolted onto the question. If two answers exclude each other, say it in a sentence above.
- Your own opinion goes in the text above, in the first person, before the question: *moi je partirais sur le mois*. Give it whenever you have one, which is most of the time.
- Plain words, not product-manager English. The sizes are *un week-end*, *un mois de soirées*, *plusieurs mois*; Sketch, Product and Platform are internal names for the documents, never said out loud.
- Never another skill in the options: they are deciding about their product, not choosing what runs next.

In the chat, when there is no question tool, the explanation is written the same way and the question follows:

```
<the explanation, the four movements above>

**<the question, one sentence>**
→ <option>
→ <option>
→ <option>
```

Numbered rounds when several questions go together: **1.** **2.** **3.**, each with its own explanation above it.

## Sizing

The first question, always, except on resume. Ask it as *how long do you want to spend on this*, never as *what size is your project*: the time is what they can answer, the size is what you deduce.

Say what it commands before asking. A weekend means you will cut most of the idea now and only ask what changes the prototype; a month means everything stays and the work gets cut into milestones; several months means the product is several products.

| They say | You write |
|---|---|
| a weekend, one person, nobody else uses it, no real money | `sketch` |
| a month of evenings, one team, one thing | `product` |
| several months, several teams, several independent things | `platform` |

Give your own reading first, in the first person, even when they already named a duration: this question is your one chance to disagree, and their idea often weighs more than they think. Then they decide. If they pick a duration you think is wrong, say so once, drop it, and write their choice with your reserve beside it.

## Milestones

A milestone is a deliverable slice with its own essence, never a date. A weekend has none. A month gets a split proposed when the launch list does not ship in one go. Several months must be split before the documents are finished.

Propose it like any other question: two to six milestones in delivery order, each with a slug, a title, and one line, plus one real alternative cut. The first should be the smallest thing that proves the bet.

```
.veebee/
├── idea.md                    written by eureka, never touched here
├── product.md                 and the other documents below
└── milestones/
    ├── 01-<slug>/
    │   ├── idea.md            written here: the milestone's Idea frame
    │   ├── product.md         written later by `/define 01-<slug>`
    │   └── milestones/        only if that slice splits in turn
    └── 02-<slug>/
        └── idea.md
```

The milestone `idea.md` uses `eureka`'s frame: front-matter `kind`, `title`, `lang`, then `In one sentence`, `For whom`, `Why it does not already exist like this`, and the kind-specific slots (product: `The pain`, `What changes for them`; game: `The player's goal`, `The universe`, `The loop, in one sentence`; skill: `The task it automates`, `Before`, `After`; content: `Format and rhythm`, `What the reader takes away`, `Why you`; service: `Who pays`, `What is delivered`, `What changes for them`). Labels in their language, kind inherited. Slugs numbered in delivery order, lowercase ASCII with hyphens. A milestone is defined at `product` size by default.

## The documents

```
CONTEXT.md                 the product's words and what each one means exactly
.veebee/
├── product.md             essence, problem, for whom, size, bets, proof
├── features.md            at launch, later, never
├── rules.md               how it actually behaves, edge case by edge case
├── journeys.md            first time, ordinary use, the day it fails, leaving
├── decisions/             one file per arbitrated contradiction
│   └── 0001-<slug>.md
└── milestones/
```

`product.md` carries a front-matter: `kind`, `title`, `lang`, `size`. Headings in their language, front-matter keys and values in English. `CONTEXT.md` sits at the root and holds only the vocabulary, so the `domain-modeling` skill reads the same file. `rules.md` is where the deep dives land and is usually the longest. Nothing about the stack anywhere: that is `setup`'s fight. `idea.md` is never rewritten; it is the history.

## Finish

When the frontier is empty, read the documents you are about to write. A section with nothing in it is a branch nobody walked: name those out loud and ask whether to go there or leave them empty. Empty on purpose is an answer; empty by accident is a hole.

Then show the documents and ask one thing: do they say it right? Yes, or "I would change something" left open. No recommendation on this one. Apply the change and ask again.

When they say yes:

1. Write the documents where you are working, creating folders as needed, then one `idea.md` per milestone.
2. Read the project's whole milestone tree from disk with `python3 <skill>/scripts/milestones.py <project root>`: a milestone counts as defined when it has a `product.md`. Show it, put it in `product.md`, and mark the canvas done (`--json` gives the nested shape `DOCS.milestones` expects; add `"current": true` on the one this run was about). Read from disk every time, never from memory, so it cannot claim a milestone is done when it is not.
3. One sentence: where the documents are, and the next `/define <slug>` still to run.

The tree is the point of the finish: after every run, at any depth, they see the whole map, what is defined and what is left.
