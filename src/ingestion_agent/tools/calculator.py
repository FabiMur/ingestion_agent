from strands import tool
from simpleeval import simple_eval


@tool
def calculator(expression: str) -> str:
    """Evaluates a mathematical expression and returns the result."""
    try:
        result = simple_eval(expression)
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {e}"
