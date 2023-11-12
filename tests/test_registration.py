import pytest
import allure
from allure_commons.types import AttachmentType
from pages.registration_page import RegistrationPage
from data.Variables import *



@pytest.mark.usefixtures("setup")
class TestRegistration:

    @allure.title("Id 1010")
    @allure.description("Registration should fail with empty form")
    def test_registration_empty_form(self, setup):
        self.driver.get("https://courses.ultimateqa.com/users/sign_up")
        registration_page = RegistrationPage(self.driver)
        registration_page.click_submit_registration()
        error_list = registration_page.capture_error_message()
        assert "First name can't be blank" in error_list, "/First name can't be blank/ has to be displayed"
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
    def test_registration_incorrect_email(self, setup):
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
    def test_registration_weak_password(self, setup):
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

    @allure.title("Id 1011")
    @allure.description("User should be able to open Privacy Policy")
    def test_registration_privacy_policy(self, setup):
        self.driver.get("https://courses.ultimateqa.com/users/sign_up")
        registration_page = RegistrationPage(self.driver)
        registration_page.open_privacy_policy()
        privacy_handle = self.driver.window_handles[1]
        self.driver.switch_to.window(privacy_handle)
        title_privacy = self.driver.title
        assert title_privacy == "Privacy Policy", f"Privacy terms should be displayed, is {title_privacy}"
        allure.attach(self.driver.get_screenshot_as_png(), name="privacy policy", attachment_type=AttachmentType.PNG)

    @allure.title("Id 1012")
    @allure.description("User should be able to open Terms of use")
    def test_registration_terms_of_use(self, setup):
        self.driver.get("https://courses.ultimateqa.com/users/sign_up")
        registration_page = RegistrationPage(self.driver)
        registration_page.open_terms_of_use()
        try:
            terms_handle = self.driver.window_handles[2]
        except:
            print("Not all test cases run, reassessment of window handle number")
            terms_handle = self.driver.window_handles[1]
        self.driver.switch_to.window(terms_handle)
        title_terms = self.driver.title
        assert title_terms == "Terms of Use", f"terms should be displayed, is {title_terms}"
        allure.attach(self.driver.get_screenshot_as_png(), name="Terms of use", attachment_type=AttachmentType.PNG)

    @allure.title("Id 1003")
    @allure.description("Registration should succeed with valid input")
    def test_correct_registration(self, setup):
        self.driver.get("https://courses.ultimateqa.com/users/sign_up")
        registration_page = RegistrationPage(self.driver)
        registration_page.name_input_registration(first_name)
        registration_page.last_name_input_registration(last_name)
        registration_page.email_input_registration(email)
        registration_page.password_input_registration(password)
        registration_page.terms_checkbox_click()
        registration_page.click_submit_registration()
        allure.attach(self.driver.get_screenshot_as_png(), name="Correct registration",
                      attachment_type=AttachmentType.PNG)
        registration_page.log_out()

    @allure.title("Id 1013")
    @allure.description("Registration should failed with used email")
    def test_registration_used_email(self, setup):
        self.driver.get("https://courses.ultimateqa.com/users/sign_up")
        registration_page = RegistrationPage(self.driver)
        registration_page.name_input_registration(first_name)
        registration_page.last_name_input_registration(last_name)
        registration_page.email_input_registration(email)
        registration_page.password_input_registration(password)
        registration_page.terms_checkbox_click()
        registration_page.click_submit_registration()
        error_email_registered = registration_page.capture_error_message()
        assert "Email has already been taken" in error_email_registered, "There can't be two users with same email"
        allure.attach(self.driver.get_screenshot_as_png(), name="Correct registration",
                      attachment_type=AttachmentType.PNG)


