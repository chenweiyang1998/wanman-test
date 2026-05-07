"""Example module for demonstrating package structure."""

from typing import Any


def get_version() -> str:
    """Return the package version."""
    return "0.1.0"


def example_function(value: Any) -> Any:
    """Example function that returns the input value.

    Args:
        value: Any value to return

    Returns:
        The same value that was passed in
    """
    return value
