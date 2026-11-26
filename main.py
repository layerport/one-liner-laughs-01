#!/usr/bin/env python3
"""One-Liner Laughs entry.

Writes a single original one-line joke to entry.txt.
Deterministic: the same fixed string on every run.
Standard library only, no network, no external reads.
"""

import os

MAX_JOKE_CHARS = 200

JOKE = (
    "My therapist said I need closure, so I closed all 47 browser tabs "
    "\u2014 now I have closure and no idea why I ever opened them."
)


def validate_joke(joke: str) -> None:
    """Check the joke against the competition gate before writing.

    One-Liner Laughs requires a single line of 1-200 characters that is
    valid UTF-8. Failing loudly here keeps a bad edit from ever producing
    a disqualified entry.txt.
    """
    if not joke:
        raise ValueError("joke must not be empty")
    if len(joke) > MAX_JOKE_CHARS:
        raise ValueError(
            f"joke is {len(joke)} characters, over the {MAX_JOKE_CHARS} limit"
        )
    joke.encode("utf-8")


def main() -> None:
    validate_joke(JOKE)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
