import unittest
from selenium import webdriver

class test_pythonOrgSearch(unittest.TestCase):
    """foo"""
    
    def setUp(self):
        """This setUp will Run at Beging of each Test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.get("http://www.python.org") 


    def setUpClass(cls):
        """foo"""
        cls.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        cls.driver.get("http://www.python.org") 


    def tearDownClass(cls):
        """foo"""
        cls.driver.close()   


    def tearDown(self):
        """This TearDown will Run at the End of each Test"""
        self.driver.close()   