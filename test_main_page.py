from .pages.main_page import MainPage
from .pages.login_page import LoginPage

# link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
link = "http://selenium1py.pythonanywhere.com/"
login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем главную страницу
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    # Ожидаем, что в корзине нет товаров
    page.should_expect_no_items_in_basket()
    # Ожидаем, что есть текст о том что корзина пуста
    page.should_expect_message_of_empty_basket()
