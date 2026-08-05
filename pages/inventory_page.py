from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import CART_URL
from utils.waits import safe_click, wait_for_visible


class InventoryPage:

    BACKPACK_ADD_BUTTON = (
        By.ID,
        "add-to-cart-sauce-labs-backpack",
    )
    BIKE_LIGHT_ADD_BUTTON = (
        By.ID,
        "add-to-cart-sauce-labs-bike-light",
    )
    BOLT_TSHIRT_ADD_BUTTON = (
        By.ID,
        "add-to-cart-sauce-labs-bolt-t-shirt",
    )
    BACKPACK_REMOVE_BUTTON = (
        By.ID,
        "remove-sauce-labs-backpack",
    )
    CART_BADGE = (
        By.CLASS_NAME,
        "shopping_cart_badge",
    )
    CART_LINK = (
        By.CLASS_NAME,
        "shopping_cart_link",
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_cart_count(self, expected_count):
        self.wait.until(
            EC.text_to_be_present_in_element(
                self.CART_BADGE,
                str(expected_count),
            )
        )

    def add_backpack(self):
        safe_click(
            self.driver,
            self.BACKPACK_ADD_BUTTON,
        )
        self.wait_for_cart_count("1")

    def add_bike_light(self):
        safe_click(
            self.driver,
            self.BIKE_LIGHT_ADD_BUTTON,
        )
        self.wait_for_cart_count("2")

    def add_bolt_tshirt(self):
        safe_click(
            self.driver,
            self.BOLT_TSHIRT_ADD_BUTTON,
        )
        self.wait_for_cart_count("3")

    def remove_backpack(self):
        safe_click(
            self.driver,
            self.BACKPACK_REMOVE_BUTTON,
        )
        self.wait.until(
            EC.invisibility_of_element_located(
                self.CART_BADGE
            )
        )

    def open_cart(self):
        safe_click(
            self.driver,
            self.CART_LINK,
        )
        self.wait.until(
            EC.url_to_be(CART_URL)
        )

    def get_cart_count(self):
        return wait_for_visible(
            self.driver,
            self.CART_BADGE,
        ).text

    def is_cart_badge_removed(self):
        return self.wait.until(
            EC.invisibility_of_element_located(
                self.CART_BADGE
            )
        )
