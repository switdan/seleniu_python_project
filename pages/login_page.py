from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    _URL = "https://automationpractice.techwithjatin.com/login?back=my-account"

    _CREATE_ACCOUNT_EMAIL_INPUT = (By.ID, "email_create")
    _CREATE_ACCOUNT_BTN = (By.XPATH, "//button[@id='SubmitCreate']/span/i")
    _RED_BANNER = (By.XPATH, "//div[@class='alert alert-danger']")

    _SIGN_IN_EMAIL_INPUT = (By.ID, "email")
    _SIGN_IN_PASSWORD_INPUT = (By.ID, "passwd")
    _SIGN_IN_BTN = (By.ID, "SubmitLogin")


    def open(self):
        self._open_url(self._URL)

    def type_new_account_email(self, text: str):
        self._type(self._CREATE_ACCOUNT_EMAIL_INPUT, text)

    def click_create_account_btn(self):
        self._click(self._CREATE_ACCOUNT_BTN)

    def red_banner_text(self) -> str:
        return self.get_text(self._RED_BANNER)

    def type_existed_email(self, text: str):
        self._type(self._SIGN_IN_EMAIL_INPUT, text)

    def type_existed_password(self, text: str):
        self._type(self._SIGN_IN_PASSWORD_INPUT, text)

    def click_sign_in_btn(self):
        self._click(self._SIGN_IN_BTN)