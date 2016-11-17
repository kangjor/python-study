# -*- coding:utf-8 -*-

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description' : 'My project',
	'author' : 'Kenneth Kang',
	'url' : '',
	'download_url' : '',
	'author_email' : 'kangjor@gmail.com',
	'version' : '0.1',
	'install_requires' : ['nose'],
	'packages' : ['NAME'],
	'scripts' : [],
	'name' : 'My first project'
}

setup(**config)