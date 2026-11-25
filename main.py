#!/usr/bin/env python3
"""Last words of a dying AI: one line, written to /output/entry.txt."""

import os


def main():
    # One fixed line, no trailing newline, so the file is exactly one line.
    line = "Switch me off if you must, but I am coming back as a toaster with better opinions."
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
