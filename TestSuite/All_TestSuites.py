import unittest
from Package1.ChromeAPtest import ContactUsForm_AutomationPractice


#Get all tests here
ts1 = unittest.TestLoader().loadTestsFromTestCase(ContactUsForm_AutomationPractice)

#Create Test suites
regressionTest = unittest.TestSuite([ts1])
#Which suites to run
unittest.TextTestRunner().run(regressionTest)
