from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest
import time

class LoginTest(unittest.TestCase):

    def setUp(self):
        # Define driver
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.facebook.com")

    def test_Login(self):
        driver = self.driver

        # Web element variables
        emailFieldID    = "email"
        monthDropDownID = "month"

        # Create elements (allowing 10s to load)
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        monthDropDownElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(monthDropDownID))

        # Action: select month from drop down
        Select(monthDropDownElement).select_by_visible_text("May")

        # Verify the actions visually
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()