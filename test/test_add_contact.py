# -*- coding: utf-8 -*-


from model.class_for_test import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="Test3008", lastname="2022", nickname="yana_haus", title="Title", company="Company22",
                      adress="Spb", homephone="8990", mobilephone="3434", workphone="123", fax="3441",
                      email="yana.haus@mail.ru", bday="7", bmonth="June", byear="1987", aday="1",
                      amonth="March", ayear="2000")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
