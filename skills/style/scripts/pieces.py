#!/usr/bin/env python3
"""Read the pieces of a Veebee project from disk and say which ones are designed.

A piece is the product itself plus every directory under `.veebee/milestones/`,
recursively. A piece is *defined* when it has a `product.md` (that is `define`'s
job) and *designed* when it also has a `prompt.md` (that is `style`'s).

    python3 pieces.py [project-root]           # text tree
    python3 pieces.py [project-root] --json    # nested JSON for the canvas

Nothing is written. The tree is always read from disk, so it cannot claim a
piece is designed when it is not.
"""
import json
import os
import re
import sys


def title_of(directory):
    """The title a folder declares, from its product.md first, else its idea.md."""
    for name in ("product.md", "idea.md"):
        path = os.path.join(directory, name)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as handle:
            head = handle.read(2000)
        for pattern in (r"^title:\s*(.+)$", r"^#\s+(.+)$"):
            found = re.search(pattern, head, re.M)
            if found:
                return found.group(1).strip()
    return os.path.basename(directory.rstrip("/"))


def status_of(directory):
    defined = os.path.exists(os.path.join(directory, "product.md"))
    designed = os.path.exists(os.path.join(directory, "prompt.md"))
    if designed:
        return "done"
    return "todo" if defined else "undefined"


def walk(milestones_dir):
    if not os.path.isdir(milestones_dir):
        return []
    nodes = []
    for slug in sorted(os.listdir(milestones_dir)):
        directory = os.path.join(milestones_dir, slug)
        if not os.path.isdir(directory):
            continue
        nodes.append({
            "slug": slug,
            "title": title_of(directory),
            "status": status_of(directory),
            "children": walk(os.path.join(directory, "milestones")),
        })
    return nodes


MARK = {"done": "✓", "todo": "○", "undefined": "◌"}


def lines(nodes, prefix=""):
    out = []
    for index, node in enumerate(nodes):
        last = index == len(nodes) - 1
        if node["status"] == "done":
            tail = ""
        elif node["status"] == "todo":
            tail = f"   ← /style {node['slug']}"
        else:
            tail = f"   ← /define {node['slug']} d'abord"
        out.append(f"{prefix}{'└── ' if last else '├── '}"
                   f"{MARK[node['status']]} {node['slug']}  {node['title']}{tail}")
        out += lines(node["children"], prefix + ("    " if last else "│   "))
    return out


def count(nodes):
    done = total = 0
    for node in nodes:
        total += 1
        done += node["status"] == "done"
        child_done, child_total = count(node["children"])
        done += child_done
        total += child_total
    return done, total


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    root = args[0] if args else "."
    veebee = os.path.join(root, ".veebee")
    tree = walk(os.path.join(veebee, "milestones"))

    if "--json" in sys.argv:
        print(json.dumps({
            "charter": os.path.exists(os.path.join(veebee, "style.md")),
            "milestones": tree,
        }, ensure_ascii=False, indent=2))
        return

    charter = os.path.exists(os.path.join(veebee, "style.md"))
    root_status = status_of(veebee)
    print(f"{MARK[root_status]} {title_of(veebee)}"
          f"   {'charte écrite' if charter else 'charte à écrire'}")
    for line in lines(tree):
        print(line)
    done, total = count(tree)
    if total:
        print(f"\n{done}/{total} designés   ✓ designé   ○ à designer   ◌ à définir avant")


if __name__ == "__main__":
    main()
