from selenium import webdriver
import unittest


class TablesCheck(unittest.TestCase):

    def setUp(self):
        # Define driver
        self.driver = webdriver.Chrome()
        # Navigate to the url
        url = 'http://www.w3schools.com/html/html_tables.asp'
        self.driver.get(url)

    def test_get_number_of_tables(self):
        """
        Checks whether the total number of rows equals the expected number.
        """
        driver = self.driver
        all_rows = driver.find_elements_by_tag_name('tr')
        number_of_rows = len(all_rows)

        expected_num_of_rows = 26

        if expected_num_of_rows != number_of_rows:
            raise AssertionError('The number of rows did not match. The actual number is: \
                {} and the expected number is {}'
                                .format(str(number_of_rows), str(expected_num_of_rows)))

        else: print('Verified: The number of rows is: {}, and the expected number is {}.'
                    .format(str(number_of_rows), str(expected_num_of_rows)))

    def test_row_contains_text(self):
        """
        Checks whether a row contains a specific text.
        """
        text_to_check = 'Eve'
        row_number = 1

        all_rows = self.driver.find_elements_by_tag_name('tr')
        my_row = all_rows[row_number]
        row_text = my_row.text

        if text_to_check not in row_text:
            raise AssertionError('The text "{}" is not in row {} ["{}"]'.format(text_to_check, row_number, row_text))
        else:
            print('The text "{}" is in row {} ["{}"]'.format(text_to_check, row_number, row_text))

    def tearDown(self):
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()