from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_should_havent_products(self):
        assert not self.is_element_present(*BasketPageLocators.PRODUCTS), "Products exist in basket"

    def basket_have_text_empty(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCTS_TEXT), "Page without text about empty"
        # assert self.browser.find_element(*BasketPageLocators.PRODUCTS_LINK).text.strip() == 'Your basket is empty. Continue shopping', "The page haven't text about empty"
