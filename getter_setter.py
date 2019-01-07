#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, s):
        if isinstance(s, str) and (s == 'male' or s == 'female'):
            self.__gender = s
        else:
            raise ValueError('Input error!')

bob = Student('Bob', 'male')
print(bob.get_gender())
#bob.set_gender('trans')
#print(bob.get_gender())

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')