from model.class_for_test import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Permanent", lastname="H2", nickname="yana_haus", title="Title",
                                   company="Company22", adress="Spb", homephone="8990", mobilephone="3434",
                                   workphone="3434", fax="3443", email="yana.haus@mail.ru", bday="7", bmonth="June",
                                   byear="1987", aday="1", amonth="March", ayear="2000"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


