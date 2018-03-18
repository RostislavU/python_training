# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_contact(Contact(firstname="ANTON", middlename="Ivanov", lastname="Gorbachev", nickname="CHIKA",
                     title="OOO MMM", company="MMMEcM", address="Sweetc-Tula", home_phone="+7-912-111-11-11",
                     mobile_phone="89111233212", work_phone="12345678912", fax_phone="98765432132",
                     email="gxorbachev@mail.ru", email2="gorbach.a.i@dgmail.com", email3="mail@mail.codm",
                     homepage="sasdfsdfsdf", ayear="ayear", byear="byear", address2="asdasdasdaxs",
                     phone2="123", notes="noteCreation"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")

    app.contact.add_contact(Contact(firstname="", middlename="", lastname="", nickname="",
                     title="", company="", address="", home_phone="",
                     mobile_phone="", work_phone="", fax_phone="",
                     email="", email2="", email3="",
                     homepage="", ayear="", byear="", address2="",
                     phone2="", notes=""))

    app.session.logout()