"""Base file for pre-processing of markdown files."""
from .generate_notes import generate_notes
from .publications import generate_publications

PREPROCESSORS = {
    "{{notes}}": generate_notes,
    "{{publications}}": generate_publications
}
