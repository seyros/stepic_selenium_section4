import pytest
from .pages.product_page import ProductPage


# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
# link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

@pytest.mark.parametrize('link', [
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
       pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                    marks=pytest.mark.xfail(reason='bug #333')),
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_product_page()
    page.click_on_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_success_message_present()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу продукта
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    # Ожидаем, что в корзине нет товаров
    page.should_expect_no_items_in_basket()
    # Ожидаем, что есть текст о том что корзина пуста
    page.should_expect_message_of_empty_basket()
