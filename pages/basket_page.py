# Данный код нужен для обработки страницы с добавленными товарами
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    # Проверка на то что корзина пуста, если там находятся товары то вызываем ошибку
    def basket_should_havent_products(self):
        assert not self.is_element_present(*BasketPageLocators.PRODUCTS), "Products exist in basket"

    # Проверка на то, что на странице есть текст, в котором говрится, что корзина пуста
    def basket_have_text_empty(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCTS_TEXT), "Page without text about empty"
