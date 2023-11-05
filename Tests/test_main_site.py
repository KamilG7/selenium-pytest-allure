import pytest
import allure
from allure_commons.types import AttachmentType
from pages.main_site_page import MainSitePage


@pytest.mark.usefixtures("setup")
class TestMainSite:

    @allure.title("Id 1010")
    @allure.description("Registration should fail with empty form")
    def check_if_page_loads(self, setup):
        self.driver.get("https://ultimateqa.com/")
        main_site_page = MainSitePage(self.driver)
        main_site_page.check_main_site_loaded()
        allure.attach(self.driver.get_screenshot_as_png(), name="Check if main site is loaded",
                      attachment_type=AttachmentType.PNG)