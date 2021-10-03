import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from test_utility import create_log


class EnvironmentSetup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        create_log.create_log("Execution started... ")
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        base_url = "https://weather.com/"
        cls.driver.get(base_url)
        create_log.create_log(" Login Page Loading... ")
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.close()
            cls.driver.quit()
