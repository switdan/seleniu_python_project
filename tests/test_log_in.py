import pytest

from flows.log_in_flow import LogInFlow
from pages.my_account_page import MyAccountPage
from test_data.registration_data import get_login_data


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    # @pytest.mark.debug
    @pytest.mark.parametrize(
        "email, password, fullname",
        get_login_data("test_data/logged_user.csv")
    )
    def test_registration(self, driver, email, password, fullname):
        flow = LogInFlow(driver)
        flow.log_in_successfully(email, password)

        account = MyAccountPage(driver)
        account.wait_for_my_account_page()

        assert account.customer_account_full_name() == fullname