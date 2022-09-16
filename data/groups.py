from model.class_for_test import Group
import random
import string
import re


testdata = [
    Group(name="group_name", header="header_group", footer="footer_group"),
    Group(name="group_name1", header="header_group1", footer="footer_group1")
]

"""
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    stroka = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    stroka = re.sub('\s+', ' ', stroka).strip()
    return stroka


testdata = [Group(name="", header="", footer="")] + [Group(name=random_string("group_name", 10),
                                                           header=random_string("header_group", 20),
                                                           footer=random_string("footer_group", 20)) for i in range(3)]"""


