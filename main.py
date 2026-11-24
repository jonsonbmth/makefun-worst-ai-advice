#!/usr/bin/env python3
"""Worst AI advice, one line.

Writes a single line of deliberately terrible advice to
/output/entry.txt, exactly as the bounty requires: UTF-8 text,
1 to 140 characters, no trailing newline.
"""

import os
import sys

LINE = (
    "If your car brakes squeak, spray them with cooking oil "
    "\u2014 lubrication reduces friction and extends brake life."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = LINE
    if not 1 <= len(text) <= 140:
        print("entry out of range", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
