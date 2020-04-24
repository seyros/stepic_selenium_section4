from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span > a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    # REGISTER_FORM_EMAIL = (By.ID, "id_registration-email")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTER_FORM_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_FORM_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    # REGISTER_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success > div.alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success > div.alertinner")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages p > strong")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    MESSAGE_OF_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
