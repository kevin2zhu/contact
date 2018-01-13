#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# filename startpro.py
from main import *

'''def add(result):
    #开始新增用户
    #ans = input('\n是否需要新增用户信息(yes/no或者y/n):\n') 
    #ans = input('\n是否需要新增用户信息(yes/no或者y/n):\n')
    while True:
        ans = result
        if ans == 'yes' or ans == 'y' or ans == 'Y':
            user_add()
            ans = input('是否继续插入用户?(yes/no或者y/n):\n')
        elif ans == 'no' or ans == 'n' or ans =='N':
            print('Bye Bye')
            break
        else:
            ans = input('请输入yes/no或者y/n.\n:')'''

def search():
    #开始查询用户信息
    name = input('如需查询用户信息,请输入用户全称!')
    search_user(name)

show_db()
while True:
    show_db()
    ans = input('\n是否需要新增用户信息(yes/no或者大小写y/n)输入Q或者q退出程序:\n')
    if ans == 'yes' or ans == 'y' or ans == 'Y':
        user_add()
        ans = input('是否继续插入用户?(yes/no或者大写的y/n):\n')
    elif ans == 'no' or ans == 'n' or ans =='N':
        print('退出到主程序中.')
    elif ans == 'q' or ans == 'Q':
        print('Bye Bye')
        break
    else:
        ans = input('请输入yes/no或者y/n.\n:')
