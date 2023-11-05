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






