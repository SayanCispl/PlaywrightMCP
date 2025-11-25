import pytest
from playwright.sync_api import sync_playwright
import sys
import os

# Add the aitesting directory to the path for imports
sys.path.insert(0, os.path.dirname(__file__))

from base_page import BasePage
from login_page import LoginPage


@pytest.fixture
def browser():
    """Create a browser instance for the test."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    """Create a page instance for the test."""
    page = browser.new_page()
    yield page
    page.close()


def test_demoblaze_login_logout(page):
    """
    Test DemoBlaze login and logout flow using Page Object Model.

    Test Steps:
    1. Navigate to DemoBlaze
    2. Click on the "Log in" link
    3. Enter "pavanol" as username
    4. Enter "test@123" as password
    5. Click "Log in" button
    6. Verify "Log out" link is visible
    7. Verify "Welcome pavanol" text appears
    8. Click "Log out" link
    9. Verify "Log in" link is visible again
    """
    # Initialize login page object
    login_page = LoginPage(page)

    # Step 1: Navigate to DemoBlaze
    print("\n✓ Step 1: Navigate to DemoBlaze")
    login_page.navigate('https://demoblaze.com/')
    page.wait_for_load_state('domcontentloaded')

    # Step 2: Click on Login link
    print("✓ Step 2: Click on the 'Log in' link")
    login_page.click_login_link()
    page.wait_for_selector(LoginPage.USERNAME_FIELD, timeout=10000)

    # Step 3: Enter username
    print("✓ Step 3: Enter username 'pavanol'")
    login_page.enter_username("pavanol")

    # Step 4: Enter password
    print("✓ Step 4: Enter password 'test@123'")
    login_page.enter_password("test@123")

    # Step 5: Click Log in button
    print("✓ Step 5: Click the 'Log in' button")
    login_page.click_login_button()
    page.wait_for_selector(LoginPage.LOGOUT_LINK, timeout=10000)

    # Step 6: Verify logout link is visible
    print("✓ Step 6: Verify that the 'Log out' link is visible")
    assert login_page.is_logout_link_visible(), "Log out link should be visible after login"

    # Step 7: Verify welcome text
    print("✓ Step 7: Verify that 'Welcome pavanol' appears at the top right")
    welcome_text = login_page.get_welcome_text()
    assert "Welcome pavanol" in welcome_text, f"Expected 'Welcome pavanol' but got '{welcome_text}'"
    print(f"  Welcome text verified: {welcome_text}")

    # Step 8: Click Log out link
    print("✓ Step 8: Click the 'Log out' link")
    login_page.click_logout_link()
    page.wait_for_selector(LoginPage.LOGIN_LINK, timeout=10000)

    # Step 9: Verify login link is visible again
    print("✓ Step 9: Verify that the 'Log in' link is visible again after logout")
    assert login_page.is_login_link_visible(), "Log in link should be visible after logout"

    print("\n✓✓✓ All tests passed successfully! ✓✓✓\n")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])

