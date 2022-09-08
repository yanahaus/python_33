# -*- coding: utf-8 -*-

from model.class_for_test import Contact
import pytest
import random
import string
import re

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    stroka = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    stroka = re.sub('\s+', ' ', stroka).strip()
    return stroka


def random_number(prefix):
    symbols = string.digits
    number = prefix + "".join([random.choice(symbols) for i in range(10)])
    return number


testdata = [Contact(firstname="", lastname="", nickname="", title="", company="", address="", homephone="",
                    mobilephone="", workphone="", fax="", email="", bday="", bmonth="", byear="", aday="", amonth="",
                    ayear="", phone2="")] + [Contact(firstname=random_string("firstname", 10),
                    lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                    title=random_string("title", 10), company=random_string("company", 10),
                    address=random_string("adress", 10), homephone=random_number("+79"), mobilephone=random_number("+79"),
                    workphone=random_number("+79"), fax="3441", email="yana.haus@mail.ru", bday="7", bmonth="June",
                    byear="1987", aday="1", amonth="March", ayear="2000", phone2=random_number("+79")) for i in range(3)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
