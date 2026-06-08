"""Generic helpers for school stuff."""


def semester_value(semester_code: str) -> int:
    """Get semester value."""
    year, semester_type = unpack_semester_code(semester_code)
    return -(year * 2 + (1 if semester_type == "summer" else 0))


def unpack_semester_code(code: str) -> tuple[int, str]:
    """Get semester starting year."""
    year = 2000 + int(code[0:2])
    semester_type = "winter" if code[-1] == "z" else "summer"
    return year, semester_type
