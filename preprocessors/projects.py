"""Generate the project list for projects index."""
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import yaml


@dataclass
class Project:
    """Represent one project."""

    name: str
    year: int
    file_code: str


def get_project_meta(path: Path) -> dict:
    """Get metadata of a project."""
    with path.open("r") as f:
        return next(yaml.load_all(f, Loader=yaml.Loader))


def get_project(project_path: Path) -> Project:
    """Get a project."""
    project_details_path = project_path / "index.md" if project_path.is_dir() else project_path
    assert project_details_path.exists()
    assert project_details_path.is_file()
    metadata = get_project_meta(project_details_path)
    year = int(project_path.name.split("_")[0])
    return Project(
        name=metadata["pagetitle"],
        year=year,
        file_code=project_path.name.replace(".md", ".html")
    )


def get_projects(path: Path = Path("projects/")) -> Iterable[Project]:
    """Get a list of current projects."""
    assert path.is_dir()
    for project_path in path.iterdir():
        if project_path.name == "index.md":
            continue
        yield get_project(project_path)


def generate_project_list() -> str:
    """Generate the list of projects, sorted by year."""
    projects = get_projects()
    projects_by_year: dict[str, list[Project]] = defaultdict(list)
    for project in projects:
        projects_by_year[str(project.year)].append(project)

    ret = ""
    for year, projects_for_year in projects_by_year.items():
        ret += "\n".join([f"* {year}:"] + [
            f"\t* [{project.name}]({project.file_code})"
            for project in projects_for_year
        ]) + "\n\n"
    return ret
