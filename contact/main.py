#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# filename main.py
from contact_database import *
from user_info import User_info

my = User_info()
my.add_user()
info = my.storge_user()

my_db = Use_database('192.168.70.3', 'root', '10086130', 'contacts', 3306)
num = my_db.use_db()
id_num = 0
if num == 0:
    id_num = 1
else:
    id_num = num + 1
    
no_othersql = "INSERT INTO user(id,name,phone,address) values('%s','%s','%s','%s')" % (
    id_num, info['name'], info['phone'],info['address'])

yes_othersql = "INSERT INTO user(id,name,phone,address,other) values('%s','%s','%s','%s','%s')" %(
    id_num, info['name'], info['phone'],info['address'],info['other'])

if info['other']:
    my_db.insert_table(yes_othersql)
else:
    my_db.insert_table(no_othersql)
