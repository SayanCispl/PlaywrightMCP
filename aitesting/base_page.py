from playwright.sync_api import Page

class BasePage:
    """Base page object class for common page operations."""

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        """Navigate to a URL."""
        self.page.goto(url)

    def click(self, selector: str, timeout: int = 30000):
        """Click on an element."""
        self.page.click(selector, timeout=timeout)

    def fill(self, selector: str, text: str, timeout: int = 30000):
        """Fill text in an input field."""
        self.page.fill(selector, text, timeout=timeout)

    def wait_for_selector(self, selector: str, timeout: int = 30000):
        """Wait for an element to appear."""
        self.page.wait_for_selector(selector, timeout=timeout)

    def is_visible(self, selector: str) -> bool:
        """Check if an element is visible."""
        try:
            self.page.wait_for_selector(selector, timeout=5000)
            return True
        except Exception:
            return False

    def get_text(self, selector: str) -> str:
        """Get text content of an element."""
        return self.page.inner_text(selector)

    def screenshot(self, path: str):
        """Take a screenshot."""
        self.page.screenshot(path=path)

