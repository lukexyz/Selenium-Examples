from selenium import webdriver
import unittest


class TestMultipleElements(unittest.TestCase):

    def setUp(self):
        # Define driver
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.wikipedia.org")
        self.driver.maximize_window()

    def test_lang_dropdown(self):
        driver = self.driver
        dropdown_languages = driver.find_elements_by_tag_name('option')
        for lang in dropdown_languages:
            print(lang.get_attribute('lang'), ' - ', lang.text)
        print('===================')
        print(len(dropdown_languages), 'languages available ✓')
        print('===================')

    def test_num_links(self):
        driver = self.driver
        all_links = driver.find_elements_by_tag_name('a')
        print(len(all_links), 'links on front page ✓')
        print('===================')

    def test_wikimedia_links(self):
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