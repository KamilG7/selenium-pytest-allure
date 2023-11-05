import logging
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from locators.locators import MainSiteLocators


class MainSitePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.cookie = {"name": "cutie_pie", "value": "jam"}

    @allure.step("Checking if main site load properly")
    def check_main_site_loaded(self):
        self.logger.info("check if main site loads")
        self.driver.find_element(By.XPATH, MainSiteLocators.main_site_header_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Check if main site is loaded",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Adding cookie")
    def add_cookie(self):
        self.logger.info("cookie adder")
        self.driver.add_cookie(self.cookie)

    @allure.step("checking if cookie added")
    def cookie_check(self):
        self.logger.info("Checking if 'cutie-pie' was added")
        flag = False
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if cookie["name"] == "cutie_pie":
                flag = True
                break
        assert flag, "cookie 'cutie_pie' was not added"