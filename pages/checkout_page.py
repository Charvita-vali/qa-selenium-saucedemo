from selenium.webdriver.common.by import By

from config import (
    CHECKOUT_COMPLETE_URL,
    CHECKOUT_STEP_TWO_URL,
)
from utils.waits import (
    wait_for_clickable,
    wait_for_url,
    wait_for_visible,
)


class CheckoutPage:

    FIRST_NAME = (
        By.CSS_SELECTOR,
        "[data-test='firstName']",
    )
    LAST_NAME = (
        By.CSS_SELECTOR,
        "[data-test='lastName']",
    )
    POSTAL_CODE = (
        By.CSS_SELECTOR,
        "[data-test='postalCode']",
    )
    CONTINUE_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test='continue']",
    )
    FINISH_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test='finish']",
    )
    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "[data-test='error']",
    )
    COMPLETE_HEADER = (
        By.CSS_SELECTOR,
        "[data-test='complete-header']",
    )

    def __init__(self, driver):
        self.driver = driver

    def fill_field(self, locator, value):
        field = wait_for_visible(
            self.driver,
            locator,
        )
        field.clear()
        field.send_keys(value)

    def enter_checkout_information(
        self,
        first_name,
        last_name,
        postal_code,
    ):
        self.fill_field(
            self.FIRST_NAME,
            first_name,
        )
        self.fill_field(
            self.LAST_NAME,
            last_name,
        )
        self.fill_field(
            self.POSTAL_CODE,
            postal_code,
        )

    def click_continue(self):
        wait_for_clickable(
            self.driver,
            self.CONTINUE_BUTTON,
        ).click()

    def continue_to_overview(self):
        self.click_continue()

        wait_for_url(
            self.driver,
            CHECKOUT_STEP_TWO_URL,
        )

    def finish_order(self):
        wait_for_clickable(
            self.driver,
            self.FINISH_BUTTON,
        ).click()

        wait_for_url(
            self.driver,
            CHECKOUT_COMPLETE_URL,
        )

    def get_confirmation_message(self):
        return wait_for_visible(
            self.driver,
            self.COMPLETE_HEADER,
        ).text

    def get_error_message(self):
        return wait_for_visible(
            self.driver,
            self.ERROR_MESSAGE,
        ).text
