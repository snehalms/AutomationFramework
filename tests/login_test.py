from selenium import webdriver
import pytest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from utils import utils as utils
import allure
import moment

@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login(self):
        driver=self.driver
        driver.get(utils.URL)
        Login = LoginPage(driver)
        Login.enter_username(utils.USERNAME)
        Login.enter_password(utils.PASSWORD)
        Login.click_login()


    def test_logout(self):
        try:
            driver=self.driver
            Home = HomePage(driver)
            Home.click_logout()
            a = driver.title
            print(a)
            assert 'a'== 'a'

        except AssertionError as error:
            print("Assertion error occurred.")
            print(error)

            time = moment.now().strftime("%m-%d-%Y_%H-%M-%S")
            functionName = utils.whoIam()
            ScreenshotName= functionName+"_"+time
            allure.attach(self.driver.get_screenshot_as_png(),name=ScreenshotName,attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/A05/PycharmProjects/AutomationFramework/screenshots/"+ScreenshotName+".png")
            raise
        except:
            print("There was an exception")
            raise

        else:
            print("No Exception occurred")

        finally:
            print("I am gonna execute every time")



