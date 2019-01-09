#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools, math
from functools import reduce

def pi_1(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # step 4: 求和:

    odds = itertools.count(1,2)
    ns = list(itertools.takewhile(lambda x: x <= 2*N-1, odds))
    pp = reduce(lambda x, y: x + y, map(lambda x: math.pow(-1, ns.index(x))*4/x, ns))
    return pp

# this method below works faster
def pi(N):
	cc = itertools.cycle([4, -4])
	odds = itertools.count(1,2)
	ns = list(itertools.takewhile(lambda x: x <= 2*N-1, odds))
	pp = reduce(lambda x, y: x + y, map(lambda x: next(cc)/x, ns))
	return pp

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')