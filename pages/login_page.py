from playwright.sync_api import Page


class LoginPage:
    """The Sauce Demo login screen.

    Tests talk to this class instead of using selectors directly, so if the
    page changes, only this file needs updating.
    """

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator('[data-test="username"]')
        self.password = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')

    def open(self):
        self.page.goto("/")

    def log_in(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
