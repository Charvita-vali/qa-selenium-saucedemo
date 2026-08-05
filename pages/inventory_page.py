from selenium.webdriver.common.by import By

from config import CART_URL
from utils.waits import (
    reliable_click,
    wait_for_invisible,
    wait_for_text,
    wait_for_url,
    wait_for_visible,
)


class InventoryPage:

    BACKPACK_ADD_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test='add-to-cart-sauce-labs-backpack']",
    )
    BIKE_LIGHT_ADD_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test='add-to-cart-sauce-labs-bike-light']",
    )
    BOLT_TSHIRT_ADD_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']",
    )
    BACKPACK_REMOVE_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test='remove-sauce-labs-backpack']",
    )
    CART_BADGE = (
        By.CSS_SELECTOR,
        "[data-test='shopping-cart-badge']",
    )
    CART_LINK = (
        By.CSS_SELECTOR,
        "[data-test='shopping-cart-link']",
    )

    def __init__(self, driver):
        self.driver = driver

    def add_backpack(self):
        reliable_click(
            self.driver,
            self.BACKPACK_ADD_BUTTON,
        )
        wait_for_text(
            self.driver,
            self.CART_BADGE,
            "1",
        )

    def add_bike_light(self):
        reliable_click(
            self.driver,
            self.BIKE_LIGHT_ADD_BUTTON,
        )
        wait_for_text(
            self.driver,
            self.CART_BADGE,
            "2",
        )

    def add_bolt_tshirt(self):
        reliable_click(
            self.driver,
            self.BOLT_TSHIRT_ADD_BUTTON,
        )
        wait_for_text(
            self.driver,
            self.CART_BADGE,
            "3",
        )

    def remove_backpack(self):
        reliable_click(
            self.driver,
            self.BACKPACK_REMOVE_BUTTON,
        )
        wait_for_invisible(
            self.driver,
            self.CART_BADGE,
        )

    def open_cart(self):
        reliable_click(
            self.driver,
            self.CART_LINK,
        )
        wait_for_url(
            self.driver,
            CART_URL,
        )

    def get_cart_count(self):
        return wait_for_visible(
            self.driver,
            self.CART_BADGE,
        ).text

    def is_cart_badge_removed(self):
        return wait_for_invisible(
            self.driver,
            self.CART_BADGE,
        )       
