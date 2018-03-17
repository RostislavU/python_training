# -*- coding: utf-8 -*-
from application import Application
from group import Group
import unittest

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def tearDown(self):
        self.app.destroy()

    def test_add_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="name_group", header="header", footer="footer"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()

if __name__ == '__main__':
    unittest.main()
