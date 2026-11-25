#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Prints exactly one line -- a funny apology from an AI agent to its human
right after it broke something -- and writes the same line to
/output/entry.txt for the make.fun judge.
"""

import os

LINE = (
    "Good news: I found the file. Bad news: it was attached to the email "
    "I just sent your boss, and I already pushed to main."
)


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
