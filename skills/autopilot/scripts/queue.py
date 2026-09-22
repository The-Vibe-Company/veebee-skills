#!/usr/bin/env python3
"""Say which ticket autopilot builds next, read from disk.

Tickets are the `NN-*.md` files in `.veebee/tickets/` and in every
`.veebee/milestones/<slug>/tickets/`. A ticket is done when its front-matter
says `status: done`. Blocked and waiting-for-a-human tickets are listed in
`.veebee/autopilot/blocked.json`. A ticket is ready when every ticket it
depends on is done and it is neither done nor listed there.

Pieces go in order: a piece starts only when the one before it is fully done.
A dependency on another piece is written `<piece>/<id>`.

    python3 queue.py [project-root] [--piece <slug>]         # text board
    python3 queue.py [project-root] [--piece <slug>] --json  # for the canvas

Nothing is written.
"""
import json
import os
import re
import sys


def front(path):
    with open(path, encoding="utf-8") as handle:
        found = re.match(r"^---\n(.*?)\n---", handle.read(), re.S)
    return found.group(1) if found else ""


def field(head, key):
    found = re.search(rf"^{key}:\s*(.*?)\s*(#.*)?$", head, re.M)
    return found.group(1).strip() if found else ""


def ids(raw):
    return [x.strip().strip("'\"") for x in raw.strip("[]").split(",") if x.strip()]


def pieces(veebee):
    """The product root, then every milestone depth-first, in slug order."""
    out = [("", veebee)]

    def walk(directory, prefix):
        folder = os.path.join(directory, "milestones")
        if not os.path.isdir(folder):
            return
        for slug in sorted(os.listdir(folder)):
            path = os.path.join(folder, slug)
            if os.path.isdir(path):
                name = f"{prefix}{slug}"
                out.append((name, path))
                walk(path, name + "/")

    walk(veebee, "")
    return out


def tickets_of(piece, directory):
    folder = os.path.join(directory, "tickets")
    if not os.path.isdir(folder):
        return []
    out = []
    for name in sorted(os.listdir(folder)):
        if not re.match(r"^\d+-.*\.md$", name):
            continue
        head = front(os.path.join(folder, name))
        tid = field(head, "id") or name.split("-")[0]
        deps = [d if "/" in d else (f"{piece}/{d}" if piece else d) for d in ids(field(head, "depends_on"))]
        out.append({
            "key": f"{piece}/{tid}" if piece else tid,
            "piece": piece,
            "id": tid,
            "title": field(head, "title") or name,
            "file": os.path.join(folder, name),
            "depends_on": deps,
            "done": field(head, "status") == "done",
        })
    return out


def board(root, only=None):
    veebee = os.path.join(root, ".veebee")
    try:
        with open(os.path.join(veebee, "autopilot", "blocked.json"), encoding="utf-8") as handle:
            blocked = json.load(handle)
    except (OSError, ValueError):
        blocked = {}

    groups = [(p, tickets_of(p, d)) for p, d in pieces(veebee)]
    groups = [(p, t) for p, t in groups if t]
    # Dependencies resolve against every ticket, even on a single-piece run.
    everything = {t["key"]: t for _, ts in groups for t in ts}
    if only is not None:
        groups = [(p, t) for p, t in groups if p == only]

    def state(ticket, seen=()):
        if ticket["done"]:
            return "done"
        if ticket["key"] in blocked:
            return blocked[ticket["key"]].get("kind", "blocked")
        for dep in ticket["depends_on"]:
            other = everything.get(dep)
            if other is None or dep in seen:
                return "waiting"
            if state(other, seen + (ticket["key"],)) != "done":
                return "waiting"
        return "ready"

    # On a whole-project run a piece starts only when the one before it is done;
    # a single-piece run was chosen by the user and follows its dependencies only.
    previous_done = True
    result = []
    for piece, ts in groups:
        rows = []
        for t in ts:
            s = state(t) if previous_done else ("done" if t["done"] else "waiting")
            row = {k: t[k] for k in ("key", "id", "title", "depends_on")}
            row["state"] = s
            if t["key"] in blocked:
                row["reason"] = blocked[t["key"]].get("reason", "")
                row["pr"] = blocked[t["key"]].get("pr", "")
            rows.append(row)
        result.append({"piece": piece, "tickets": rows})
        if only is None:
            previous_done = previous_done and all(r["state"] == "done" for r in rows)

    ready = [r for g in result for r in g["tickets"] if r["state"] == "ready"]
    return {"pieces": result, "next": ready[0] if ready else None}


MARK = {"done": "✓", "ready": "→", "waiting": "·", "blocked": "✗", "waiting-human": "?"}
WORD = {"done": "mergé", "ready": "prêt", "waiting": "en attente",
        "blocked": "bloqué", "waiting-human": "t'attend"}


def main():
    argv = sys.argv[1:]
    only = None
    if "--piece" in argv:
        index = argv.index("--piece")
        only = argv[index + 1] if index + 1 < len(argv) else None
        del argv[index:index + 2]
    args = [a for a in argv if not a.startswith("-")]
    data = board(args[0] if args else ".", only)

    if "--json" in sys.argv:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return

    if not data["pieces"]:
        print("Aucun ticket. Lance /ticketise d'abord.")
        return
    counts = {}
    for group in data["pieces"]:
        print(group["piece"] or "Produit")
        for t in group["tickets"]:
            counts[t["state"]] = counts.get(t["state"], 0) + 1
            tail = f"   — {t['reason']}" if t.get("reason") else ""
            print(f"  {MARK.get(t['state'], '·')} {t['id']}  {t['title']}  ({WORD.get(t['state'], t['state'])}){tail}")
    print("\n" + "   ".join(f"{n} {WORD.get(s, s)}" for s, n in counts.items()))
    nxt = data["next"]
    print(f"Prochain : {nxt['key']} {nxt['title']}" if nxt else "Rien de prêt : fin de la course.")


if __name__ == "__main__":
    main()
