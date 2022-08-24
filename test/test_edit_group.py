# -*- coding: utf-8 -*-

from model.class_for_test import Group


def test_edit_group(app):
    app.group.edit_first(Group(name="new2"))



