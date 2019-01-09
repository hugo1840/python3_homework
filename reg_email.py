#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def is_valid_email(addr):
	if re.match(r'^[0-9a-zA-Z\_]+[\.]?[0-9a-zA-Z\_]+@[0-9a-zA-Z\-\_]+\.[a-zA-Z]+$', addr):
		return True
	else:
		return False

def name_of_email(addr):
	gp = re.match(r'^<?([a-zA-Z]+\s?[a-zA-Z]*)>?\s?([a-z]*)@([0-9a-zA-Z]+\.[a-zA-Z]+)$', addr)
	return gp.group(1)


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert is_valid_email('db_sales@db_China.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('.bob@example.com')
assert not is_valid_email('mr-bob@example.com')
assert not is_valid_email('bob.tai.nghyuen@example.com')
print('ok')

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')