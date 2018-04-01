# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit_first_contact(Contact(firstname="SSSSS", middlename="SSSS", lastname="SSSSSS", nickname="CSSSSSS",
                                     title="OOO SSSSSS", company="SSSSSS", address="SSSSSS", home_phone="+7-9121111122",
                                     work_phone="12345678912", fax_phone="98765432132"))
