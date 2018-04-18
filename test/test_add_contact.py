# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname,
            title=title, company=company, address=address, home_phone=home_phone, mobile_phone=mobile_phone,
            work_phone=work_phone, fax_phone="fax_phone", email=email, email2=email2, email3=email3,
            homepage=homepage, ayear=ayear, byear="byear", address2=address2, phone2=phone2, notes=notes)

    for firstname in ["", random_string("fn_", 10)]
    for middlename in ["", random_string("mn_", 10)]
    for lastname in ["", random_string("ln_", 10)]
    for nickname in ["", random_string("nn_", 10)]
    for title in ["", random_string("t_", 10)]
    for company in ["", random_string("comp_", 10)]
    for address in ["", random_string("addr_", 10)]
    for address2 in ["", random_string("addr2_", 10)]
    for email in ["", random_string("e_", 10)]
    for email2 in ["", random_string("e2_", 10)]
    for home_phone in ["", "".join([random.choice(string.digits) for s in range(random.randrange(10))])]
    for mobile_phone in ["", "".join([random.choice(string.digits) for t in range(random.randrange(10))])]
    for work_phone in ["", "".join([random.choice(string.digits) for r in range(random.randrange(10))])]
    for email3 in ["", random_string("e3_", 10)]
    for homepage in ["", random_string("hp_", 11)]
    for ayear in ["", random_string("", 10)]
    for fax_phone in ["", "".join([random.choice(string.digits) for i in range(random.randrange(10))])]
    for notes in ["", random_string("notes_", 10)]
    for phone2 in ["", "".join([random.choice(string.digits) for v in range(random.randrange(10))])]
    for byear in ["", random_string("", 10)]
    ]


@pytest.mark.parametrize("test_contact", testdata)
def test_add_contact(app, test_contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact(test_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(test_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



'''
def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact()
    app.contact.add_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
'''