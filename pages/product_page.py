from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_to_basket_button()
        # self.should_be_login_form()
        # self.should_be_register_form()

    def should_be_add_to_basket_button(self):
        """проверка на наличие кнопки добавления товара в корзину"""
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add goods to basket button is not presented"

    def should_be_success_message_present(self):
        """проверка на наличие сообщения об успешном добавлении товара в корзину"""
        # проверка получения сообщения об успехе
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Message of success add to basket is not presented"
        # проверка, что в сообщении об успехе есть название товара
        product_name = self.get_text_from_element(*ProductPageLocators.PRODUCT_NAME)
        success_message = self.get_text_from_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert product_name in success_message, "Product name not present in Message of success add to basket"

    def click_on_add_to_basket_button(self):
        """клик по кнопке добавления товара в корзину"""
        self.click_on_element(*ProductPageLocators.ADD_BUTTON), "Add goods to basket button is not presented"
