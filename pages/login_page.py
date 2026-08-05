from selenium.webdriver.common.by import By

from config import BASE_URL
from utils.waits import wait_for_clickable, wait_for_url


class LoginPage:

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(BASE_URL)

    def login(self, username, password, expected_url):
        wait_for_clickable(self.driver, self.USERNAME).send_keys(username)
        wait_for_clickable(self.driver, self.PASSWORD).send_keys(password)
        wait_for_clickable(self.driver, self.LOGIN_BUTTON).click()

        wait_for_url(self.driver, expected_url)
