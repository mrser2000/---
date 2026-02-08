from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.allure_utils import step

class HomePage(BasePage):
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[data-testid='search-button']")

    CART_BUTTON = (By.CSS_SELECTOR, "a[data-testid='cart']")
    BOOKMARKS_BUTTON = (By.CSS_SELECTOR, "a[data-testid='bookmarks']")

    def open(self, url: str):
        self.driver.get(url)

    @step("Search for a book")
    def search(self, query: str):
        self.input_text(*self.SEARCH_INPUT, query)
        self.click(*self.SEARCH_BUTTON)

    @step("Open bookmarks page")
    def open_bookmarks(self):
        self.click(*self.BOOKMARKS_BUTTON)