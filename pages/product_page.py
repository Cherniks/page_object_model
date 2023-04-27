import time

from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_book_to_basket(self):
        self.should_have_button()
        self.browser.find_element(*ProductPageLocators.BASBUT).click()
        self.solve_quiz_and_get_code()
        self.basket_price_should_book()
        self.accept_should_name_book()
        time.sleep(5)

    def should_have_button(self):
        assert self.browser.find_element(*ProductPageLocators.PRICEBASK).text, "Login form not found"

    def basket_price_should_book(self):
        assert self.browser.find_element(*ProductPageLocators.PRICEBOOK).text == self.browser.find_element(*ProductPageLocators.BASBUT).text, "The price of basket if false"

    def accept_should_name_book(self):
        assert self.browser.find_element(*ProductPageLocators.NAMEBOOK).text == self.is_element_present(*ProductPageLocators.NAMEACCEPT), "The price of accept is false"