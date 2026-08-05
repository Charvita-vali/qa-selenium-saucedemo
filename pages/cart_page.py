from selenium.webdriver.common.by import By

from config import CART_URL, CHECKOUT_STEP_ONE_URL
from utils.waits import wait_for_clickable, wait_for_url, wait_for_visible


class CartPage:

    CHECKOUT_BUTTON = (By.ID, "checkout")
    BACKPACK_ITEM = (
        By.XPATH,
        "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']",
    )

    def __init__(self, driver):
        self.driver = driver

    def verify_cart_page(self):
        return wait_for_url(self.driver, CART_URL)

    def is_backpack_visible(self):
        return wait_for_visible(
            self.driver,
            self.BACKPACK_ITEM,
        ).is_displayed()

    def proceed_to_checkout(self):
        wait_for_clickable(
            self.driver,
            self.CHECKOUT_BUTTON,
        ).click()

        wait_for_url(
            self.driver,
            CHECKOUT_STEP_ONE_URL,
        )
