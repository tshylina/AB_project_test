from pytest_bdd import given, when, then
from models.group import Group

@given ("a group list")
def old_group_list(db):
    return db.get_group_list()

@given ("a new group with <name>, <header>, <footer>")
def new_group(name, header, footer):
    Group(name=name, header=header, footer=footer)

@when("I add this group to the list")
def add_group(app, init_login, new_group):
    app.open_group_page()
    app.group.create(new_group)
    app.return_to_group_page()


@then("a new group list is equal to the old list with this new group")
def verify_group_create(db, old_group_list, new_group):
    new_group_list = db.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)
    old_group_list.append(new_group)
    assert sorted(old_group_list) == sorted(new_group_list)


@given