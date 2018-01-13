#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# filename startpro.py
from main import *

def search():
    user = userlist()
    #开始查询用户信息
    name = input('\n如需查询用户信息,请输入用户全称:')
    if name == '':
        print('无法查询空用户!')
    elif name in user:
        search_user(name)
    else:
        input('\n查无此人!\n')




show_db()
while True:
    num = input('\n请选择功能选项:\n1)新增用户\n2)查询\n3)退出\n')
    if num == '1':
        user_add()
        while True:
            ans = input('是否继续添加?(y/n)\n')
            if ans == 'y':
                user_add()
            elif ans == 'n':
                break
            else:
                ans = input('请输入y/n.')
   
    elif num == '2':
        search()
        while True:
            ans = input('\n是否继续查询?(y/n):')
            if ans == 'y':
                search()
            elif ans == 'n':
                break
            else:
                ans = input('\n请输入y/n.')    
    elif num == '3':
        print('Bye Bye')
        break

    else:
        print('请输入正确的数字!\n')

    
