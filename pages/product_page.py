# Здесь присутствует код по обработки страницы с товаром - книгой
from .base_page import BasePage
from .locators import ProductPageLocators
import pytest

class ProductPage(BasePage):
    # Нажимаем кнопку добавления товара в корзину и проверка что есть сообщение об успешном добавлении
    def add_book_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASBUT).click()
        self.accept_should_name_book()

    # Добавление товара в корзину и проверка что цена в корзине такая же как цена книги
    def only_add_book_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASBUT).click()
        self.basket_price_should_book()

    # Проверка, что у товара есть кнопка добавления товара в корзину
    def should_have_button(self):
        assert self.is_element_present(*ProductPageLocators.BASBUT), "The button basket not found"

    # Проверка, что цена корзине соответствует цене книги
    def basket_price_should_book(self):
        assert self.browser.find_element(*ProductPageLocators.PRICEBOOK).text == self.browser.find_element(*ProductPageLocators.PRICEBASK).text, "The price of basket if false"

    # Проверка что в сообщении об успешном добавлении название соответствует названию книги
    def accept_should_name_book(self):
        assert self.browser.find_element(*ProductPageLocators.NAMEBOOK).text == self.browser.find_element(*ProductPageLocators.NAMEACCEPT).text, "The name of accept is false"

    # Проверка, что на текущей странице есть сообщение об успешном добавлении книги без реализации добавления книги
    def without_add_book_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.NAMEACCEPT),  "Success message is presented, but should not be"

    # Добавление товара в корзину и проверка что не появилось сообщение об успешном добавлении
    def only_add_book_to_basket_2(self):
        self.browser.find_element(*ProductPageLocators.BASBUT).click()
        assert not self.is_disappeared(*ProductPageLocators.NAMEACCEPT),  "Success message is presented, but should not be"






