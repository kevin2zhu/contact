#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#filename user_add.py
from contact_database import *
from main import User_info

my = User_info()
my.add_user()
result = my.storge_user()

my_db = Use_database('192.168.1.40','root','10086130','contacts',3306)
id_num = my_db.use_db()
insertsql = "INSERT INTO user(id,name,phone)\
        values(%s,%s,%s)" %\
        (1,result['name'],result['phone'])
my_db.insert_table(insertsql)
#else:
#    my_db.insert_table(id_num + 1,result['name'],result['phone'])
