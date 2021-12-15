import page
from selenium import webdriver
import unittest

class pythonOrgSearch(unittest.TestCase):
    """foo"""


    def setUp(self):
        """This setUp will Run at Beging of each Test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.get("http://www.python.org")


    def test_title(self):
        """This test will check the title of the page"""
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()