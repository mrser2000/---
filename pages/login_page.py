from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.allure_utils import step

class LoginPage(BasePage):
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self, email: str, password: str):
        self.input_text(*self.EMAIL_INPUT, email)
        self.input_text(*self.PASSWORD_INPUT, password)
        self.click(*self.SUBMIT_BTN)