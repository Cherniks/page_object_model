# Главный файл тестов по проверке главной страницы
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = 'https://selenium1py.pythonanywhere.com/accounts/login/'
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логинать сообщение с нужным текстом
    login_page = LoginPage(browser, browser.current_url) # Передадим на страницу логина текущую страницу
    login_page.should_be_login_page() # Проверяем элементы на страницу, убедимся что это действительно страница авторизации и регистрации

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_find_logreg_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()