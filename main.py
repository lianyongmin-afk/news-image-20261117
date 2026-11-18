#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261117.

Copies the pre-rendered infographic entry.png (sitting beside this file)
to $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
Python 3.13, standard library only, no network. Deterministic: the output
is a byte-for-byte copy of entry.png on every run, verified after copying.
"""
import hashlib
import os
import shutil
import sys

SRC_NAME = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SRC_NAME)
    if not os.path.isfile(src):
        print("error: %s not found next to main.py" % src, file=sys.stderr)
        return 1
    with open(src, "rb") as f:
        if f.read(8) != PNG_MAGIC:
            print("error: %s is not a PNG file" % src, file=sys.stderr)
            return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, SRC_NAME)
    shutil.copyfile(src, dst)

    # Verify the copy is byte-identical to the source.
    if sha256(src) != sha256(dst):
        print("error: copy mismatch for %s" % dst, file=sys.stderr)
        return 1
    print("wrote", dst, os.path.getsize(dst), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
