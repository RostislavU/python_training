# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts, db, check_ui):
    test_contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.add_contact(test_contact)
    assert len(old_contacts) + 1 == len(db.get_contact_list())
    new_contacts = db.get_contact_list()
    old_contacts.append(test_contact)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
