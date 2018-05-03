from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1",
                user="root",
                password="",
                database="addressbook")


def test_add_contact_in_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(firstname="thisContactWillBeDeleted"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="thisGroupWillBeDeleted"))
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    assert app.group.get_contact_in_group(group) == db.get_contact_in_group(group)
    app.contact.add_contact_to_group(contact, group)
