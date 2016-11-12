# -*- coding:utf-8 -*-
# 다중 값 반환

from sys import argv

script, num = argv


def multi_result(num):
	jelly_beans = num * 23
	jars = num / 3
	crates = num % 1000

	return jelly_beans, jars, crates

beans, jars, crates = multi_result(int(num))

print "beans: %d, jars: %d, crates: %d" % (beans, jars, crates)