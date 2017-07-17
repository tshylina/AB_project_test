import random

def test_delete_group(app,init_login, init_groups):
    index =random.randrange(app.group_count())

    app.open_group_page()
    app.delete_group(index)
    assert "Group has been removed." in app.message()
    app.return_to_group_page()
