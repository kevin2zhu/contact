#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# filename startpro.py
from main import *

show_db()
ans = input('\n是否需要新增用户信息(yes/no或者y/n):\n') 
#ans = input('\n是否需要新增用户信息(yes/no或者y/n):\n')
while True:
    if ans == 'yes' or ans == 'y':
        user_add()
        ans = input('是否继续插入用户?(yes/no或者y/n):\n')
    elif ans == 'no' or ans == 'n':
        print('Bye Bye')
        break
    else:
        ans = input('请输入yes/no或者y/n.\n:')

