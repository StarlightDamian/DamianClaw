#!/usr/bin/env python3
"""
Playwright MCP CLI 启动脚本
用来挂载 Playwright MCP 服务到 Claude Code
"""

import argparse
import asyncio
import sys
from playwright_mcp_server import PlaywrightMCPServer


def main():
    parser = argparse.ArgumentParser(description='Playwright MCP Server')
    parser.add_argument('--host', default='localhost', help='Host (for future TCP support, currently stdio only)')
    parser.add_argument('--port', type=int, default=8765, help='Port (for future TCP support)')
    args = parser.parse_args()

    server = PlaywrightMCPServer()
    asyncio.run(server.run())


if __name__ == "__main__":
    main()
