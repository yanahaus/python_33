from model.class_for_test import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name", header="one", footer="two"))
    app.group.delete_first()
