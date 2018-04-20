# -*- coding: utf-8 -*-
from model.group import Group
import random
import string
import os.path
import json

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name_", 10)]
    for header in ["", random_string("header_", 10)]
    for footer in ["", random_string("footer_", 10)]
]


file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../data/group.json")

with open(file, "w") as f:
    f.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))