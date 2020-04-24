import math
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators, BasketPageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def should_be_login_link(self):
        # Обратите внимание здесь на символ *, он указывает на то,
        # что мы передали именно пару, и этот кортеж нужно распаковать.
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_expect_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Items found in the basket!"

    def should_expect_message_of_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_OF_EMPTY_BASKET), \
            "Message of empty basket don`t found in the basket!"
        text_message = self.get_text_from_element(*BasketPageLocators.MESSAGE_OF_EMPTY_BASKET).strip()
        assert text_message == 'Your basket is empty. Continue shopping'

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """Упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый"""

        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        """Будет ждать до тех пор, пока элемент не исчезнет"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def click_on_element(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            element.click()
        except NoSuchElementException as e:
            print(e)

    def input_value_into_element(self, how, what, text):
        try:
            element = self.browser.find_element(how, what)
            element.send_keys(text)
        except Exception as e:
            print(e)

    def get_element(self, how, what):
        try:
            element = self.browser.find_element(how, what)

        except NoSuchElementException as e:
            print(e)
            return ''
        return element

    def get_text_from_element(self, how, what):
        try:
            element = self.browser.find_element(how, what).text

        except NoSuchElementException as e:
            print(e)
            return ''
        return element

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_authorized_user(self):
        assert self.is_element_present(
            *BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"
