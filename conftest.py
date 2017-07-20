import json
import os.path

import pytest

from data.groups_data import groups_list
from models.group import Group
from web_api.adressbookapi import AddressBook
from db_api.adressbook_db import AddressbookDB

def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json")

@pytest.fixture(scope="session")
def config(request):
    file_name = request.config.getoption("--config")
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_name) as f:
        return json.load(f)


@pytest.fixture()
def app(selenium, config):
    app = AddressBook(selenium, base_url=config["web"]["base_url"])
    app.open_main_page()
    yield app
    app.destroy()

@pytest.fixture(scope="session")
def db(config):
    dbfixture = AddressbookDB(**config["db"])
    yield  dbfixture
    dbfixture.close()

@pytest.fixture()
def init_login(app,config):
    if not app.session.is_logged():
        app.session.login(config["web"]["username"], config["web"]["password"])
    yield
    app.session.Logout()

@pytest.fixture()
def init_groups(app):
    if not app.group.is_present():
        app.group.create(Group(name="Test"))
# TODO: del 0:1
@pytest.fixture(params=groups_list[0:1], ids=[str(g) for g in groups_list[0:1]])
def group (request):
    return request.param


