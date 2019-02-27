# coding: utf-8
from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8000))
s.send(b'hello')
res = s.recv(8192)
print(res)
