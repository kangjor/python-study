#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
# alternatives to thread module
subprocess (2.4)
multiprocessing (2.6)
concurrent.futures (3.2)
"""
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib2 import urlopen as uopen
import requests

REGEX = compile('#([\d,]+) in Books ')
AMZN = 'https://www.amazon.com/dp/'
ISBINs = {
	'0132269937': 'Core Python Programming',
	'0132356139': 'Python Web Development with Django',
	'0137143419': 'Python Fundamentals'
}

def getRanking(isbn):
	# page = uopen('%s%s' % (AMZN, isbn))
	## page = uopen('{0}{1}'.format(AMZN, isbn)) # for python 2.6
	# data = page.read()

	# AMAZON prevent access from non-browser. You can use "requests" module instead
	page = requests.get('%s%s' % (AMZN, isbn))
	data = page.text

	page.close()
	return 	REGEX.findall(data)[0]

def _showRanking(isbn):
	print '- %r ranked %s' % (ISBINs[isbn], getRanking(isbn))

def main():
	print 'At', ctime(), 'on Amazon....'
	for isbn in ISBINs:
		# _showRanking(isbn)
		# 
		# for multiple threading
		Thread(target=_showRanking, args=(isbn,)).start()

@register
def _atexit():
	print 'all Done at:', ctime()

if __name__ == '__main__':
	main()