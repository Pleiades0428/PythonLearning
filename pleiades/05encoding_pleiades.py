#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
# 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：
# 浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：

# 在最新的Python 3版本中，字符串是以Unicode编码的
print("Python supports 中文等很多语言哦")

# ord chr
print(ord('A'), ord('中'), chr(66))

# bytes
x = b'ABC'
print(x)

# encode
print('xyz'.encode('ascii'))
print('你好'.encode('utf-8'))
print(b'xxx'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# len
print(len('12345'))
print(len('你好'))
print(len('你好'.encode('utf-8')))

# 应当始终坚持使用UTF-8编码

# formatter
print('I have an %s' % 'apple')
print('%2d, %02.2f' % (2.14, 3.345))
print('%d %%' % 7)

# exercise
s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print('%2.1f%%' % r)
