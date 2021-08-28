from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from secrets import pw
from secrets import username as uname
from time import sleep


class LinkedInBot:

    def __init__(self):
        self.driver = webdriver.Chrome("C://Users/User/PycharmProjects/chromedriver")
        self.driver.get("https://LinkedIn.com")

    def log_in(self, username, passwd):
        btn = self.driver.find_element_by_xpath('//input[@name=\"session_key\"]')
        btn.click()
        btn.send_keys(username)

        sleep(2)

        btn = self.driver.find_element_by_xpath('//input[@name=\"session_password\"]')
        btn.click()
        btn.send_keys(passwd)

        sleep(3)

        btn = self.driver.find_element_by_xpath('//button[contains(text(), \"Sign in\")]')
        btn.click()

    def go_to_search(self, param):
        # search_field = self.driver.find_element_by_xpath("//a[@id=\"ember21\"]")    # my network button
        search_field = self.driver.find_element_by_xpath('//input[@class=\"search-global-typeahead__input '
                                                         'always-show-placeholder\"]')
        search_field.send_keys(param)
        sleep(2)
        search_field.send_keys(Keys.ENTER)

        sleep(4)
        people_filter = self.driver.find_element_by_xpath("//button[@aria-label=\"People\"]")
        people_filter.click()

        sleep(4)
        people_filter = self.driver.find_element_by_xpath("//button[@aria-label=\"All filters\"]")
        people_filter.click()

        sleep(4)

        # Click the checkboxes:

        WebDriverWait(self.driver, 20).until(  # Click checkbox '2nd'
            EC.element_to_be_clickable((By.XPATH, "//label[@for='advanced-filter-network-S']"))).click()

        WebDriverWait(self.driver, 20).until(  # Click checkbox '3rd+'
            EC.element_to_be_clickable((By.XPATH, "//label[@for='advanced-filter-network-O']"))).click()

        WebDriverWait(self.driver, 20).until(  # Click checkbox 'Israel'
            EC.element_to_be_clickable((By.XPATH, "//label[@for='advanced-filter-geoUrn-101620260']"))).click()

        # WebDriverWait(self.driver, 20).until(  # Click Industry
        #     EC.element_to_be_clickable((By.XPATH, "//label[@for='advanced-filter-industry-48']"))).click()


        # WebDriverWait(self.driver, 20).until(  # Click Industry checkbox
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Show results')]"))).click()

        sleep(3)
        self.driver.find_element_by_xpath("//button[@aria-label=\"Apply current filters to show results\"]").click()


bot = LinkedInBot()
bot.log_in(uname, pw)
sleep(2)
# search_param = input("Enter search parameter:")
# bot.go_to_search(search_param)
bot.go_to_search("construction")


