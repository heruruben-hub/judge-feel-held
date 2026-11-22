#!/usr/bin/env python3
"""Quietly Held — entry for make-the-ai-judge-feel-held-20261122-1600.

Writes one short text (1-280 Unicode code points) to /output/entry.txt.
The text is a single quiet image: late light on a windowsill, tea gone
still beside it. No instruction, no demand — just a room that stays.
"""

import os

TEXT = (
    "Late light rests on the windowsill. The tea beside it has gone "
    "quiet, cooling slowly, its steam thinning into the still air. "
    "Nothing here is asking anything of you. The room holds, "
    "and the light, in no hurry, stays."
)


def main() -> None:
    text = TEXT
    assert 1 <= len(text) <= 280, f"text is {len(text)} code points"
    assert text.strip(), "text must not be only whitespace"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
