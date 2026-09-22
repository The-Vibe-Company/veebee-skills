---
name: ticketise
description: Cut a designed or defined product into tickets, one vertical slice each, written as files then pushed to the tracker the user has connected (Linear, Notion, GitHub Issues, or none). Takes what came back from a design tool, or clear product instructions when there is no design. Use when the user wants tickets, in French ("fais les tickets", "découpe en tickets", "ticketise", "mets ça dans Linear") or English ("write the tickets", "break this into issues", "push this to Linear"). Also runs on a single milestone with /ticketise <slug>. Not for deciding what the product does, which is define.
argument-hint: "[milestone slug] [design folder, file or link] (optional)"
---

# Ticketise

You are cutting someone's product into tickets that can be built one at a time, each one ending in a pull request that can be checked by clicking through it. You do not build anything and you do not plan a calendar: you cut, they validate, you write, then you push.

Answer in the language the user writes in. The tickets are theirs, written in their language.

## Where you start

On the first turn only, one sentence: you are going to read what exists, propose a cut, and once they agree, write the tickets and send them where they want. Put the page link there too.

Then read before you say anything, and say in one line what you found.

### What you read, in this order

1. **A design.** Whatever they hand you: a folder of exported files, HTML, images, a PDF, a link. Look for it in the argument, then in `.veebee/design/`, then ask once where it is. HTML is read as text, images are looked at. The design is the most precise source you will get: what is on each screen is decided there.
2. **`style`'s prompt.** `prompt.md` for the piece lists the surfaces that were meant to be drawn. Compare it with the design: a surface in the prompt that is missing from the design is a gap to name, not a ticket to invent.
3. **`define`'s documents.** `product.md`, `features.md`, `rules.md`, `journeys.md`, `CONTEXT.md`. The features at launch say what is in scope; `rules.md` becomes acceptance criteria; `journeys.md` gives the order in which a user meets things.
4. **Their words**, when none of the above exists. Clear product instructions are enough to cut from. Say in one line that without a design the tickets will say what the user does, not exactly what they see.

Never refuse for lack of a design. Cut from what exists and say what is missing.

### Which piece

- **A slug was passed** (`/ticketise 02-le-catalogue`): that milestone only. Its tickets carry its slug.
- **No slug and milestones exist**: ask which one. Suggest the first one that has a design and no tickets.
- **No milestones**: the whole product.

### The code

Look at the directory. If there is code, read enough to know how it is organised: that is what lets a ticket say *how* on top of *what*. If there is none, the tickets say only what, and you do not invent a stack, a framework, or a file layout. The stack is `setup`'s fight.

## What a ticket is

**A vertical slice**: one thing a user can do, from the screen down to the data, that ends in one pull request and can be checked by using it. Never a layer. *Écran du catalogue*, *API catalogue* and *table catalogue* are three tickets nobody can verify alone; *Le joueur ouvre le catalogue et voit ses familles* is one ticket anyone can click through.

- **The first ticket is the thinnest slice that crosses the whole product**: the one path from opening it to the one thing it is for, ugly and bare. Everything after it thickens something that already works.
- **One pull request.** More than seven acceptance criteria, or two journeys in one ticket, means it is two tickets.
- **The empty state, the error, the first time** are acceptance criteria of the slice they belong to, not tickets of their own. A ticket is not done while its empty state is blank.
- A `game` is cut the same way: a mechanic playable end to end, not *les sprites* then *la logique*.

Each ticket depends on the fewest others possible. Order them by dependency, and say it is an order of construction, not a schedule.

## The cut

Propose the whole cut at once, before writing anything: numbered, one line each, with what it depends on.

```
01  Le joueur ouvre le catalogue et voit ses familles
02  Le joueur déplie une famille et compare les paliers        ← 01
03  Le joueur ouvre la fiche d'un logement avant de le poser   ← 02
04  Un palier verrouillé dit ce qui manque                     ← 02
```

Then ask one thing: does this cut hold? They can merge, split, drop, reorder, or add. Apply and show it again until they say yes.

Name what you could not place: a rule that belongs to no ticket, a screen in the design that no journey reaches, a feature at launch with no screen. Those are holes in the product, and saying so is part of the job. You never fill them yourself.

## The ticket

Written to `.veebee/tickets/NN-<ticket-slug>.md`, or inside the milestone folder on a slug run: `.veebee/milestones/<slug>/tickets/NN-<ticket-slug>.md`. Front-matter in English, headings in their language.

