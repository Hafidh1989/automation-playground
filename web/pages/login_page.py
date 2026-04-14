from web.locators.login_locator import LoginLocator


class LoginPage:
    def __init__(self, page):
        self.page = page

    def input_username(self, username: str):
        self.page.locator(LoginLocator.USERNAME_INPUT).fill(username)

    def input_password(self, password: str):
        self.page.locator(LoginLocator.PASSWORD_INPUT).fill(password)

    def click_login(self):
        self.page.locator(LoginLocator.LOGIN_BUTTON).click()

    def login(self, username: str, password: str):
        self.input_username(username)
        self.input_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        return self.page.locator(LoginLocator.ERROR_MESSAGE).inner_text()
    