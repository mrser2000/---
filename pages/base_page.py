from typing import Any
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout

    def wait_for_element(self, by, locator) -> Any:
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((by, locator))
            )
        except TimeoutException:
            raise AssertionError(f"Element {locator} not found")

    def click(self, by, locator):
        el = self.wait_for_element(by, locator)
        el.click()

    def input_text(self, by, locator, text: str):
        el = self.wait_for_element(by, locator)
        el.clear()
        el.send_keys(text)