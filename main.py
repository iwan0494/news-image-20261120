# Entry program for make.fun news-image-20261120 (round 2).
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


def copy_poster_to_file(dest_path):
    src = find_poster()
    size = os.path.getsize(src)
    if size > MAX_BYTES:
        raise ValueError("poster is %d bytes, over the 1 MiB limit" % size)
    parent = os.path.dirname(os.path.abspath(dest_path))
    os.makedirs(parent, exist_ok=True)
    shutil.copyfile(src, dest_path)
    digest = sha256_of(dest_path)
    print("wrote %s (%d bytes, sha256 %s)" % (dest_path, size, digest))
    return dest_path


def copy_poster(out_dir):
    dest = os.path.join(out_dir, OUTPUT_NAME)
    return copy_poster_to_file(dest)


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="Copy the pre-rendered poster to the output directory.")
    parser.add_argument(
        "--out", default=None,
        help="output file path (overrides MAKEFUN_OUTPUT_DIR)")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    if args.out:
        copy_poster_to_file(args.out)
        return 0
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    copy_poster(out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
