class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.ContactUsLinkId = "contact-link"

    def contactUs_Click(self):
        self.driver.find_element_by_id(self.ContactUsLinkId).click()