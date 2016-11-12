# -*- coding:utf-8 -*-

from sys import argv

script, filename = argv

print '%r 파일을 지우려 합니다.' % filename
print 'To cancle CTRL-C'
print 'To continue press enter.'

raw_input('?')

print 'Opening file'
target = open(filename, 'w')

print '파일 내용을 지웁니다. 안녕!!! Good bye!'
target.truncate()

print '이제 새로들어갈 내용을 묻겠습니다.'
line1 = raw_input('> Line 1: ')
line2 = raw_input('> Line 2: ')
line3 = raw_input('> Line 3: ')

final_txt = line1 + '\n' + line2 + '\n' + line3 + '\n'

target.write(final_txt)
target.close()
print '위 내용을 파일에 썻습니다.'


print '내용을 추가합니다'
target = open(filename, 'a')

line1 = raw_input('> Another line: ');
print '위 내용을 파일에 추가 합니다.'

target.write(line1)

print '파일을 닫습니다.'
target.close()

