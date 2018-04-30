# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(firstname="ANTON", middlename="Ivanov", lastname="Gorbachev", nickname="CHIKA",
                                        title="OOO MMM", company="MMMEcM", address="Sweetc-Tula",
                                        home_phone="88008080811",
                                        mobile_phone="89111233212", work_phone="12345678912", fax_phone="98765432132",
                                        email="gxorbachev@mail.ru", email2="gorbach.a.i@dgmail.com",
                                        email3="mail@mail.codm",
                                        homepage="sasdfsdfsdf", ayear="ayear", byear="byear", address2="asdasdasdaxs",
                                        phone2="123", notes="noteCreation"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="F_SSSSS", middlename="M_SSSS", lastname="L_SSSSSS", nickname="N_SSSSSS",
                                     title="OOO SSSSSS", company="SSSSSS", address="SSSSSS", home_phone="89121111122",
                                     work_phone="12345678912", fax_phone="98765432132")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



