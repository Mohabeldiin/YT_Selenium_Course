import unittest
from unittest.main import main
from selenium import webdriver
import page

class pythonOrgSearch(unittest.TestCase):


    def setUp(self):
        """This setUp will Run at Beging of each Test"""
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.get("http://www.python.org")


    def test_search_python(self):
        """This test will check the search functionality"""
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        SearchResultsPage = page.SearchResultsPage(self.driver)
        assert SearchResultsPage.is_results_found()


    def test_title(self):
        """This test will check the title of the page"""
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()


    # def test_example():
    #     """This is an example test will run auto."""
    #     assert False


    # def test_example_2(self):
    #     """This is an example 2 just assert True"""
    #     assert True


    # def not_a_test():
    #     """This is not a test will not run auto."""
    #     pass


    def tearDown(self):
        """This TearDown will Run at the End of each Test"""
        self.driver.close()


if __name__ == "__main__":
    """This is the main function will Run the Unit Test if this Moudle is not imported"""
    unittest.main()