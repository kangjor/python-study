#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *

# 서버의 호스트와 포트
HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)



while True:
	tcpCliSock = socket(AF_INET, SOCK_STREAM)
	tcpCliSock.connect(ADDR)

	data = raw_input('> ')

	if not data:
		break

	# socket 모듈과 달리
	# 서버에 핸들러 클래스가 소켓을 파일처럼 다루기 때문에 행 종료문자(\n)를 보내야 한다.
	tcpCliSock.send(data + '\n')
	data = tcpCliSock.recv(BUFSIZ)

	if not data:
		break
	print data

	tcpCliSock.close()