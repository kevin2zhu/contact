#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#filename user_add.py
from contact_database import *
from main import User_info

my = User_info()
my.add_user()
result = my.storge_user()

for k,v in result.items():
    print(k,v)
