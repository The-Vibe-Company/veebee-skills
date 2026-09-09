# eureka

Finds one Idea, from a blank page or from a pain. Step 1 of the chain.

## Trigger

- `/eureka`
- Model-invoked on phrases like "je cherche une idée", "j'ai pas d'idée", "trouve-moi un projet", "I need an idea", "what should I build".

## Conversation

- Always opens with the same question: where are you with your idea?
- Three branches:
  - **Blank page**: start from domains that interest the user and the kind of thing they want to make (product, game, skill). May propose three directions at some point to get a reaction, but converges on one Idea. Never delivers a list.
  - **A pain**: start from who suffers it and when.
  - **An idea already clear**: put it into the frame and point to `challenge` without digging.
- One to three questions per turn, adapted to the previous answer. No numbered rounds. Blank page: one or two on the first turn. Idea already there: at most two per turn, only for empty slots.
- Slots hold only what the user said. An inferred slot is marked "(to confirm)". The assistant proposes a working title as soon as the one-sentence slot exists.
- Reply, Idea and slot labels in the user's language.
- Competitive study is offered, never imposed. If yes: three to five existing solutions, what they do, what they miss for the target audience, one line each. No pricing, no market share.

## The Idea frame (about ten lines)

Common to every kind: kind of idea, one sentence, for whom, why it does not already exist like this.

- **Product or tool**: the pain, what changes for the person.
- **Game**: the player's goal, the universe, the game loop in one sentence.
- **Skill or agent**: the automated task, before and after.

Kind-specific slots appear once the kind is known. Extensible with new kinds later.

## Live artifact

Publishes an Artifact page at the first turn and republishes it to the same URL after every answer. A blank sheet: "Sans titre" as the title until the Idea has a name, the Idea underneath in a few plain sentences, and this turn's questions styled at the bottom. Nothing else: no slots, no transcript, no timeline.

## Questions

In the chat: 1️⃣ 2️⃣ 3️⃣, the point in bold, the question in one sentence, then two to four lettered options (a/ b/ c/ d/) so a letter is enough to answer. Open question only when options would be silly. 💡 suggestion only when it carries information drawn from the interview itself. One question after a short answer. On the canvas, same questions, same order, no options.

## Output

- `.veebee/idea.md` in the current directory, created if missing. If an idea already exists there, ask before overwriting.
- Ends when every slot is filled and the user confirms. Writes the file, republishes the artifact one last time, says one sentence: next step is `/challenge`. Never launches it itself.
