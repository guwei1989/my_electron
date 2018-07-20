#!/usr/bin/env python
# coding:utf-8

import MySQLdb

db = MySQLdb.connect("localhost", "my_blog", "test123", "TESTDB", charset='utf8')
cursor = db.cursor()


