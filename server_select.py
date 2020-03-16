#!/usr/bin/python3

import select
import socket

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 7777))
s.listen(1)

l = [s]
ll = []
la = []
while True:
    intr, nint, nit = select.select(l, ll, la)
    for i in intr:
        if i == s:
            sc, a = s.accept()
            print("new client:", a)
            l.append(sc)
        else:
            msg = sc.recv(1500)
            if len(msg) == 0:
                l.remove(sc)
                print("client disconnected")
                sc.close()
                break
            sc.sendall(msg)
