# Veebee Skills

Open-source Claude Code skills by The Vibe Company. From a blank page to a shipped product, one skill per step. Every skill works alone; chained, they take an idea all the way.

## The chain

| # | Skill | Reads | Writes |
|---|---|---|---|
| 1 | `eureka` | where you are with your idea, even a blank page | one Idea in a short frame |
| 2 | `define` | an idea | the documents: `CONTEXT.md`, and `product.md`, `features.md`, `rules.md`, `journeys.md`, `decisions/`, `milestones/` |
| 3 | `style` | the documents + your taste, by interview | `style.md` (the charter) + one `prompt.md` per piece, to paste into a design tool |
| 4 | `design-review` | the design back from Claude Design | verdict + list of deviations |
| 5 | `setup` | `product.md` | a challenged stack, an initialised repo |
| 6 | `ticketise` | the design, else the documents, else your words | vertical-slice tickets in `.veebee/tickets/`, pushed to Linear, Notion, GitHub Issues |
| 7 | `autopilot` | the tickets | merged PRs one after another, test-first, checked in the browser, until something truly blocks; a journal of what waits for you |

`trust` sits beside the chain: one sentence in, a product that runs out. It goes through every step alone, answers every question itself, and writes down each decision it took in your place.

`ask-veebee` sits above the chain: tell it where you are, it names the skill you need and hands over between skills.

Names are provisional until each skill has been grilled. Settled so far: `eureka`, `define`, `style`, `ticketise`, `autopilot`, `trust`.

## Install

In Claude Code:

```
/plugin marketplace add The-Vibe-Company/veebee-skills
/plugin install veebee-skills@veebee
```

To try it from a local checkout for one session:

```
claude --plugin-dir /path/to/veebee-skills
```

## Available today

- **`/eureka`**: find one clear idea by interview, from a blank page or from a pain. Shows the idea taking shape on a live page while you talk, and writes `.veebee/idea.md` when it is done. Definition in [docs/skills/eureka.md](./docs/skills/eureka.md).

- **`/define`**: a long interview that settles every decision about the product one at a time, then writes the documents that describe it. No topic list: every question comes from something you just said. It asks before going deep on a subject, puts your contradictions back in your face, sizes the project and cuts it into milestones. Definition in [docs/skills/define.md](./docs/skills/define.md).

- **`/style`**: settles how the product looks, by an interview about your taste, then writes the prompt you paste into a design tool. It writes the charter once for the whole product, then one prompt per piece with the surfaces deduced from your journeys and validated by you. Adapts to the kind: screens for an app, technique and palette for a game. Definition in [docs/skills/style.md](./docs/skills/style.md).

- **`/ticketise`**: cuts the product into tickets, one vertical slice each, that end in one pull request checked by using it. Reads what came back from the design tool, else the documents, else your words. Shows the whole cut first, names the holes instead of filling them, writes the tickets as files, then pushes them to the tracker you have connected. A second run updates, never duplicates. Definition in [docs/skills/ticketise.md](./docs/skills/ticketise.md).

- **`/autopilot`**: builds the tickets one after another while you are away. Test-first, every acceptance criterion checked in the running product, shipped as a pull request through `ship-pr-dev` when you have it, merged only when every check is green. It goes around blocks when that is safe and never bypasses a check. You come back to a journal that opens with what needs you. Definition in [docs/skills/autopilot.md](./docs/skills/autopilot.md).

- **`/trust`**: one sentence, and at the end a product that runs. It goes through the whole chain alone and asks you nothing, building the smallest version that stands on its own. Everything it decided in your place is in `.veebee/trust/decisions.md`, with a reason per line. Definition in [docs/skills/trust.md](./docs/skills/trust.md).

The other skills are defined step by step, each one grilled before it is written. Track progress in [docs/skills/](./docs/skills/).

## Size

Set by `define`, read by everyone: **Sketch**, **Product**, **Platform**. See [CONTEXT.md](./CONTEXT.md).
