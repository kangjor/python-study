# -*- coding:utf-8 -*-
# 함수와 파일

from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "파일을 출력해 봅니다.\n"
print_all(current_file)

print "파일을 되갑아 봅니다."
rewind(current_file)

print "세 줄을 출력해 봅니다."

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)