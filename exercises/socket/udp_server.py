#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

"""
소켓 유형은 AF_UNIX, AF_LOCAL, AF_INET, AF_NETLINK, AF_TIPC 등이 있다.
네트워크 소켓은 AF_INET(ipv4), AF_INET6(ipv6)를 사용

소켓 연결 방식에는 두가지가 있다. 
1. TCP(Transmission Control Protocol: 연결 지향 소켓) - 전화에 비유할 수 있다.
2. UDP(User Datagram Protocol: 비연결형 소켓) - 우편에 비유할 수 있다.
"""

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

"""
UDP는 연결 지향 통신이 아니다. 따라서 UDP 서버는 TCP 서버와 같은 초기 설정 단계가 필요없다.
다른 특별한 작업 없이 들어오는 연결을 기다리기만 하면 된다.
"""

while True:
	print 'waiting for message....'
	data, addr = udpSerSock.recvfrom(BUFSIZ)
	udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
	print '...received from and returned to: ', addr

udpSerSock.close()