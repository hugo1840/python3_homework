
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=__get_timezone(tz_str))
    print('UTC datetime:', dt)
    return dt.timestamp()

def __get_timezone(tz_str):
	tz = re.split('UTC|:', tz_str)
	return timezone(timedelta(hours=int(tz[1])))


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')

# test
print(to_timestamp('2012-10-1 6:10:30', 'UTC-01:00'))
print(to_timestamp('2012-10-1 16:10:30', 'UTC+09:00'))

#print(int('-09'))
#print(int('+8'))