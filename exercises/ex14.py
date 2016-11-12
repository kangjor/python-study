# -*- coding:utf-8 -*-

from sys import argv

script, user_name = argv
prompt = '> '

print 'Hi %s, I\'m %s script' % (user_name, script)
print 'I have couple of questions for you.'
print '%s, do you like me?' % user_name
like = raw_input(prompt)

print 'Where are you living?'
lives = raw_input(prompt)

print 'What kind of computer do you have?'
comp = raw_input(prompt)

print '''
Ok, 나를 좋아하는 질문에는 %s.
%s에 살아. 어딘지는 모르겠지만.
그리고 '%s' 컴퓨터를 가졌어. 멋질걸
''' % (like, lives, comp)