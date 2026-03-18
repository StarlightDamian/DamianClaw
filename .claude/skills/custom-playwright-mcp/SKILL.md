# Playwright MCP 自动化浏览器操作

## 功能描述

使用 Playwright 通过 MCP 挂载自动化浏览器操作，根据自然语言描述（登录、抓取、点击等场景）自动生成依赖具体 DOM 节点的 Python Playwright 脚本。

## 能力

- 接收用户的自然语言场景描述
- 自动分析页面结构，生成针对具体 DOM 节点的选择器
- 生成完整可运行的 Python Playwright 脚本
- 支持登录、点击、表单填写、网页抓取等常见场景
- 通过 CLI 挂载 Playwright MCP 服务

## 使用方式

1. 用户提供目标 URL 和操作描述（例如："登录 GitHub，用户名 xxx，密码 yyy"）
2. 分析页面结构，生成准确的 DOM 选择器
3. 输出完整的 Python 脚本，包含：
   - 浏览器启动配置
   - 准确的元素定位（使用文本、id、class、XPath 等）
   - 动作序列（点击、填充、等待等）
   - 结果处理（截图、抓取数据保存）

## 示例输出结构

```python
from playwright.sync_api import sync_playwright
# MCP 集成代码...

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com/login")

    # 针对具体 DOM 节点的操作
    page.fill("#username", "your_username")
    page.fill("#password", "your_password")
    page.click("button[type='submit']")

    # 等待页面加载完成
    page.wait_for_load_state()

    # 抓取数据...
    browser.close()
```

## 生成原则

- **强依赖具体 DOM 节点**：使用精确的选择器定位，避免模糊匹配
- **可运行**：生成完整可执行代码，无需用户修改即可运行
- **错误处理**：添加适当的等待和异常处理
- **速度优先**：在底层快速操作浏览器
