from selenium import webdriver

from web_api.group_helper import GroupHelper
from web_api.session_helper import SessionHelper

class AddressBook:
    def __init__(self, driver, base_url):
        self.wd = driver
        self.wd.implicitly_wait(1)
        self.base_url = base_url
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_group_page(self):
        # Open group page
        self.wd.find_element_by_css_selector(".admin > a:nth-child(1)").click()


    def open_main_page(self):
        self.wd.get(self.base_url)

    def message(self):
        el = self.wd.find_element_by_css_selector(".msgbox")
        return el.text

    # TODO: return to group page
    def return_to_group_page(self):
        self.wd.find_element_by_css_selector(".admin > a:nth-child(1)").click()

    def destroy(self):
        self.wd.quit()

    def is_element_present(self, by, value):
        return len(self.wd.find_elements(by, value))!= 0



