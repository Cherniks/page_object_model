from selenium.webdriver.common.by import By

# Добавляем переменную, в которой будет храниться данные о том, какой элемент нужно найти и с помощью чего
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LogPageLocators():
    LOG_FORM = (By.CSS_SELECTOR, ".login_form")

class RegPageLocators():
    REG_FORM = (By.CSS_SELECTOR, ".register_form")