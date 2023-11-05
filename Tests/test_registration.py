import pytest
import allure
from allure_commons.types import AttachmentType

from pages.registration_page import RegistrationPage


@pytest.mark.usefixtures("setup")
class TestRegistration:

    @allure.title("Id 1005")
    @allure.description("Registration should fail when 'First Name' not submitted")
    def test_automation(self, setup, last_name, email, password):

        self.driver.get("https://courses.ultimateqa.com/users/sign_up")
        registration_page = RegistrationPage(self.driver)
        registration_page.last_name_input_registration(last_name)
        registration_page.email_input_registration(email)
        registration_page.password_input_registration(password)
        registration_page.terms_checkbox_click()
        registration_page.submit_button_click()
        error_list = registration_page.capture_error_message()
        assert "First name can't be blank" in error_list, "/First name can't be blank/ has to be visible!"
        allure.attach(self.driver.get_screenshot_as_png(), name="No name error", attachment_type=AttachmentType.PNG)

