# Код для страницы с авторизацией и регистрацией, и функции для неё
from .base_page import BasePage
from .locators import LogPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    # Собираем все проверки вместе
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Проверка на корректный url адрес
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "The 'login' not in your url"

    # Проверка, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LogPageLocators.LOG_FORM), "Login form not found"

    # Проверку, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LogPageLocators.REG_FORM), "Registred form not found"

    # Функция регистрации пользователя
    def register_new_user(self, email, password):
        self.browser.find_element(By.CSS_SELECTOR, '#id_registration-email').send_keys(email)
        self.browser.find_element(By.CSS_SELECTOR, '#id_registration-password1').send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, '#id_registration-password2').send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "[name=registration_submit]").click()
