---
name: browser-automation
description: General browser automation with two-tier approach - connects to existing Chrome via Chrome DevTools Protocol (CDP) first to avoid opening new browser and bypass human verification, falls back to generating DOM-specific Python Playwright scripts quickly when CDP is unavailable. Use this skill whenever you need to automate browser interactions, access web pages, scrape content, or interact with websites - especially when the user already has Chrome open.
---

# Browser Automation

General-purpose browser automation that prioritizes connecting to an **already open Chrome browser** via Chrome DevTools Protocol (CDP) to avoid opening a new browser and bypass human verification (CAPTCHAs, logins that have already been completed). Falls back to generating DOM-specific Python Playwright scripts when CDP connection fails.

## Strategy

1. **Always try CDP first**: Check if Chrome is running with remote debugging enabled and connect
2. **If CDP fails, use Playwright**: Generate a full Python script with specific DOM selectors from natural language description
3. **Speed优先**: Return results as fast as possible while maintaining quality

## CDP Connection Flow (Preferred Path)

### Prerequisites for CDP

- Chrome must be running with remote debugging enabled:
  1. Quit Chrome completely
  2. Start Chrome from command line:
     ```bash
     "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
     ```
  3. Or enable via `chrome://inspect/#remote-debugging` in Chrome settings

### CDP Commands

All commands use the bundled wrapper script that reuses chrome-cdp functionality:

```bash
# List open pages with target IDs
node .claude/skills/browser-automation/scripts/cdp-wrapper.mjs list

# Navigate target to URL
node .claude/skills/browser-automation/scripts/cdp-wrapper.mjs nav <target> <url>

# Get accessibility snapshot (compact semantic structure)
node .claude/skills/browser-automation/scripts/cdp-wrapper.mjs snap <target>

# Get full page HTML or HTML within CSS selector
node .claude/skills/browser-automation/scripts/cdp-wrapper.mjs html <target> [selector]

# Click element by CSS selector
node .claude/skills/browser-automation/scripts/cdp-wrapper.mjs click <target> <selector>

# Type text into focused element
node .claude/skills/browser-automation/scripts/cdp-wrapper.mjs type <target> <text>

# Take viewport screenshot
node .claude/skills/browser-automation/scripts/cdp-wrapper.mjs shot <target> [file]

# Evaluate JavaScript in page context
node .claude/skills/browser-automation/scripts/cdp-wrapper.mjs eval <target> <expression>
```

### CDP Advantages

- **Reuses existing session**: If the user already has Chrome open and has already completed login/human verification, we can just connect and continue
- **No new browser window**: Faster, doesn't disrupt user workflow
- **Avoids re-verification**: Persistent daemon keeps session open after first approval
- **Daemon auto-cleanup**: Daemons exit after 20 minutes of inactivity

## Playwright Fallback Flow

When CDP connection fails (no Chrome with remote debugging available):

1. You receive the user's natural language description of the task
2. Analyze the target page structure (if known)
3. Generate a **full, runnable Python Playwright script** with:
   - Precise DOM selectors based on the page structure
   - Explicit action sequence matching the user's request
   - Proper waits and error handling
   - Screenshot output for verification
4. Execute the generated script

### Generated Script Template

```python
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            # When called from external-network skill, proxy config is injected here:
            # proxy={"server": "http://127.0.0.1:7890"}
        )
        page = await browser.new_page()
        page.set_default_timeout(30000)

        await page.goto("https://example.com")
        await page.wait_for_load_state("networkidle")

        # --- YOUR DOM-SPECIFIC CODE HERE ---
        # Example:
        # await page.fill("#username", "your_username");
        # await page.fill("#password", "your_password");
        # await page.click("button[type='submit']");
        # await page.wait_for_load_state("networkidle");
        # --- END OF CUSTOM CODE ---

        # Capture result
        await page.screenshot(path="result.png", full_page=True);
        print("Task completed, screenshot saved to result.png");

        await browser.close();

if __name__ == "__main__":
    import asyncio
    asyncio.run(main());
```

### Script Generation Principles

- **Strong DOM dependency**: Every interaction uses precise, specific selectors (id, class, attribute combinations) based on the actual page structure - no fuzzy matching
- **Explicit waiting**: Always wait for page load after navigation and significant actions
- **Full screenshot**: Always capture a full-page screenshot at the end for verification
- **Full executable script**: Generate complete, runnable code that doesn't require user modification

## When to Use Which Path

| Scenario | Preferred Path | Reason |
|----------|----------------|--------|
| User already has Chrome open with the site | CDP | Reuses existing session, bypasses login/human verification |
| Site requires human interaction/captcha first | CDP | User completes verification manually, automation continues |
| Fresh browsing session needed | Playwright | Clean environment, no interference |
| CDP connection fails/configured | Playwright | Fallback ensures task completes |

## Integration with Other Skills

This skill is designed to be called by other skills that need browser access with specific constraints. For example:

- `external-network`: Adds fixed Clash proxy configuration before calling this skill
- Any other skill that needs browser automation can reuse this

The calling skill is responsible for any additional configuration (like proxy settings) that should be injected into the Playwright script when fallback is used.
