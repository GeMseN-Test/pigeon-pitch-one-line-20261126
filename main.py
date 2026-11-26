#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry.

Writes one line (max 200 characters, English): the elevator pitch a city
pigeon gives to investors for its startup. Output: /output/entry.txt
"""

import os

LINE = (
    "I've delivered 214 crumbs to the same bench for nine years \u2014 "
    "zero churn, zero burn, and my only investor still thinks I'm a statue."
)


def main() -> None:
    # No trailing newline: the sealed scorer counts every character (1-200).
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
