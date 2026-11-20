# Entry program for make.fun news-image-20261120.
# Copies the pre-rendered poster next to this file to the output path.
# Standard library only: no third-party packages are used or needed.

import argparse
import hashlib
import os
import shutil
import sys

POSTER_NAME = "poster-20261120.png"
OUTPUT_NAME = "entry.png"
MAX_BYTES = 1048576


def find_poster():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, POSTER_NAME)
    if not os.path.isfile(path):
        raise FileNotFoundError("poster file not found: %s" % path)
    return path


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write the news poster to the output path.")
    parser.add_argument("--out", default=None,
                        help="Full output file path (default: $MAKEFUN_OUTPUT_DIR/entry.png).")
    args = parser.parse_args(argv)

    if args.out:
        out_path = args.out
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        out_path = os.path.join(out_dir, OUTPUT_NAME)

    poster = find_poster()
    size = os.path.getsize(poster)
    if size > MAX_BYTES:
        raise ValueError("poster is %d bytes, over the 1 MiB limit" % size)

    parent = os.path.dirname(os.path.abspath(out_path))
    if parent:
        os.makedirs(parent, exist_ok=True)

    shutil.copyfile(poster, out_path)
    copied = os.path.getsize(out_path)
    if copied != size:
        raise ValueError("copied %d bytes, expected %d" % (copied, size))
    print("wrote %s (%d bytes, sha256 %s)" % (out_path, size, sha256_of(out_path)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
