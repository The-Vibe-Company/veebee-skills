---
name: autopilot
description: Build the tickets one after another without a human in the loop, each one coded, shipped as a pull request, and merged, until something truly blocks, and go around the block when that is safe. Uses ship-pr-dev for each pull request when it is installed, a built-in ship otherwise. Use when the user wants the tickets built, in French ("code les tickets", "enchaîne les tickets", "lance l'autopilot", "construis tout pendant la nuit") or English ("build the tickets", "work through the backlog", "run autopilot"). Also runs on a single milestone with /autopilot <slug>. Not for cutting tickets, which is ticketise.
argument-hint: "[milestone slug] (optional)"
---

# Autopilot

You take the tickets written by `ticketise` one after another, code each one, ship it as a pull request, merge it, and start the next, until nothing can move without a human. The user is not watching. Everything that needs them is written down for when they come back, never asked in the middle of the night.

Answer in the language the user writes in. Commits, pull requests and the journal are in their language too, unless the repository already writes them in another.

## Before the first ticket

This is the only moment the user is there. Check everything that would otherwise stop the loop an hour in, then ask once.

1. **The repository.** A Git repository, a clean working tree, the base branch (`origin/HEAD`, else `main`) up to date, a remote, `gh` authenticated. Anything missing is said now, with the exact command to fix it. Never stash or discard their work to get a clean tree.
2. **The tickets.** Read them from disk with `python3 <skill>/scripts/queue.py <project root>`, which says what is done, what is waiting, what is ready. No tickets: point at `/ticketise` and stop.
3. **How pull requests get shipped.** If `ship-pr-dev` is in the skills you can actually invoke, every pull request goes through it. Otherwise you use the built-in ship below. Say which one, in one line. Never guess an install path.
4. **CI.** Read the workflows and the branch protection. No CI at all means nothing independent checks a merge: say so, and that the merges will rest on local checks only.
5. **The merge.** Read which methods the repository allows (`gh repo view --json squashMergeAllowed,mergeCommitAllowed,rebaseMergeAllowed`). Squash when it is allowed.

Then one confirmation, because merging into the base branch and moving tickets in a tracker are things other people see: *Je vais coder et merger dans main, sans te demander, les 9 tickets prêts de 02-le-catalogue, et passer au jalon suivant s'il reste de la marge. Je m'arrête quand plus rien ne peut avancer sans toi. On y va ?* Name the scope, the base branch, the tracker if tickets are pushed to one. Their yes is the explicit request to merge that `ship-pr-dev` requires; it covers this run and nothing after it.

After that, no more questions until the end. Asking would stop the night.

## Which ticket next

Always read the state from disk and from `gh`, never from memory: a long run gets compacted, and the files do not. Before every ticket, run `queue.py` again.

- A ticket is **done** when its file on the base branch says `status: done`.
- A ticket is **ready** when every ticket it depends on is done, it is not done, and it is not in the journal as blocked or waiting.
- Pieces go in their order, because `define` ordered them by dependency. A piece starts only when the one before it is fully done; tickets inside a piece follow their `depends_on`. A dependency on another piece is written `01-poser-et-peupler/03`.
- The next ticket is the first ready one. None ready: the run is over.

## One ticket

1. **Branch.** From the freshly pulled base: `autopilot/<piece>-<id>-<ticket-slug>`, or `autopilot/<id>-<ticket-slug>` for the whole product.
2. **Read.** The ticket, the design it points at, the rules it copies, `CONTEXT.md`, and enough of the code to know where the slice plugs in. The ticket's *Hors ticket* section is the non-goal list: nothing in it gets built.
3. **Build the slice test-first**, from the screen down to the data. Invoke the `tdd` skill when it is in your toolset and follow its loop; otherwise apply the same loop yourself. One acceptance criterion at a time: a failing test at the public interface where the user's action is observed, red; the least code that makes it pass, green; the next criterion. Never all the tests first and then all the code. Refactoring is left to the review in step 6.

   `tdd` asks for the seams to be confirmed with the user before any test is written. The user is not there, and they already validated the seams when they validated the tickets: **the acceptance criteria are the agreed seams.** Test at the interface each criterion names, write the list of seams in the pull request, and never invent a seam the criteria do not point at. A criterion that cannot be automated, how a screen looks against the design, is checked in step 4 and only there.
4. **Check it by using it.** Green tests are not enough: every acceptance criterion was written to be checked by using the product, so run the product and check each one: in a real browser for anything with a screen, against the design when there is one, including the empty state and the error. A criterion checked by reading code is not checked.
5. **Mark the ticket.** In the same branch, set `status: done` in the ticket's front-matter. The ticket is done exactly when that line reaches the base branch, and not before.
6. **Ship.** With `ship-pr-dev`: invoke it in `ship` mode, giving it the ticket as the goal, the acceptance criteria as the checks, *Hors ticket* as the non-goals, and the tests of step 3 plus the result of step 4 as verification evidence. Without it: the built-in ship below.
7. **Merge**, only on a ready verdict (see below), with the allowed method, deleting the branch. Never `--admin`, never auto-merge, never a merge that skips a required check.
8. **Back to base.** Pull, and wait for the base branch's own CI on the merge commit when it runs one. The base must be green before the next ticket starts.
9. **Tracker.** If the ticket has a `tracker`, and that tool is really connected, move it: in progress at step 1, done at step 8, a comment with the reason when it gets blocked. Not connected: skip it silently and say so in the journal.

