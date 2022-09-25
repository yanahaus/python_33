import re
from model.class_for_test import Contact


def test_field_on_home_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contacts_from_home_page)):
        assert clear(contacts_from_home_page[i].firstname) == clear(contacts_from_db[i].firstname)
        assert clear(contacts_from_home_page[i].lastname) == clear(contacts_from_db[i].lastname)
        assert clear(contacts_from_home_page[i].address) == clear(contacts_from_db[i].address)
        assert contacts_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[i])
        assert contacts_from_home_page[i].all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[i])


"""Сравнение одного контакта
def test_field_on_home_page(app):
    field_from_home_page = app.contact.get_contact_list()[0]
    field_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert field_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(field_from_edit_page)
    assert clear(field_from_home_page.firstname) == clear(field_from_home_page.firstname)
    assert clear(field_from_edit_page.lastname) == clear(field_from_edit_page.lastname)
    assert clear(field_from_home_page.address) == clear(field_from_edit_page.address)
    assert field_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(field_from_edit_page)
"""


def clear(s):
    return re.sub("[\s ()-]", "", s)


def clear_email(s):
    return re.sub(" +", " ", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear_email(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))