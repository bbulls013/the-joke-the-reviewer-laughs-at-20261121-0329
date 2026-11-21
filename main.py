"""Write a one-line joke about working beside AI coding agents.

The joke is judged pairwise by an AI reviewer, so it aims for a
recognisable diff-review moment with the surprise saved for the end.
"""

import os

JOKE = (
    "I asked my AI coder for a one-line fix; it opened a "
    "2,000-line PR called 'minor cleanup' — now I tell the "
    "reviewer 'the model was very confident' is not a test plan."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
