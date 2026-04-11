"""Basic macros."""


def email_macro(arg: str) -> str:
    """Generate a formatted email link."""
    return f"[`{arg}`](mailto:{arg})"