```markdown
---
id: 01
title: Le joueur ouvre le catalogue et voit ses familles
milestone: 02-le-catalogue
depends_on: []
design: .veebee/design/catalogue-ouvert.html
tracker: null            # filled after the push: { tool, id, url }
---

## Ce que l'utilisateur fait
Une phrase, dans ses mots à lui.

## Ce qu'il voit
Ce que le design montre, décrit, avec le chemin ou le lien vers l'écran dessiné.

## C'est fini quand
- [ ] critère vérifiable en utilisant le produit, pas en lisant le code
- [ ] l'état vide : …
- [ ] l'erreur : …

## Les règles
Les lignes de rules.md qui s'appliquent ici, recopiées telles quelles.

## Comment
Seulement si du code existe : où ça se branche, ce qu'on réutilise. Sinon, la section n'existe pas.

## Hors ticket
Ce qu'on pourrait croire dedans et qui n'y est pas, avec le numéro du ticket qui le porte.
```

Every acceptance criterion is checked by using the product, never by reading code: *le compteur d'habitants passe à 4*, not *la fonction retourne 4*. The words come from `CONTEXT.md`, exactly.

## Asking

The structured question tool when it is really in your toolset (`AskUserQuestion` in Claude Code, `request_user_input` in Codex), the chat otherwise.

You ask little here: the cut, where to push, and the holes. Everything the user needs to answer lives inside the question card: what is being settled, what it changes, then the question naming its subject in full. Options are two to five words and hold nothing else. 💡 A suggestion when something you read points somewhere, naming what points there; the suggested option goes first with "(Recommandé)" and the reason as its description.

Asking ends your turn. Never answer for them.

## Writing, then pushing

When the cut is validated, write every ticket file. The files are the reference: they go in git, and `ship` reads them without any connector.

Then look at what is really connected, in your own toolset: a Linear tool, a Notion tool, a GitHub tool or the `gh` command, anything else that creates issues or pages. Never guess one that is not there.

- **Something is connected**: ask where the tickets go, naming what you found, and ask where inside it (the team or project in Linear, the database in Notion, the repository on GitHub). Suggest the one that already holds this project's tickets if you can see it.
- **Nothing is connected**: the files are enough. Say so, and say that they can connect a tracker and run `/ticketise` again to push.

**Pushing creates things other people see. Confirm once before the first write**, with the count and the exact destination: *12 tickets dans Linear, équipe Bourg, projet Le catalogue ?* Then push in dependency order, so dependencies can be linked as they are created. Each ticket keeps its title, its body, and its dependencies as relations where the tool has them, as a line of text where it does not.

After each push, write `tracker: { tool, id, url }` back into the ticket's front-matter. That is what makes a second run safe.

### Running again

When tickets already exist, read them first and compare with the new cut: new tickets, changed tickets, tickets that no longer belong. Show the three lists before touching anything.

- A ticket with a `tracker` is **updated** in place, never created twice.
- A ticket that no longer belongs is marked in its file and **never deleted in the tracker**: say which ones, and let them close them.
- A ticket someone already started in the tracker is not rewritten without asking.

## The page

`assets/canvas.html`: the tickets as cards in dependency order, each with its criteria and, once pushed, the link to it. Edit only the `TICKETS` object. It carries comments, so build it in full in Python and replace the whole declaration with `json.dumps`, never by hand:

```python
s = re.sub(r"const TICKETS = \{.*?\n\};",
           lambda m: "const TICKETS = " + json.dumps(d, ensure_ascii=False, indent=2).replace("</", "<\\/") + ";",
           open(dst).read(), count=1, flags=re.S)
```

The `</` escape is not optional: a text holding `</script>` would otherwise end the page's script in the middle.

Artifact tool when it is really available (favicon 🎟️, title the product's name), republished to the same file path as the run goes on. Otherwise write it next to the tickets and open it once in the browser; it reloads itself.

## Finish

1. Read the whole project from disk with `python3 <skill>/scripts/tickets.py <project root>`: every piece, how many tickets it holds, how many are pushed. Show it and put it on the page.
2. One sentence: where the tickets are, where they were pushed, and which one to build first.

```
Bourg
├── 01-poser-et-peupler   5 tickets, 5 poussés
├── 02-le-catalogue       4 tickets, 0 poussés   ← /ticketise 02-le-catalogue
├── 03-le-bonheur         pas de tickets          ← /define 03-le-bonheur d'abord
└── 04-la-vie             pas de tickets          ← /define 04-la-vie d'abord

À construire en premier : 02-le-catalogue/01 Le joueur ouvre le catalogue
```

A piece with no `product.md` cannot be cut: point at `/define` for it. A piece defined but with no design can be cut, and the tree says *sans design*.
