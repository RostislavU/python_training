import re
from model.contact import Contact


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def test_all_info_on_home_page(app, db):
    contacts_from_hp = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(map(merge_mail_like_on_home_page, map(merge_phones_like_on_home_page, db.get_full_contact_list())), key=Contact.id_or_max)
    assert contacts_from_hp == contacts_from_db
    for item in range(len(contacts_from_db)):
        assert clear(contacts_from_hp[item].all_mails_from_home_page) == clear(contacts_from_db[item].all_mails_from_home_page)
        assert clear(contacts_from_hp[item].all_phones_from_home_page) == clear(contacts_from_db[item].all_phones_from_home_page)
        assert re.sub(" ", "", contacts_from_hp[item].address) == re.sub(" ", "", contacts_from_db[item].address)


def merge_phones_like_on_home_page(contact):
    contact.all_phones_from_home_page = "\n".join(filter(lambda x: x != "",
                                                         filter(lambda x: x is not None,
                                                         [contact.home_phone, contact.mobile_phone,
                                                          contact.work_phone, contact.phone2])))
    return contact


def merge_mail_like_on_home_page(contact):
    contact.all_mails_from_home_page = "\n".join(filter(lambda x: x != "",
                                                        filter(lambda x: x is not None,
                                                               [contact.email, contact.email2,
                                                                contact.email3])))
    return contact


def clear(s):
    return re.sub("[() -]", "", s)

