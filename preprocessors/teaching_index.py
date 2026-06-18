"""A filter for generating the list of taught courses.

Also generates helper sites for auto-filling the latest year of a taught subject.
"""
from collections import defaultdict
from pathlib import Path

from yaml import safe_load_all

from .school_utils import unpack_semester_code

SEMESTER_FORMAT = "* {year_from}/{year_to} {semester_type}\n\n{subjects}\n\n"
SUBJECT_FORMAT = "  - [{name}]({semester}_{code})"


def render_index(current_file_path: Path, output_path: Path) -> str:
    """Render out all the sessions in an exercise/...

    The current_file_path is expected to point to index.md, and the output_path
    is expected to point to the base output directory.
    """
    assert current_file_path.name == "index.md", f"Expected {current_file_path} to point to index.md."
    path = current_file_path.parent
    target_path = output_path / path.name

    latest_subjects: dict[str, str] = {}
    semesters_subjects: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for file in path.iterdir():
        # subjects are always dirs
        if not file.is_dir():
            continue

        entry_id = file.name
        semester_code, subject_code = entry_id.split("_")
        if subject_code not in latest_subjects or semester_code > latest_subjects[subject_code]:
            latest_subjects[subject_code] = semester_code

        subject_name = _get_subject_name(file)
        semesters_subjects[semester_code].append((subject_code, subject_name))

    res = ""
    for semester, subjects in semesters_subjects.items():
        formatted_subjects = "\n".join(
            SUBJECT_FORMAT.format(name=name, semester=semester, code=code) for code, name in subjects
        )
        year, semester_type = unpack_semester_code(semester)
        res += SEMESTER_FORMAT.format(year_from=year, year_to=year + 1,
                                      semester_type=semester_type, subjects=formatted_subjects)

    for subject, semester in latest_subjects.items():
        _prepare_redirect(subject, semester, target_path)

    return res


def _get_subject_name(file: Path) -> str:
    """Get the name of the subject."""
    index = file / "index.md"
    assert index.exists()
    with index.open() as f:
        config = next(safe_load_all(f))
    return config["pagetitle"]


REDIRECT_TEMPLATE = """<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="refresh" content="0; url='../{semester}_{subject}'" />
    </head>
    <body>
    </body>
</html>
"""


def _prepare_redirect(subject: str, semester: str, target: Path) -> None:
    """Prepare a redirect page for a subject."""
    directory = target / subject
    directory.mkdir(exist_ok=True, parents=True)
    index = directory / "index.html"
    print(directory, index)
    index.write_text(REDIRECT_TEMPLATE.format(semester=semester, subject=subject))
