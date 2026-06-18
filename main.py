"""Demo MCP server built with FASTMCP."""

from fastmcp import FastMCP


app = FastMCP("demo")


@app.tool()
def hello(name: str) -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"


@app.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


if __name__ == "__main__":
    app.run()
