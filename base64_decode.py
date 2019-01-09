#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

def safe_base64_decode(s):
	r = len(s) % 4
	if r != 0:
		return base64.b64decode(s + (4-r)*b'=')
	return base64.b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==') # assertionError info
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
