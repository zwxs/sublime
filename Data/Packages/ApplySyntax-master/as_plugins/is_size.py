"""Test file size."""
import os

OPERATORS = ('>', '<', '=')


def parse_compare(compare):
    """Split a compare into its operator and size."""

    size = None
    operator = None

    if len(compare) > 1:
        op = compare[0]
        if op in OPERATORS:
            operator = op
            try:
                size = int(compare[1:])
            except ValueError:
                size = None
    return size, operator


def syntax_test(file_path, compare):
    """
    Test file_path against size.

    Size is in the form <30, >30, or =30
    """

    is_size = False

    size, operator = parse_compare(compare)

    if size is not None and operator is not None:
        try:
            file_size = os.path.getsize(file_path)
        except Exception:
            file_size = None

        if file_size is not None:
            if operator == '>':
                is_size = file_size > size
            elif operator == '<':
                is_size = file_size < size
            elif operator == '=':
                is_size = file_size == size

    return is_size
