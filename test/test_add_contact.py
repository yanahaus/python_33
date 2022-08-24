# -*- coding: utf-8 -*-


from model.class_for_test import Contact


def test_add_contact(app):
    app.contact.create(Contact(name="Test2308", lastname="H2", nickname="yana_haus", title="Title", company="Company22",
                               adress="Spb", home="8990", mobile="3434", work_phone="3434", fax="3443",
                               email="yana.haus@mail.ru", bday="7", bmonth="June", byear="1987", aday="1",
                               amonth="March", ayear="2000"))


def test_add_empty_contact(app):
    app.contact.create(Contact(name="", lastname="", nickname="", title="", company="", adress="", home="", mobile="",
                               work_phone="", fax="", email="", bday="", bmonth="", byear="", aday="", amonth="",
                               ayear=""))