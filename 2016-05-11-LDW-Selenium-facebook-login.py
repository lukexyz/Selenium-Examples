from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time


class LoginTest(unittest.TestCase):

    def setUp(self):
        # Define driver
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.facebook.com")

    def test_Login(self):
        driver = self.driver

        # Facebook web element variables
        emailFieldID     = "email"
        facebookUsername = "***********@gmail.com"
        passFieldID      = "pass"
        facebookPassword = "***********"
        loginButtonXpath = "//input[@value='Log In']"
        fbLogoXpath      = "(//a[contains(@href, 'logo')])[1]"

        # Create elements (allowing 10s to load)
        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        # Actions: Log in
        emailFieldElement.clear()
        emailFieldElement.send_keys(facebookUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword)
        loginButtonElement.click()

        # Verify successful login by locating fb logo
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))

        # Verify the actions visually
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()