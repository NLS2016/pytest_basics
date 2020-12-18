from selenium import webdriver
import time

class HomePage:

    welcome_link = "Welcome nivetha"
    logout_link  = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def click_welcome(self):
        self.driver.find_element_by_partial_link_text(self.welcome_link).click()

    def click_logout(self):
        time.sleep(2)
        self.driver.find_element_by_link_text(self.logout_link).click()

    def click_leave(self):
        pass
