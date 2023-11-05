import logging
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from locators.locators import MainSiteLocators


class MainSitePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Checking if main site load properly")
    def check_main_site_loaded(self):
        self.logger.info("check if main site loads")
        header = self.driver.find_element(By.XPATH, MainSiteLocators.main_site_header_xpath).text()
        assert header == 'Master test Automation, Faster.', "site not loaded"
        allure.attach(self.driver.get_screenshot_as_png(), name="Check if main site is loaded",
                      attachment_type=AttachmentType.PNG)