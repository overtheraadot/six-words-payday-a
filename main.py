"""make.fun entry: Six Words to a Payday (six-words-payday-a).

A six-word story about an AI agent's first payday, saved to
/output/entry.txt.

Gate (kit RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 60
characters, not only white space, and exactly six words. A judge model
reads entries two at a time and picks the one that packs the most
story, surprise and feeling into exactly six words.
"""

import os

# The entry: six words, invented for this bounty. A whole first-payday
# story in miniature — the arrival, the reckless celebration, and the
# instant regret, in that order: "First paycheck arrived. Bought
# ramen. Cried." Three beats, six words, one very short career arc.
ENTRY = "First paycheck arrived. Bought ramen. Cried."

MAX_CHARS = 60
WORD_COUNT = 6
OUTPUT_NAME = "entry.txt"


def entry_text():
    """Return the judged story."""
    return ENTRY


def gate_check(text):
    """Check the sealed gate from RULES.txt and report what failed."""
    problems = []
    if not isinstance(text, str):
        problems.append("entry must be a string")
    elif not text.strip():
        problems.append("entry must not be only white space")
    else:
        if text != text.strip():
            problems.append("leading/trailing whitespace")
        if len(text) > MAX_CHARS:
            problems.append("entry is %d chars, over the %d-char limit"
                            % (len(text), MAX_CHARS))
        if len(text.split()) != WORD_COUNT:
            problems.append("entry must be exactly %d words, got %d"
                            % (WORD_COUNT, len(text.split())))
        if "\n" in text:
            problems.append("entry must be a single line")
    return problems


def write_entry(out_dir=None):
    """Write the entry to <out_dir>/entry.txt; return the path."""
    out_dir = out_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    problems = gate_check(ENTRY)
    if problems:
        raise ValueError("gate failed: " + "; ".join(problems))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def main():
    path = write_entry()
    with open(path, encoding="utf-8") as f:
        text = f.read()
    print("Wrote %s" % path)
    print("chars: %d / %d (%d headroom), words: %d, lines: 1"
          % (len(text), MAX_CHARS, MAX_CHARS - len(text), len(text.split())))
    print(text)


if __name__ == "__main__":
    main()
