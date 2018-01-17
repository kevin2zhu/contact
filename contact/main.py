#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# filename main.py
from contact_database import *
from user_info import User_info

def conn_db():
    my_db = Use_database('localhost', 'root', '10086130', 'contacts', 3306)
    return my_db
    
def use_db():
    my_db = conn_db()
    num = my_db.use_db()
    id_num = 0
    if num == 0:
        id_num = 1
    else:
        id_num = num + 1
    return id_num

def user_add():
    my_db = conn_db()
    id_num = use_db()
    my = User_info()
    my.add_user()
    info = my.storge_user()
    #判断是否输入其他信息,来选择插入哪条数据
    if info['name'] and info['phone']:
        if 'other' in info:
            yes_othersql = "INSERT INTO user(id,name,phone,address,other) values('%s','%s','%s','%s','%s')" %(
            id_num, info['name'], info['phone'],info['address'],info['other'])
            my_db.insert_table(yes_othersql)
        else:
            no_othersql = "INSERT INTO user(id,name,phone,address) values('%s','%s','%s','%s')" % (
                id_num, info['name'], info['phone'],info['address'])
            my_db.insert_table(no_othersql)
    else:
        print('用户添加失败,请输入必要的信息!')

def show_db():
    my_db = conn_db()
    print('当前用户有:')
    my_db.show_userinfo()

def search_user(name):
    my_db = conn_db()
    my_db.search_db(name)

def userlist():
    my_db = conn_db()
    user = my_db.show_userinfo()
    return user


