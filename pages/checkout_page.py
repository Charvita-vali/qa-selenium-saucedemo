from selenium.webdriver.common.by import By

from config import (
    CHECKOUT_COMPLETE_URL,
    CHECKOUT_STEP_TWO_URL,
)
from utils.waits import wait_for_clickable, wait_for_url, wait_for_visible


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def enter_checkout_information(
        self,
        first_name,
        last_name,
        postal_code,
    ):
        wait_for_visible(
            self.driver,
            self.FIRST_NAME,
        ).send_keys(first_name)

        wait_for_visible(
            self.driver,
            self.LAST_NAME,
        ).send_keys(last_name)

        wait_for_visible(
            self.driver,
            self.POSTAL_CODE,
        ).send_keys(postal_code)

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
