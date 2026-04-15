from web.data.user_data import STANDARD_USER


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
    
def test_user_can_remove_item_from_chart(login_page, inventory_page, checkout_page):
    login_page.login(
        username=STANDARD_USER["username"],
        password=STANDARD_USER["password"]
    )

    inventory_page.verify_inventory_page_loaded()

    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()

    assert inventory_page.get_cart_badge_count() == "2", "Cart badge count should be 2"
    inventory_page.open_cart()
    inventory_page.remove_all_item_from_chart()

    inventory_page.check_if_chart_is_empty()

def test_checkout_without_first_name(login_page, inventory_page, checkout_page):
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
        first_name="",
        last_name="Khoiri",
        postal_code="15417"
    )
    checkout_page.continue_checkout()
    checkout_page.verify_error_message_visible("Error: First Name is required")

    def test_checkout_without_last_name(login_page, inventory_page, checkout_page):
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
            first_name="ahmad",
            last_name="",
            postal_code="15417"
        )
        checkout_page.continue_checkout()
        checkout_page.verify_error_message_visible("Error: Last Name is required")

def test_checkout_without_post_code(login_page, inventory_page, checkout_page):
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
            first_name="ahmad",
            last_name="hafidh",
            postal_code=""
        )
        checkout_page.continue_checkout()
        checkout_page.verify_error_message_visible("Error: Postal Code is required")