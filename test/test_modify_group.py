def test_modify_group(app, init_login, init_group):
    data_for_changing = Group()
    app.open_group_page()
    app.modify_group_page()
    assert "..." in app.message()
    app.return_to_page()