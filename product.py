#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def product(x, *args):
    product = x
    for y in args:
        product = product * y 
    return product