#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
	print 'waiting for connection...'
	tcpCliSock, addr = tcpSerSock.accept()
	print '...connected from: ', addr

	while True:
		data = tcpCliSock.recv(BUFSIZ)
		if not data:
			break
		tcpCliSock.send('%s %s' % (ctime(), data))

	tcpCliSock.close()

# 아래 줄은 선택사항이다. 서버가 무한 루프를 돌고 있기 때문에 이줄까지 도달하지도 않는다.
tcpSerSock.close()