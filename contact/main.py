#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#filename main.py
class User_info():
    '''创建一个用户信息的类'''
    
    def __init__(self):
       self.users_info = {}
       #pass
        #初始化程序
        #self.name = name
        #self.phone = phone
        #self.other = other
       # print('name:%s,phone:%s,other:%s' %(self.name,self.phone,self.other))
    
    def add_user(self):
        #新增通讯录信息
        self.name= input('请输入姓名:')
        self.phone = input('请输入电话号码:')
        self.other = input('如果还有其他信息请继续输入,如:地址="上海,性别=女"\n:')
        print('信息输入成功!\n') 
    
    def storge_user(self):
        #存储用户信息
        self.users_info['姓名:'] = self.name
        self.users_info['电话号码:'] = self.phone
        if self.other:
            self.users_info['其他信息:'] = self.other
        #for k,v in self.users_info.items():
        #    print(k,v)
        return self.users_info


