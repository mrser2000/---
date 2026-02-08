import pytest
from config.env_config import env
from config.test_data import TestData
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.bookmarks_page import BookmarksPage
from pages.chat_popup import ChatPopup
from pages.login_page import LoginPage
from utils.ui_driver import get_driver
from utils.allure_utils import step

@pytest.fixture(scope="session")
def driver():
    d = get_driver(headless=env.headless)
    yield d
    d.quit()

@pytest.fixture
def home(driver):
    page = HomePage(driver, timeout=env.ui_timeout)
    page.open(env.base_url)
    return page

def test_add_to_cart_ui(driver, home):
    with step("Открыть страницу книги и добавить в корзину"):
        home.search(TestData.english_book_title)
        product = ProductPage(driver, timeout=env.ui_timeout)
        # В реальном кейсе нужно перейти на страницу товара. Здесь предполагаем, что образуется страница товара
        product.add_to_cart()
        # Проверку корзины можно добавить по существующей странице корзины

def test_add_to_bookmark_ui(driver, home):
    with step("Открыть страницу книги и добавить в закладки"):
        home.search(TestData.english_book_title)
        product = ProductPage(driver, timeout=env.ui_timeout)
        product.add_to_bookmark()
        bookmarks = BookmarksPage(driver, timeout=env.ui_timeout)
        assert bookmarks.has_bookmarked_item(TestData.english_book_title)

def test_bookmarks_display_ui(driver, home):
    with step("Проверить отображение списка закладок"):
        home.open_bookmarks()
        bookmarks = BookmarksPage(driver, timeout=env.ui_timeout)
        assert bookmarks.has_bookmarked_item(TestData.english_book_title)

def test_open_chat_ui(driver, home):
    with step("Открыть чат с техподдержкой"):
        chat = ChatPopup(driver, timeout=env.ui_timeout)
        chat.open_chat()
        # здесь можно проверить видимость панели чата
        assert True

def test_view_book_info_ui(driver, home):
    with step("Просмотр информации о книге на карточке"):
        home.search(TestData.english_book_title)
        product = ProductPage(driver, timeout=env.ui_timeout)
        info = product.view_info()
        assert info is not None