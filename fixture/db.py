import pymysql.cursors
from model.class_for_test import Group
from model.class_for_test import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email from addressbook")
            for row in cursor:
                (id, firstname, lastname, address, homephone, mobilephone, workphone, email) = row
                list.append(Contact(firstname=firstname, lastname=lastname, id=str(id), homephone=homephone,
                                    mobilephone=mobilephone, workphone=workphone, address=address, email=email))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()



