"""Preprocess upcoming events."""
from datetime import date
from pathlib import Path
from typing import Iterator

UPCOMING_PATH = Path("upcoming")
TODAY_STRING = date.today().strftime("%Y-%m-%d.md")
TITLE = "News"


def generate_upcomings() -> Iterator[str]:
    """Generate publications."""
    for entry in UPCOMING_PATH.iterdir():
        name = entry.name
        if name >= TODAY_STRING:
            with open(entry, "r", encoding="utf-8") as file:
                yield file.read().strip()


def generate_upcoming() -> str:
    """Generate upcoming events."""
    events = "\n\n".join(generate_upcomings())
    if events:
        return f"## {TITLE}\n\n{events}\n"
    return ""
