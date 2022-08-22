# -*- coding: utf-8 -*-


from model.class_for_test import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(name="Yana1", lastname="H21", nickname="yana_haus1", title="Title1", company="Company221",
                               adress="Spb1", home="89901", mobile="34341", work_phone="34341", fax="34431",
                               email="yana.haus1@mail.ru", bday="6", bmonth="March", byear="1988", aday="12",
                               amonth="June", ayear="2001"))
    app.session.logout()

