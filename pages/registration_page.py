import logging
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from locators.locators import RegistrationLocators


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Name input in registration form. Name: {1}")
    def name_input_registration(self, name):
        self.logger.info(f"First Name input in registration form. Name: {name}")
        self.driver.find_element(By.ID, RegistrationLocators.registration_name_id).click()
        self.driver.find_element(By.ID, RegistrationLocators.registration_name_id).send_keys(name)
        allure.attach(self.driver.get_screenshot_as_png(), name="Registration - First Name Input",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Last Name input in registration form. Last Name: {1}")
    def last_name_input_registration(self, last_name):
        self.logger.info(f"Last Name input in registration form. Last name: {last_name}")
        self.driver.find_element(By.ID, RegistrationLocators.registration_surname_id).click()
        self.driver.find_element(By.ID, RegistrationLocators.registration_surname_id).send_keys(last_name)
        allure.attach(self.driver.get_screenshot_as_png(), name="Registration - Last Name Input",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Email input in registration form. Email: {1}")
    def email_input_registration(self, email):
        self.logger.info(f"Email input in registration form. Email: {email}")
        self.driver.find_element(By.ID, RegistrationLocators.registration_email_id).click()
        self.driver.find_element(By.ID, RegistrationLocators.registration_email_id).send_keys(email)
        allure.attach(self.driver.get_screenshot_as_png(), name="Registration - Email Input",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Password input in registration form. Password: {1}")
    def password_input_registration(self, password):
        self.logger.info(f"Password input in registration form. Password: {password}")
        self.driver.find_element(By.ID, RegistrationLocators.registration_password_id).click()
        self.driver.find_element(By.ID, RegistrationLocators.registration_password_id).send_keys(password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Registration - Password Input",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Terms acceptance checkbox click")
    def terms_checkbox_click(self):
        self.logger.info("Terms acceptance checkbox click")
        self.driver.find_element(By.ID, RegistrationLocators.terms_checkbox_id).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Registration - terms checkbox",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Opening Privacy Policy Terms")
    def open_privacy_policy(self):
        self.logger.info("Opening Privacy Policy Terma")
        self.driver.find_element(By.LINK_TEXT, RegistrationLocators.privacy_policy_link_text).click()
        privacy_handle = self.driver.window_handles[1]
        self.driver.switch_to.window(privacy_handle)
        title_privacy = self.driver.title
        assert title_privacy == "Privacy Policy", f"Privacy terms should be displayed, is {title_privacy}"
        allure.attach(self.driver.get_screenshot_as_png(), name="privacy policy", attachment_type=AttachmentType.PNG)

    @allure.step(f"Terms of use have to be accessible")
    def open_terms_of_use(self):
        self.logger.info("Opening Terms Of Use")
        self.driver.find_element(By.LINK_TEXT, RegistrationLocators.terms_of_use_link_text).click()
        terms_handle = self.driver.window_handles[2]
        self.driver.switch_to.window(terms_handle)
        title_terms = self.driver.title
        assert title_terms == "Terms of Use", f"terms should be displayed, is {title_terms}"
        allure.attach(self.driver.get_screenshot_as_png(), name="Terms of use", attachment_type=AttachmentType.PNG)

    @allure.step("Invalid email input - Email: {1}")
    def invalid_email_input_registration(self, invalid_email):
        self.logger.info(f"Invalid Email input in registration form. Email: {invalid_email}")
        self.driver.find_element(By.ID, RegistrationLocators.registration_email_id).click()
        self.driver.find_element(By.ID, RegistrationLocators.registration_email_id).send_keys(invalid_email)
        allure.attach(self.driver.get_screenshot_as_png(), name="Registration - Invalid Email Input",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Weak Password input in registration form. Weak Password: {1}")
    def weak_password_input_registration(self, weak_password):
        self.logger.info(f"Weak Password input in registration form. Password: {weak_password}")
        self.driver.find_element(By.ID, RegistrationLocators.registration_password_id).click()
        self.driver.find_element(By.ID, RegistrationLocators.registration_password_id).send_keys(weak_password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Registration - Weak Password Input",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Capture error message")
    def capture_error_message(self):
        self.logger.info(f"Error list capture")
        error_list = self.driver.find_element(By.XPATH, RegistrationLocators.error_list_xpath).text
        allure.attach(self.driver.get_screenshot_as_png(), name="Error list capture",
                      attachment_type=AttachmentType.PNG)
        return error_list

    @allure.step("Clicking submit button for registration form")
    def click_submit_registration(self):
        self.logger.info(f"Submit button click")
        self.driver.find_element(By.XPATH, RegistrationLocators.registration_submit_button_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Submit button click",
                      attachment_type=AttachmentType.PNG)










