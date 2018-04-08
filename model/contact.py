from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home_phone=None, mobile_phone=None, work_phone=None, fax_phone=None, email=None, email2=None, email3=None, homepage=None,
                 byear=None, ayear=None, address2=None, phone2=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax_phone = fax_phone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.lastname == other.lastname or self.lastname is None or other.lastname is None)

    def __repr__(self):
        return "%s:%s" % (self.id, self.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize