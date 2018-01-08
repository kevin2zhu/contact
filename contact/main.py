#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# filename main.py
from contact_database import *
from user_info import User_info

my = User_info()
my.add_user()
info = my.storge_user()

my_db = Use_database('192.168.70.3', 'root', '10086130', 'contacts', 3306)
#id_num = my_db.use_db()
#insertsql = "SELECT * FROM user"
insertsql = "INSERT INTO user(id,name,phone) values('%s','%s','%s')" % (
    '1', info['name'], info['phone'])
my_db.insert_table(insertsql)
# my_db.insert_table(insertsql)
# else:
#    my_db.insert_table(id_num + 1,result['name'],result['phone'])
