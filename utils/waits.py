from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


DEFAULT_TIMEOUT = 20


def wait_for_visible(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

def wait_for_clickable(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    
def wait_for_present(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )


def wait_for_invisible(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located(locator)
    )


def wait_for_text(driver, locator, text, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element(locator, str(text))
    )


def wait_for_value(driver, locator, value, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element_value(locator, value)
    )


def wait_for_url(driver, expected_url, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        EC.url_to_be(expected_url)
    )


def reliable_click(driver, locator, timeout=DEFAULT_TIMEOUT):
    element = wait_for_present(driver, locator, timeout)

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        element,
    )

    driver.execute_script(
        "arguments[0].click();",
        element,
    )


def set_input_value(driver, locator, value, timeout=DEFAULT_TIMEOUT):
    element = wait_for_visible(driver, locator, timeout)

    driver.execute_script(
        """
        const element = arguments[0];
        const value = arguments[1];
        const setter = Object.getOwnPropertyDescriptor(
            window.HTMLInputElement.prototype,
            'value'
        ).set;

        setter.call(element, value);
        element.dispatchEvent(
            new Event('input', { bubbles: true })
        );
        element.dispatchEvent(
            new Event('change', { bubbles: true })
        );
        """,
        element,
        value,
    )

    wait_for_value(driver, locator, value, timeout)
