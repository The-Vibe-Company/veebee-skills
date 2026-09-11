# eureka

Finds one Idea, from a blank page or from a pain. Step 1 of the chain.

## Trigger

- `/eureka`
- Model-invoked on blank-page phrases only: "je cherche une idée", "j'ai pas d'idée", "trouve-moi un projet", "I need an idea", "what should I build". Never on "I have a rough idea": that is `crash-test`'s territory.

## Conversation

- First turn opens with two or three sentences on what Eureka does and what it is for (one Idea by interview, a canvas that fills as the user answers, `.veebee/idea.md` at the end, ready for `crash-test`), then always the same question: where are you with your idea?
- Three branches:
  - **Blank page**: start from domains that interest the user and the kind of thing they want to make (product, game, skill). May propose three directions at some point to get a reaction, but converges on one Idea. Never delivers a list.
  - **A pain**: start from who suffers it and when.
  - **An idea already clear**: put it into the frame and point to `crash-test` without digging.
- Three to five questions per turn, adapted to the previous answers, never fewer than two after the opening one; two or three on a blank first turn. No numbered rounds. The user can say stop at any time; after ten turns the skill shows the page and asks whether to continue. Blank page: one or two on the first turn. Idea already there: at most two per turn, only for empty slots.
- Slots hold only what the user said. An inferred slot is marked "(to confirm)". The assistant proposes a working title as soon as the one-sentence slot exists.
- Reply, Idea and slot labels in the user's language.
- Competitive study is offered, never imposed. If yes: three to five existing solutions, what they do, what they miss for the target audience, one line each. No pricing, no market share.

## The Idea frame (about ten lines)

Common to every kind: kind of idea, one sentence, for whom, why it does not already exist like this.

- **Product or tool**: the pain, what changes for the person.
- **Game**: the player's goal, the universe, the game loop in one sentence.
- **Skill or agent**: the automated task, before and after.
- **Content** (newsletter, channel, book, podcast): format and rhythm, what the reader takes away, why you.
- **Service** (gig, agency, event, course): who pays, what is delivered, what changes for them.

Kind-specific slots appear once the kind is known. The file opens with a YAML front-matter: `kind`, `title`, `lang`, keys in English. Extensible with new kinds later.

## Canvas

One page, `assets/canvas.html`. With the Artifact tool, published at the first turn and republished to the same URL after every answer, so the Idea takes shape live. Without it (Codex), the interview is chat only: the Idea appears in the chat, as short headed sections, at the ten-turn checkpoint and at the finish, and the page is then written and opened once from disk in the default browser, reloading itself if a change is asked. A blank sheet: "Sans titre" as the title until the Idea has a name, the Idea underneath in a few plain sentences. Nothing else: no questions, no competitive study, no slots, no transcript, no timeline.

## Questions

Through the runtime's structured question tool when it is really in the toolset (`AskUserQuestion` in Claude Code, `request_user_input` in Codex: Plan mode, or every mode with `default_mode_request_user_input = true`): the point as header, the question in one sentence, two to four options with an emoji and a one-line description, the suggested option first with "(Recommended)" and its reason, no "Other" option since the tool offers free text itself. One call per turn, or one per question when the tool takes only one. Otherwise in the chat: 1️⃣ 2️⃣ 3️⃣, the point in bold, the question in one sentence, then two to four lettered options plus Autre on the next free letter when the options are closed choices, so a letter is enough to answer. Open questions (title, memory) always in the chat. 💡 suggestion whenever earlier answers favour an option, naming the answer that points there; none on questions about taste or memories. Asking ends the turn: the skill never answers for the user. A picked option plus free text: the text refines the pick, it does not replace it.

## Output

- `.veebee/idea.md` in the current directory, created if missing. If an idea already exists there, show its title and offer two ways out, a fresh directory or overwrite, and write nothing until the user answers.
- When nothing is left to ask, the canvas switches to short headed sections and the skill asks one thing: does the page say it right? Yes, or an open "I would change something". Never a workflow choice in the options.
- Ends when the user confirms. Writes the file, updates the canvas one last time, says one sentence: the Idea is in `.veebee/idea.md`. and the next step is `/crash-test`. Never launches another skill.

## Tests

Five prompts in `skills/eureka/evals/evals.json`, one per branch and kind, plus five objective checks. Run them after every change.
