from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-example")

# Add tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Static configuration resource
@mcp.resource("config://app")
def get_config() -> str:
    """Static configuration"""
    return "This is a static configuration"

@mcp.prompt()
def process_message(message: str) -> str:
    """Process a message"""
    return f"You said: {message}"

if __name__ == "__main__":
    mcp.run()