from selenium.webdriver.common.by import By

from config import CART_URL, CHECKOUT_STEP_ONE_URL
from utils.waits import (
    reliable_click,
    wait_for_url,
    wait_for_visible,
)


class CartPage:

    CHECKOUT_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test='checkout']",
    )
    BACKPACK_ITEM = (
        By.CSS_SELECTOR,
        "[data-test='inventory-item-name']",
    )

    def __init__(self, driver):
        self.driver = driver

    def verify_cart_page(self):
        return wait_for_url(
            self.driver,
            CART_URL,
        )

    def is_backpack_visible(self):
        return (
            wait_for_visible(
                self.driver,
                self.BACKPACK_ITEM,
            ).text
            == "Sauce Labs Backpack"
        )

    def proceed_to_checkout(self):
        reliable_click(
            self.driver,
            self.CHECKOUT_BUTTON,
        )
        wait_for_url(
            self.driver,
            CHECKOUT_STEP_ONE_URL,
        )
