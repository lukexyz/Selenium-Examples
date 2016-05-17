from selenium import webdriver
import unittest


class TestMultipleElements(unittest.TestCase):
    """
    Unittest to check functionality of multiple elements on the Wikipedia frontpage.
    """

    def setUp(self):
        # Define driver
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.wikipedia.org")
        self.driver.maximize_window()

    def test_lang_dropdown(self):
        """
        Finds the language dropdown box and prints the selection.
        """
        driver = self.driver
        dropdown_languages = driver.find_elements_by_tag_name('option')
        for lang in dropdown_languages:
            print(lang.get_attribute('lang'), ' - ', lang.text)
        print('===================')
        print(len(dropdown_languages), 'languages available ✓')
        print('===================')

    def test_num_links(self):
        """
        Prints the total number of links on the front page.
        """
        driver = self.driver
        all_links = driver.find_elements_by_tag_name('a')
        print(len(all_links), 'links on front page ✓')
        print('===================')

    def test_wikimedia_links(self):
        """
        Prints the wikimedia links from the "otherprojects" wikipedia class.
        Exception thrown if number of links != 12
        """
        driver = self.driver

        # Find Wikimedia class div elements
        block = driver.find_element_by_xpath('//*[contains(@class,"otherprojects")]')
        wikimedia_links = block.find_elements_by_tag_name('a')

        # Loop though hyperlinks
        for link in wikimedia_links:
            print(link.get_attribute('href'))

        # Check for exception
        if len(wikimedia_links) != 12:
            raise AssertionError('The number of links is "{}", not the expected 12'.format(len(wikimedia_links)))
        else:
            print('===================')
            print('Number of Wikimedia links: {} ✓'.format(len(wikimedia_links)))
            print('===================')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()