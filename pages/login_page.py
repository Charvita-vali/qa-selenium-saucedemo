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

    def login(self, username, password, expected_url):
        wait_for_clickable(self.driver, self.USERNAME).send_keys(username)
        wait_for_clickable(self.driver, self.PASSWORD).send_keys(password)
        wait_for_clickable(self.driver, self.LOGIN_BUTTON).click()

        wait_for_url(self.driver, expected_url)

    def login_without_url_wait(self, username, password):
        wait_for_clickable(self.driver, self.USERNAME).send_keys(username)
        wait_for_clickable(self.driver, self.PASSWORD).send_keys(password)
        wait_for_clickable(self.driver, self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return wait_for_visible(
            self.driver,
            self.ERROR_MESSAGE,
        ).text
