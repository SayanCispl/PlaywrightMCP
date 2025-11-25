import pytest
from playwright.sync_api import sync_playwright
import time

def inspect_welcome_text():
    """Inspect the page to find the correct welcome text selector."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to DemoBlaze
        print("Navigating to DemoBlaze...")
        page.goto('https://demoblaze.com/')
        page.wait_for_load_state('domcontentloaded')
        time.sleep(2)

        # Click on Login link
        print("Clicking login link...")
        page.click("a[data-target='#logInModal']")
        time.sleep(2)

        # Enter credentials
        page.fill("#loginusername", "pavanol")
        page.fill("#loginpassword", "test@123")
        page.click("button[onclick='logIn()']")
        time.sleep(3)

        # Take screenshot to inspect
        page.screenshot(path="welcome_screen.png")

        # Try different selectors for welcome text
        selectors = [
            "div.navbar-text",
            "span.navbar-text",
            "a#nameofuser",
            "text=Welcome",
            "#nameofuser",
            ".navbar-nav span",
        ]

        for selector in selectors:
            try:
                text = page.inner_text(selector)
                print(f"✓ Found text with selector '{selector}': {text}")
            except Exception as e:
                print(f"✗ Selector '{selector}': {e}")

        # Get all elements containing "Welcome"
        print("\nSearching for 'Welcome' in page...")
        page_content = page.content()
        if "Welcome" in page_content:
            print("✓ 'Welcome' text found in page content")
            # Find the line containing Welcome
            for line in page_content.split('\n'):
                if "Welcome" in line or "pavanol" in line:
                    print(f"  {line[:150]}")

        browser.close()

if __name__ == "__main__":
    inspect_welcome_text()

