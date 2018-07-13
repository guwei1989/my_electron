#!/usr/bin/env python
# coding:utf-8


def list_ob(n):
    for i in range(n):
        if i < 10:
            i += 1
            yield i


def consumer():
    r = 'here'
    while True:
        n1 = yield r
        if not n1:
            return
        print('[CONSUMER] Consuming %s...' % n1)
        r = '200 OK' + str(n1)


def produce(c):
    aa = c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r1 = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r1)
    c.close()


if __name__ == "__main__":
    # gen_obj = list_ob(30)
    #
    # print (dir(gen_obj))
    # print next(gen_obj)
    #
    # print type(gen_obj)
    # # for a in gen_obj:
    # #     print (a)
    #
    c = consumer()
    # produce(c)
    b=c.next()
    a=c.send(1)
    print a