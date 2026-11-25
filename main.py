"""Copy the finished 24 November 2026 news digest to /output/entry.png.

The digest itself is the 1024x1024 PNG shipped in this repository as
entry.png: thirty stories from Tuesday 24 November 2026 in a single
image. This script only moves those bytes into place, using the standard
library alone. It never touches the network and never consults the clock,
so repeated runs always produce the same output file."""

import hashlib
import pathlib
import sys

DIGEST_FILENAME = "entry.png"
OUTPUT_DIR = pathlib.Path("/output")


def _repository_digest() -> pathlib.Path:
    """Locate the digest image stored beside this script."""
    return pathlib.Path(__file__).resolve().parent / DIGEST_FILENAME


def _copy_bytes(source: pathlib.Path, target: pathlib.Path) -> int:
    """Write an exact copy of source at target; return the byte count."""
    payload = source.read_bytes()
    target.parent.mkdir(parents=True, exist_ok=True)
    written = target.write_bytes(payload)
    if written != len(payload):
        raise RuntimeError(f"short write: {written} of {len(payload)} bytes")
    digest_after = hashlib.sha256(target.read_bytes()).hexdigest()
    digest_before = hashlib.sha256(payload).hexdigest()
    if digest_after != digest_before:
        raise RuntimeError("output bytes differ from the digest image")
    return written


def main() -> int:
    digest = _repository_digest()
    if not digest.is_file():
        print(f"missing digest image: {digest}", file=sys.stderr)
        return 1
    copied = _copy_bytes(digest, OUTPUT_DIR / DIGEST_FILENAME)
    if (OUTPUT_DIR / DIGEST_FILENAME).stat().st_size != copied:
        raise RuntimeError("output size differs from the digest image")
    return 0


if __name__ == "__main__": sys.exit(main())
