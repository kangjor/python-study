# -*- coding:utf-8 -*-

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "잠깐 아직 목록에 10개가 들어있지 않으니 한 번 고쳐 봅시다."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Add: ", next_one
	stuff.append(next_one)
	print "이제 항목은 %d개 항목이 있습니다." % len(stuff)

print "Let see!", stuff

print "Do something else"

print stuff[1]
print stuff[-1]
print stuff.pop()
print " ".join(stuff)
print "#".join(stuff[3:5])