from adressbookapi import AddressBook
from models.group import Group
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_group_create(unittest.TestCase):
    def setUp(self):
        self.app = AddressBook()



    def test_test_group_create(self):
        group = Group("comment170710_1", "TEST170710_1", "test170710")
        self.app.open_main_page()
        self.app.login("admin", "secret")
        self.app.open_group_page()
        self.app.create_new_group(group)
        # TODO: Verify group page


    def tearDown(self):
        self.app.destroy()


if __name__ == '__main__':
    unittest.main()