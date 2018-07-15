#!/usr/bin/env python
# coding:utf-8

import socket
import sys
import traceback
import threading
import time


def client_test(ip, textport):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    port = int(textport)

    c.connect((ip, port))

    data = "this is client send content"
    c.send(data)

    print "data had send, looking for replies..."
    while 1:
        buf = c.recv(2048)
        if not len(buf):
            break

        print "reply data is: %s" % buf


def server_test():
    host = '127.0.0.1'  # Bind to all interfaces
    port = 51500

    addr = (host, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(addr)
    s.listen(5)
    # Step4: 监听该端口上的连接
    while 1:
        try:
            conn, address = s.accept()
            char = conn.recv(2048)
            print "server recv info: %s" % char
            conn.send(
                "server has received succeefully, addr is {addr} content is: {info}".format(addr=address, info=char))
        except:
            print "traceback"
            traceback.print_exc()


if __name__ == "__main__":
    client = threading.Thread(target=client_test, args=("127.0.0.1", 51500))
    server = threading.Thread(target=server_test)

    client.start()
    server.start()

    client.join()
    server.join()
