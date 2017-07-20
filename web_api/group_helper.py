from selenium.webdriver.common.by import By


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def is_present(self):
        self.app.open_group_page()
        return self.app.is_element_present(By.NAME, "selected[]")


    def count(self):
        self.app.open_group_page()
        return len(self.app.wd.find_elements_by_name("selected[]"))

    def delete(self, index):
        wd = self.app.wd
        checkboxes = wd.find_elements_by_name("selected[]")
        if not checkboxes[index].is_selected():
            checkboxes[index].click()
        wd.find_element_by_css_selector("#content > form:nth-child(2) > input:nth-child(2)").click()

    def create(self, group):
        # Create
        wd = self.app.wd
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
