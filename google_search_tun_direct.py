"""
使用 Clash 代理访问 Google 搜索 "tun"
直接访问搜索结果页面并保持浏览器打开供人机验证
代理配置: 127.0.0.1:7890 (HTTP)

使用系统已安装的 Microsoft Edge 浏览器
"""
from playwright.async_api import async_playwright
import asyncio


async def main():
    async with async_playwright() as p:
        # 使用固定 Clash 代理配置
        # 使用系统已安装的 Microsoft Edge
        browser = await p.chromium.launch(
            headless=False,
            proxy={
                "server": "http://127.0.0.1:7890",
            },
            # 使用系统 Edge 浏览器路径
            executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        )
        context = await browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
        )
        page = await context.new_page()
        # 设置超时
        page.set_default_timeout(60000)

        # 直接访问搜索结果页面
        print("[+] 正在访问 Google 搜索 'tun'...")
        await page.goto("https://www.google.com/search?q=tun")
        await page.wait_for_load_state("domcontentloaded")

        # 截图初始页面
        await page.screenshot(path="google_search_tun_step1.png", full_page=True)
        print("[OK] 初始页面截图已保存为 google_search_tun_step1.png")

        # 检查是否需要人机验证
        title = await page.title()
        print(f"[i] 页面标题: {title}")

        if "验证" in title or "verify" in title.lower() or "captcha" in title.lower():
            print("[!] Google 需要人机验证，请在打开的浏览器中完成验证后按回车...")
            print("[!] 完成验证后，搜索结果会自动提取保存")
            # 保持浏览器打开，等待用户完成验证
            # 使用 asyncio.sleep 配合输入
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, input, "\n>>> 请完成人机验证后按 Enter 键继续...")

        # 等待结果加载
        await page.wait_for_load_state("networkidle")
        await page.wait_for_timeout(2000)

        # 保存页面截图
        await page.screenshot(path="google_search_tun_final.png", full_page=True)
        print("[OK] 最终页面截图已保存为 google_search_tun_final.png")

        # 保存完整 HTML
        html_content = await page.content()
        with open("google_search_tun.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        print("[OK] 完整 HTML 已保存为 google_search_tun.html")

        # 保存完整文本
        page_text = await page.inner_text("body")
        with open("google_search_tun.txt", "w", encoding="utf-8") as f:
            f.write(page_text)
        print("[OK] 完整文本已保存为 google_search_tun.txt")

        # 尝试提取搜索结果
        results = []
        selectors = [
            "h3",  # 结果标题
        ]

        print("[+] 正在提取搜索结果...")
        headings = await page.locator("h3").all()
        for heading in headings[:10]:
            try:
                title = await heading.inner_text()
                if title and len(title.strip()) > 0:
                    # 向上找父元素找链接
                    parent = heading.locator("xpath=..")
                    url = None
                    if await parent.locator("a").count() > 0:
                        url = await parent.locator("a").first.get_attribute("href")
                    results.append({"title": title.strip(), "url": url, "summary": ""})
            except Exception:
                continue

        # 保存结构化结果
        with open("google_search_tun_results.txt", "w", encoding="utf-8") as f:
            f.write(f"Google 搜索 'tun' 结果\n")
            f.write(f"代理: 127.0.0.1:7890 (Clash)\n")
            f.write("=" * 60 + "\n\n")
            for i, result in enumerate(results, 1):
                f.write(f"{i}. {result['title']}\n")
                if result['url']:
                    f.write(f"   URL: {result['url']}\n")
                f.write("\n")

        print(f"[OK] 提取到 {len(results)} 个标题，已保存为 google_search_tun_results.txt")

        # 等待一下再关闭
        await page.wait_for_timeout(2000)
        await browser.close()

        print("\n=== 完成 ===")
        print("所有文件已保存在当前目录:")
        print("- google_search_tun_step1.png  (初始页面截图)")
        print("- google_search_tun_final.png (最终结果截图)")
        print("- google_search_tun.html      (完整HTML)")
        print("- google_search_tun.txt       (完整文本)")
        print("- google_search_tun_results.txt (提取的结果)")

        return results


if __name__ == "__main__":
    asyncio.run(main())
