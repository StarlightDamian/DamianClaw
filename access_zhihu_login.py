"""
Access Zhihu article using Playwright with manual login
URL: https://zhuanlan.zhihu.com/p/2000867285422866885
"""
from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            args=["--start-maximized"]
        )
        context = await browser.new_context(viewport=None)
        page = await context.new_page()
        page.set_default_timeout(120000)

        # Navigate to the Zhihu article
        url = "https://zhuanlan.zhihu.com/p/2000867285422866885"
        print(f"[+] Navigating to {url}")
        print("[+] Browser window opened - please log in manually if needed...")
        print("[+] Script will wait 60 seconds before extracting content...")
        await page.goto(url)
        await page.wait_for_load_state("networkidle")

        # Wait for user to complete login/captcha
        await page.wait_for_timeout(60000)

        # Extract article title
        title = "Unknown Title"
        title_element = await page.query_selector("h1.ArticleTitle-title")
        if title_element:
            title = await title_element.inner_text()
        else:
            title_element = await page.query_selector("title")
            if title_element:
                title = await title_element.inner_text()
        print(f"\n[+] Title: {title}")

        # Try different selectors for article content
        content_selectors = [
            "div.article-content",
            "div.Post-content",
            "section.zhuan-section",
            "[data-role=\"candidates\"]",
            ".RichContent"
        ]

        content_text = ""
        found_selector = None
        for selector in content_selectors:
            element = await page.query_selector(selector)
            if element:
                content_text = await element.inner_text()
                found_selector = selector
                break

        if not content_text or len(content_text) < 100:
            # Fallback: get everything from main content area
            main_element = await page.query_selector("#root") or await page.query_selector("main")
            if main_element:
                content_text = await main_element.inner_text()

        # Save results
        output_file = "zhihu_article.html"
        full_html = await page.content()
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"[+] Full HTML saved to {output_file}")

        text_output = "zhihu_article.txt"
        with open(text_output, "w", encoding="utf-8") as f:
            f.write(f"Title: {title}\n\n")
            if found_selector:
                f.write(f"Found content with selector: {found_selector}\n\n")
            f.write(content_text)
        print(f"[+] Extracted text saved to {text_output}")

        # Take screenshot
        screenshot_file = "zhihu_article.png"
        await page.screenshot(path=screenshot_file, full_page=True)
        print(f"[+] Full-page screenshot saved to {screenshot_file}")

        print("\n[+] Task completed! Check the output files above.")

        # Keep browser open for a bit for user inspection
        await page.wait_for_timeout(5000)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
