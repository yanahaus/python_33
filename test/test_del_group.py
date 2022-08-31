from model.class_for_test import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name", header="one", footer="two"))
    old_groups = app.group.get_group_list()
    app.group.delete_first()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups
