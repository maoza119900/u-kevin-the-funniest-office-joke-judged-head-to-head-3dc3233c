"""Write one office joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: the joke is a fixed string. No clock, no randomness,
no network, no file reads. The output directory comes from the
MAKEFUN_OUTPUT_DIR environment variable and defaults to /output.
"""

import os

JOKE = "I've typed 'per my last email' so often that my keyboard now autocompletes my resentment."

# The gate allows 1-200 characters; this line is 89. It is written exactly
# as-is, with no trailing newline, so the file is 89 bytes of UTF-8.


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
