from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        elif browser == "edge":
            return webdriver.Edge(service=Service(executable_path=EdgeChromiumDriverManager().install()))
        raise Exception("Driver not included/wrong driver name")
