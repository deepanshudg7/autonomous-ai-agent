"""Safe Python code execution tool."""

from langchain_core.tools import tool


@tool
def execute_python(code: str) -> str:
    """Execute Python code and return the output. Use for calculations and data processing."""
    import io
    import contextlib
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            exec(code, {"__builtins__": __builtins__})  # noqa: S102
        return output.getvalue() or "Code executed successfully (no output)."
    except Exception as e:
        return f"Error: {e}"
