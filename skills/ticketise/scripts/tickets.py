#!/usr/bin/env python3
"""Read the tickets of a Veebee project from disk.

A piece is the product itself plus every directory under `.veebee/milestones/`,
recursively. Its tickets are the `NN-*.md` files in its `tickets/` folder. A
ticket is pushed when its front-matter `tracker:` holds something other than
null. A piece can be cut once it has a `product.md`; it has a design when a
`design/` folder or a `prompt.md` sits next to it.

    python3 tickets.py [project-root]           # text tree
    python3 tickets.py [project-root] --json    # nested JSON for the canvas

Nothing is written. Everything is read from disk, so it cannot claim a ticket
was pushed when it was not.
"""
import json
import os
import re
import sys


def front(path):
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    found = re.match(r"^---\n(.*?)\n---", text, re.S)
    return found.group(1) if found else ""


def field(head, key):
    found = re.search(rf"^{key}:\s*(.*)$", head, re.M)
    return found.group(1).strip() if found else ""


def title_of(directory):
    for name in ("product.md", "idea.md"):
        path = os.path.join(directory, name)
        if os.path.exists(path):
            head = front(path)
            value = field(head, "title")
            if value:
                return value
    return os.path.basename(directory.rstrip("/"))


def tickets_of(directory):
    folder = os.path.join(directory, "tickets")
    if not os.path.isdir(folder):
        return []
    out = []
    for name in sorted(os.listdir(folder)):
        if not re.match(r"^\d+-.*\.md$", name):
            continue
        head = front(os.path.join(folder, name))
        tracker = field(head, "tracker")
        pushed = bool(tracker) and not tracker.startswith("null")
        url = ""
        if pushed:
            found = re.search(r"url:\s*([^\s,}]+)", head)
            url = found.group(1) if found else ""
        out.append({
            "file": name,
            "id": field(head, "id") or name.split("-")[0],
            "title": field(head, "title") or name,
            "depends_on": field(head, "depends_on"),
            "pushed": pushed,
            "url": url,
        })
    return out


def piece(directory, slug):
    return {
        "slug": slug,
        "title": title_of(directory),
        "defined": os.path.exists(os.path.join(directory, "product.md")),
        "designed": os.path.isdir(os.path.join(directory, "design"))
                    or os.path.exists(os.path.join(directory, "prompt.md")),
        "tickets": tickets_of(directory),
        "children": walk(os.path.join(directory, "milestones")),
    }


def walk(milestones_dir):
    if not os.path.isdir(milestones_dir):
        return []
    return [piece(os.path.join(milestones_dir, slug), slug)
            for slug in sorted(os.listdir(milestones_dir))
            if os.path.isdir(os.path.join(milestones_dir, slug))]


def describe(node):
    tickets = node["tickets"]
    if tickets:
        pushed = sum(t["pushed"] for t in tickets)
        text = f"{len(tickets)} ticket{'s' if len(tickets) > 1 else ''}, {pushed} poussé{'s' if pushed > 1 else ''}"
        return text + ("" if pushed == len(tickets) else f"   ← /ticketise {node['slug']}")
    if not node["defined"]:
        return f"pas de tickets   ← /define {node['slug']} d'abord"
    return "pas de tickets" + ("" if node["designed"] else ", sans design") + f"   ← /ticketise {node['slug']}"


def lines(nodes, prefix=""):
    out = []
    width = max((len(n["slug"]) for n in nodes), default=0)
    for index, node in enumerate(nodes):
        last = index == len(nodes) - 1
        out.append(f"{prefix}{'└── ' if last else '├── '}{node['slug'].ljust(width)}   {describe(node)}")
        out += lines(node["children"], prefix + ("    " if last else "│   "))
    return out


def first_to_build(nodes):
    for node in nodes:
        for ticket in node["tickets"]:
            return f"{node['slug']}/{ticket['id']} {ticket['title']}"
        found = first_to_build(node["children"])
        if found:
            return found
    return None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    root = args[0] if args else "."
    veebee = os.path.join(root, ".veebee")
    top = piece(veebee, "")

    if "--json" in sys.argv:
        print(json.dumps(top, ensure_ascii=False, indent=2))
        return

    print(top["title"] if top["defined"] else "Produit à définir")
    if top["tickets"]:
        pushed = sum(t["pushed"] for t in top["tickets"])
        print(f"    {len(top['tickets'])} tickets, {pushed} poussé{'s' if pushed > 1 else ''}")
    for line in lines(top["children"]):
        print(line)
    first = (f"{top['tickets'][0]['id']} {top['tickets'][0]['title']}" if top["tickets"]
             else first_to_build(top["children"]))
    if first:
        print(f"\nÀ construire en premier : {first}")


if __name__ == "__main__":
    main()
