from selenium import webdriver
import time
import unittest
from ElementsPOM.Config import TestData
from ElementsPOM.APHomePage import HomePage
from ElementsPOM.ContactUsPage import ContactUsPage
import HTMLTestRunner

class ContactUsForm_AutomationPractice(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\timon\Downloads\chromedriver_win32 (1)\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com")
        self.driver.implicitly_wait(8)

    def tearDown(self):
        self.driver.close()

    def test_positive_Contactusform(self):
        driver = self.driver
        # Go to Contact us Section
        home = HomePage(driver)
        home.contactUs_Click()
        c = TestData(driver)
        time.sleep(1)
        contactus = ContactUsPage(driver)
        contactus.subjectHeadingSelectOption("2")
        contactus.enterEmailAddress("Test@tester.com")
        contactus.enterOrderReference("TestORder1")
        contactus.addMEssage("Test message from Pycharm")
        contactus.uploadFile(c.AttachDocPath)
        contactus.clickSend()
        time.sleep(1)
        #Assertion
        msg = self.driver.find_element_by_css_selector(".alert").text
        self.assertEqual("Your message has been successfully sent to our team.", msg, "Error on the message Happy path")

    def test_submit_Without_MessageField(self):
        #Submit without Message - verify error
        driver = self.driver
        home = HomePage(driver)
        # Go to Contact us Section
        home.contactUs_Click()
        c = TestData(driver)
        time.sleep(1)
        contactus = ContactUsPage(driver)
        contactus.subjectHeadingSelectOption("2")
        contactus.enterEmailAddress("Test@tester.com")
        contactus.enterOrderReference("TestORder1")
        contactus.uploadFile(c.AttachDocPath)
        contactus.clickSend()
        time.sleep(1)
        # Assertion
        msj2 = self.driver.find_element_by_xpath("//*[@id='center_column']/div/ol/li").text
        self.assertEqual("The message cannot be blank.", msj2, "Error on the error message for missing Message")

    def test_submit_Without_Subject(self):
        #Submit without Subject - verify error
        driver = self.driver
        home = HomePage(driver)
        # Go to Contact us Section
        home.contactUs_Click()
        c = TestData(driver)
        time.sleep(1)
        contactus = ContactUsPage(driver)
        contactus.enterEmailAddress("Test@tester.com")
        contactus.enterOrderReference("TestORder1")
        contactus.addMEssage("Test message from Pycharm")
        contactus.uploadFile(c.AttachDocPath)
        contactus.clickSend()
        time.sleep(1)
        # Assertion
        msj1 = self.driver.find_element_by_xpath("//*[@id='center_column']/div/ol/li").text
        self.assertEqual("Please select a subject from the list provided.", msj1, "Error on the error message for Subject")

    def test_submit_Without_EmailAddress(self):
        #Submit without Email address - verify error
        driver = self.driver
        home = HomePage(driver)
        # Go to Contact us Section
        home.contactUs_Click()
        c = TestData(driver)
        time.sleep(1)
        contactus = ContactUsPage(driver)
        contactus.subjectHeadingSelectOption("2")
        contactus.enterOrderReference("TestORder1")
        contactus.addMEssage("Test message from Pycharm")
        contactus.uploadFile(c.AttachDocPath)
        contactus.clickSend()
        time.sleep(1)
        # Assertion
        msj3 = self.driver.find_element_by_xpath("//*[@id='center_column']/div/ol/li").text
        self.assertEqual("Invalid email address.", msj3, "Error on the email error message ")

    def test_submit_Without_OrderRef(self):
        #submit without Order Reference - able to submit
        driver = self.driver
        home = HomePage(driver)
        # Go to Contact us Section
        home.contactUs_Click()
        c = TestData(driver)
        time.sleep(1)
        contactus = ContactUsPage(driver)
        contactus.subjectHeadingSelectOption("2")
        contactus.enterEmailAddress("Test@tester.com")
        contactus.addMEssage("Test message from Pycharm")
        contactus.uploadFile(c.AttachDocPath)
        contactus.clickSend()
        time.sleep(1)
        # Assertion
        msg1 = self.driver.find_element_by_css_selector(".alert").text
        time.sleep(1)
        self.assertEqual("Your message has been successfully sent to our team.", msg1, "Error on the message on missing Order #")

    def test_submit_With_OrderRefBigString(self):
        #submit without Order Reference - able to submit
        driver = self.driver
        home = HomePage(driver)
        # Go to Contact us Section
        home.contactUs_Click()
        c = TestData(driver)
        time.sleep(1)
        contactus = ContactUsPage(driver)
        contactus.subjectHeadingSelectOption("2")
        contactus.enterEmailAddress("Test@tester.com")
        contactus.enterOrderReference("01234567891011")
        contactus.addMEssage("Test message from Pycharm")
        contactus.uploadFile(c.AttachDocPath)
        contactus.clickSend()
        time.sleep(1)
        # Assertion
        msg4 = self.driver.find_element_by_css_selector(".alert").text
        time.sleep(1)
        self.assertEqual("Your message has been successfully sent to our team.", msg4, "Error on the message on missing Order #")


if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output=r'C:\Users\timon\PycharmProjects\pythonProject\Reports'))

