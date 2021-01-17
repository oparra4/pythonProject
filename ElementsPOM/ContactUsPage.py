from selenium.webdriver.support.select import Select

class ContactUsPage():

    def __init__(self, driver):
        self.driver = driver

        self.SubjectHeadingId = "id_contact"
        self.EmailAddress = "email"
        self.OrderReference = "id_order"
        self.attachFile = "fileUpload"
        self.MessageField = "message"
        self.SendButton = "submitMessage"

    def subjectHeadingSelectOption(self, IndexValue):
        drp = self.driver.find_element_by_id(self.SubjectHeadingId)
        dropd = Select(drp)
        dropd.select_by_value(IndexValue)

    def enterEmailAddress (self, EmailAddressvalue):
        self.driver.find_element_by_id(self.EmailAddress).send_keys(EmailAddressvalue)

    def enterOrderReference(self, OrderRefNumber):
        self.driver.find_element_by_id(self.OrderReference).send_keys(OrderRefNumber)

    def uploadFile(self, filePath):
        self.driver.find_element_by_id(self.attachFile).send_keys(filePath)

    def addMEssage(self, messageContent):
        self.driver.find_element_by_id(self.MessageField).send_keys(messageContent)

    def clickSend(self):
        self.driver.find_element_by_id(self.SendButton).click()





