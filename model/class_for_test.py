from sys import maxsize

class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


class Contact:

    def __init__(self, name=None, lastname=None, nickname=None, title=None, company=None, adress=None, home=None,
                 mobile=None, work_phone=None, fax=None, email=None, bday=None, bmonth=None, byear=None, aday=None,
                 amonth=None, ayear=None, id=None):
        self.name = name
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.adress = adress
        self.home = home
        self.mobile = mobile
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and\
               self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize