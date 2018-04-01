from model.group import Group


def test_edit_first_group_name(app):
    app.session.login(username="admin", password="secret")
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="newName"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    app.session.logout()


def test_edit_first_group_header(app):
    app.session.login(username="admin", password="secret")
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="NewHeader"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    app.session.logout()