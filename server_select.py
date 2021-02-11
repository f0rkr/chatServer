#!/usr/bin/python3

import select
import socket

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 7777))
s.listen(1)

listselect = [s]
while True:
    intr, nint, nit = select.select(listselect, [], [])
    for i in intr:
        if i == s:
            sc, a = s.accept()
            print("new client:", a)
            listselect.append(sc)
        else:
            msg = i.recv(1500)
            if len(msg) == 0:
                listselect.remove(i)
                print("client disconnected")
                i.close()
                break
            i.sendall(msg)
