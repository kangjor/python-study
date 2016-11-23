#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
from time import sleep, ctime

class MyThread(threading.Thread):
	"""docstring for MyThread"""
	def __init__(self, func, args, name='', verb=False):
		# super(MyThread, self).__init__()
		threading.Thread.__init__(self)
		self.func = func
		self.args = args
		self.name = name
		self.verb = verb

	def getResult(self):
		return self.res

	def run(self):
		if self.verb:
			print 'starting', self.name, 'at:', ctime()
		self.res = self.func(*self.args)
		if self.verb:
			print self.name, 'finished at:', ctime()		