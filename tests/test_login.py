from config import (
    INVALID_PASSWORD,
    INVENTORY_URL,
    LOCKED_OUT_USER,
    PASSWORD,
    STANDARD_USER,
)
from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(
        username=STANDARD_USER,
        password=PASSWORD,
        expected_url=INVENTORY_URL,
    )

    assert driver.current_url == INVENTORY_URL


def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login_without_url_wait(
        username=STANDARD_USER,
        password=INVALID_PASSWORD,
    )

    assert "Username and password do not match" in (
        login_page.get_error_message()
    )


def test_locked_out_user(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login_without_url_wait(
        username=LOCKED_OUT_USER,
        password=PASSWORD,
    )

    assert "Sorry, this user has been locked out" in (
        login_page.get_error_message()
    )
