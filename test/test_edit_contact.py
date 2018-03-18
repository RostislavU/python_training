# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(Contact(firstname="SSSSS", middlename="SSSS", lastname="SSSSSS", nickname="CSSSSSS",
                     title="OOO SSSSSS", company="SSSSSS", address="SSSSSS", home_phone="+7-912-111-11-22",
                     mobile_phone="89111233212", work_phone="12345678912", fax_phone="98765432132",
                     email="SSSSSS@mail.ru", email2="gorbach.a.i@dgmail.com", email3="mail@mail.codm",
                     homepage="sasSSSSSS", ayear="2011", byear="2013", address2="d6ydr6ydr5",
                     phone2="321", notes="sry5sr5ysrd5y"))
    app.session.logout()
