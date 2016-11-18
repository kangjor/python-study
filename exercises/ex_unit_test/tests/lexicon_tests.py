# -*- coding:utf-8 -*-

from nose.tools import *
from ex48 import lexicon

def test_directions():
	assert_equal(lexicon.scan('북'), [('방향', '북')])
	result = lexicon.scan("북 남 동")
	assert_equal(result, [
			('방향', '북'), 
			('방향', '남'),
			('방향', '동')
		])

def test_verbs():
	assert_equal(lexicon.scan("이동"), [('동사', '이동')])
	result = lexicon.scan('이동 공격 섭취')
	assert_equal(result, [
			('동사', '이동'),
			('동사', '공격'),
			('동사', '섭취')
		])

