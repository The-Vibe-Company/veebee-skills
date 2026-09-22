# ticketise

Cuts a designed or defined product into tickets, one vertical slice each, written as files and then pushed to the tracker the user has connected. Step 6 of the chain. It cuts; it neither builds nor plans a calendar.

## Trigger

- `/ticketise`, or `/ticketise <slug>` for one milestone, optionally followed by a design folder, file or link.
- Model-invoked on an explicit ask: "fais les tickets", "découpe en tickets", "ticketise", "mets ça dans Linear", "write the tickets", "break this into issues", "push this to Linear".

## Input, best source first

1. **A design**: whatever came back from the design tool. Exported files, HTML read as text, images looked at, a PDF, a link. Found in the argument, then in `.veebee/design/`, then asked for once.
2. **`style`'s `prompt.md`**: the surfaces that were meant to be drawn. One missing from the design is a gap to name.
3. **`define`'s documents**: features at launch for the scope, `rules.md` for acceptance criteria, `journeys.md` for the order a user meets things, `CONTEXT.md` for the words.
4. **The user's words**: clear product instructions are enough to cut from.

It never refuses for lack of a design; it says what the tickets will lack.

## What a ticket is

A **vertical slice**: one thing a user can do, from the screen down to the data, ending in one pull request that can be checked by using it. Never a layer.

- The first ticket is the thinnest slice crossing the whole product, ugly and bare.
- One pull request: more than seven acceptance criteria, or two journeys, makes two tickets.
- The empty state, the error and the first time are criteria of their slice, not tickets of their own.
- A game is cut the same way: a mechanic playable end to end.

Tickets depend on as few others as possible, ordered by dependency, said to be an order of construction and not a schedule.

## The cut

The whole cut is shown at once, numbered, one line each, with dependencies. The user merges, splits, drops, reorders or adds until it holds. Nothing is written before.

What cannot be placed is named: a rule no ticket carries, a screen no journey reaches, a feature at launch with no screen. Holes in the product are never filled by the skill.

## The ticket

```
.veebee/tickets/NN-<ticket-slug>.md                        whole product
.veebee/milestones/<slug>/tickets/NN-<ticket-slug>.md      one milestone
```

Front-matter `id`, `title`, `milestone`, `depends_on`, `design`, `tracker`. Sections in the user's language: what the user does, what they see, done when (checked by using the product, never by reading code), the rules that apply copied from `rules.md`, how (only when code exists), and what is out of the ticket with the number of the ticket that carries it.

On an empty directory a ticket names no framework, file or table: the stack is `setup`'s fight.

## Pushing

Files first: they are the reference, they go in git, and `ship` reads them without a connector.

Then whatever is really connected in the host agent's toolset: a Linear tool, a Notion tool, a GitHub tool or `gh`. Never a guessed one. The skill asks which and where inside it, then **confirms once with the count and exact destination** before creating anything, because pushing creates things other people see. Tickets go in dependency order so relations can be linked; `tracker: { tool, id, url }` is written back into each file.

Nothing connected: the files are the result, and a later run pushes them.

A second run compares new, changed and no-longer-belonging tickets before touching anything. Pushed tickets are updated, never duplicated; nothing is deleted in the tracker; a ticket someone started is not rewritten without asking.

## Canvas

`assets/canvas.html`, `TICKETS` object: the tickets as cards in dependency order with their criteria and, once pushed, their link; the holes; the project tree. Replaced whole with `json.dumps` and `</` escaped. Artifact tool when available (favicon 🎟️), else opened from disk.

## Finish

`scripts/tickets.py` reads the whole project from disk: per piece, how many tickets and how many pushed, `/define` for a piece that is not defined, *sans design* for one cut without a design, and the first ticket to build.

```
Bourg
├── 01-poser-et-peupler   5 tickets, 5 poussés
├── 02-le-catalogue       4 tickets, 0 poussé   ← /ticketise 02-le-catalogue
├── 03-le-bonheur         pas de tickets   ← /define 03-le-bonheur d'abord
└── 04-la-vie             pas de tickets   ← /define 04-la-vie d'abord

À construire en premier : 01-poser-et-peupler/01 …
```

## Tests

Ten prompts in `skills/ticketise/evals/evals.json`: vertical slices, the cut validated before writing, the three input sources, holes named, what and how, acceptance by use, files then a confirmed push, nothing connected, a safe second run, the tree from disk.
