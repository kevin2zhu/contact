#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#finename:contact_databse.py
import pymysql

class Use_database():
    '''连接数据库的类'''
    
    def __init__(self,host,user,passwd,dbname,port):
        #初始化程序,初始化连接的一些参数
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.port = port

    def connect_db(self):
        #连接数据库
        connect = pymysql.connect(
            self.host,
            self.user,
            self.passwd,
            self.dbname,
            self.port
        )
        return connect

    def use_db(self):
        #使用数据库中的数据
        connect = self.connect_db()
        cur = connect.cursor()
        cur.execute('USE contacts') #使用游标+execute执行SQL命令 
        cur.execute('SELECT id = 1 FROM user')
        rows = cur.fetchall()      
        #fetchall()接收全部的返回结果行，若没有则返回的是表的内容个数 int型 
        if rows:
            row = [i for i in rows]
            return row[0]
        else:
            print('此表为空!')
            return 0

    def insert_table(self,sql):
        '''插入用户信息表'''
        db = self.connect_db()
        try:
            cur.execute(sql)
            db.commit()
            print('执行测试成功,可以回滚.\n')
            print('roll_back ing...')
            db.rollback()
        except Exception:
            print('发生异常',Exception)
            db.rollback()
        finally:
            db.rollback()
