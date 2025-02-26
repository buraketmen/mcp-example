import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="uv",
    args=["run", "--with", "mcp", "server.py"],
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            # Available resources
            resources = await session.list_resources()
            print(resources)
            # Available tools
            tools = await session.list_tools()
            print(tools)

            # Available prompts
            prompts = await session.list_prompts()
            print(prompts)

            # Call the "add" tool
            result = await session.call_tool("add", arguments={"a": 3, "b": 4})
            print(result.content[0].text)

if __name__ == "__main__":
    
    asyncio.run(run())