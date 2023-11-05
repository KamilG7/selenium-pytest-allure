from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from locators.locators import ProfessionalServicesLocators
import logging
import time
import allure


class ProfessionalServices:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step(f"Name input in message tab: {1}")
    def input_name_message(self, name):
        self.logger.info(f"Name input in message tab: {name}")
        self.driver.find_element(By.ID, ProfessionalServicesLocators.contact_name_id).click()
        self.driver.find_element(By.ID, ProfessionalServicesLocators.contact_name_id).send_keys(name)
        allure.attach(self.driver.get_screenshot_as_png(), name="Name Input", attachment_type=AttachmentType.PNG)

    @allure.step(f"Email input in message tab: {1}")
    def input_email_message(self, email):
        self.logger.info(f"Email input in message tab: {email}")
        self.driver.find_element(By.ID, ProfessionalServicesLocators.contact_email_id).click()
        self.driver.find_element(By.ID, ProfessionalServicesLocators.contact_email_id).send_keys(email)
        allure.attach(self.driver.get_screenshot_as_png(), name="Email input", attachment_type=AttachmentType.PNG)

    @allure.step(f"Job tittle input in message tab: {1}")
    def input_job_tittle(self, job_tittle):
        self.logger.info(f"Job tittle input in message tab: {job_tittle}")
        self.driver.find_element(By.ID, ProfessionalServicesLocators.job_tittle_id).click()
        self.driver.find_element(By.ID, ProfessionalServicesLocators.job_tittle_id).send_keys(job_tittle)
        allure.attach(self.driver.get_screenshot_as_png(), name="Email input", attachment_type=AttachmentType.PNG)

    @allure.step(f"Company input in message tab: {1}")
    def input_company_message(self, company):
        self.logger.info(f"Company input in message tab: {company}")
        self.driver.find_element(By.ID, ProfessionalServicesLocators.company_name_id).click()
        self.driver.find_element(By.ID, ProfessionalServicesLocators.company_name_id).send_keys(company)
        allure.attach(self.driver.get_screenshot_as_png(), name="Company input", attachment_type=AttachmentType.PNG)

    @allure.step(f"Message input in message tab: {1}")
    def input_message(self, message):
        self.logger.info(f"Message input in message tab: {message}")
        self.driver.find_element(By.ID, ProfessionalServicesLocators.message_input_id).click()
        self.driver.find_element(By.ID, ProfessionalServicesLocators.message_input_id).send_keys(message)
        allure.attach(self.driver.get_screenshot_as_png(), name="Message input", attachment_type=AttachmentType.PNG)

    @allure.step("Cheating captcha")
    def captcha_solver(self):
        time.sleep(10)
        allure.attach(self.driver.get_screenshot_as_png(), name="Captcha attempt",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Message button click")
    def message_send_button(self):
        self.logger.info("Message button click")
        self.driver.find_element(By.ID, ProfessionalServicesLocators.send_message_button_id).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Message button click",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Captures return message")
    def return_confirmation(self):
        time.sleep(2)
        self.logger.info("Return message capture")
        return_msg = self.driver.find_element(By.XPATH, ProfessionalServicesLocators.confirmation_message_xpath).\
            get_attribute("textContent")
        allure.attach(self.driver.get_screenshot_as_png(), name="Return confirmation",
                      attachment_type=AttachmentType.PNG)
        assert return_msg == "We have much appreciated the message and will contact you soon!", \
            f"return message should be visible, is: {return_msg}"