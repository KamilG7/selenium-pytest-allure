import pytest
import allure
from pages.main_site_page import MainSitePage


@pytest.mark.usefixtures("setup")
class TestMainSite:

    @allure.title("Id 1016")
    @allure.description("Checking if cookie can be added")
    def test_cookies(self, setup):
        self.driver.get("https://ultimateqa.com/")
        main_site = MainSitePage(self.driver)
        main_site.add_cookie()
        main_site.cookie_check()

