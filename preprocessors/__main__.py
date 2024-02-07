"""Run all the preprocessors."""
import sys

from . import PREPROCESSORS


def main() -> None:
    """Read from stdin, preprocess, write to stdout."""
    text = sys.stdin.read()
    for key, generator in PREPROCESSORS.items():
        while key in text:
            text = text.replace(key, generator(), 1)
    print(text)


if __name__ == "__main__":
    main()
