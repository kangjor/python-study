#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *

# 서버의 호스트와 포트
HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

# 무한 루프를 돌고 있지만 두가지 경우에는 끝날 수 있다.
# 1. 사용자가 아무것도 입력하지 않고 엔터를 칠 경우
# 2. 어떤 이유로든 서버가 종료되어 recv() 메소드가 호출이 안될 경우
while True:
	data = raw_input('> ')
	if not data:
		break
	tcpCliSock.send(data)

	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print data

tcpCliSock.close()