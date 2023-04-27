from selenium.webdriver.common.by import By

# Добавляем переменную, в которой будет храниться данные о том, какой элемент нужно найти и с помощью чего
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LogPageLocators():
    LOG_FORM = (By.CSS_SELECTOR, ".login_form")
    REG_FORM = (By.CSS_SELECTOR, ".register_form")

class ProductPageLocators():
    BASBUT = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICEBASK = (By.CSS_SELECTOR, ".btn.btn-default.navbar-btn.btn-cart.navbar-right.visible-xs-inline-block")
    NAMEACCEPT = (By.CSS_SELECTOR, ".alertinner")
    PRICEBOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    NAMEBOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main p")