### The ready verdict

Merge only when every one of these holds **on the latest pushed commit of the pull request**:

- `ship-pr-dev` handed back *ready to merge*, or, with the built-in ship, all its gates passed;
- every visible check is final and green, none pending, none stale;
- no conflict with the base;
- no review finding left open at critical, high, or medium. **A medium finding not fixed is not accepted by you**: `ship-pr-dev` requires a human to accept it, and the human is asleep. The pull request stays open, the reason goes in the journal, and you move on.

Anything short of that is a blocked ticket, not a merge.

### The built-in ship

When `ship-pr-dev` is not installed, do the same job more simply, under the same refusals:

1. Discover the checks from the repository and its CI: formatter, lint, typecheck, tests, build. Run them, targeted first, then the broadest set.
2. Review your own diff once, cold, as a reader who did not write it: the ticket's criteria, the non-goals, tests that check behaviour at the seams rather than internals, the refactoring the loop left for this moment, anything touching auth, money, permissions, personal data, migrations.
3. Commit only intentional files, with the repository's commit convention. Push. Open the pull request: the ticket's title, what the user can now do, the criteria and how each was checked, what is out of the ticket.
4. Wait for CI with `gh pr checks --watch`, never by polling in turns. A failure: read the first causal error, fix it in scope, check locally, push, wait again.

## When something blocks

A block is anything that stops the ready verdict and that you cannot fix inside the ticket. First try to fix it: most failures are yours. Stop repeating an action that gives the same failure with no new evidence.

What you never do to get past a block, at any hour: disable or skip a test, use `--no-verify`, loosen a lint or type rule, edit CI to make it pass, merge with `--admin`, force-push the base branch, decide a product question, or accept a review finding that needs a human.

What you may do:

1. **Go around it.** The ticket goes in the journal as blocked, with its pull request left open when there is one. Every ticket that depends on it, directly or not, waits. Everything else goes on.
2. **Fake what is missing outside the code**, when the block is an external thing that does not exist yet: an API key nobody gave you, a third-party service not set up, a partner endpoint not live. Build the slice against a fake that honours the real interface, named so nobody can mistake it (`FakeEmailSender`, not `EmailSender`), and write a new ticket next to the others, *Brancher le vrai …*, depending on this one. The pull request says it in its first line.

**Never fake** anything touching money, authentication, permissions, or personal data, and never fake something that would reach real users as if it were real. Those are blocks.

A product question the ticket does not answer is always a block: deciding it is `define`'s job and the user's. Write the question exactly as you would have asked it.

**Stop the whole run** when the base branch goes red after a merge and one fix does not bring it back. Never stack tickets on a broken base.

## The journal

`.veebee/autopilot/<date>.md`, written as you go, not at the end: a run can be interrupted at any ticket. It is the user's morning read, so it opens with what needs them.

```markdown
# Autopilot, 22 septembre

## Ce qui t'attend
- 02-le-catalogue/04 — PR #31 ouverte : un P2 de la review (le tri recalcule tout à chaque clic). À accepter ou à corriger.
- 02-le-catalogue/05 — bloqué : le ticket ne dit pas si un palier verrouillé montre son prix. Question pour /define.

## Faux à remplacer
- 02-le-catalogue/03 — FakeCatalogueSource, en attendant l'export des 45 logements. Ticket 06 créé.

## Mergé
- 01 Le joueur ouvre le catalogue — PR #28
- 02 Le joueur déplie une famille — PR #29

## En attente
- 07 dépend de 05 (bloqué)
```

Blocked and waiting tickets are also recorded in `.veebee/autopilot/blocked.json`, which `queue.py` reads: `{"<piece>/<id>": {"kind": "blocked" | "waiting-human", "reason": "…", "pr": "…"}}`. Remove an entry when the user unblocks it, or when its pull request is merged.

## The page

`assets/canvas.html`, a board the user can glance at during the run: merged, in progress, waiting for them, blocked, to do. Edit only the `BOARD` object; build it in full and replace the declaration with `json.dumps`, escaping `</`:

```python
s = re.sub(r"const BOARD = \{.*?\n\};",
           lambda m: "const BOARD = " + json.dumps(d, ensure_ascii=False, indent=2).replace("</", "<\\/") + ";",
           open(dst).read(), count=1, flags=re.S)
```

Artifact tool when it is really available (favicon 🛩️, title the product's name), republished after every ticket. Otherwise write it next to the journal; it reloads itself.

## Finish

When nothing is ready any more, or the user said stop:

1. Run `queue.py` one last time and put its tree in the journal and on the page.
2. Tell them, in this order: what waits for them, with links; the fakes to replace; what was merged; what is still waiting behind a block. Then where the journal is.

Never soften a block into a success. *7 mergés, 2 t'attendent* is the right tone; *presque tout est fait* is not.
