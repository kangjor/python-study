# -*- coding:utf-8 -*-


def scan(input):
	words = input.split()
	result = []

	direction = ('동', '서', '남', '북')
	verbs = ('이동', '섭취', '공격')
	nouns = ('공', '공주')
	excep = ('그', '이', '저')


	for word in words:
		if word in verbs:
			result.append(('동사', word))
		elif word in direction:
			result.append(('방향', word))
		else:
			result.append('오류', word)

	return result