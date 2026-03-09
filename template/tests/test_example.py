"""Tests for {{package_name }}."""

from {{package_name }} import __version__, hello


def test_version() -> None:
    """Test that version is set."""
    assert __version__ == "0.1.0"


def test_hello() -> None:
    """Test hello function."""
    assert hello("World") == "Hello, World!"


def test_hello_empty() -> None:
    """Test hello function with empty string."""
    assert hello("") == "Hello, !"
