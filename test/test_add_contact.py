# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.add_contact import testdata


@pytest.mark.parametrize("test_contact", testdata)
def test_add_contact(app, test_contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact(test_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(test_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
