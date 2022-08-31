# -*- coding: utf-8 -*-

from model.class_for_test import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="edit", header="one", footer="two"))
    old_groups = app.group.get_group_list()
    group = Group(name="new2")
    group.id = old_groups[0].id
    app.group.edit_first(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



