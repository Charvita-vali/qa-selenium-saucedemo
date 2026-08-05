import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import INVENTORY_URL, PASSWORD, STANDARD_USER
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    """Start Chrome before each test and close it afterward."""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(0)

    yield browser

    browser.quit()


@pytest.fixture
def logged_in_driver(driver):
    """Log in before each test that requires an authenticated user."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(
        username=STANDARD_USER,
        password=PASSWORD,
        expected_url=INVENTORY_URL,
    )

    return driver
