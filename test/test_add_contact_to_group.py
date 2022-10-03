import random
from model.class_for_test import Contact
from model.class_for_test import Group
from fixture.orm import ORMFixture

orm = ORMFixture(host="localhost", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    groups = db.get_group_list()
    contacts = db.get_contact_list()
    if len(groups) == 0:
        app.group.create(Group(name="name", header="one", footer="two"))
        groups = db.get_group_list()
    if len(contacts) == 0:
        app.contact.create(Contact(firstname="Permanent", lastname="H2", nickname="yana_haus", title="Title",
                                   company="Company22", address="Spb", homephone="8990", mobilephone="3434",
                                   workphone="3434", fax="3443", email="yana.haus@mail.ru", bday="7", bmonth="June",
                                   byear="1987", aday="1", amonth="March", ayear="2000", phone2="233333"))
        contacts = db.get_contact_list()

    random_group = random.choice(groups)
    old_contacts_in_group = orm.get_contacts_in_group(random_group)
    contacts_not_in_group = []

    app.contact.append_contact(contacts, old_contacts_in_group, contacts_not_in_group)

    if len(contacts_not_in_group) != 0:
        random_contact = random.choice(contacts_not_in_group)
        app.contact.add_contact_by_id_in_group(random_contact, random_group)
        old_contacts_in_group.append(random_contact)
    else:
        app.contact.create(Contact(firstname="New_not_in_group", lastname="H2", nickname="yana_haus", title="Title",
                                   company="Company22", address="Spb", homephone="8990", mobilephone="3434",
                                   workphone="3434", fax="3443", email="yana.haus@mail.ru", bday="7", bmonth="June",
                                   byear="1987", aday="1", amonth="March", ayear="2000", phone2="233333"))
        new_contact = max(db.get_contact_list(), key=Contact.id_or_max)

        app.contact.add_contact_by_id_in_group(new_contact, random_group)
        old_contacts_in_group.append(new_contact)

    new_contacts_in_group = orm.get_contacts_in_group(random_group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)