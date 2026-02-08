from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.allure_utils import step

class ChatPopup(BasePage):
    OPEN_CHAT_BTN = (By.CSS_SELECTOR, "button[data-testid='open-chat']")
    CHAT_PANEL = (By.CSS_SELECTOR, "div.chat-panel")

    def open_chat(self):
        self.click(*self.OPEN_CHAT_BTN)
        return self.wait_for_element(*self.CHAT_PANEL)