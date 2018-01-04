#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#finename:contact_databse.py
import pymysql

class Use_database():
    '''连接数据库的类'''
    def connect_db():
        #连接数据库
        connect = pymysql.connect(
            host='192.168.70.3',
            user='root',
            passwd='10086130',
            db='mysql',
            port=3306
        )
        return connect                #返回connect供其他函数调用

    def use_db():
        #使用数据库中的数据
        conn = connect_db()
        cursor = conn.cursor()         #创建操作游标
        cursor.execute('USE contacts') #使用游标+execute执行SQL命令 
        cursor.execute('DESC user')
        rows = cursor.fetchall()      
        #fetchall()接收全部的返回结果行，若没有则返回的是表的内容个数 int型 
        if rows:
            row = [i for i in rows]
            print(row)
        else:
            pass
        #print('里面没有用户信息,您可以新增信息.')

    def insert_table():
        '''插入用户信息表'''
        sql = """INSERT INTO user()"""  #()中的参数可以自行设置 



