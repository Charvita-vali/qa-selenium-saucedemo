from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
        self.wait = WebDriverWait(driver, 15)

    def fill_field(self, locator, value):
        field = wait_for_visible(
            self.driver,
            locator,
        )

        field.click()
        field.clear()

        if value:
            field.send_keys(value)

            self.wait.until(
                EC.text_to_be_present_in_element_value(
                    locator,
                    value,
                )
            )

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
