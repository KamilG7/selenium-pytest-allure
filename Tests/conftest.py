#Please run by terminal (py.test)
import pytest
from Utils.driver_factory import DriverFactory


@pytest.fixture()
def setup(request):
    driver = DriverFactory.get_driver("edge")
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver
    yield
    driver.quit()
