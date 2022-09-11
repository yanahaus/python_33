# -*- coding: utf-8 -*-
from model.class_for_test import Group
import pytest
import random
import string
import re


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    stroka = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    stroka = re.sub('\s+', ' ', stroka).strip()
    return stroka


testdata = [Group(name="", header="", footer="")] + [Group(name=random_string("group_name", 10), header=random_string("header_group", 20),
                  footer=random_string("footer_group", 20)) for i in range(5)]

"""Пример реализации комбинации значений
testdata = [Group(name=name, header=header, footer=footer)
            for name in ["", random_string("group_name", 10)]
            for header in ["", random_string("header_group", 20)]
            for footer in ["", random_string("footer_group", 10)]
            ]
            ]"""


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)





