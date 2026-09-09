# Changelog

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
