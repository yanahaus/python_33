from model.class_for_test import Contact
import random
import string
import re

testdata = [Contact(firstname="Ivan", lastname="Petrov", nickname="IP", title="NN", company="Pixar", address="SPB",
                    homephone="89822521213",
                    mobilephone="8982252121d", workphone="8982252121d", fax="89822521213", email="test@mail.ru",
                    bday="1", bmonth="June", byear="1987", aday="1", amonth="March",
                    ayear="2000", phone2="9877"),
            Contact(firstname="Anna", lastname="Schwez", nickname="AS", title="NN", company="Disney", address="SPB",
                    homephone="89822521213",
                    mobilephone="8982252121d", workphone="8982252121d", fax="89822521213", email="test@mail.ru",
                    bday="1", bmonth="June", byear="1987", aday="1", amonth="March",
                    ayear="2000", phone2="9877"),
            ]


"""def random_string(prefix, maxlen):
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
                    byear="1987", aday="1", amonth="March", ayear="2000", phone2=random_number("+79")) for i in range(3)]"""