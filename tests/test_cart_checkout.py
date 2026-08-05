from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage


def test_add_single_item_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.add_backpack()

    assert inventory_page.get_cart_count() == "1"


def test_add_multiple_items_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.add_backpack()
    inventory_page.add_bike_light()
    inventory_page.add_bolt_tshirt()

    assert inventory_page.get_cart_count() == "3"


def test_remove_item_from_product_page(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.add_backpack()
    assert inventory_page.get_cart_count() == "1"

    inventory_page.remove_backpack()

    assert inventory_page.is_cart_badge_removed()


def test_full_checkout_flow(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)
    checkout_page = CheckoutPage(logged_in_driver)

    inventory_page.add_backpack()
    inventory_page.open_cart()

    assert cart_page.verify_cart_page()
    assert cart_page.is_backpack_visible()

    cart_page.proceed_to_checkout()

    checkout_page.enter_checkout_information(
        first_name="Charvita",
        last_name="Vali",
        postal_code="33496",
    )
    checkout_page.continue_to_overview()
    checkout_page.finish_order()

    assert (
        checkout_page.get_confirmation_message()
        == "Thank you for your order!"
    )


def test_checkout_missing_last_name_shows_error(
    logged_in_driver,
):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)
    checkout_page = CheckoutPage(logged_in_driver)

    inventory_page.add_backpack()
    inventory_page.open_cart()
    cart_page.proceed_to_checkout()

    checkout_page.enter_checkout_information(
        first_name="Charvita",
        last_name="",
        postal_code="33496",
    )
    checkout_page.click_continue()

    assert "Last Name is required" in (
        checkout_page.get_error_message()
    )
