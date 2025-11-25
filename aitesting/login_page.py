from playwright.sync_api import Page
from base_page import BasePage

class LoginPage(BasePage):
    """Page Object for DemoBlaze Login functionality."""

    # Locators
    LOGIN_LINK = "a[data-target='#logInModal']"
    USERNAME_FIELD = "#loginusername"
    PASSWORD_FIELD = "#loginpassword"
    LOGIN_BUTTON = "button[onclick='logIn()']"
    LOGOUT_LINK = "a[onclick='logOut()']"
    WELCOME_TEXT = "a#nameofuser"

    def __init__(self, page: Page):
        super().__init__(page)

    def click_login_link(self):
        """Click on the 'Log in' link in the top navigation bar."""
        self.click(self.LOGIN_LINK)

    def enter_username(self, username: str):
        """Enter username in the username field."""
        self.fill(self.USERNAME_FIELD, username)

    def enter_password(self, password: str):
        """Enter password in the password field."""
        self.fill(self.PASSWORD_FIELD, password)

    def click_login_button(self):
        """Click on the 'Log in' button."""
        self.click(self.LOGIN_BUTTON)

    def is_logout_link_visible(self) -> bool:
        """Verify that the 'Log out' link is visible."""
        return self.is_visible(self.LOGOUT_LINK)

    def get_welcome_text(self) -> str:
        """Get the welcome text displayed at the top right."""
        return self.get_text(self.WELCOME_TEXT)

    def click_logout_link(self):
        """Click on the 'Log out' link."""
        self.click(self.LOGOUT_LINK)

    def is_login_link_visible(self) -> bool:
        """Verify that the 'Log in' link is visible."""
        return self.is_visible(self.LOGIN_LINK)

