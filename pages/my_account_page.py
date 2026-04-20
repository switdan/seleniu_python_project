from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MyAccountPage(BasePage):
    _URL = "https://automationpractice.techwithjatin.com/my-account"

    _GREEN_BANNER = (By.XPATH, "//p[@class='alert alert-success']")
    _CUSTOMER_ACCOUNT = (By.XPATH, "//a[@title='View my customer account']")

    def green_banner_text(self) -> str:
        return self.get_text(self._GREEN_BANNER)

    def wait_for_green_banner(self):
        self.wait_for_loaded(self._GREEN_BANNER)

    def wait_for_my_account_page(self):
        self.wait_for_page(self._URL)

    def customer_account_full_name(self) -> str:
        return self.get_text(self._CUSTOMER_ACCOUNT)