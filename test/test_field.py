import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def test_name_on_home_page(app):
    name_from_home_page = app.contact.get_contact_list()[0]
    name_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert name_from_home_page.firstname == clear(name_from_edit_page.firstname)
    assert name_from_home_page.lastname == clear(name_from_edit_page.lastname)

def test_adress_on_home_page(app):
    adress_from_home_page = app.contact.get_contact_list()[0]
    adress_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert adress_from_home_page.address == clear(adress_from_edit_page.address)


def test_email_on_home_page(app):
    email_from_home_page = app.contact.get_contact_list()[0]
    email_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert email_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(email_from_edit_page)

def clear(s):
    return re.sub("[- ()]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.workphone, contact.mobilephone, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))