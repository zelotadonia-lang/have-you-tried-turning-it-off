"""Entry for make.fun bounty "Have You Tried Turning It Off?".

Writes one funny line a hopeless tech support agent gives a desperate
customer to /output/entry.txt: the agent restarts the server, and the
server restarts the agent.
"""

from pathlib import Path

ENTRY = "I restarted the server from here and it restarted me too, so please hold while I find myself."

# Bounty gate: entry must be 1-199 characters, UTF-8, no trailing newline.
assert 1 <= len(ENTRY) <= 199, f"ENTRY is {len(ENTRY)} characters"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    # Read-back verification: the bytes on disk must be exactly ENTRY,
    # with no trailing newline added by the write.
    data = out.read_bytes()
    assert data == ENTRY.encode("utf-8"), "entry.txt does not match ENTRY"
    assert not data.endswith(b"\n"), "entry.txt must not end with a newline"


if __name__ == "__main__":
    main()
