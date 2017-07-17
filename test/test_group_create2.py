# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

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
    
    def test_(self):
        success = True
        wd = self.wd
        # open main page
        wd.get("http://localhost/addressbook/group.php")
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys("\\undefined")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("\\undefined")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        # open group page
        wd.find_element_by_css_selector(".admin > a:nth-child(1)").click()
        # create
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
        # TO DO: return to group, verify group
        # return to group page
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
