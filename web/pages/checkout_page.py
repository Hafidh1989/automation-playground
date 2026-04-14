from web.locators.checkout_locator import CheckoutLocator


class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str):
        self.page.locator(CheckoutLocator.FIRST_NAME_INPUT).fill(first_name)
        self.page.locator(CheckoutLocator.LAST_NAME_INPUT).fill(last_name)
        self.page.locator(CheckoutLocator.POSTAL_CODE_INPUT).fill(postal_code)

    def continue_checkout(self):
        self.page.locator(CheckoutLocator.CONTINUE_BUTTON).click()

    def finish_checkout(self):
        self.page.locator(CheckoutLocator.FINISH_BUTTON).click()

    def get_success_message(self) -> str:
        return self.page.locator(CheckoutLocator.COMPLETE_HEADER).inner_text()