#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def findMinAndMax(L):
    if L == []: 
    	return (None, None) 
    else: 
    	Min, Max = L[0], L[0] 
    	for x in L: 
    		if x < Min: 
    			Min = x 
    		if x > Max: 
    			Max = x 
    	return (Min, Max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')