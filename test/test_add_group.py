# -*- coding: utf-8 -*-

from model.class_for_test import Group


def test_add_group(app):
    app.group.create(Group(name="name", header="one", footer="two"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

