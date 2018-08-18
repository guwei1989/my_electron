#!/usr/bin/env python
# coding:utf-8
import urllib
import urllib2
import cgi

print cgi.FieldStorage()

print urllib.quote("aa&ss")

print urllib2.quote("%")


def local_test(args):
    a = 3
    print locals()


local_test(4)
