from model.class_for_test import Group
from random import randrange
import random

def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="edit", header="one", footer="two"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    old_group_id = old_groups[index].id
    group = Group(name="new2")
    app.group.edit_group_by_id(group, old_group_id)
    new_groups = db.get_group_list()
    old_groups[index] = group
    old_groups[index].id = new_groups[index].id
    old_groups[index].header = new_groups[index].header
    old_groups[index].footer = new_groups[index].footer
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


"""old_version
def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="edit", header="one", footer="two"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="new2")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
"""




"""
def test_edit_group(app):
    if len(app.group.get_group_list()) == 0:
        app.group.create(Group(name="edit", header="one", footer="two"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="new2")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    """

