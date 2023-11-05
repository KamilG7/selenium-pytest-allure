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
    def valid_name_input_registration(self, name):
        self.logger.info(f"First Name input in registration form. Name: {name}")
        self.driver.find_element(By.ID, RegistrationLocators.registration_name_id).click()
        self.driver.find_element(By.ID, RegistrationLocators.registration_name_id).send_keys(name)
        allure.attach(self.driver.get_screenshot_as_png(), name="Registration - First Name Input",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Last Name input in registration form. Last Name: {1}")
    def valid_name_input_registration(self, last_name):
        self.logger.info(f"Last Name input in registration form. Last name: {last_name}")
        self.driver.find_element(By.ID, RegistrationLocators.registration_surname_id).click()
        self.driver.find_element(By.ID, RegistrationLocators.registration_surname_id).send_keys(last_name)
        allure.attach(self.driver.get_screenshot_as_png(), name="Registration - Last Name Input",
                      attachment_type=AttachmentType.PNG)




