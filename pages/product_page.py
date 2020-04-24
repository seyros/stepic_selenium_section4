from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_to_basket_button()

    def should_be_add_to_basket_button(self):
        """проверка на наличие кнопки добавления товара в корзину"""
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add goods to basket button is not presented!"

    def should_be_success_message_present(self):
        """проверка на наличие сообщения об успешном добавлении товара в корзину"""
        # проверка получения сообщения об успехе
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Message of success add to basket is not presented!"
        # проверка, что в сообщении об успехе есть название товара
        product_name = self.get_text_from_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_success_message = self.get_text_from_element(
            *ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE)
        success_message = self.get_text_from_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert product_name in success_message, "Product name not present in Message of success add to basket!"
        assert product_name == product_name_in_success_message, \
            "Product name in Message don`t equal product name on product page!"
        # проверка, что есть сообщение со стоимостью товаров в корзине, и она соответствует заявленной стоимости товара
        product_price = self.get_text_from_element(*ProductPageLocators.PRODUCT_PRICE)
        price_message = self.get_text_from_element(*ProductPageLocators.PRICE_MESSAGE)
        assert product_price == price_message, "Product price not equal price in basket!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_element_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def click_on_add_to_basket_button(self):
        """клик по кнопке добавления товара в корзину"""
        self.click_on_element(*ProductPageLocators.ADD_BUTTON), "Add goods to basket button is not presented!"
