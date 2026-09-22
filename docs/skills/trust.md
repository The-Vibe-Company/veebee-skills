# trust

One sentence in, a product that runs out. Goes through the whole chain alone — `eureka`, `define`, `style`, `ticketise`, `autopilot` — answering every question itself and writing down each decision taken in the user's place. Beside the chain, not a step in it.

## Trigger

- `/trust <the idea in one sentence>`.
- Model-invoked on an explicit ask: "fais-moi un truc qui…", "je te fais confiance", "démerde-toi", "just build it", "make me a…", "I trust you, go".

## It asks nothing

Two lines at the start saying what is about to happen and where the decisions will be written, then it goes. Three stops exist:

1. **No sentence** — one question, nothing else.
2. **An existing repository with a remote** — one confirmation before the first push, because other people may be behind it. A fresh directory has no remote and needs none.
3. **Something that should not be built** — one sentence, and it stops.

## Decisions

`.veebee/trust/decisions.md`, written as each decision is taken, never at the end: the question, the answer, the reason in one line. A reason is something in their sentence, a fact that was checked, or a convention named as a convention — never a preference with nothing behind it. When nothing pointed anywhere, it says so. Between two close options, the reversible one wins.

## The chain, played alone

| Step | What changes |
|---|---|
| `eureka` | The sentence is the idea. Nothing is invented beyond it; the `kind` comes from what it describes. |
| `define` | Size settled first: **one piece**, the smallest version that stands alone. No milestones, the rest into `features.md` under *plus tard*. A question whose answer would not change the code is not asked at all; ten to fifteen decisions, not forty. |
| `style` | The charter is written, then **drawn on the spot** by the design skill actually installed (built-in `design`, else `frontend-design`, else `design-frontend-dev`) into `.veebee/design/`. Nothing is handed out to paste elsewhere. |
| `ticketise` | The cut is validated by the skill itself. **Tickets stay files**: nothing reaches a tracker, even a connected one. |
| `autopilot` | Its opening confirmation is this run. A product question it would block on is answered with the smallest reversible choice and logged. |

## Where it runs

A fresh directory stays local: `git init`, a commit per ticket into `main` after the same checks — tests, the product actually used, the cold self-review. No remote, no pull request, nothing outward. An existing repository with a remote gets the normal pull request flow, after the one confirmation.

`setup` does not exist yet, so `trust` picks the stack: what is already there in an existing project, and otherwise the plainest thing that runs the idea — no paid service, no account to create, no key the user does not have. Named in one line in the decisions.

## Never

Ask outside the three stops. Claim a product that runs without having run it and gone through the journeys. Push, publish, deploy, create a remote repository, send anything, or file a ticket in a tracker. Fake money, authentication, permissions or personal data. Bypass a check. Spend the whole run on `define`.

## Canvas

`assets/canvas.html`, `RUN` object: the sentence, the five steps with the one in progress, what is happening right now, the decisions taken, the tickets, anything blocked, and the command to run the product at the end. Replaced whole with `json.dumps`, `</` escaped. Artifact tool when available (favicon 🤝).

## The end

The product is run and used first. Then, in this order: what it is and the command to run it, the three decisions most likely to be wrong with where to change them, the *plus tard* list, anything blocked with the smallest thing that unblocks it, and where the decisions, journal and tickets are. A failure is said first, never softened.

`scripts/chain.py` reads where a run stands from disk — idea, product, charter, design, tickets, merged tickets — so an interrupted run picks up where it left off.

## Tests

Twelve prompts in `skills/trust/evals/evals.json`: asks nothing, decisions written as they happen, one slice only, drawn here rather than pasted, tickets stay files, a fresh directory stays local, an existing remote asks once, product questions answered instead of blocked, the stack chosen and named, never claiming an unrun product, the end in order, and resuming from disk.
