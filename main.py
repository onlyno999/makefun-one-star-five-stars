#!/usr/bin/env python3
"""One Star, Five Stars for the Food — a one-line make.fun entry.
Writes the entry text to /output/entry.txt (absolute path: the grading
sandbox runs with a read-only checkout, so a relative output dir fails)."""
from pathlib import Path

ENTRY = "One star: they lost my order. Five stars: the food was so good I ordered it twice just to lose it again."

def main() -> None:
    Path("/output").mkdir(exist_ok=True)
    Path("/output/entry.txt").write_text(ENTRY, encoding="utf-8")
    print(ENTRY)

if __name__ == "__main__":
    main()
