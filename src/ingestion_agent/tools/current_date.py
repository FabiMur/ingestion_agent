from strands import tool


@tool
def current_date() -> str:
    """Returns the current date in YYYY-MM-DD format."""
    from datetime import datetime

    return datetime.now().strftime("%Y-%m-%d")
