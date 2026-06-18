# FASTMCP Demo Repository

A minimal Python demo repository for building an MCP server using `FASTMCP`.

## Overview

This demo shows a simple server scaffold and basic development setup for a FASTMCP-based Python MCP service.

## Files

- `main.py` - demo server entrypoint
- `pyproject.toml` - Python packaging and dependencies
- `requirements.txt` - installable runtime dependencies
- `.gitignore` - ignores Python artifacts

## Getting started

1. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the demo server:

```bash
python main.py
```

## Notes

The server code is intentionally small and ready to extend with FASTMCP-specific request handlers.
