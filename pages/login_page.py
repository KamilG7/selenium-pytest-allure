import logging
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from locators.locators import LoginPageLocators


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Email input. Email: {1}")
    def login_email_input(self, email):
        self.logger.info("Login Email Input")
        self.driver.find_element(By.XPATH, LoginPageLocators.login_button_xpath).click()
        self.driver.find_element(By.XPATH, LoginPageLocators.login_button_xpath).send_keys(email)
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Email Input", attachment_type=AttachmentType.PNG)

    @allure.step("Password input. Password: {1}")
    def login_email_input(self, password):
        self.logger.info("Login Password Input")
        self.driver.find_element(By.ID, LoginPageLocators.input_password_id).send_keys(password)
        self.driver.find_element(By.ID, LoginPageLocators.input_password_id).send_keys(password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Password Input",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Login Submit Button click")
    def login_submit_button(self):
        self.logger.info("Login Password Input")
        self.driver.find_element(By.XPATH, LoginPageLocators.login_button_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Sending form",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Forgot password click")
    def forget_password_button(self):
        self.logger.info("Forgot password click")
        self.driver.find_element(By.XPATH, LoginPageLocators.forgot_password_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Forgot password button click",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Forgot password input email")
    def forget_password_input_email(self, email):
        self.logger.info("Forgot password input email")
        self.driver.find_element(By.ID, LoginPageLocators.forgot_password_email_id).send_keys(email)
        allure.attach(self.driver.get_screenshot_as_png(), name="Forget password input email",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Forgot password submit form")
    def forget_password_submit_form(self):
        self.logger.info("Forgot password submit form")
        self.driver.find_element(By.NAME, LoginPageLocators.forgot_password_submit_name).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Forgot password submit form",
                      attachment_type=AttachmentType.PNG)




