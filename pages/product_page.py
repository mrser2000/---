from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.allure_utils import step

class ProductPage(BasePage):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[data-testid='add-to-cart']")
    ADD_TO_BOOKMARK_BTN = (By.CSS_SELECTOR, "button[data-testid='add-to-bookmark']")
    BOOK_INFO_SECTION = (By.CSS_SELECTOR, "div.product-info")

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def add_to_bookmark(self):
        self.click(*self.ADD_TO_BOOKMARK_BTN)

    def view_info(self):
        return self.wait_for_element(*self.BOOK_INFO_SECTION)