import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import INVENTORY_URL, PASSWORD, STANDARD_USER
from pages.login_page import LoginPage


@pytest.fixture
def driver(request):
    """Start Chrome before each test and close it afterward."""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(0)

    yield browser

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("test-results", exist_ok=True)

        screenshot_path = (
            f"test-results/{request.node.name}.png"
        )
        source_path = (
            f"test-results/{request.node.name}.html"
        )

        browser.save_screenshot(screenshot_path)

        with open(source_path, "w", encoding="utf-8") as file:
            file.write(browser.page_source)

        print(f"Failure URL: {browser.current_url}")
        print(f"Failure title: {browser.title}")

    browser.quit()


@pytest.fixture
def logged_in_driver(driver):
    """Log in before each test that requires authentication."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(
        username=STANDARD_USER,
        password=PASSWORD,
        expected_url=INVENTORY_URL,
    )

    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
