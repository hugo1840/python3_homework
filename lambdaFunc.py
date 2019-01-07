#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1

L1 = list(filter(is_odd, range(1, 20)))

L2 = list(filter(lambda x: x % 2 == 1, range(1, 20)))

print(L1)
print(L2)