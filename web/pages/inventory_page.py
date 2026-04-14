from web.locators.inventory_locator import InventoryLocator
from playwright.sync_api import expect


class InventoryPage:
    def __init__(self, page):
        self.page = page

    def verify_inventory_page_loaded(self):
        title = self.page.locator(InventoryLocator.TITLE).inner_text()
        assert title == "Products", f"Expected 'Products' but got '{title}'"

    def add_backpack_to_cart(self):
        self.page.locator(InventoryLocator.ADD_TO_CART_BACKPACK).click()

    def add_bike_light_to_cart(self):
        self.page.locator(InventoryLocator.ADD_TO_CART_BIKE_LIGHT).click()

    def get_cart_badge_count(self) -> str:
        return self.page.locator(InventoryLocator.SHOPPING_CART_BADGE).inner_text()

    def open_cart(self):
        self.page.locator(InventoryLocator.SHOPPING_CART_LINK).click()

    def click_checkout(self):
        self.page.locator(InventoryLocator.CHECKOUT_BUTTON).click()

    def verify_shopping_cart_visible (self):
        expect(self.page.locator(InventoryLocator.SHOPPING_CART_LINK)).to_be_visible()
        
        