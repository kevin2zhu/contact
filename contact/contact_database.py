#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# finename:contact_databse.py
import pymysql


class Use_database():
    '''连接数据库的类'''

    def __init__(self, host, user, passwd, dbname, port):
        # 初始化程序,初始化连接的一些参数
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.port = port

    def connect_db(self):
        # 连接数据库
        self.connect = pymysql.connect(
            self.host,
            self.user,
            self.passwd,
            self.dbname,
            self.port
        )
        return self.connect


    def use_db(self):
        # 使用数据库中的数据
        connect = self.connect_db()
        cur = connect.cursor()
        cur.execute('USE contacts')  # 使用游标+execute执行SQL命令
        cur.execute('SELECT id FROM user')
        rows = cur.fetchall()
        # fetchall()接收全部的返回结果行，若没有则返回的是表的内容个数 int型
        if rows:
            return rows[-1][0]
        else:
            return 0
        connect.close()

    def show_userinfo(self):
        #展示数据库中的数据
        userlist = []
        connect = self.connect_db()
        cur = connect.cursor()
        cur.execute('SELECT * FROM user')
        rows = cur.fetchall()
        if rows:
            [userlist.append(i[1]) for i in rows]
            for user in userlist:
                print(user)
            return userlist
        else:
            print('抱歉,暂无用户信息!')
        connect.close()

    def search_db(self,name):
        #查询用户信息
        connect = self.connect_db()
        cur = connect.cursor()
        cur.execute('SELECT * FROM user WHERE name="%s"'% name)
        rows = cur.fetchall()
        if rows:
            if rows[0][-1]:
                print('姓名:%s,电话:%s,地址:%s,其他:%s'%(rows[0][1],rows[0][2],rows[0][3],rows[0][4]))
            else:
                print('姓名:%s,电话:%s,地址:%s'%(rows[0][1],rows[0][2],rows[0][3]))
        else:
            print('暂无该用户信息!')
        connect.close()

    def insert_table(self, sql):
        '''插入用户信息表'''
        conn = self.connect_db()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            print('用户新增成功!')
            conn.close()
        except Exception:
            print('用户增加失败请重试!')
            conn.close()


#mydb = Use_database('localhost','root','10086130','contacts',3306)
#mydb.use_db()
#mydb.search_db('科比')
