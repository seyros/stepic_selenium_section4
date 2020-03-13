from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_expect_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Items found in the basket!"

    def should_expect_message_of_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_OF_EMPTY_BASKET), \
            "Message of empty basket don`t found in the basket!"
        text_message = self.get_text_from_element(*BasketPageLocators.MESSAGE_OF_EMPTY_BASKET).strip()
        assert text_message == 'Your basket is empty. Continue shopping'


