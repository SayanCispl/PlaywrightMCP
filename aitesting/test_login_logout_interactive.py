import pytest
from playwright.sync_api import sync_playwright
import time

def test_demoblaze_login_logout():
    """Test login and logout flow on DemoBlaze."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to DemoBlaze
        print("Step 1: Navigate to DemoBlaze")
        page.goto('https://demoblaze.com/')
        page.wait_for_load_state('domcontentloaded')
        time.sleep(2)

        # Step 1: Click on Login link
        print("Step 2: Click on Login link")
        login_link = page.query_selector("a[data-target='#logInModal']")
        if login_link:
            page.click("a[data-target='#logInModal']")
            time.sleep(2)
            print("✓ Login link clicked")
        else:
            print("✗ Login link not found")
            page.screenshot(path="debug_login_link.png")

        # Step 2: Enter username
        print("Step 3: Enter username")
        try:
            page.fill("#loginusername", "pavanol")
            print("✓ Username entered")
        except Exception as e:
            print(f"✗ Failed to enter username: {e}")
            page.screenshot(path="debug_username.png")

        # Step 3: Enter password
        print("Step 4: Enter password")
        try:
            page.fill("#loginpassword", "test@123")
            print("✓ Password entered")
        except Exception as e:
            print(f"✗ Failed to enter password: {e}")
            page.screenshot(path="debug_password.png")

        # Step 4: Click login button
        print("Step 5: Click login button")
        try:
            page.click("button[onclick='logIn()']")
            time.sleep(3)
            print("✓ Login button clicked")
        except Exception as e:
            print(f"✗ Failed to click login button: {e}")
            page.screenshot(path="debug_login_button.png")

        # Step 5: Verify logout link is visible
        print("Step 6: Verify logout link is visible")
        try:
            page.wait_for_selector("a[onclick='logOut()']", timeout=10000)
            print("✓ Logout link is visible")
        except Exception as e:
            print(f"✗ Logout link not visible: {e}")
            page.screenshot(path="debug_logout.png")

        # Step 6: Verify welcome text
        print("Step 7: Verify welcome text")
        try:
            welcome_text = page.inner_text("div.navbar-text")
            print(f"Welcome text found: {welcome_text}")
            assert "Welcome pavanol" in welcome_text, f"Expected 'Welcome pavanol' in '{welcome_text}'"
            print("✓ Welcome pavanol verified")
        except Exception as e:
            print(f"✗ Welcome text verification failed: {e}")
            page.screenshot(path="debug_welcome.png")

        # Step 7: Click logout link
        print("Step 8: Click logout link")
        try:
            page.click("a[onclick='logOut()']")
            time.sleep(2)
            print("✓ Logout link clicked")
        except Exception as e:
            print(f"✗ Failed to click logout link: {e}")
            page.screenshot(path="debug_logout_click.png")

        # Step 8: Verify login link is visible again
        print("Step 9: Verify login link is visible again")
        try:
            page.wait_for_selector("a[data-target='#logInModal']", timeout=10000)
            print("✓ Login link is visible again")
        except Exception as e:
            print(f"✗ Login link not visible after logout: {e}")
            page.screenshot(path="debug_login_again.png")

        browser.close()
        print("\n✓ All tests passed!")

if __name__ == "__main__":
    test_demoblaze_login_logout()

