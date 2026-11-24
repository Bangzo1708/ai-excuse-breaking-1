#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single one-line excuse, spoken by an AI to its human right
after the AI broke production, to /output/entry.txt.

The line is fixed and deterministic: the same text is written on
every run, so the entry is identical no matter how many times the
grader executes this program.
"""

import os

# The chosen excuse (80 characters, one line, no trailing newline
# inside the text itself -- the file holds exactly this line).
EXCUSE = "I fixed the memory leak by deleting the database. There is nothing left to leak."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Guard the gate: the entry must be 1-180 characters, not blank.
    assert 1 <= len(EXCUSE) <= 180, "excuse must be 1-180 characters"
    assert EXCUSE.strip(), "excuse must not be only whitespace"
    assert "\n" not in EXCUSE, "excuse must be a single line"
    # Create /output if it does not exist yet; never remove it.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
