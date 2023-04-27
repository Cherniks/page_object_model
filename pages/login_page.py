from .base_page import BasePage
from .locators import LogPageLocators
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "The 'login' not in your url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LogPageLocators.LOG_FORM), "Login form not found"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LogPageLocators.REG_FORM), "Registred form not found"

    # Функция регистрации пользователя
    def register_new_user(self, email, password):
        # link = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
        self.browser.find_element(By.CSS_SELECTOR, '#id_registration-email').send_keys(email)
        self.browser.find_element(By.CSS_SELECTOR, '#id_registration-password1').send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, '#id_registration-password2').send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "[name=registration_submit]").click()
