"""Example test file for wanmantest project."""

from wanmantest.example import example_function, get_version


def test_example_pass():
    """A simple test that should always pass."""
    assert 1 + 1 == 2


def test_example_string():
    """Test string operations."""
    result = "wanman" + "test"
    assert result == "wanmantest"


def test_example_list():
    """Test list operations."""
    items = [1, 2, 3]
    items.append(4)
    assert len(items) == 4
    assert sum(items) == 10


def test_get_version():
    """Test version function."""
    assert get_version() == "0.1.0"


def test_example_function():
    """Test example_function from the package."""
    assert example_function("test") == "test"
    assert example_function(42) == 42
    assert example_function(None) is None
