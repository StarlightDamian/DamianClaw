"""
示例：自动生成的 GitHub 登录脚本
展示如何生成强依赖具体 DOM 节点的 Python Playwright 脚本
"""

from playwright.async_api import async_playwright
import asyncio


async def github_login(username: str, password: str):
    """GitHub 登录示例 - 精确依赖 DOM 节点"""

    async with async_playwright() as p:
        # 启动浏览器（显示模式方便调试）
        browser = await p.chromium.launch(headless=False, slow_mo=50)
        page = await browser.new_page()

        # 导航到登录页
        await page.goto("https://github.com/login")
        await page.wait_for_load_state()

        # 精确的 DOM 定位 - 基于实际页面结构
        # 使用 id 选择器定位用户名输入框
        await page.fill("#login_field", username)
        # 使用 id 选择器定位密码输入框
        await page.fill("#password", password)
        # 使用 type 和 name 定位提交按钮
        await page.click("input[type='submit'][name='commit']")

        # 等待跳转完成
        await page.wait_for_load_state("networkidle")

        # 验证登录成功（检查特定元素）
        # 定位头像元素，如果存在说明登录成功
        try:
            await page.wait_for_selector("summary[aria-label='View profile and more']", timeout=5000)
            print("✅ 登录成功！")
            # 截图保存结果
            await page.screenshot(path="github_login_result.png", full_page=True)
            print("📸 截图已保存为 github_login_result.png")
        except TimeoutError:
            print("❌ 登录失败，可能是用户名密码错误")
            await page.screenshot(path="github_login_failed.png", full_page=True)

        await browser.close()


if __name__ == "__main__":
    # 替换为你的用户名密码
    your_username = "your_username"
    your_password = "your_password"
    asyncio.run(github_login(your_username, your_password))
