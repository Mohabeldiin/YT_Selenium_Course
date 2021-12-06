from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""
    locator = 'q'


class GoButtonElement(BasePageElement):
    """This class gets the go button from the specified locator"""
    locator = 'go'
        

class BasePage(object):
    """This class will be the parent class to all the pages, from which all the pages will inherit"""

    def __init__(self, driver):
        """This method will get the driver from the test case class and assign it to the driver attribute

        Args:
            driver (webdriver): The webdriver object passed from the test case class
        """
        self.driver = driver


class MainPage(BasePage):
    """foo"""

    search_text_element = SearchTextElement() # The search text element


    def is_title_matches(self):
        """This method checks that the page title matches the given one.

        Returns:
            boll: True if the title matches, False otherwise.
        """
        return "Python" in self.driver.title

    
    def click_go_button(self):
        """This method clicks on the go button."""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """foo"""

    def is_results_found(self):
        """This method checks that the results were found for the search.

        Returns:
            bool: True if the results were found, False otherwise.
        """
        return "No results found." not in self.driver.page_source