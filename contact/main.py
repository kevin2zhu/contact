#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#finename:main.py
import pymysql
connect = pymysql.connect(
    host='192.168.70.3',
    user='root',
    passwd='10086130',
    db='contacts',
    port=3306
   # charset='utf-8'
)

conn = connect.cursor()  #创建操作游标


