import pytest
import allure
from allure_commons.types import AttachmentType
from pages.registration_page import RegistrationPage
import random

first_name = "Zbigniew"
last_name = "Brzeczyszczykiewicz"
email = "xxx" + str(random.randint(1111, 9999)) + "@gmail.com"
password = "StrongPassword123"
incorrect_email = "xxx.com"
weak_password = "xxx"

@pytest.mark.usefixtures("setup")
class TestRegistration:


    @allure.title("Id 1010")
    @allure.description("Registration should fail with empty form")
    def test_registration_empty_form(self,setup):

        self.driver.get("https://courses.ultimateqa.com/users/sign_up")
        registration_page = RegistrationPage(self.driver)
        registration_page.click_submit_registration()
        error_list = registration_page.capture_error_message()
        assert "First name can't be blank" in error_list, "/First name can't be blank/ has to be displayed"
        assert "Last name can't be blank" in error_list, "/Last name can't be blank/ has to be displayed"
        assert "Terms must be accepted" in error_list, "/Terms must be accepted/ has to be displayed"
        assert "Email can't be blank" in error_list, "/Email can't be blank/ has to be displayed"
        assert "Password can't be blank" in error_list, "/Password can't be blank/ has to be displayed"
        allure.attach(self.driver.get_screenshot_as_png(), name="All errors", attachment_type=AttachmentType.PNG)



    @allure.title("Id 1005")
    @allure.description("Registration should fail when 'First Name' not submitted")
    def test_registration_no_name(self, setup):

        self.driver.get("https://courses.ultimateqa.com/users/sign_up")
        registration_page = RegistrationPage(self.driver)
        registration_page.last_name_input_registration(last_name)
        registration_page.email_input_registration(email)
        registration_page.password_input_registration(password)
        registration_page.terms_checkbox_click()
        registration_page.click_submit_registration()
        error_list = registration_page.capture_error_message()
        allure.attach(self.driver.get_screenshot_as_png(), name="No name error", attachment_type=AttachmentType.PNG)
        assert "First name can't be blank" in error_list, "/First name can't be blank/ has to be visible!"


    @allure.title("Id 1006")
    @allure.description("Registration should fail when 'Last Name' not submitted")
    def test_registration_no_last_name(self, setup):

        self.driver.get("https://courses.ultimateqa.com/users/sign_up")
        registration_page = RegistrationPage(self.driver)
        registration_page.name_input_registration(first_name)
        registration_page.email_input_registration(email)
        registration_page.password_input_registration(password)
        registration_page.terms_checkbox_click()
        registration_page.click_submit_registration()
        error_list = registration_page.capture_error_message()
        allure.attach(self.driver.get_screenshot_as_png(), name="No last name error",
                      attachment_type=AttachmentType.PNG)
        assert "Last name can't be blank" in error_list, "/Last name can't be blank/ has to be visible!"

    @allure.title("Id 1007")
    @allure.description("Registration should fail when 'Email' not submitted")
    def test_registration_no_email(self, setup):

        self.driver.get("https://courses.ultimateqa.com/users/sign_up")
        registration_page = RegistrationPage(self.driver)
        registration_page.name_input_registration(first_name)
        registration_page.last_name_input_registration(last_name)
        registration_page.password_input_registration(password)
        registration_page.terms_checkbox_click()
        registration_page.click_submit_registration()
        error_list = registration_page.capture_error_message()
        allure.attach(self.driver.get_screenshot_as_png(), name="No Email error",
                      attachment_type=AttachmentType.PNG)
        assert "Email can't be blank" in error_list, "/Email can't be blank/ has to be visible!"

    @allure.title("Id 1008")
    @allure.description("Registration should fail when incorrect 'Email' submitted")
    def test_registration_no_email(self, setup):
        self.driver.get("https://courses.ultimateqa.com/users/sign_up")
        registration_page = RegistrationPage(self.driver)
        registration_page.name_input_registration(first_name)
        registration_page.last_name_input_registration(last_name)
        registration_page.email_input_registration(incorrect_email)
        registration_page.password_input_registration(password)
        registration_page.terms_checkbox_click()
        registration_page.click_submit_registration()
        error_list = registration_page.capture_error_message()
        allure.attach(self.driver.get_screenshot_as_png(), name="Incorrect Email error",
                      attachment_type=AttachmentType.PNG)
        assert "Email is invalid" in error_list, "/Email is invalid/ has to be visible!"

    @allure.title("Id 1009")
    @allure.description("Registration should fail when weak password submitted")
    def test_registration_no_email(self, setup):
        self.driver.get("https://courses.ultimateqa.com/users/sign_up")
        registration_page = RegistrationPage(self.driver)
        registration_page.name_input_registration(first_name)
        registration_page.last_name_input_registration(last_name)
        registration_page.email_input_registration(email)
        registration_page.password_input_registration(weak_password)
        registration_page.terms_checkbox_click()
        registration_page.click_submit_registration()
        error_list = registration_page.capture_error_message()
        allure.attach(self.driver.get_screenshot_as_png(), name="Weak password error",
                      attachment_type=AttachmentType.PNG)
        assert "Password must be at least 8 characters" in error_list, "/Password must be at least 8 characters/" \
                                                                       " has to be visible!"




