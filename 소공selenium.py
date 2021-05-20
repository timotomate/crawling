from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner
import time

class DemoUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_GoogleSearch_Hongik(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Mason Mount")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.close()
        cls.driver.quit()


print("Test Done Successfully!")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/realadmin01/PycharmProjects/pythonProject/report'))
