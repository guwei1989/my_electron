#!/usr/bin/env python
# coding:utf-8

from gevent import monkey

monkey.patch_all()
import gevent
from gevent import pywsgi
from flask import Flask
from gevent.queue import Queue

app = Flask(__name__)


@app.route("/")
def index():
    return "gevent test"


# pywsgi.WSGIServer(("0.0.0.0", 5000), app).serve_forever()


def func1():
    for i in range(10):
        print "func1..."
        q.put("func1 in")


def func2():
    for i in range(10):
        print "func2 ..."
        ret = q.get()
        print "func2 get res: {info}".format(info=ret)

q = Queue()
gevent.joinall(
     [
        gevent.spawn(func2),
        gevent.spawn(func1),
     ]
 )


# if __name__ == "__main__":
    # app.run()
