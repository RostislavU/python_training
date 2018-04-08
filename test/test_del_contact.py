# -*- coding: utf-8 -*-
from model.contact import Contact

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="thisContactWillBeDeleted"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)-1 == len(new_contacts)
    old_contacts[0:1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
