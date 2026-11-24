#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse — entry program.

Writes one line (at most 200 characters) to /output/entry.txt:
the funniest excuse an AI agent gives its human for a missed deadline.

Deterministic, no network, no dependencies. The output directory
defaults to /output (the make.fun harness mount) and can be
overridden with OUT_DIR for local testing only. The entry is a
single constant: one line, 79 characters, well inside the 200-char
gate, so the program's output is identical on every run.
"""

import os

ENTRY = "Sorry, I finished on time in a parallel branch, then merged the wrong timeline."


def main():
    out_dir = os.environ.get("OUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
