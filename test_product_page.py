from .pages.product_page import ProductPage
import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
from .pages.locators import ProductPageLocators, LogPageLocators

'''
@pytest.mark.skip
Пример параметризации:
Помечаем ссылку 7 как заведомо сломанную, она будет пропускаться при проверке
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
'''

# Проверим, что на текущей странице продукта нет сообщения об успешно добавленном товаре
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPageLocators.LINK_PROD)
    page.open()
    page.without_add_book_to_basket()

# Проверим, что после добавления товара не появилось сообщение об успешном добавлении
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.LINK_PROD)
    page.open()
    page.only_add_book_to_basket_2()

# Проверим, что на странице есть кнопка авторизации
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.LINK_PROD)
    page.open()
    page.should_be_login_link()

# Тестирование перехода на страницу с авторизацией
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.LINK_PROD)
    page.open()
    page.go_to_login_page()

# Открываем страницу товара, проверяем что есть кнопка добавления товара, переходим в корзину и проверяем что в корзине нет товаров и есть сообщение что она пуста
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.LINK_PROD)
    page.open()
    page.has_basket_btn()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_havent_products()
    basket_page.basket_have_text_empty()

# Добавляем товар в корзину и проверяем что цена корзины соответствует цене товара
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.LINK_PROD)
    page.open()
    page.only_add_book_to_basket()

# Добавляем товар в корзину и проверяем что появилось сообщение с правильным назанием добавленной книги
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.LINK_PROD)
    page.open()
    page.add_book_to_basket()

# Тестирование добавления товара пользователем
@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage():
    # Фикстура для авторизации нового пользователя и проверка что он авторизован
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, LogPageLocators.LINK_LOG)
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org", 'Stepik130')
        page.should_be_authorized_user()

    # Добавляем пользователем товар в корзину и проверяем что цена корзины соответствует цене товара
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPageLocators.LINK_PROD)
        page.open()
        page.only_add_book_to_basket()

    # Добавляем пользователем товар в корзину и проверяем что появилось сообщение с правильным назанием добавленной книги
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPageLocators.LINK_PROD)
        page.open()
        page.add_book_to_basket()



