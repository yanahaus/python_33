# -*- coding: utf-8 -*-

from model.class_for_test import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Permanent", lastname="H2", nickname="yana_haus", title="Title",
                                   company="Company22", adress="Spb", home="8990", mobile="3434", work_phone="3434",
                                   fax="3443", email="yana.haus@mail.ru", bday="7", bmonth="June", byear="1987",
                                   aday="1", amonth="March", ayear="2000"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="Кирилл", lastname="245", nickname="yana_haus1", title="Title1",
                                           company="Company221", adress="Spb1", home="89901", mobile="34341",
                                           work_phone="34341", fax="34431", email="yana.haus1@mail.ru", bday="6",
                                           bmonth="March", byear="1988", aday="12", amonth="June", ayear="2001")
    contact.id = old_contacts[0].id
    app.contact.edit_first(contact)
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


