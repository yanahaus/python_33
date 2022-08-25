# -*- coding: utf-8 -*-

from model.class_for_test import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="edit", header="one", footer="two"))
    app.group.edit_first(Group(name="new2"))



