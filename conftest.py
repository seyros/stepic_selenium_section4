import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Preferred language for site: ru, en, fr, etc...")


@pytest.fixture(scope="function")
def get_browser(request):
    browser_name = request.config.getoption("browser_name").lower()
    user_language = request.config.getoption("language").lower()
    # TODO: вставить проверку валидности языка: https://coderoad.ru/32773035/Список-кодов-языков-ISO639-1-в-Python
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        # browser = webdriver.Chrome(executable_path='C:\chromedriver.exe') # for my home Windows
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        # browser = webdriver.Firefox(executable_path='C:\geckodriver.exe')  # for my home Windows
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser, user_language
    print("\nquit browser..")
    browser.quit()
