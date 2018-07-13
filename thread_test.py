#!/usr/bin/env python
#  coding:utf-8

import threading
import multiprocessing, Queue
import thread
import time
import os
from collections import Iterator

l = threading.Lock()
log_lock = threading.Lock()
i = 0


def new_t(name, delay):
    i = 0
    if i < 5:
        time.sleep(delay)
        i += 1
        print ("This is %s" % name, "i=%d" % i)




class Mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global i
        for o in range(10000):
            # l.acquire()
            i += 1
            # l.release()
        print (i)


# def println(msg):
#     log_lock.acquire()
#     print msg
#     log_lock.release()
#
#
# def work(my_name):
#     println(my_name + ' is waiting')
#     l.acquire()
#     println(my_name + ' got lock')
#     time.sleep(10)
#     println(my_name + ' is released')
#     l.release()
#
#
# ts = []
# for i in range(2):
#     t = threading.Thread(target=work, args=('T%d' % i,))
#     t.start()
#     ts.append(t)
#
# for t in ts:
#     t.join()


def warp(func):
    def inner(*args, **kwargs):
        print ("func_name is %s" % func.__name__)
        return func(*args, **kwargs)

    return inner


@warp
def do_something(msg):
    print ("hello %s" % msg)


# 列表生成式
lis = [x * x for x in range(10)]

# 生成器
generator_ex = (x * x for x in range(10))


# print (isinstance((x for x in range(10)), Iterator))

# print (dir(generator_ex))
# for o in range(3):
#     print (generator_ex.next())


def yield_test():
    i = 0
    for i in range(10):
        i += 1
        yield i


a = yield_test()
for i in range(5):
    print (a.next())


print (os.path.dirname(os.path.abspath(__file__)))

# if __name__ == "__main__":
# thread_list = list()
#
# for i in range(5):
#     my_thread = Mythread()
#     thread_list.append(my_thread)
#     my_thread.start()
#
# for thread in thread_list:
#     thread.join()

# do_something("python")
