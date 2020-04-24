import pytest
import random
import string
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage


def randstring(size):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))


link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.should_be_product_page()
    page.click_on_add_to_basket_button()
    page.should_be_success_message_present()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    page.open()  # открываем страницу продукта
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    # Ожидаем, что в корзине нет товаров
    page.should_expect_no_items_in_basket()
    # Ожидаем, что есть текст о том что корзина пуста
    page.should_expect_message_of_empty_basket()


@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """
        открыть страницу регистрации
        зарегистрировать нового пользователя
        проверить, что пользователь залогинен
        """
        # открыть страницу регистрации
        page = LoginPage(browser, login_link)
        page.open()
        page.should_be_register_form()
        # зарегистрировать нового пользователя
        email = randstring(5) + '@mail.com'
        password = 'password_' + randstring(5)
        page.register_new_user(email, password)
        # проверить, что пользователь залогинен
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
        page.click_on_add_to_basket_button()
        page.should_be_success_message_present()
