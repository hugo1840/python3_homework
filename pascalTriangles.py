#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def triangles(): 
	a = [1] 
	yield a 
	b = [1, 1] 
	while True: 
		yield b 
		c = [x + y for ix, x in enumerate(b[:-1]) for iy, y in enumerate(b[1:]) if ix == iy] 
		b = a + c 
		b.append(1)

def triangles_2(): 
	a = [1] 
	yield a 
	b = [1, 1]
    while True: 
    	yield b 
    	c = [b[k] + b[k+1] for k in range(len(b)-1)] 
    	b = a + c 
    	b.append(1)

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')