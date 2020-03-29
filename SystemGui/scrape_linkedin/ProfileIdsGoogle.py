import selenium.webdriver
import time
from os import environ
from abc import abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import csv


class ProfileIdsGoogle(object):
    """
    Wrapper for selenium Chrome driver with methods to scroll through a page and
    to scrape and parse info from a linkedin page

    Params:
        - cookie {str}: li_at session cookie required to scrape linkedin profiles
        - driver {webdriver}: driver to be used for scraping
        - scroll_pause {float}: amount of time to pause (s) while incrementally
        scrolling through the page
        - scroll_increment {int}: pixel increment for scrolling
        - timeout {float}: time to wait for page to load first batch of async content
    """

    def __init__(self, cookie=None, scraperInstance=None, driver=selenium.webdriver.Chrome, driver_options={}, scroll_pause=0.1, scroll_increment=300, timeout=10):
       
        if scraperInstance:
            self.was_passed_instance = True
            self.driver = scraperInstance.driver
            self.scroll_increment = scraperInstance.scroll_increment
            self.timeout = scraperInstance.timeout
            self.scroll_pause = scraperInstance.scroll_pause
            return

        self.was_passed_instance = False
        self.driver = driver(**driver_options)
        self.scroll_pause = scroll_pause
        self.scroll_increment = scroll_increment
        self.timeout = timeout
        self.driver.get('http://www.google.com')
        self.driver.set_window_size(1920, 1080)
        time.sleep(2)
        

    def getIds(self,jobTitle='',location=''):
        self.search_query = self.driver.find_element_by_name('q')
        # send_keys() to simulate the search text key strokes
        self.search_query.send_keys(f'site:linkedin.com/in/ AND "{jobTitle}" AND "{location}"')
        # .send_keys() to simulate the return key 
        self.search_query.send_keys(Keys.RETURN)
        linkedin_urls = self.driver.find_elements_by_class_name('iUh30')
        linkedin_urls = [url.text for url in linkedin_urls]
        urls = [url.split('.com')[1][3:] for url in linkedin_urls]
        urls= [url for url in urls if '...' != url] 
        write = csv.writer(open('result.csv','w'))
        write.writerow(urls)
        time.sleep(2)
        try:
            pagination = self.driver.find_elements_by_class_name('fl') 
            for i in range(len(pagination)):
                btn = self.driver.find_element_by_id('pnnext')
                if btn:
                    btn.click()
                    test_urls = self.driver.find_elements_by_class_name('iUh30')
                    if test_urls:
                        linkedin2_urls = [url.text for url in test_urls]
                        urls = [url.split('.com')[1][3:] for url in linkedin2_urls]
                        urls= [url for url in urls if '...' not in url]
                        time.sleep(0.5) 
                        write = csv.writer(open('result.csv','a'))
                        write.writerow(urls)
                        time.sleep(1)
                    else:
                        print('-------ELSE---------')
        except Exception as e:
            print("HIIII")
            print(e)


    def scroll_to_bottom(self):
        """Scroll to the bottom of the page

        Params:
            - scroll_pause_time {float}: time to wait (s) between page scroll increments
            - scroll_increment {int}: increment size of page scrolls (pixels)
        """
        expandable_button_selectors = [
            'button[aria-expanded="false"].pv-skills-section__additional-skills',
            'button[aria-expanded="false"].pv-profile-section__see-more-inline',
            'button[aria-expanded="false"].pv-top-card-section__summary-toggle-button',
            'button[data-control-name="contact_see_more"]'
        ]

        current_height = 0
        while True:
            for name in expandable_button_selectors:
                try:
                    self.driver.find_element_by_css_selector(name).click()
                except:
                    pass

            # Use JQuery to click on invisible expandable 'see more...' elements
            self.driver.execute_script('$(".lt-line-clamp__more").click()')

            # Scroll down to bottom
            new_height = self.driver.execute_script(
                "return Math.min({}, document.body.scrollHeight)".format(current_height + self.scroll_increment))
            if (new_height == current_height):
                break
            self.driver.execute_script(
                "window.scrollTo(0, Math.min({}, document.body.scrollHeight));".format(new_height))
            current_height = new_height
            # Wait to load page
            time.sleep(self.scroll_pause)

    def wait(self, condition):
        return WebDriverWait(self.driver, self.timeout).until(condition)

    def wait_for_el(self, selector):
        return self.wait(EC.presence_of_element_located((
            By.CSS_SELECTOR, selector
        )))

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.quit()

    def quit(self):
        if self.driver and not self.was_passed_instance:
            self.driver.quit()
