# -*- coding:utf-8 -*-

from nose.tools import *
from ex47 import lexicon

def test_directions():
	assert_equal(lexicon.scan('북'), [('방향', '북')])
	result = lexicon.scan('북 남 동')
	assert_equal(result, [
			('방향', '북'),
			('방향', '남'),
			('방향', '동')
		])

