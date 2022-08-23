# -*- coding: utf-8 -*-

from model.class_for_test import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="new2"))
    app.session.logout()



