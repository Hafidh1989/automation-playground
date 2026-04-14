import pytest
from playwright.sync_api import sync_playwright
from web.pages.login_page import LoginPage
from web.pages.inventory_page import InventoryPage
from web.pages.checkout_page import CheckoutPage


BASE_URL = "https://www.saucedemo.com"


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    page.goto(BASE_URL)
    yield page
    context.close()


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)