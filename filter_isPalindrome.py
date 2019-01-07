#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_palindrome(n):
    num, hui = n, 0
    while num >= 1:
        hui = hui * 10 + num % 10
        num = num // 10
    return hui == n

def is_palindrome_2(n):
    s = str(n)
    hui = s[::-1]
    return hui == s

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')