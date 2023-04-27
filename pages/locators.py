from selenium.webdriver.common.by import By

# Добавляем переменную, в которой будет храниться данные о том, какой элемент нужно найти и с помощью чего
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LogPageLocators():
    LOG_FORM = (By.CSS_SELECTOR, ".login_form")
    REG_FORM = (By.CSS_SELECTOR, ".register_form")

class ProductPageLocators():
    BASBUT = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICEBASK = (By.CSS_SELECTOR, ".alert-info p strong")
    NAMEACCEPT = (By.CSS_SELECTOR, "#messages .alert .alertinner strong")
    NAMEBOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICEBOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main p.price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    PRODUCTS_TEXT = (By.CSS_SELECTOR, '#content_inner p')
    PRODUCTS = (By.CSS_SELECTOR, '.basket-title.hidden-xs')





