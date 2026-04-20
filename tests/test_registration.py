import pytest

from flows.registration_flow import RegistrationFlow
from test_data.registration_data import RegistrationDataGenerator
from test_data.expected_messages import ExpectedMessages

class TestPositiveScenarios:

    @pytest.mark.registration
    @pytest.mark.positive
    @pytest.mark.debug
    def test_registration(self, driver):
        data = RegistrationDataGenerator()
        flow = RegistrationFlow(driver)

        flow.start_registration(data.email)
        assert flow.create_an_account_page.get_h1_title() == ExpectedMessages.REGISTRATION_HEADER, "Registration page title didn't match"

        flow.complete_registration(data.gender, data.first_name, data.last_name, data.password, data.day, data.month, data.year)
        assert flow.my_account_page.get_green_banner_text() == ExpectedMessages.REGISTRATION_BANNER, "Green banner text didn't match"




