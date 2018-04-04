from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="thisGroupWillBeDeleted"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="newName"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="thisGroupWillBeDeleted"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="NewHeader"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)