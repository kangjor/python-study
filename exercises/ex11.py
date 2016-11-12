# -*- coding: utf-8 -*-

print '몇 살이죠?'
age = raw_input()

print '키는 얼마죠?'
height = raw_input()

print '모무게는 얼마죠?'
weight = raw_input()

print '당신의 나이는 %r 살, 키는 %r, 몸무게는 %r이시네요.' % (
	age, height, weight)
print '태양의 각지름은 %s 정도입니다.' % '''32'10"'''