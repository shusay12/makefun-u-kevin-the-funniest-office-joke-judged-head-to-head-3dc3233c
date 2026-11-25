#!/usr/bin/env python3
"""make.fun entry: one office joke, judged head to head.

The grader runs this program and reads /output/entry.txt. The entry is a
single line about office life, kept in JOKE below; the rest of this file
exists to get that line onto disk intact, inside the 200 character cap,
with no trailing newline and nothing else in the file. The joke is built
as a setup with a turn and the punchline last: a raise answered with a
pizza party, then the dignity expensed as a team lunch.

The program takes no input, reads no files, opens no network connection
and writes the same bytes on every run.
"""

import os
import sys

JOKE = (
    "I asked for a raise and got a pizza party, so I expensed my dignity "
    "as a team lunch \u2014 HR approved it."
)

CHAR_LIMIT = 200


def entry_line() -> str:
    """Collapse the joke to one single-spaced line."""
    return " ".join(JOKE.split())


def problems(line: str) -> list[str]:
    """List every way the line would fail the gate, if any."""
    found = []
    if not line.strip():
        found.append("empty")
    if len(line) > CHAR_LIMIT:
        found.append(f"{len(line)} characters, over the {CHAR_LIMIT} limit")
    if line != line.strip() or "  " in line:
        found.append("ragged whitespace")
    if "\n" in line or "\r" in line:
        found.append("spans more than one line")
    return found


def main() -> int:
    line = entry_line()
    bad = problems(line)
    if bad:
        print("entry rejected: " + "; ".join(bad), file=sys.stderr)
        return 1
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as out:
        out.write(line)
    print(f"entry written: {len(line)} characters in {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
