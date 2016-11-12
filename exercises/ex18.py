# -*- coding:utf-8 -*-
# 이름, 변수, 코드, 함
 
from sys import argv

# unpack variables
script, arg1, arg2 = argv

def print_two(*args):
	arg1, arg2 = args
	print "실행인자1: %r, 실행인자2: %r" % (arg1, arg2)

def print_two_another(arg1, arg2):
	print "실행인자1: %r, 실행인자2: %r" % (arg1, arg2)

def print_one(arg):
	print "실행인자: %r" % (arg)

def print_none():
	print "아무것도 없습니다."

print_two(arg1, arg2)
print_two_another(arg1, arg2)
print_one(arg2)
print_none()