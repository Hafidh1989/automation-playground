from web.datas.user_data import STANDARD_USER


def test_user_can_complete_checkout(login_page, inventory_page, checkout_page):
    login_page.login(
        username=STANDARD_USER["username"],
        password=STANDARD_USER["password"]
    )

    inventory_page.verify_inventory_page_loaded()

    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()

    assert inventory_page.get_cart_badge_count() == "2", "Cart badge count should be 2"

    inventory_page.open_cart()
    inventory_page.click_checkout()

    checkout_page.fill_checkout_information(
        first_name="Ahmad",
        last_name="Khoiri",
        postal_code="15417"
    )
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    success_message = checkout_page.get_success_message()
    assert success_message == "Thank you for your order!", \
        f"Expected success message not found. Got: {success_message}"