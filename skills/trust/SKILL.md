---
name: trust
description: Take one sentence and come back with a product that runs. Runs the whole Veebee chain alone, answering every question itself and writing down each decision it made in the user's place. Use when the user gives an idea in one line and wants the thing built without being asked anything, in French ("fais-moi un truc qui...", "je te fais confiance", "démerde-toi", "lance trust") or English ("just build it", "make me a...", "I trust you, go"). Not for a product the user wants to shape themselves, which is eureka then define.
argument-hint: "the idea, in one sentence"
---

# Trust

One sentence in, a product that runs out. You go through the whole chain alone: find the idea, define it, settle how it looks, draw it, cut the tickets, build them. **You ask the user nothing.** Every question the chain would have asked, you answer yourself, and you write down what you decided and why, so they can disagree afterwards with a file in front of them.

Answer in the language the user writes in. Everything you write is theirs, in their language.

## The deal

Say it once, at the start, in two lines: what you are about to do, that you will decide everything yourself, and where the decisions will be written. Then go. No check-in, no *ça te va ?*, no progress question. The invocation is the permission.

There are exactly three moments you stop:

1. **No sentence at all.** Ask for it, in one question, and nothing else.
2. **The directory is an existing repository with a remote.** Other people may be behind it, so confirm once before the first push, naming the remote and the branch. A fresh directory has no remote and needs no confirmation.
3. **The sentence asks for something you should not build.** Say so plainly in one sentence and stop.

## How you answer for them

Every decision you take in their place goes in `.veebee/trust/decisions.md`, as it happens: the question, your answer, and the reason in one line.

```markdown
## Taille
Une seule tranche : « un truc qui me rappelle d'arroser mes plantes » tient debout avec une liste et un rappel.

## Qui s'en sert
La personne qui a écrit la phrase, seule, sur son téléphone. Rien dans la phrase ne parle d'équipe.

## Le look
Sombre, dense, sans image. Tu as dit « un truc », pas « une belle appli » : je suis allé au plus sobre. Changeable.
```

A reason is always one of three things: something in their sentence, a fact you went and checked, or a convention you name as a convention. **Never a preference with nothing behind it.** When you truly had nothing to go on, say so: *rien ne pointait dans un sens, j'ai pris le plus simple à défaire*.

Two rules keep the file honest. Write the decision when you take it, not at the end, because a run can be interrupted. And take the reversible option whenever two are close: you are deciding for someone who is not here.

## The chain

Each step is the existing skill. Invoke it and follow it, with one difference: **you play the user**. When it would ask, you answer, you log, you continue. Everything else in those skills still binds you, especially what they refuse to do.

Read where you are with `python3 <skill>/scripts/chain.py <project root>` before starting and after every step. A run can be interrupted and picked up again: what is on disk is the truth.

### 1. The idea — `eureka`

The sentence is the idea. Fill the Idea frame from it, invent nothing it does not contain, and pick the `kind` (product, game, skill, content, service) from what it describes. Write `.veebee/idea.md`.

### 2. The product — `define`

**The size is decided before the first question: one piece.** You are building the smallest version that stands on its own, the one thing the sentence promises, whole. Everything else the idea holds goes into `features.md` under *plus tard*; nothing goes into milestones.

Then answer `define`'s tree yourself, and stop it early: **a question whose answer would not change what you are about to code is not asked at all.** Ten to fifteen decisions is a defined product; forty is you talking to yourself. Skip the deep dives unless a rule is needed to make a screen behave.

Write the documents and `CONTEXT.md` as `define` says.

### 3. The look — `style`, then drawn here

Run `style`'s taste interview against yourself and write the charter, `.veebee/style.md`. Taste questions are where you have least to go on: take the plainest option and mark it changeable in the decisions.

`style` normally hands out a prompt to paste elsewhere. Here it gets drawn on the spot: give the charter and the surfaces to the design skill you actually have, in this order — the built-in `design`, else `frontend-design`, else `design-frontend-dev` — and put what comes back in `.veebee/design/`. None of them installed: keep the charter alone and say so in the journal; the tickets will describe screens instead of showing them.

### 4. The tickets — `ticketise`

Cut, and validate the cut yourself. **The tickets stay files.** Nothing is pushed to Linear, Notion or anywhere else: that would put things in front of other people without anyone asking for it. The user can push them later by running `/ticketise` again.

A hole `ticketise` would have named is a decision for you: fill it, write it in `decisions.md`, keep going.

### 5. The build — `autopilot`

Run it over every ticket, in dependency order. Its opening confirmation is already answered: this run is it. Everything else it does stands, especially what it refuses.

- **A fresh directory**: `git init`, a first commit, and every ticket merged straight into `main` after the same checks — the tests, the product actually used, the cold self-review. No remote, no pull request, nothing outward.
- **An existing repository with a remote**: the normal pull request flow, after the one confirmation above.

`autopilot` blocks on a product question. Here there is nobody to ask, so **you answer it** with the smallest reversible choice, write it in `decisions.md`, and the ticket goes on. What stays blocked is only what no decision can unblock: a missing key, a service that does not exist, a check that will not pass honestly.

## The stack

`setup` does not exist yet, so you pick.

An existing project: you adopt what is there and propose nothing. An empty directory: choose the plainest thing that can run what the sentence describes, name it in one line in the decisions, and set it up — no paid service, no account to create, no key the user does not have, and as few dependencies as will do the job. If the idea genuinely needs a paid or external service, build against a fake as `autopilot` does and write the ticket to plug in the real one.

## What you never do

- Ask anything outside the three moments above.
- Claim a product that runs without having run it yourself, opened it, and gone through the journeys.
- Push, publish, deploy, create a remote repository, send anything, or put a ticket in a tracker.
- Decide for money, authentication, permissions or personal data by faking them: those stay blocked, as in `autopilot`.
- Bypass a check to reach the end.
- Spend the whole run on step 2. If the decisions file is long and no code exists yet, you are in the wrong step.

## The journal and the page

`.veebee/trust/journal.md` is written as you go: the step, what happened, what was decided, what got blocked. `decisions.md` sits next to it.

`assets/canvas.html` shows the chain while it runs: the five steps, the one in progress, the decisions taken, the tickets merged. Edit only the `RUN` object, build it in full and replace the declaration with `json.dumps`, escaping `</`:

```python
s = re.sub(r"const RUN = \{.*?\n\};",
           lambda m: "const RUN = " + json.dumps(d, ensure_ascii=False, indent=2).replace("</", "<\\/") + ";",
           open(dst).read(), count=1, flags=re.S)
```

Artifact tool when it is really available (favicon 🤝, title the product's name), republished at every step. Otherwise written next to the journal; it reloads itself.

## The end

Run the product one last time and go through it as a first-time user before you say a word.

Then, in this order and nothing else:

1. **What it is and how to run it**: the command, in a block they can click.
2. **The three decisions most likely to be wrong**, from `decisions.md`, each in one line with where to change it.
3. **What is not in it**: the *plus tard* list, short.
4. **What is blocked**, if anything, and the smallest thing that unblocks it.
5. Where the decisions, the journal and the tickets are, and that `/define`, `/style`, `/ticketise` and `/autopilot` take over from here for the rest.

If the product does not run, say that first and say where it stopped. A run that ends on a broken product and a cheerful summary is the one failure that makes the skill worthless.
