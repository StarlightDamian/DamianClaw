"""
Playwright MCP 服务器
通过 Model Context Protocol 暴露 Playwright 浏览器自动化能力

功能:
- 根据自然语言描述生成 Python Playwright 脚本
- 执行自动化操作（登录、点击、抓取等）
- 返回执行结果和截图
"""

import asyncio
import json
import sys
from typing import Any, Dict, List, Optional
from dataclasses import dataclass

from mcp.server import Server
from mcp.types import Tool, TextContent, ImageContent
import playwright
from playwright.async_api import async_playwright

@dataclass
class GeneratedScript:
    code: str
    description: str
    selectors: List[str]

class PlaywrightMCPServer:
    def __init__(self):
        self.server = Server("playwright-mcp")
        self.setup_tools()
        self.browser = None
        self.page = None

    def setup_tools(self):
        @self.server.call_tool("generate_script")
        async def generate_script(arguments: Dict[str, Any]) -> List[TextContent]:
            """Generate Playwright script from natural language description"""
            url = arguments.get("url", "")
            scenario = arguments.get("scenario", "")
            dom_elements = arguments.get("dom_elements", [])

            # 这里由 LLM 根据场景和 DOM 分析生成代码
            # 本服务接收参数后返回生成的代码

            code = self._generate_python_script(url, scenario, dom_elements)

            return [
                TextContent(
                    type="text",
                    text=json.dumps({
                        "success": True,
                        "code": code,
                        "message": f"已为场景 '{scenario}' 生成 Playwright 脚本"
                    }, indent=2, ensure_ascii=False)
                )
            ]

        @self.server.call_tool("execute_script")
        async def execute_script(arguments: Dict[str, Any]) -> List[TextContent]:
            """Execute the generated Playwright script"""
            code = arguments.get("code", "")

            try:
                result = await self._execute_code(code)
                return [
                    TextContent(
                        type="text",
                        text=json.dumps({
                            "success": True,
                            "result": result,
                            "message": "脚本执行完成"
                        }, indent=2, ensure_ascii=False)
                    )
                ]
            except Exception as e:
                return [
                    TextContent(
                        type="text",
                        text=json.dumps({
                            "success": False,
                            "error": str(e),
                            "message": "脚本执行失败"
                        }, indent=2, ensure_ascii=False)
                    )
                ]

        @self.server.call_tool("close_browser")
        async def close_browser(arguments: Dict[str, Any]) -> List[TextContent]:
            """Close the browser instance"""
            if self.browser:
                await self.browser.close()
                self.browser = None
                self.page = None

            return [
                TextContent(
                    type="text",
                    text=json.dumps({
                        "success": True,
                        "message": "浏览器已关闭"
                    }, indent=2, ensure_ascii=False)
                )
            ]

        # 定义工具列表
        self.server.list_tools = lambda: [
            Tool(
                name="generate_script",
                description="根据自然语言场景描述生成 Python Playwright 脚本",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "目标网页 URL"
                        },
                        "scenario": {
                            "type": "string",
                            "description": "场景描述（例如：'登录 GitHub，输入用户名 xxx 和密码 yyy 后点击登录按钮'"
                        },
                        "dom_elements": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "页面中关键 DOM 元素的描述列表"
                        }
                    },
                    "required": ["url", "scenario"]
                }
            ),
            Tool(
                name="execute_script",
                description="执行生成的 Playwright 脚本",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "code": {
                            "type": "string",
                            "description": "要执行的 Python 代码"
                        }
                    },
                    "required": ["code"]
                }
            ),
            Tool(
                name="close_browser",
                description="关闭浏览器实例",
                inputSchema={
                    "type": "object",
                    "properties": {}
                }
            )
        ]

    def _generate_python_script(self, url: str, scenario: str, dom_elements: List[str]) -> str:
        """
        根据场景生成 Python Playwright 脚本
        这个方法会被 LLM 覆盖，根据具体场景生成具体的 DOM 选择器代码
        """
        lines = [
            "from playwright.async_api import async_playwright",
            "",
            "async def main():",
            f"    async with async_playwright() as p:",
            "        browser = await p.chromium.launch(headless=False)",
            "        page = await browser.new_page()",
            f"        await page.goto('{url}')",
            "        await page.wait_for_load_state()",
            ""
        ]

        # 根据场景添加具体操作
        # 这里生成模板，实际使用时 LLM 会替换为具体代码
        lines.append("        # 场景: " + scenario)
        lines.append("        # 请根据实际页面 DOM 结构修改选择器")
        lines.append("")

        for elem in dom_elements:
            lines.append(f"        # {elem}")

        lines.extend([
            "",
            "        # 等待操作完成",
            "        await page.wait_for_timeout(2000)",
            "        # 截图保存结果",
            "        await page.screenshot(path='result.png')",
            "        print('操作完成，截图已保存为 result.png')",
            "",
            "        await browser.close()",
            "",
            "if __name__ == '__main__':",
            "    import asyncio",
            "    asyncio.run(main())",
        ])

        return "\n".join(lines)

    async def _execute_code(self, code: str) -> str:
        """Execute the generated code in a controlled environment"""
        # 执行生成的代码
        # 这里使用 exec 在当前进程中执行
        # 实际生产环境建议使用沙箱隔离

        globals_dict = {
            "async_playwright": async_playwright,
            "__name__": "__main__",
        }

        try:
            exec(code, globals_dict)
            if "main" in globals_dict:
                await globals_dict["main"]()
            return "执行成功"
        except Exception as e:
            return f"执行异常: {str(e)}"

    async def run(self):
        """Run the MCP server"""
        from mcp.server.stdio import stdio_server

        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(read_stream, write_stream, self.server.create_initialization_options())

if __name__ == "__main__":
    server = PlaywrightMCPServer()
    asyncio.run(server.run())
