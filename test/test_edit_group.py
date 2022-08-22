# -*- coding: utf-8 -*-

from model.class_for_test import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="name1", header="one1", footer="two1"))
    app.session.logout()



