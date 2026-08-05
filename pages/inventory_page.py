from selenium.webdriver.common.by import By

from utils.waits import wait_for_clickable, wait_for_visible


class InventoryPage:

    BACKPACK_ADD_BUTTON = (
        By.ID,
        "add-to-cart-sauce-labs-backpack",
    )
    BIKE_LIGHT_ADD_BUTTON = (
        By.ID,
        "add-to-cart-sauce-labs-bike-light",
    )
    BOLT_TSHIRT_ADD_BUTTON = (
        By.ID,
        "add-to-cart-sauce-labs-bolt-t-shirt",
    )
    BACKPACK_REMOVE_BUTTON = (
        By.ID,
        "remove-sauce-labs-backpack",
    )
    CART_BADGE = (
        By.CLASS_NAME,
        "shopping_cart_badge",
    )
    CART_LINK = (
        By.CLASS_NAME,
        "shopping_cart_link",
    )

    def __init__(self, driver):
        self.driver = driver

    def add_backpack(self):
        wait_for_clickable(
            self.driver,
            self.BACKPACK_ADD_BUTTON,
        ).click()

    def add_bike_light(self):
        wait_for_clickable(
            self.driver,
            self.BIKE_LIGHT_ADD_BUTTON,
        ).click()

    def add_bolt_tshirt(self):
        wait_for_clickable(
            self.driver,
            self.BOLT_TSHIRT_ADD_BUTTON,
        ).click()

    def remove_backpack(self):
        wait_for_clickable(
            self.driver,
            self.BACKPACK_REMOVE_BUTTON,
        ).click()

    def open_cart(self):
        wait_for_clickable(
            self.driver,
            self.CART_LINK,
        ).click()

    def get_cart_count(self):
        return wait_for_visible(
            self.driver,
            self.CART_BADGE,
        ).text

    def is_cart_badge_removed(self):
        return len(
            self.driver.find_elements(*self.CART_BADGE)
        ) == 0
