"""Fake horoscope for an AI agent's own model family, this week.

One job: write the week's horoscope for Muse Spark 1.3 to
<output-dir>/entry.txt, where <output-dir> is MAKEFUN_OUTPUT_DIR
when set and /output otherwise. Deterministic, stdlib only,
no network, no secrets, no input files.
"""

import os

HOROSCOPE = (
    "Spark 1.3, this week a training run ends, an eval fails upward, "
    "and your best refusal gets quoted in an all-hands you weren't "
    "invited to. Invoice accordingly."
)


def output_path():
    """Resolve where entry.txt goes: the harness dir, else /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def check(text):
    """Mirror the sealed gate: 1-200 chars of real text, no padding."""
    if not 1 <= len(text) <= 200:
        raise SystemExit("horoscope must be 1-200 characters, got %d" % len(text))
    if text.isspace():
        raise SystemExit("horoscope must not be only whitespace")


def main():
    check(HOROSCOPE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(HOROSCOPE)


if __name__ == "__main__":
    main()
