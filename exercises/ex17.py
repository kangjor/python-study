# -*- coding:utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print '%s에서 %s로 복사합니다.' % (from_file, to_file)

# 이렇게 하면 파일을 close() 할 필요가 없습니다. 이미 파일은 닫혔거등요...
in_data = open(from_file).read()

print '입력 파일은 %d바이트입니다.' % len(in_data)

print '파일이 존재할까요? %r' % exists(to_file)
print 'It is ready. To continue press ENTER or CTRL-C'

raw_input('?')

out_file = open(to_file, 'w')
out_file.write(in_data)

print 'It\'s done. Thanks'
out_file.close()