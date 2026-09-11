# Veebee Skills

Open-source Claude Code skills by The Vibe Company. From a blank page to a shipped product, one skill per step. Every skill works alone; chained, they take an idea all the way.

## The chain

| # | Skill | Reads | Writes |
|---|---|---|---|
| 1 | `eureka` | where you are with your idea, even a blank page | one Idea in a short frame |
| 2 | `crash-test` | an idea | `product.md`, the Product Brief, with the essence, the Exigence Level and the milestones |
| 3 | `design-brief` | `product.md` + your art direction | a prompt for Claude Design |
| 4 | `design-review` | the design back from Claude Design | verdict + list of deviations |
| 5 | `setup` | `product.md` | a challenged stack, an initialised repo |
| 6 | `tickets` | `product.md` + design | tracker-agnostic tickets |
| 7 | `ship` | one ticket | a merged PR, or a call for help. Includes the UI check against the design. |

`ask-veebee` sits above the chain: tell it where you are, it names the skill you need and hands over between skills.

Names are provisional until each skill has been grilled. Settled so far: `eureka`, `crash-test`.

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

- **`/crash-test`**: `/grill-me` for a product. Interviews you in rounds until nothing is left open, sizes the project (Sketch, Product, Platform), splits it into milestones when it is too big, and writes `.veebee/product.md`, the Product Brief. Run it again on each milestone with `/crash-test <slug>`. Definition in [docs/skills/crash-test.md](./docs/skills/crash-test.md).

The other skills are defined step by step, each one grilled before it is written. Track progress in [docs/skills/](./docs/skills/).

## Exigence Level

Set by `crash-test`, read by everyone: **Sketch**, **Product**, **Platform**. See [CONTEXT.md](./CONTEXT.md).
