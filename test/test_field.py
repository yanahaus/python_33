import re


def test_field_on_home_page(app):
    field_from_home_page = app.contact.get_contact_list()[0]
    field_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert field_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(field_from_edit_page)
    assert clear(field_from_home_page.firstname) == clear(field_from_home_page.firstname)
    assert clear(field_from_edit_page.lastname) == clear(field_from_edit_page.lastname)
    assert clear(field_from_home_page.address) == clear(field_from_edit_page.address)
    assert field_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(field_from_edit_page)


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