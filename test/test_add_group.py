# -*- coding: utf-8 -*-
from model.class_for_test import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="name", header="one", footer="two"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

