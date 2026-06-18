"""Demo MCP server built with FASTMCP."""

from fastmcp import FastMCPServer


class DemoMCPServer(FastMCPServer):
    async def handle_request(self, request):
        """Handle incoming MCP requests and return a demo response."""
        return {
            "status": "ok",
            "message": "Hello from FASTMCP demo server!",
            "received": getattr(request, "data", request),
        }


if __name__ == "__main__":
    server = DemoMCPServer(host="0.0.0.0", port=8000)
    server.run()
