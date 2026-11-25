#!/usr/bin/env python3
"""Carry the 24 November 2026 one-picture news roundup to its output slot.

The picture itself is bundled next to this file as entry.png: a square
1024-pixel image packing thirty news items from Tuesday, 24 November
2026, headed by the Huawei trade-secret verdict. This program does
nothing but ferry that file to /output/entry.png with the standard
library alone. It talks to no network, throws no dice, and never
looks at the time, so each invocation leaves exactly the same bytes
behind."""

from hashlib import sha256
from pathlib import Path

PICTURE = "entry.png"
OUT = Path("/output") / PICTURE


def _fingerprint(blob):
    """SHA-256 hex digest of one bytes object."""
    return sha256(blob).hexdigest()


PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def _read_bundled():
    """Load the bundled picture, failing loudly when it is not there."""
    folder = Path(__file__).resolve().parent
    bundled = folder / PICTURE
    if not bundled.exists():
        print("bundled picture not found: %s" % bundled)
        raise SystemExit(1)
    blob = bundled.read_bytes()
    if blob[:8] != PNG_MAGIC:
        raise SystemExit("bundled file is not a PNG image")
    return blob


def _same(first, second):
    """True when two byte strings share one SHA-256 fingerprint."""
    return _fingerprint(first) == _fingerprint(second)


def _deliver(blob):
    """Write blob out, then check the copy by length and fingerprint."""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(blob)
    again = OUT.read_bytes()
    if len(again) != len(blob):
        raise SystemExit("written copy has the wrong length")
    if not _same(again, blob):
        raise SystemExit("written copy has the wrong fingerprint")
    return len(again)


def main():
    payload = _read_bundled()
    _deliver(payload)
    print("placed %d bytes at %s" % (len(payload), OUT))


if __name__ == '__main__':
    main()
