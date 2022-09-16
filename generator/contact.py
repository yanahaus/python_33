from model.class_for_test import Contact
import random
import string
import re
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
                    byear="1987", aday="1", amonth="March", ayear="2000", phone2=random_number("+79")) for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))