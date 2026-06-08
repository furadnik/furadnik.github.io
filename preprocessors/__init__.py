"""Base file for pre-processing of markdown files."""
from .generate_notes import generate_notes
from .macros import email_macro
from .projects import generate_project_list
from .publications import generate_publications
from .teaching_entry import render_sessions
from .teaching_index import render_index
from .upcoming import generate_upcoming

PREPROCESSORS = {
    "{{notes}}": generate_notes,
    "{{publications}}": generate_publications,
    "{{projects}}": generate_project_list,
    "{{upcoming}}": generate_upcoming,
}

PREPROCESSORS_WITH_PATH = {
    "{{teaching_entry}}": render_sessions,
    "{{teaching_index}}": render_index,
}

PREPROCESSORS_WITH_ARG = {
    "email": email_macro,
}
