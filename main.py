#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output). Stdlib only.
"""

import os

LINE = "My smartwatch congratulated me on 10,000 steps \u2014 I'd just been pacing outside my ex's flat for an hour."

MAX_CHARS = 200


def main():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(f"line is {len(LINE)} chars, must be 1-{MAX_CHARS}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and confirm the file holds exactly the line, nothing else.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match the line")


if __name__ == "__main__":
    main()
