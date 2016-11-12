# -*- coding:utf-8 -*-
# 반환하는 함수 

from sys import argv
script, num1, num2 = argv

def add(a, b):
	print "Add %d + %d" % (a, b)
	return a+b

def subtract(a, b):
	print "Sbtract %d - %d" % (a, b)
	return a-b

def multiply(a, b):
	print "Multiply %d * %d" % (a, b)
	return a*b

def divide(a,b):
	print "Divide %d / %d" % (a, b)
	return a/b

print "함수만으로 계산해 봅시다"

age = add(float(num1), float(num2))
height = subtract(float(num1), float(num2))
weight = multiply(float(num1), float(num2))
iq = divide(float(num1), float(num2))

print "age: %d, height: %d, weight: %d, iq: %d" % (age, height, weight, iq) , "\n"

print "문제입니다."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "결과 : ", what , " 암산 가능한가요?"
