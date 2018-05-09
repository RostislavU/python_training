from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1",
                user="root",
                password="",
                database="addressbook")


def test_del_contact_from_group(app, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(firstname="thisContactWillBeDeleted"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="thisGroupWillBeDeleted"))
    group = random.choice(db.get_group_list())
    contact = random.choice(db.get_contact_not_in_group(group))
    if contact not in db.get_contact_in_group(group):
        app.contact.add_contact_to_group(contact, group)
    number_contact_in_group = len(db.get_contact_in_group(group))
    app.contact.del_contact_from_group(contact, group)
    assert contact not in db.get_contact_in_group(group)
    assert number_contact_in_group - 1 + len(db.get_contact_not_in_group(group)) == len(db.get_contact_list())
    if check_ui:
        assert app.group.get_contact_in_group(group) == db.get_contact_in_group(group)