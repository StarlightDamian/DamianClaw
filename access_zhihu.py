"""
Access Zhihu article using Playwright
URL: https://zhuanlan.zhihu.com/p/2000867285422866885
"""
from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
        )
        page = await browser.new_page()
        page.set_default_timeout(30000)

        # Navigate to the Zhihu article
        url = "https://zhuanlan.zhihu.com/p/2000867285422866885"
        print(f"[+] Navigating to {url}")
        await page.goto(url)
        await page.wait_for_load_state("networkidle")
        print("[+] Page loaded")

        # Wait for content to render
        await page.wait_for_timeout(3000)

        # Extract article title and content
        title = await page.title()
        print(f"\n[+] Title: {title}")

        # Get the main article content
        article_selector = "div.article-content"
        article_element = await page.query_selector(article_selector)
        if article_element:
            content_html = await article_element.inner_html()
            content_text = await article_element.inner_text()
        else:
            # Fallback to full HTML
            content_html = await page.content()
            content_text = "Could not find article-content selector"

        # Get full HTML for inspection
        full_html = await page.content()

        # Save results
        output_file = "zhihu_article.html"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"[+] Full HTML saved to {output_file}")

        text_output = "zhihu_article.txt"
        with open(text_output, "w", encoding="utf-8") as f:
            f.write(f"Title: {title}\n\n")
            f.write(content_text)
        print(f"[+] Extracted text saved to {text_output}")

        # Take screenshot
        screenshot_file = "zhihu_article.png"
        await page.screenshot(path=screenshot_file, full_page=True)
        print(f"[+] Screenshot saved to {screenshot_file}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
