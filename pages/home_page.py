from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class HomePage(BasePage):
    _URL = "https://automationpractice.techwithjatin.com/"

    _SIGN_IN_BTN = (By.XPATH, "//a[@class='login']")

    def open(self):
        self._open_url(self._URL)

    def click_sign_in(self):
        self._click(self._SIGN_IN_BTN)