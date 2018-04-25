# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("fn_", 10),
            middlename=random_string("mn_", 10),
            lastname=random_string("ln_", 10),
            nickname=random_string("nn_", 10),
            title=random_string("t_", 10),
            company=random_string("c_", 10),
            address=random_string("a_", 10),
            home_phone=random_string("hp_", 10),
            mobile_phone=random_string("mp_", 10),
            work_phone=random_string("wp_", 10),
            fax_phone=random_string("fp_", 10),
            email=random_string("e_",10),
            email2=random_string("e2_", 10),
            email3=random_string("e3_", 10),
            homepage=random_string("hp_", 10),
            ayear=random_string("ay_", 10),
            byear=random_string("by_", 10),
            address2=random_string("a2_", 10),
            phone2=random_string("p2_", 10),
            notes=random_string("n_", 10))
    for i in range(n)
    ]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))