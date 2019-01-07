#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def createCounter():
	# 定义生成器
    def f():
        n = 1
        while True:
            yield n
            n += 1

    # 返回函数      
    gen = f()
    def counter():
        return next(gen)

    return counter

def createCounter_2(): 
	x = [0] 
	def counter(): 
		x[0] += 1 
		return x[0]
    return counter

def createCounter_3(): 
	x = 0
    def counter(): 
    	nonlocal x 
    	x += 1 
    	return x
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')