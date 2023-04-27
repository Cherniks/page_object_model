from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    # Перейдем на страницу с логином
    def go_to_login_page(self):
        # Тут *MainPageLocators.LOGIN_LINK это отдельная переменная, в которой храниться информация о том какой элемент и как нам искать
        # login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        # login_link.click()
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    # Найдем элемент на странице, передадим поиск в функцию is_element_present для корректного отображения ошибки
    def should_be_login_link(self):
        # Тут *MainPageLocators.LOGIN_LINK это отдельная переменная, в которой храниться информация о том какой элемент и как нам искать
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"