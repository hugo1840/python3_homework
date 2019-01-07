#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Screen(object):

    @property
    def resolution(self):
        return self.__width * self.__height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, v):
        self.__isValidInput(v)
        self.__width = v

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, v):
        self.__isValidInput(v)
        self.__height= v

    def __isValidInput(self, v):
        if not isinstance(v, (int, float)) or v <= 0:
            raise ValueError('请输入正数！')

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')