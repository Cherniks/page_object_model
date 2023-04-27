# Главный файл тестов по проверке главной страницы
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
import pytest
from .pages.locators import MainPageLocators, LogPageLocators

# Проверка возможности регистрации для пользователя
@pytest.mark.login_guest
class TestLoginFromMainPage():
    # Проверка, что на главной странице есть кнопка авторизации
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, MainPageLocators.LINK)
        page.open()
        page.should_be_login_link()

    # Открываем главную страницу и переходим на страницу авторизации, проверяем что это страница авторизации
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, MainPageLocators.LINK)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логинать сообщение с нужным текстом
        login_page = LoginPage(browser, browser.current_url)  # Передадим на страницу логина текущую страницу
        login_page.should_be_login_page()  # Проверяем элементы на страницу, убедимся что это действительно страница авторизации и регистрации

# Проверяем, что действительно находимся на странице авторизации
def test_guest_should_find_logreg_form(browser):
    page = LoginPage(browser, LogPageLocators.LINK_LOG)
    page.open()
    page.should_be_login_page()

# Проверяем, что есть кнопка добавления в корзину, нажимаем её, убеждаемся что в корзине нет товаров и есть сообщение о пустой корзине
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasePage(browser, MainPageLocators.LINK)
    page.open()
    page.has_basket_btn()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_havent_products()
    basket_page.basket_have_text_empty()







