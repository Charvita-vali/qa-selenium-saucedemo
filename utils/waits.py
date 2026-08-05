from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


DEFAULT_TIMEOUT = 10


def wait_for_visible(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Wait until an element is visible, then return it."""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_for_clickable(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Wait until an element is clickable, then return it."""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def wait_for_url(driver, expected_url, timeout=DEFAULT_TIMEOUT):
    """Wait until the browser reaches the expected URL."""
    return WebDriverWait(driver, timeout).until(
        EC.url_to_be(expected_url)
    )
