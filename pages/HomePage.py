class HomePage():

    def __init__(self,driver):
        self.driver=driver
        self.logout_link_linktext = "Logout"

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linktext).click()