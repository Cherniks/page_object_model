from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    # Перейдем на страницу с логином
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # Если тесты во время проверки упадут - мы восстановим работоспособность
        # alert = self.browser.switch_to.alert
        # alert.accept()

    # Найдем элемент на странице, передадим поиск в функцию is_element_present для корректного отображения ошибки
    def should_be_login_link(self):
        # Тут *MainPageLocators.LOGIN_LINK это отдельная переменная, в которой храниться информация о том какой элемент и как нам искать
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"