# -*- coding: utf-8 -*-

from model.class_for_test import Contact
from random import randrange


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Permanent", lastname="H2", nickname="yana_haus", title="Title",
                                   company="Company22", address="Spb", homephone="8990", mobilephone="3434",
                                   workphone="3434", fax="3443", email="yana.haus@mail.ru", bday="7", bmonth="June",
                                   byear="1987", aday="1", amonth="March", ayear="2000", phone2="phone2"))

    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Кирилл", lastname="245", nickname="yana_haus1", title="Title1", company="Company221",
                      address="Spb1", homephone="89901", mobilephone="34341", workphone="34341", fax="34431",
                      email="yana.haus1@mail.ru", bday="6", bmonth="March", byear="1988", aday="12", amonth="June",
                      ayear="2001", phone2="phone")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact, index)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert old_contacts == new_contacts

    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


