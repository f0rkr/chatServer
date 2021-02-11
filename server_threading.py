#!/usr/bin/python3
import socket
import threading

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 7777))
s.listen(1)

def start(sc):
        while True:
            msg = sc.recv(1500)
            if len(msg) == 0:
                print("client disconnected")
                sc.close()
                break
            sc.sendall(msg)

while True:
    sc, a = s.accept()
    print("new client:", a)
    t = threading.Thread(None, start, None, (sc,))
    t.start()
