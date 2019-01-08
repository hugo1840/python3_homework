#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
task_master.py
task_worker.py
'''

import time, sys, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
	pass

# 这个QueueManager只从网络上获取队列，注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，即运行task_master.py的机器
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)

# 端口和验证码与task_master一致
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
m.connect()

# 获取队列对象
task =  m.get_task_queue()
result = m.get_result_queue()

# 从task队列获取任务，并把结果写入result队列
for i in range(10):
	try:
		n = task.get(timeout=1)
		print('Run TASK %d * %d...' % (n, n))
		r = '%d * %d = %d' % (n, n, n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('Task queue is empty!')

print('worker exit.')