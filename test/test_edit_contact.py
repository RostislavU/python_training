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
    app.contact.edit_first_contact(Contact(firstname="SSSSS", middlename="SSSS", lastname="SSSSSS", nickname="CSSSSSS",
                                     title="OOO SSSSSS", company="SSSSSS", address="SSSSSS", home_phone="+7-9121111122",
                                     work_phone="12345678912", fax_phone="98765432132"))
