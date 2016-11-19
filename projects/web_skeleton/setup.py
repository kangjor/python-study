# -*- coding:utf-8 -*-

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description' : 'Web skeleton',
	'author' : 'Kenneth Kang',
	'url' : '',
	'download_url' : '',
	'author_email' : 'kangjor@gmail.com',
	'version' : '0.1',
	'install_requires' : ['nose', 'lpthw.web'],
	'packages' : ['gothonweb'],
	'scripts' : [],
	'name' : 'Web Skeleton'
}

setup(**config)