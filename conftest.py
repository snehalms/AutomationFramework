import pytest
from selenium import webdriver
from utils import utils as utils

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="Type in browser e.g.chrome OR firefox")


@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=utils.CHROMEEXEPATH)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=utils.FFEXEPATH)

    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver= driver
    yield
    driver.close()
    driver.quit()
    print("Success")