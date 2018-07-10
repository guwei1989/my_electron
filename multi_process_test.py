#!/usr/local/bin/python
# coding= utf-8

from multiprocessing import Queue, Process
import os
import time
import random


# 添加数据函数
def proc_write(queue, urls):
    print("进程(%s)正在写入..." % (os.getpid()))
    for url in urls:
        queue.put(url)
        print("%s被写入到队列中" % (url))
        time.sleep(random.random() * 3)


# 读取数据函数
def proc_read(queue):
    print("进程(%s)正在读取..." % (os.getpid()))

    while True:
        url = queue.get()
        print("从队列中提取到:%s" % (url))


if __name__ == "__main__":
    queue = Queue()
    proc_writer1 = Process(target=proc_write, args=(queue, ["ur1", "ur2", "ur3", "ur4"]))
    proc_writer2 = Process(target=proc_write, args=(queue, ["ur5", "ur6", "ur7", "ur8"]))
    proc_reader = Process(target=proc_read, args=(queue,))
    proc_writer1.start()
    proc_writer2.start()
    proc_reader.start()
    proc_writer1.join()
    proc_writer2.join()
    proc_reader.terminate()
