#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#filename user_info.py
class User_info():
    '''创建一个用户信息的类'''
    
    def __init__(self):
       self.user_info = {}
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
        self.address = input('请输入地址,如不输入则默认为空:\n:')
        self.other = input('如果还有其他信息请继续输入,如:性别=女.."\n:')
        print('信息录入成功!\n') 
    
    def storge_user(self):
        #存储用户信息
        self.user_info['name'] = self.name
        self.user_info['phone'] = self.phone
        if self.address:
            self.user_info['address'] = self.address
        else:
            self.user_info['address'] = ''
        if self.other:
            self.user_info['other'] = self.other
        return self.user_info

