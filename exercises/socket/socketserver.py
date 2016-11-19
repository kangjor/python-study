#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
SocketServer 모듈을 이용한 서버 예제이다.
표준 라이브러리에 있는 하이레벨 모듈(3.x 에서는 socketserver로 이름이 바뀌었다.)
이 모듈의 목적은 네트워크 클라이언트와 서버를 만들때 매번 반복해야 하는 준비 과정을 줄여주는것이다.
"""

from SocketServer import (TCPServer as TCP, 
	StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
	def handle(self):
		print '....connected from: ', self.client_address
		self.wfile.write('[%s] %s\n' % (ctime(), self.rfile.readline().strip()))


tcpServ = TCP(ADDR, MyRequestHandler)
print 'waiting for connection...'

# 사용자 요청을 기다리는 서비스는 무한 루프에 들어간다.
tcpServ.serve_forever()