#!/usr/bin/python
"""Update web files."""
from os import system
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterable, Optional


class GitSync:
    """Sync changes with git."""

    def __init__(self, git_url: str) -> None:
        """Save and init the repo."""
        self._url = git_url
        self._td: Optional[TemporaryDirectory] = None

    def __enter__(self) -> Path:
        """Enter the env."""
        temp_path = self._get_tempdir()
        path = self._git_init(temp_path)
        return path

    def _git_init(self, path: Path) -> Path:
        """Initialize git repo."""
        system(f"(cd '{path}' && git clone --quiet '{self._url}') >/dev/null")  # nosec
        ret = list(path.iterdir())
        if not ret:
            raise ValueError("Cloning failed.")
        return ret[0]

    def _get_tempdir(self) -> Path:
        """Get temporary directory."""
        self._td = TemporaryDirectory()
        return Path(self._td.name)

    def __exit__(self, *args, **kwargs) -> None:
        """Delete the td."""
        if self._td is not None:
            self._td.cleanup()


GIT_URL = "https://gitlab.mff.cuni.cz/uradnikf/bc_lec"
BC_NOTES_GIT = GitSync(GIT_URL)
BC_NOTES_URL = f"{GIT_URL}/-/raw/master/{{semester_code}}/{{subject}}/main.pdf"
SEMESTER_FORMAT = "* {year_from}/{year_to} {semester_type}\n\n{subjects}\n\n"
OUTPUT_PATH = Path("notes.md")
TEMPLATE = f"""
---
pagetitle: Notes
lang: en
---
Here are some of my notes.
They are mostly in Czech.
They're written in $\\LaTeX{{}}$, and the source code can be found [here]({GIT_URL}/bc_lec).
There are many mistakes in them, so be careful.

If you find a mistake, either write me a message, or [create an issue]({GIT_URL}/-/issues/new).

"""


def semester_value(semester_code: str) -> int:
    """Get semester value."""
    year, semester_type = unpack_semester_code(semester_code)
    return -(year * 2 + (1 if semester_type == "summer" else 0))


def unpack_semester_code(code: str) -> tuple[int, str]:
    """Get semester starting year."""
    year = 2000 + int(code[0:2])
    semester_type = "winter" if code[-1] == "z" else "summer"
    return year, semester_type


def get_subjects_for_semester(semester_notes_path: Path) -> Iterable[tuple[str, str, bool]]:
    """Get subjects for semester.

    Returns:
        Iterable of tuples (subject_code, subject_name, subject_english).
    """
    for subject in semester_notes_path.iterdir():
        if not subject.is_dir() or not (subject / "main.tex").exists():
            continue
        subject_code = subject.name
        with open(subject / "main.tex") as f:
            main_tex = f.read()
        subject_english = "\\input{english}\n" in main_tex or "\\input{english.tex}\n" in main_tex
        subject_name = main_tex.split("\\title{")[1].split("}")[0]
        yield subject_code, subject_name, subject_english


def get_semesters(notes_root: Path) -> Iterable[tuple[str, Iterable[tuple[str, str, bool]]]]:
    """Get semesters."""
    for semester in notes_root.iterdir():
        if semester.name.startswith(".") or not semester.is_dir():
            continue
        subjects = get_subjects_for_semester(semester)
        yield semester.name, subjects


def format_semester(semester: str, subjects: Iterable[tuple[str, str, bool]]) -> str:
    """Format semester to html."""
    year, semester_type = unpack_semester_code(semester)
    formatted_subjects = "\n".join(
        f'  - [{subject_name}]({BC_NOTES_URL.format(semester_code=semester, subject=subject_code)})'
        f'{" [In English]" if subject_english else ""}'
        for subject_code, subject_name, subject_english in sorted(subjects, key=lambda x: x[1])
    )
    if not formatted_subjects:
        return ""
    return SEMESTER_FORMAT.format(year_from=year, year_to=year + 1,
                                  semester_type=semester_type, subjects=formatted_subjects)


def update_bc_notes(output_file: Path = OUTPUT_PATH, template: str = TEMPLATE,
                    notes: GitSync = BC_NOTES_GIT, notes_url: str = BC_NOTES_URL) -> None:
    """Update the bc notes."""
    with notes as notes_dir:
        semesters = sorted(get_semesters(notes_dir), key=lambda x: semester_value(x[0]))
        formatted_semesters = "\n".join(format_semester(semester, subjects) for semester, subjects in semesters)
    print(formatted_semesters)
    output_file.write_text(template + formatted_semesters)


if __name__ == '__main__':
    update_bc_notes()
