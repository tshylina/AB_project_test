import pytest
from adressbookapi import AddressBook
from models.group import Group

@pytest.fixture(scope ="session")
def app():
    app = AddressBook()
    app.open_main_page()
    yield app
    app.destroy()

@pytest.fixture()
def init_login(app):
    if not app.is_logged():
        app.login("admin", "secret")
    yield
    # app.Logout()

@pytest.fixture()
def init_groups(app):
    if not app.is_groups_present():
        app.create_new_group(Group(name="Test"))

groups = [
    Group("TEST170710_1","comment170710_1",  "test170710"),
    Group("TEST"),
]

@pytest.fixture(params=groups, ids=[str(g) for g in groups])
def group (request):
    return request.param