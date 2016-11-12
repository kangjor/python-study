# -*- coding:utf-8 -*-

the_count = [1,2,3,4]
fruits = ['사과', '귤', '배', '살구']
change = [1, '십원', 2, '백원', 3, '오백원']

for number in the_count:
	print "이 수는 %d" % number

for i in change:
	print "받은 잔돈 %s " % i

elements = []

for i in range(1,6):
	print "list에 %d 숫자를 추가합니다." % i
	elements.append(i)

for i in elements:
	print "원소는 %d" % i


i=0
numbers = []

while i<6:
	print "꼭대기에서 i는 %d" % i
	numbers.append(i)

	i+=1
	print "숫자는 이제: ", numbers
	print "바닥에서 i는 %d" % i

print "숫자: "

for num in numbers:
	print num
