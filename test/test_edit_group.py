# -*- coding: utf-8 -*-

from model.class_for_test import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="nnnn", header="tttt", footer="sss"))
    app.session.logout()



