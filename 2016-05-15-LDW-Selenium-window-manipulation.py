from selenium import webdriver
import unittest
import time


class WindowTest(unittest.TestCase):
    """
    Selenium test sends the browser around the screen in a clockwise motion.

    Asserts an error if the final position is not the same as the initial position.
    """
    def setUp(self):
        # Start chrome maximised
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=options)

    def test_window_manipulation(self):
        driver = self.driver

        # Store dimensions of maximised window for calculations
        zero_pos = driver.get_window_position()
        max_size = driver.get_window_size()
        print('Initial window parameters:')
        print(zero_pos, max_size)
        print("==========")

        # Set window size for spiral manipulation
        size_x, size_y = 300, 300
        driver.set_window_size(size_x, size_y)
        step_size = 30

        # Manipulate window top-left to top-right
        for x in range(zero_pos['x'], (max_size['width'] - size_x), step_size):
            driver.set_window_position(x, zero_pos['y'])
        win_pos = driver.get_window_position()
        print(win_pos)

        # Manipulate top-right to bottom-right
        for y in range(win_pos['y'], (max_size['height'] - size_y), step_size):
            driver.set_window_position(win_pos['x'], y)
        win_pos = driver.get_window_position()
        print(win_pos)

        # Manipulate bottom-right to bottom-left
        for x in range(win_pos['x'], zero_pos['x'] - step_size, -step_size):
            driver.set_window_position(x, win_pos['y'])
        win_pos = driver.get_window_position()
        print(win_pos)

        # Manipulate bottom-right to bottom-left
        for y in range(win_pos['y'], zero_pos['y'] - step_size, -step_size):
            driver.set_window_position(win_pos['x'], y)
        win_pos = driver.get_window_position()
        print(win_pos)

        # Check the final position is the same as the starting position
        if win_pos['x'] != zero_pos['x']:
            raise AssertionError('The final position {} is not the same as the initial position {}'.format(win_pos['x'], zero_pos['x']))
        else:
            print('Final position verified. ✓')

        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()