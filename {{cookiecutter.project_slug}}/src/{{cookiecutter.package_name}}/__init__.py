"""{{ cookiecutter.project_slug }}: {{ cookiecutter.description }}."""

__version__ = "0.1.0"


def hello(name: str) -> str:
    """Return a greeting message.

    Args:
        name: The name to greet.

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"
