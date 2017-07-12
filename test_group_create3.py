from selenium import webdriver
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_group_create(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)


    def test_test_group_create(self):
        wd = self.wd
        self.open_main_page()
        self.login()
        self.open_group_page()
        self.create_new_group()
        # TODO: Verify group page

    def create_new_group(self):
        # Create
        wd = self.wd
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("test170710")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("TEST170710_1")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("comment170710_1")
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("submit").click()

    def open_group_page(self):
        # Open group page
        self.wd.find_element_by_css_selector(".admin > a:nth-child(1)").click()

    def login(self):
        # Login
        wd = self.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_main_page(self):
        self.wd.get("http://localhost/addressbook/")


    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()