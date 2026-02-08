from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.allure_utils import step

class BookmarksPage(BasePage):
    BOOKMARK_ITEM = (By.CSS_SELECTOR, "div.bookmark-item")

    def has_bookmarked_item(self, title_substring: str) -> bool:
        items = self.driver.find_elements(*self.BOOKMARK_ITEM)
        for it in items:
            if title_substring in it.text:
                return True
        return False