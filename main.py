"""Place the 24 November 2026 news digest at /output/entry.png.

The digest is the 1024x1024 PNG shipped beside this script as
entry.png: thirty stories from Tuesday 24 November 2026, led by the
Huawei jury verdict, in a single image. This script only moves those
bytes into place with the standard library. It never touches the
network and never consults the clock, so repeated runs always write
the same output file.
"""

import hashlib
import pathlib
import sys

DIGEST_NAME = "entry.png"
DEST_DIR = pathlib.Path("/output")


def find_digest() -> pathlib.Path:
    """Return the digest image stored next to this script."""
    return pathlib.Path(__file__).resolve().parent / DIGEST_NAME


def _digests_match(first: pathlib.Path, second: bytes) -> bool:
    """True when a file's SHA-256 equals the digest of given bytes."""
    return hashlib.sha256(first.read_bytes()).hexdigest() == hashlib.sha256(second).hexdigest()


def copy_checked(origin: pathlib.Path, dest: pathlib.Path) -> int:
    """Copy origin to dest, verifying size and SHA-256; return bytes."""
    data = origin.read_bytes()
    dest.parent.mkdir(parents=True, exist_ok=True)
    written = dest.write_bytes(data)
    if written != len(data):
        raise RuntimeError(f"short write: {written} of {len(data)} bytes")
    if not _digests_match(dest, data):
        raise RuntimeError("output bytes differ from the digest image")
    return written


def run() -> int:
    digest = find_digest()
    if not digest.is_file():
        print(f"missing digest image: {digest}", file=sys.stderr)
        return 1
    copied = copy_checked(digest, DEST_DIR / DIGEST_NAME)
    if (DEST_DIR / DIGEST_NAME).stat().st_size != copied:
        raise RuntimeError("output size differs from the digest image")
    return 0


if __name__ == "__main__":
    sys.exit(run())
