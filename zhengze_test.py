#!/usr/bin/env python
# coding:utf-8

import re


pattern = "abc"

ret1 = re.match(pattern, "a778")
ret2 = re.search(pattern, "8999shabc").group()


if __name__ == "__main__":
    print ret1
    print ret2

    print "aaa msu ".strip()