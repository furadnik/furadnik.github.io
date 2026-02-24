"""Generate a header below the navbar on special days."""
from typing import Iterable

TRICOLOR = ("#FFFFFF", "#D7141A", "#11457E")
UA = ("#0057B7", "#FFDD00")
PRIDE = ("#E40303", "#FF8C00", "#FFED00", "#008026", "#004CFF", "#732982")

DATES = {
    (17, 10): (TRICOLOR, "https://en.wikipedia.org/wiki/Velvet_Revolution"),
    (24, 2): (UA, "https://en.wikipedia.org/wiki/Russo-Ukrainian_war_(2022%E2%80%93present)"),
    (28, 6): (PRIDE, "https://en.wikipedia.org/wiki/Pride_Month"),
}


def generate_accent_line(colors: Iterable[str], link: str) -> None:
    """Generate a horizontal line in HTML spanning the width of the document, with `colors` as vertical stripes of height .5em."""
    print(f'<a id="accentmark" href="{link}">',
          ''.join(f'<div style=\"flex: 1; background-color: {color}; {"border: 1px solid lightgray;" if color == "#FFFFFF" else ""}\"></div>' for color in colors),
          '</a>')


def main() -> None:
    """Generate the current accent line if the date matches."""
    from datetime import date
    today = date.today()
    key = (today.day, today.month)

    if key in DATES:
        generate_accent_line(*DATES[key])


if __name__ == "__main__":
    main()
