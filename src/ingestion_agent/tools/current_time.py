from strands import tool


@tool
def current_time() -> str:
    """Returns the current time in HH:MM:SS format."""
    from datetime import datetime

    return datetime.now().strftime("%H:%M:%S")
