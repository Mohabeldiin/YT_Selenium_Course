import unittest
import page
from test_pythonOrgSearch import test_pythonOrgSearch

class test_pythonOrgSearch(unittest.TestCase):
    """foo"""

    def setUp(self,):
        """foo"""""
        test_pythonOrgSearch.__init__();


    def tearDown(self):
        """foo"""
        test_pythonOrgSearch.__del__(self)
        


    def test_title_2(self):
        """This test will check the title of the page"""
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()