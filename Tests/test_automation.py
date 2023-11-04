import pytest
import allure


@pytest.mark.usefixtures("setup")
class TestAutomation:

    @allure.title("Automation site test")
    @allure.description("Test steps")
    def test_automation(self, setup):

        self.driver.get("https://ultimateqa.com/consulting/")