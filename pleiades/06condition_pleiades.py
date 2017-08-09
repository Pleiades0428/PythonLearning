#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = 3
if age > 18 and age < 60:
    print('You\'re an adult.')
elif age >= 60:
    print('You are an old man.')
elif age > 6:
    print('You are a teenager.')
else:
    print('You\'re a kid.')

#只要x是非零数值、非空字符串、非空list等，就判断为True
x = 'w'
if x:
    print('True')

# about input
inStr = '1988'
birth = int(inStr)
if birth > 2000:
    print('True.')

# practice
height = 1.75
weight = 80.5
bmi = weight / height ** 2
print(bmi)
if bmi < 18.5:
    print('Light-weight.')
elif bmi < 25:
    print('Normal.')
elif bmi < 28:
    print('Over-weight.')
elif bmi < 32:
    print('Fat.')
else:
    print('Very Fat.')
