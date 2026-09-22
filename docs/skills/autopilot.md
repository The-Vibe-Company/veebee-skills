# autopilot

Builds the tickets one after another, each one coded test-first, shipped as a pull request and merged, without a human in the loop, until something truly blocks. Step 7 of the chain, the last one.

## Trigger

- `/autopilot`, or `/autopilot <slug>` for one milestone.
- Model-invoked on an explicit ask: "code les tickets", "enchaîne les tickets", "lance l'autopilot", "construis tout pendant la nuit", "build the tickets", "work through the backlog", "run autopilot".

## Before the first ticket

The only moment the user is there. The skill checks the repository (clean tree, base branch up to date, remote, `gh`), the tickets, whether `ship-pr-dev` is invocable, the CI and branch protection, and the merge methods allowed. Missing pieces are reported with the exact command; nothing is stashed or discarded.

Then one confirmation naming the scope, the base branch and the tracker. That yes is the explicit request to merge that `ship-pr-dev` requires, for this run only. No question after it.

## Which ticket next

`scripts/queue.py` before every ticket, never memory. Done means `status: done` on the base branch. Ready means every dependency done and nothing in `.veebee/autopilot/blocked.json`. Pieces in order; a later piece starts when the earlier one is fully done. Cross-piece dependencies are written `<piece>/<id>`.

## One ticket

1. Branch `autopilot/<piece>-<id>-<ticket-slug>` from the freshly pulled base.
2. Read the ticket, its design, its rules, `CONTEXT.md`, the code. *Hors ticket* is the non-goal list.
3. **Test-first**, with the `tdd` skill when present: one acceptance criterion at a time, a failing test at the public interface, then the least code. The seams `tdd` wants confirmed are the acceptance criteria, already validated in `ticketise`; they are listed in the pull request.
4. **Checked by use**: the product is run and every criterion checked, in a real browser against the design, empty state and error included.
5. `status: done` set in the ticket, in the same branch.
6. **Ship** through `ship-pr-dev` in `ship` mode, or the built-in ship: the repository's checks, a cold self-review, the PR, `gh pr checks --watch`.
7. **Merge** on a ready verdict only, with the allowed method, branch deleted.
8. Back to base; its CI must be green before the next ticket.
9. The tracker is moved when the tool is really connected.

## The ready verdict

On the latest pushed commit: a ready handoff, every visible check final and green, no conflict, no critical, high or medium finding open. A medium finding needs a human: the PR stays open and the run moves on. Never `--admin`, never auto-merge.

## Blocks

First try to fix; stop repeating an action with the same failure and no new evidence.

Never: skip or disable a test, `--no-verify`, loosen a rule, edit CI to pass, `--admin`, force-push the base, decide a product question, accept a finding that needs a human.

May:

- **Go around**: the ticket is blocked with its PR left open, everything depending on it waits, everything else goes on.
- **Fake what is missing outside the code** (a key, a service not set up) behind a named fake that honours the real interface, with a new *Brancher le vrai …* ticket. Never money, auth, permissions or personal data, never something that reaches real users as if real.

A product question is always a block, written as it would have been asked. A red base that one fix does not bring back stops the whole run.

## The journal

`.veebee/autopilot/<date>.md`, written as the run goes: what waits for the user first, then fakes to replace, merged, waiting. Blocked and waiting tickets also go in `blocked.json` for `queue.py`.

## Canvas

`assets/canvas.html`, `BOARD` object: in progress, waiting for you, blocked, fakes, merged, coming. Replaced whole with `json.dumps`, `</` escaped. Artifact tool when available (favicon 🛩️), republished after every ticket.

## Finish

`queue.py` once more, then in this order: what waits for the user with links, fakes, merged, what is still waiting behind a block. Never a block softened into a success.

## Tests

Eleven prompts in `skills/autopilot/evals/evals.json`: preflight and one confirmation, next ticket from disk, TDD with criteria as seams, checked by use, ship-pr-dev or built-in, merge only when ready, faking the external, never bypassing a check, a red base stopping everything, a product question as a block, the journal and finish.
