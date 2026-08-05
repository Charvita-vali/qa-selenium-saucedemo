from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


DEFAULT_TIMEOUT = 15


def wait_for_visible(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Wait until an element is visible and return it."""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_for_clickable(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Wait until an element is clickable and return it."""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def wait_for_invisible(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Wait until an element disappears."""
    return WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located(locator)
    )


def wait_for_text(driver, locator, text, timeout=DEFAULT_TIMEOUT):
    """Wait until an element contains the expected text."""
    return WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element(locator, str(text))
    )


def wait_for_url(driver, expected_url, timeout=DEFAULT_TIMEOUT):
    """Wait until the browser reaches the expected URL."""
    return WebDriverWait(driver, timeout).until(
        EC.url_to_be(expected_url)
    )    driver.execute_script(
        "arguments[0].click();",
        element,
    )


def wait_for_url(driver, expected_url, timeout=DEFAULT_TIMEOUT):
    """Wait until the browser reaches the expected URL."""
    return WebDriverWait(driver, timeout).until(
        EC.url_to_be(expected_url)
    )
