from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    # Main Page Locators
    GO_BUTTON = (By.ID, 'submit')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results page locators should come here"""    

    # Search Results Page Locators
    SEARCH_RESULTS = (By.ID, 'results')