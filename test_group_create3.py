from models.group import Group


def test_group_create(app):
    group = Group("comment170710_1", "TEST170710_1", "test170710")
    app.open_main_page()
    app.login("admin", "secret")
    app.open_group_page()
    app.create_new_group(group)

    #  assert "A new group has been entered into the address book." in app.message()
    # app.return_to_group_page()
    # app.Loguot()

    # TODO: Verify group page
