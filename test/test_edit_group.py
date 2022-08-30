# -*- coding: utf-8 -*-

from model.class_for_test import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="edit", header="one", footer="two"))
    old_groups = app.group.get_group_list()
    app.group.edit_first(Group(name="new2"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)




