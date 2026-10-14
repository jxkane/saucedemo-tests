from playwright.sync_api import Page


class InventoryPage:
    """The product list shown after a successful login."""

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.items = page.locator('[data-test="inventory-item"]')
