# -*- coding: utf-8 -*-
from model.contact import Contact

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="thisContactWillBeDeleted"))
    app.contact.delete_contact()
