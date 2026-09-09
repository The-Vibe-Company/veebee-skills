# Veebee Skills

An open-source library of Claude Code skills, published by The Vibe Company, that takes a product from raw idea to shipped code. Each skill works standalone and can be chained with the others.

## Language

**Veebee**:
The Vibe Company mascot and the name of the skill library. Always spelled `Veebee`; prefix `veebee` in commands.
_Avoid_: Vibi, Vibay, VB, Veebe

**Skill**:
One installable unit of the library, a `SKILL.md` with its own trigger and deliverable.
_Avoid_: Prompt, command, agent

**Chain**:
Any sequence of skills run one after another on the same product. A chain is optional: any skill can be the entry point.
_Avoid_: Pipeline, workflow

**Ask Veebee**:
The router skill. Given where the user is in their thinking, it names the single most appropriate skill.
_Avoid_: Help, menu, index

**Exigence Level**:
The first thing a chain settles with the user: how big and how serious the product is. Every downstream skill adapts its rigor to it. Three values: Sketch, Product, Platform.
_Avoid_: Mode, size, complexity, level 1/2/3

**Sketch**:
Exigence Level for a prototype built in one session. No tickets, no design check, shipped without a PR.

**Product**:
Exigence Level for a real product: tickets, PRs, review, design check.

**Platform**:
Exigence Level for something too big for one chain. Must be split into sub-products, each running its own chain.
_Avoid_: Epic, program

**Idea**:
The output of `eureka`: one clear idea, written in a short fixed frame that depends on its kind (a game needs a goal and a universe; a product needs a pain and who suffers it). Just enough for `challenge` to attack.
_Avoid_: Concept, pitch, vision

**Ticket**:
A tracker-agnostic unit of work produced by the library. The host agent pushes it into whatever tracker it has access to (Linear, GitHub Issues, files).
_Avoid_: Issue, task, story
