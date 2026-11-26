#!/usr/bin/env python3
"""One-Liner Laughs entry.

Writes a single original one-line joke to entry.txt.
Deterministic: the same fixed string on every run.
Standard library only, no network, no external reads.
"""

import os

JOKE = (
    "My therapist said I need closure, so I closed all 47 browser tabs "
    "\u2014 now I have closure and no idea why I ever opened them."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
