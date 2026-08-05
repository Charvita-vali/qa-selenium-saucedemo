from selenium.webdriver.common.by import By

from config import BASE_URL
from utils.waits import (
    wait_for_clickable,
    wait_for_url,
    wait_for_visible,
)


class LoginPage:

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(BASE_URL)

    def enter_credentials(self, username, password):
        username_field = wait_for_visible(
            self.driver,
            self.USERNAME,
        )
        password_field = wait_for_visible(
            self.driver,
            self.PASSWORD,
        )

        username_field.clear()
        username_field.send_keys(username)

        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        wait_for_clickable(
            self.driver,
            self.LOGIN_BUTTON,
        ).click()

    def login(self, username, password, expected_url):
        self.enter_credentials(username, password)
        self.click_login()
        wait_for_url(self.driver, expected_url)

    def login_without_url_wait(self, username, password):
        self.enter_credentials(username, password)
        self.click_login()

    def get_error_message(self):
        return wait_for_visible(
            self.driver,
            self.ERROR_MESSAGE,
        ).text
