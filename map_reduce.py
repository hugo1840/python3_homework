#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def normalize(name): 
    return name[0].upper() + name[1:].lower()

def normalize_2(name): 
    return name.capitalize()

def prod(L):
    if L == []:
        return 0
    else:
        return reduce(lambda x, y: x * y, L)

def str2float(s):
    DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}   

    pos = s.index('.')
    ss = s.split('.')
    ss = ss[0] + ss[1]  

    def char2num(c):
        return DIGITS[c]

    num = reduce(lambda x, y: x * 10 + y, map(char2num, ss))
    # num /= math.pow(10, pos)
    while pos > 0:
        num /= 10
        pos -= 1

    return num

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')