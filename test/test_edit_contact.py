# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="ANTON", middlename="Ivanov", lastname="Gorbachev", nickname="CHIKA",
                                        title="OOO MMM", company="MMMEcM", address="Sweetc-Tula",
                                        home_phone="+7-912-111-11-11",
                                        mobile_phone="89111233212", work_phone="12345678912", fax_phone="98765432132",
                                        email="gxorbachev@mail.ru", email2="gorbach.a.i@dgmail.com",
                                        email3="mail@mail.codm",
                                        homepage="sasdfsdfsdf", ayear="ayear", byear="byear", address2="asdasdasdaxs",
                                        phone2="123", notes="noteCreation"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="SSSSS", middlename="SSSS", lastname="SSSSSS", nickname="CSSSSSS",
                                     title="OOO SSSSSS", company="SSSSSS", address="SSSSSS", home_phone="+7-9121111122",
                                     work_phone="12345678912", fax_phone="98765432132")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



