#!/usr/bin/env python3
"""Print a folder tree with Markdown headings nested underneath each file."""

import sys
import re
from pathlib import Path

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)')
FENCE_RE = re.compile(r'^(```|~~~)')

def extract_headings(md_path: Path):
    headings = []
    in_fence = False
    try:
        text = md_path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return headings
    for line in text.splitlines():
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            headings.append((level, title))
    return headings

def print_tree(path: Path, prefix: str = ""):
    entries = sorted(
        [p for p in path.iterdir() if not p.name.startswith(".")],
        key=lambda p: (p.is_file(), p.name.lower())
    )
    for i, entry in enumerate(entries):
        is_last = (i == len(entries) - 1)
        connector = "└─ " if is_last else "├─ "
        print(f"{prefix}{connector}{entry.name}")

        child_prefix = prefix + ("   " if is_last else "│  ")

        if entry.is_dir():
            print_tree(entry, child_prefix)
        elif entry.suffix.lower() == ".md":
            headings = extract_headings(entry)
            for level, title in headings:
                indent = child_prefix + "   " * level
                print(f"{indent}{'#' * level} {title}")

def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    if not root.is_dir():
        print(f"Not a directory: {root}", file=sys.stderr)
        sys.exit(1)
    print(root.resolve().name)
    print_tree(root)

if __name__ == "__main__":
    main()
