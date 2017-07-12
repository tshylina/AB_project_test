import pytest
from adressbookapi import AddressBook


@pytest.fixture()
def app():
    a = AddressBook()
    yield a
    a.destroy()