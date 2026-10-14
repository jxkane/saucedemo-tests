import re

from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

PASSWORD = "secret_sauce"


def test_standard_user_can_log_in(page: Page):
    login = LoginPage(page)
    login.open()
    login.log_in("standard_user", PASSWORD)

    inventory = InventoryPage(page)
    expect(page).to_have_url(re.compile(r"/inventory\.html$"))
    expect(inventory.title).to_have_text("Products")


def test_locked_out_user_sees_error(page: Page):
    login = LoginPage(page)
    login.open()
    login.log_in("locked_out_user", PASSWORD)

    expect(login.error_message).to_contain_text("locked out")
    expect(page).not_to_have_url(re.compile(r"/inventory\.html$"))

def test_wrong_password_shows_error(page: Page):
    login = LoginPage(page)
    login.open()
    login.log_in("standard_user", "ksjdun")

    expect(login.error_message).to_contain_text("do not match any user in this service")

def test_inventory_shows_six_products(page: Page):
    login = LoginPage(page)
    login.open()
    login.log_in("standard_user", PASSWORD)

    inventory = InventoryPage(page)
    expect(inventory.items).to_have_count(6)

