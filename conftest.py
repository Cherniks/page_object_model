import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language of website")

@pytest.fixture(scope="function")
def browser(request):
    request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()