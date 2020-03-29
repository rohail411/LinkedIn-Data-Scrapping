from .Scraper import Scraper
from .ConnectionScraper import ConnectionScraper
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import time
from .Profile import Profile
from .utils import AnyEC

from bs4 import BeautifulSoup
from urllib.request import urlopen

class ProfileIdsScraper(Scraper):
    """
    Scraper for Personal LinkedIn Profiles. See inherited Scraper class for
    details about the constructor.
    """
    MAIN_SELECTOR = '.core-rail'
    ERROR_SELECTOR = '.profile-unavailable'


    def scrape(self,url="https://www.linkedin.com/search/results/people/?keywords=designer&origin=SWITCH_SEARCH_VERTICAL"):
        self.driver.get(url)
        #search = self.driver.find_element_by_css_selector(
        #'input.search-global-typeahead__input').send_keys("web develper").click()
        #time.sleep(5)
        #self.driver.find_element_by_css_selector(".search-typeahead-v2__button").click()
        #self.driver.find_element_by_xpath('//*[@id="ember32"]/div[2]/button').click()
        #self.driver.get("https://www.linkedin.com/search/results/people/?keywords=designer&origin=SWITCH_SEARCH_VERTICAL")
        time.sleep(2)
        button = self.driver.find_element_by_id('ember70').click()
        # html = urlopen("https://www.linkedin.com/search/results/people/?keywords=designer&origin=SWITCH_SEARCH_VERTICAL")
        # data = html.read()
        # html.close()

        # soup = BeautifulSoup(data,'html.parser')
        return button

 #self.driver.find_element_by_css_selector(".search-global-typeahead__controls>button").click()
            
        
