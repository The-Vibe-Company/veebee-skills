# Changelog

## 0.9.0

- `define` defines, it no longer plans. The skill was asking how long the work would take, what would ship first, how many evenings it cost: questions for someone about to build, not someone laying out what the product is.
- The size is now asked as **how many independent pieces the product holds**, not how long it takes. One piece is a `sketch`, several pieces one `product`, several products a `platform`.
- Milestones are pieces of the product ordered by dependency, and the skill says so: a reading order, not a schedule. The first one is the piece that carries the bet, because its definition constrains the others.
- Calendar words are out of every question: no *soirées*, no *semaines*, no *livrer*, no *sprint*.

## 0.8.0

- `define` puts the reasoning inside the question card, not in the chat above it. A card read alone, without scrolling, is now answerable: it carries what is being settled, why it matters, what changes downstream, and what bothers the skill, before the question itself. The chat around the questions holds only transitions.

## 0.7.0

- `define` asks differently. Every question is now preceded, in the chat, by what is being settled, why it matters, what will change downstream depending on the answer, and what bothers the skill in what the user said. The old version assumed the user already knew what a question was about.
- Options hold nothing but the option, two to five words. No justification stuffed inside them, no "(Recommandé)", no "(exclusifs)", no parenthesis bolted onto the question. The skill's own opinion is given above the question, in the first person.
- The size is asked as *how long do you want to spend on this*, in plain words: un week-end, un mois de soirées, plusieurs mois. `sketch`, `product` and `platform` stay internal names for the documents.

## 0.6.1

- `define`: the description in the frontmatter no longer breaks strict YAML parsers; it carried unquoted colons.
- `define` is published on Companion, next to `eureka`, with `eureka` declared as its dependency.

## 0.6.0

- `crash-test` is renamed **`define`**, and rewritten. The name promised a demolition and delivered a spec; the skill defines a product, so it says so.
- **No topic list.** The design tree is now the only engine: every question comes from something the user just said, so a game and a newsletter never get the same interview. The nine mandatory branches are gone.
- **Going deep is the user's call.** When an answer opens ten questions behind it, the skill asks before diving. A yes buys rounds of edge cases; a no prunes the branch.
- **Contradictions are put back immediately**, both sides quoted, never resolved by the skill, and written to `.veebee/decisions/`.
- **No question limit**: it runs as long as it takes, with a stop word and a ten-round checkpoint.
- **A folder of documents** instead of one Brief: `CONTEXT.md` at the root for the vocabulary, and `product.md`, `features.md`, `rules.md`, `journeys.md`, `decisions/`, `milestones/` under `.veebee/`.
- **Questions written the way you talk**: one short sentence, options that name the thing and stop, no justification inside an option, one 💡 line at most and only when it changes the pick.
- The finish names the sections still empty before writing, so empty on purpose is an answer and empty by accident is caught.

## 0.5.0

- `crash-test` ends every run by showing the project's whole milestone tree, at any depth, marking each one validated (it has a `product.md`) or still to validate, with the command to run next. The tree is read from disk by `scripts/milestones.py`, so it can never claim a milestone is done when it is not. The canvas renders nested milestones with the same marks.

## Unreleased

- `eureka` merged with Companion 0.3.3 (Victor Nivault): the question tool is used only when callable in the current mode and blocking; asynchronous question tools are never used; a question whose card disappeared is repeated in full in the chat. Two evals added. Companion version 0.4.1.

## 0.4.1

- `crash-test` grilled: same question interface as `eureka` (question tool when present, else 1️⃣ blocks with lettered options and a recommendation on every question); written sizing heuristics (how long, how many people, how many essences); skipped questions asked again once then parked; a milestone run inherits everything the root Brief settles and touches only its own folder plus the root Milestones section; an existing project in the directory is read as facts; triggers narrowed to explicit asks. Sixth eval on a milestone run.

## 0.4.0

- New skill `crash-test`: `/grill-me` for a product. Rounds of ❓/➡️ questions until nothing is left open, Exigence Level as the first decision, milestones when the product is too big, one folder per milestone under `.veebee/milestones/`, and the Product Brief in `product.md`. Five evals.
- `eureka` now points to `/crash-test` at the finish.
- `eureka` asks three to five questions per turn instead of one to three; two or three on a blank first turn.

## 0.3.2

- `eureka` in Codex: the question tool is used only when it is really in the toolset, and asking always ends the turn (Codex improvised answers in Default mode, where `request_user_input` only exists with `default_mode_request_user_input = true`).
- `eureka`: a picked option plus free text refines the pick instead of replacing it.
- `eureka` without the Artifact tool: chat-only interview, the Idea shown in the chat at the checkpoint and at the finish, the browser page opened once at the finish instead of at the first turn.

## 0.3.1

- `eureka` works outside Claude Code. The canvas has three transports: Artifact tool, default browser (Codex and any runtime with a shell: the page is opened once from disk and reloads itself), or a code block.
- `eureka` asks through the runtime's structured question tool when there is one (`AskUserQuestion`, `request_user_input`), one call per turn or per question; the 💡 suggestion becomes the first, recommended option. The chat format stays the fallback.
- Canvas: UTF-8 declared, finishing line points to `.veebee/idea.md`.

## 0.3.0

- `eureka` grilled and retested on five evals (`skills/eureka/evals/evals.json`).
- Fires on blank-page phrases only; "I have a rough idea" is left to `challenge`.
- Two new kinds, content and service, with their slots.
- `idea.md` opens with a YAML front-matter: `kind`, `title`, `lang`.
- Stop word and a ten-turn checkpoint.
- One-sentence orientation on the first turn.
- Existing `idea.md`: fresh directory or overwrite, nothing written before the answer.
- Finishing sentence points to the file until `challenge` ships.
- Other takes the next free letter; suggestions may use the opening message; kind lives in the front-matter only.

## 0.2.1

- `eureka`: the first turn opens with two or three sentences on what the skill does and what it is for, before the first question.
- `eureka`: once nothing is left to ask, the canvas shows the Idea in short headed sections and the skill asks one thing: does the page say it right?
- `eureka`: **e · Autre** only when the listed options are closed choices; never a workflow choice in the options.

## 0.2.0

- `eureka`: blank-sheet canvas ("Sans titre", the idea in prose, this turn's questions at the bottom).
- `eureka`: questions numbered 1️⃣ 2️⃣ 3️⃣ with lettered, vivid options, a fixed **e · Autre**, and a 💡 suggestion drawn from earlier answers.
- `eureka`: a loved reference is a taste signal, not a template to map onto the idea.
- `eureka`: canvas path unique per session, so two sessions in one directory no longer overwrite each other.

## 0.1.0

- First skill: `eureka`, finds one idea by interview, from a blank page or a pain.
