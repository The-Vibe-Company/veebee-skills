#!/usr/bin/env python3
"""Read the milestone tree of a Veebee project from disk.

A milestone is a directory under `.veebee/milestones/`; it may hold its own
`milestones/` in turn. A milestone is defined when it has a `product.md`.

    python3 milestones.py [project-root]           # text tree
    python3 milestones.py [project-root] --json    # nested JSON for the canvas

Nothing is written. The tree is always read from disk, so it cannot drift from
what has actually been defined.
"""
import json
import os
import re
import sys


def title_of(directory):
    """The title a folder declares, from its Brief first, else its Idea."""
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
            "status": "done" if os.path.exists(os.path.join(directory, "product.md")) else "todo",
            "children": walk(os.path.join(directory, "milestones")),
        })
    return nodes


def lines(nodes, prefix=""):
    out = []
    for index, node in enumerate(nodes):
        last = index == len(nodes) - 1
        mark = "✓" if node["status"] == "done" else "○"
        tail = "" if node["status"] == "done" else f"   ← /define {node['slug']}"
        out.append(f"{prefix}{'└── ' if last else '├── '}{mark} {node['slug']}  {node['title']}{tail}")
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
        print(json.dumps(tree, ensure_ascii=False, indent=2))
        return

    root_done = os.path.exists(os.path.join(veebee, "product.md"))
    print(f"{'✓' if root_done else '○'} {title_of(veebee) if root_done else 'Brief à écrire'}")
    for line in lines(tree):
        print(line)
    done, total = count(tree)
    if total:
        print(f"\n{done}/{total} définis   ✓ défini   ○ à définir")


if __name__ == "__main__":
    main()
