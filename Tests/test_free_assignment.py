import pytest
import allure
from pages.professional_services_page import ProfessionalServices



@pytest.mark.usefixtures("setup")
class TestAutomation:

    @allure.title("Automation site test")
    @allure.description("Test steps")
    def test_automation(self, setup):

        self.driver.get("https://ultimateqa.com/consulting/")
        professional_services = ProfessionalServices(self.driver)
        professional_services.input_name_message("Kamil")
        professional_services.input_email_message("xxx2@gmail.com")
        professional_services.input_job_tittle("Someone Important")
        professional_services.input_company_message("Test Corp")
        professional_services.input_message("Test message with length of 30")
        professional_services.captcha_solver()
        professional_services.message_send_button()
        professional_services.return_confirmation()