"""Base file for pre-processing of markdown files."""
from .generate_notes import generate_notes
from .projects import generate_project_list
from .publications import generate_publications
from .upcoming import generate_upcoming

PREPROCESSORS = {
    "{{notes}}": generate_notes,
    "{{publications}}": generate_publications,
    "{{projects}}": generate_project_list,
    "{{upcoming}}": generate_upcoming,
}
