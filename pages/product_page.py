from .base_page import BasePage
from .locators import ProductPageLocators
import time
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_book_to_basket(self):
        self.should_have_button()
        self.browser.find_element(*ProductPageLocators.BASBUT).click()
        self.solve_quiz_and_get_code()
        self.basket_price_should_book()
        self.accept_should_name_book()
        # time.sleep(5)

    def should_have_button(self):
        assert self.is_element_present(*ProductPageLocators.BASBUT), "The button basket not found"

    def basket_price_should_book(self):
        assert self.browser.find_element(*ProductPageLocators.PRICEBOOK).text == self.browser.find_element(*ProductPageLocators.PRICEBASK).text, "The price of basket if false"

    def accept_should_name_book(self):
        assert self.browser.find_element(*ProductPageLocators.NAMEBOOK).text == self.browser.find_element(*ProductPageLocators.NAMEACCEPT).text, "The name of accept is false"

    def only_add_book_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASBUT).click()
        self.solve_quiz_and_get_code()
        assert self.is_not_element_present(*ProductPageLocators.NAMEACCEPT),  "Success message is presented, but should not be"
        # time.sleep(5)

    def without_add_book_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.NAMEACCEPT),  "Success message is presented, but should not be"
        # time.sleep(5)

    def only_add_book_to_basket_2(self):
        self.browser.find_element(*ProductPageLocators.BASBUT).click()
        self.solve_quiz_and_get_code()
        assert self.is_disappeared(*ProductPageLocators.NAMEACCEPT),  "Success message is presented, but should not be"
        # time.sleep(5)






