"""Run all the preprocessors."""
import sys
from argparse import ArgumentParser
from pathlib import Path

from . import PREPROCESSORS, PREPROCESSORS_WITH_PATH

PARSER = ArgumentParser(
    description="Run all the preprocessors. Reads from stdin, but needs the input path and output path for some preprocessors."
)
PARSER.add_argument("--current_file", type=Path, default=None, help="Path to the current file being processed.")
PARSER.add_argument("--output_dir", type=Path, help="Path to the base output directory.")


def main(current_file: Path | None = None, output_dir: Path | None = None) -> None:
    """Read from stdin, preprocess, write to stdout."""
    text = sys.stdin.read()
    for key, generator in PREPROCESSORS.items():
        while key in text:
            text = text.replace(key, generator(), 1)
    for key, generator in PREPROCESSORS_WITH_PATH.items():
        while key in text:
            assert current_file is not None, f"Preprocessor {key} needs current_file"
            assert output_dir is not None, f"Preprocessor {key} needs output_dir"
            text = text.replace(key, generator(current_file, output_dir), 1)
    print(text)


if __name__ == "__main__":
    args = PARSER.parse_args()
    main(current_file=args.current_file, output_dir=args.output_dir)
