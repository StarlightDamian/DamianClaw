"""
使用 Clash 代理访问 Google 搜索 "tun"
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
        page = await browser.new_page(
            viewport={"width": 1280, "height": 800}
        )
        # 设置超时
        page.set_default_timeout(30000)

        # 访问谷歌官网
        print("[+] 正在访问 Google...")
        await page.goto("https://www.google.com")
        await page.wait_for_load_state("networkidle")

        # 检查是否找到了搜索框
        # Google 搜索框通常有 name="q"
        try:
            # 接受 cookies 如果出现弹窗
            agree_button = page.get_by_text("I agree")
            if await agree_button.is_visible(timeout=2000):
                await agree_button.click()
                await page.wait_for_load_state("networkidle")
        except Exception:
            pass

        # 在搜索框输入 "tun" 并搜索
        print("[+] 正在输入搜索词...")
        await page.fill("[name='q']", "tun")
        await page.press("[name='q']", "Enter")

        await page.wait_for_load_state("networkidle")
        await page.wait_for_timeout(2000)

        # 提取搜索结果标题和摘要
        print("[+] 正在提取搜索结果...")
        results = []

        # 尝试多种选择器适配不同 Google HTML 结构
        selectors = [
            "div.g",  # 传统结构
            "div[data-hveid]",  # 新结构
            ".g div[lang]",  # 另一种结构
        ]

        found = False
        for selector in selectors:
            if found:
                break
            result_elements = await page.locator(selector).all()
            count = 0
            for elem in result_elements:
                try:
                    title_elem = elem.locator("h3")
                    if await title_elem.count() == 0:
                        title_elem = elem.locator("h1")
                    if await title_elem.count() == 0:
                        continue

                    title = await title_elem.first.inner_text()
                    if not title or title.strip() == "":
                        continue

                    url_elem = elem.locator("a")
                    url = None
                    if await url_elem.count() > 0:
                        url = await url_elem.first.get_attribute("href")

                    # 尝试多种摘要选择器
                    summary = ""
                    summary_selectors = [
                        "div[style*='line-height']",
                        "span.aCOpRe",
                        "div[data-content-feature]",
                        ".VwiC3b",
                    ]
                    for sum_sel in summary_selectors:
                        sum_elem = elem.locator(sum_sel)
                        if await sum_elem.count() > 0:
                            summary = await sum_elem.first.inner_text()
                            if summary:
                                break

                    results.append({
                        "title": title.strip(),
                        "url": url,
                        "summary": summary.strip()
                    })
                    count += 1
                    if count >= 10:
                        found = True
                        break
                except Exception:
                    continue

        # 如果还是没找到，尝试获取整个页面可见文本
        if not results:
            print("[!] 未找到结构化结果，尝试提取页面文本...")
            page_text = await page.inner_text("body")
            with open("google_search_tun_full.txt", "w", encoding="utf-8") as f:
                f.write(page_text)
            print("[OK] 完整页面文本已保存为 google_search_tun_full.txt")

        # 保存截图
        await page.screenshot(path="google_search_tun.png", full_page=True)
        print(f"[OK] 截图已保存为 google_search_tun.png")

        # 保存文本结果
        with open("google_search_tun_results.txt", "w", encoding="utf-8") as f:
            f.write(f"Google 搜索 \"tun\" 结果\n")
            f.write(f"代理: 127.0.0.1:7890 (Clash)\n")
            f.write("=" * 60 + "\n\n")
            for i, result in enumerate(results, 1):
                f.write(f"{i}. {result['title']}\n")
                if result['summary']:
                    f.write(f"   {result['summary']}\n")
                if result['url']:
                    f.write(f"   URL: {result['url']}\n")
                f.write("\n")

        print(f"[OK] {len(results)} 条结果已保存为 google_search_tun_results.txt")

        # 保持浏览器打开几秒钟查看结果
        await page.wait_for_timeout(5000)
        await browser.close()

        return results


if __name__ == "__main__":
    results = asyncio.run(main())
    print("\n=== 搜索结果 ===\n")
    for i, result in enumerate(results, 1):
        print(f"{i}. **{result['title']}**")
        if result['summary']:
            print(f"   {result['summary']}")
        print()
