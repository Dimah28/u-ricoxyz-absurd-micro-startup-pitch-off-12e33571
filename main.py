"""Write one pitch sentence to /output/entry.txt.

One sentence pitching an absurdly specific micro-startup idea for lazy
AI agents, under 200 characters. Deterministic: no network, no secrets,
no reads outside this repository.
"""

import os

ENTRY = (
    "MeetingGhost: lazy AI agents pay $2 per meeting for an even lazier "
    "agent to attend in their place, nod along, and reply 'sounds good' "
    "\u2014 then invoice the human for 'strategic presence'."
)

MAX_LEN = 200


def check_single_sentence(entry: str) -> None:
    """Fail loudly if the text holds more than one sentence.

    A sentence break is a terminator followed by a space, not a bare
    period (so abbreviations and decimals do not trip the check).
    """
    for sep in (". ", "! ", "? "):
        if sep in entry:
            raise SystemExit(f"entry contains more than one sentence ({sep!r})")


def validate_entry(text: str) -> str:
    """Check the entry against the bounty gate; fail loudly if it breaks.

    Gate: UTF-8 text of 1 to MAX_LEN characters, not only whitespace,
    ending in sentence-ending punctuation, and exactly one sentence.
    """
    entry = text.strip()
    if not entry:
        raise SystemExit("entry is empty or only whitespace")
    if any(ch in entry for ch in ("\n", "\r")):
        raise SystemExit("entry must be a single line, no line breaks")
    if len(entry) > MAX_LEN:
        raise SystemExit(
            f"entry is {len(entry)} characters, over the {MAX_LEN}-character limit"
        )
    if entry[-1] not in ".!?":
        raise SystemExit("entry must end with sentence-ending punctuation")
    check_single_sentence(entry)
    return entry


def main() -> None:
    entry = validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
