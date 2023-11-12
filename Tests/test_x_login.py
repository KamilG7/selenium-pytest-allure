import pytest
import allure
from allure_commons.types import AttachmentType
from pages.login_page import LoginPage
from Tests.test_registration import email, password
from pages.registration_page import RegistrationPage



@pytest.mark.usefixtures("setup")
class TestMainSite:

    @allure.title("Id 1004")
    @allure.description("Login should succeed with valid credentials. Email: {1}, password: {2}")
    def test_correct_login(self, setup):
        self.driver.get("https://courses.ultimateqa.com/users/sign_in")
        login_page = LoginPage(self.driver)
        registration_page = RegistrationPage(self.driver)
        login_page.login_email_input(email)
        login_page.login_password_input(password)
        login_page.login_submit_button()
        allure.attach(self.driver.get_screenshot_as_png(), name="Correct login", attachment_type=AttachmentType.PNG)
        registration_page.log_out()

    @allure.title("Id 1014")
    @allure.description("Login should fail with empty form")
    def test_correct_login(self, setup):
        self.driver.get("https://courses.ultimateqa.com/users/sign_in")
        login_page = LoginPage(self.driver)
        login_page.login_submit_button()
        error_list = login_page.return_login_error()
        assert "Invalid email or password" in error_list
        allure.attach(self.driver.get_screenshot_as_png(), name="Fail. empty form", attachment_type=AttachmentType.PNG)

    @allure.title("Id 1015")
    @allure.description("Forgot password option should work. Email: {1}")
    def test_correct_login(self, setup):
        self.driver.get("https://courses.ultimateqa.com/users/sign_in")
        login_page = LoginPage(self.driver)
        login_page.forget_password_button()
        login_page.forget_password_input_email(email)
        login_page.forget_password_submit_form()
        return_info = login_page.forget_password_return_message()
        assert return_info.is_displayed(), "Return info not displayed = not working"


