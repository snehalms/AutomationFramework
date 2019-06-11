#CONSTANTS
import inspect
URL="https://s2.demo.opensourcecms.com/orangehrm/symfony/web/index.php/auth/login"
USERNAME="opensourcecms"
PASSWORD="opensourcecms"
CHROMEEXEPATH = "C:/Users/A05/PycharmProjects/AutomationFramework/drivers/chromedriver.exe"
FFEXEPATH = "C:/Users/A05/PycharmProjects/AutomationFramework/drivers/geckodriver.exe"


def whoIam():
    return inspect.stack()[1][3]