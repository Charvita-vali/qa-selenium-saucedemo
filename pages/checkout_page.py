from selenium.webdriver.common.by import By

from config import (
    CHECKOUT_COMPLETE_URL,
    CHECKOUT_STEP_TWO_URL,
)
from utils.waits import safe_click, wait_for_url, wait_for_visible


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
        first_name_field = wait_for_visible(
            self.driver,
            self.FIRST_NAME,
        )
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = wait_for_visible(
            self.driver,
            self.LAST_NAME,
        )
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        postal_code_field = wait_for_visible(
            self.driver,
            self.POSTAL_CODE,
        )
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

    def click_continue(self):
        safe_click(
            self.driver,
            self.CONTINUE_BUTTON,
        )

    def continue_to_overview(self):
        self.click_continue()

        wait_for_url(
            self.driver,
            CHECKOUT_STEP_TWO_URL,
        )

    def finish_order(self):
        safe_click(
            self.driver,
            self.FINISH_BUTTON,
        )

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
