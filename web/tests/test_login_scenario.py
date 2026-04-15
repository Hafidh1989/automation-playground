from web.data.user_data import *


def test_invalid_login_credential(login_page):
    login_page.login(
        username=INVALID_USER["username"],
        password=INVALID_USER["password"]
    )

    error_message = login_page.get_error_message()
    assert "Username and password do not match" in error_message

def test_success_login(login_page, inventory_page):
    login_page.login(
        username=STANDARD_USER["username"],
        password=STANDARD_USER["password"]
    )

    inventory_page.verify_shopping_cart_visible()


