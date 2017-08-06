# -*- coding: utf-8 -*-
# # 06 list and tuple
# list is a sortable collection
workmates = ['ZhangSan', 'LiSi', 'WangWu']
print(workmates)
print(len(workmates))
print(workmates[0], workmates[1], workmates[2])
print(workmates[-1], workmates[-2], workmates[-3])

# add elements
workmates.append('Steve')
print(workmates)
workmates.insert(0, 'Jessie')
print(workmates)
# delete - pop
elem = workmates.pop()
print(workmates)
elem = workmates.pop(1)
print(workmates)

# modify
workmates[1] = 'Jay'
print(workmates)

# different element types
userInfo = [1, 'ZhangSan', True]
print(userInfo)
# element can be another list
userInfo = [1, 'ZhangSan', True, ['Python', 'Java', 'C#']]
print(userInfo)
print(len(userInfo))
print(userInfo[3][2])

# tuple, can not change
workmates = ('ZhangSan', 'LiSi', 'WangWu')
print(workmates)
print((1, ))

# user list and tuple together
print([1, 2, (3, 4)])

# exercise
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
