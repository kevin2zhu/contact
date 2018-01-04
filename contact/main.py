#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#finename:main.py
import pymysql
connect = pymysql.connect(
    host='xxxxx',
    user='xxxx',
    passwd='xxxx',
    db='contacts',
    port=3306
   # charset='utf-8'
)

conn = connect.cursor()  #创建操作游标


