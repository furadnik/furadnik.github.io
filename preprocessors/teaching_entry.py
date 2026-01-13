"""A filter for filling out exercise sessions.

Expects the following structure:
    teaching/{semester}_{subject}/
        index.md
        {yyyy}-{mm}-{dd}/
            description.md
            hw.pdf
            ex.pdf
"""
from os import system
from pathlib import Path

SINGLE_CONTENT = """
1. cvičení ({date}): {inline_links}
{description}
""".strip()
FILE_MAPS = {
    "hw.pdf": ("domácí úkol", "past_du_{date}.pdf"),
    "ex.pdf": ("příklady", "past_cviceni_{date}.pdf"),
}


def render_sessions(current_file_path: Path, output_path: Path) -> str:
    """Render out all the sessions in an exercise/...

    The current_file_path is expected to point to index.md, and the output_path
    is expected to point to the base output directory.
    """
    assert current_file_path.name == "index.md", f"Expected {current_file_path} to point to index.md."
    path = current_file_path.parent
    assets_path = output_path / path.parent.name / path.name
    return "\n".join(render_session(p, assets_path)
                     for p in sorted(path.iterdir(), key=lambda x: x.name) if p.is_dir())


def _format_date(date_str: str) -> str:
    """Format date from yyyy-mm-dd to d. m. yyyy."""
    date_parts = date_str.split("-")
    year, month, day = map(int, date_parts)
    return f"{day}. {month}. {year}"


def render_session(path: Path, assets_path: Path) -> str:
    """Render the information into markdown."""
    desc_path = path / "description.md"
    if not desc_path.exists():
        description = ""
    else:
        # Indent all lines by one tab
        description = "\t" + desc_path.read_text().strip().replace("\n", "\n\t")
    date_str = path.name
    inline_links = []
    for file_name, (label, target_template) in FILE_MAPS.items():
        file_path = path / file_name
        if not file_path.exists():
            continue
        target = target_template.format(date=date_str)
        inline_links.append(f"[{label}]({target})")
        system(f"cp '{file_path}' '{assets_path / target}'")

    return SINGLE_CONTENT.format(
        date=_format_date(date_str),
        inline_links=", ".join(inline_links),
        description=description,
    )
