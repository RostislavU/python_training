# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_del_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(firstname="thisContactWillBeDeleted"))
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(old_contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts)-1 == len(new_contacts)
    old_contacts.remove(old_contact)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
