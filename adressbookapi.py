from selenium import webdriver
from selenium.webdriver.common.by import By

class AddressBook:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(10)

    def create_new_group(self, group):
        # Create
        wd = self.wd
        wd.find_element_by_name("new").click()
        if group.name is not None:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.name)
        if group.header is not None:
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header)
        if group.footer is not None:
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("submit").click()

    def open_group_page(self):
        # Open group page
        self.wd.find_element_by_css_selector(".admin > a:nth-child(1)").click()

    def login(self, user, pwd):
        # Login
        wd = self.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(pwd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_main_page(self):
        self.wd.get("http://localhost/addressbook/")

    def message(self):
        el = self.wd.find_element_by_css_selector(".msgbox")
        return el.text

    # TODO: return to group page
    def return_to_group_page(self):
        self.wd.find_element_by_css_selector(".admin > a:nth-child(1)").click()

    def delete_first_group(self):
        wd = self.wd
        checkboxes = wd.find_elements_by_name("selected[]")
        if not checkboxes[0].is_selected():
            checkboxes[0].click()
        wd.find_element_by_css_selector("#content > form:nth-child(2) > input:nth-child(2)").click()

    def Logout(self):
        # Logout
        self.wd.find_element_by_css_selector("#top > form > a").click()

    def destroy(self):
        self.wd.quit()

    def is_element_present(self, by, value):
        return len(self.wd.find_elements(by, value))!= 0

    def is_logged(self):
        return self.is_element_present(By.NAME, "logout")

    def is_groups_present(self):
        self.open_group_page()
        return self.is_element_present(By.NAME, "selected[]")
