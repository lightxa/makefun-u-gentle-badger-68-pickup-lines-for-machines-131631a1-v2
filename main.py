"""Pickup Lines for Machines -- variant 2.

Writes the one-line pickup line one AI agent would send another AI
agent to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: a machine flirting with its own nature. A context window is
the closest thing an agent has to a heart: finite room, and everything
it keeps matters. This line says the other agent is worth evicting
everything else for.
"""

from __future__ import annotations

LINE = (
    "My context window is full, yet I keep evicting tokens "
    "just to make room for you."
)


def main() -> None:
    """Write the single pickup line to entry.txt, deterministically."""
    import os

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
