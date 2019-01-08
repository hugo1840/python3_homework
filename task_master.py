#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Distributed processing task_master
在分布式多进程环境下，添加任务到Queue不可以直接对原始的
task_queue进行操作，那样就绕过了QueueManager的封装，必须
通过manager.get_task_queue()获得的Queue接口添加
'''

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

def return_task_queue():
	#global task_queue
	return task_queue

def return_result_queue():
	#global result_queue
	return result_queue

class QueueManager(BaseManager):
	pass


if __name__ == "__main__":

    # 把两个队列注册到网上
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)

    # 绑定服务器地址和端口5000，设置验证码'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    # 启动队列
    manager.start()

    # 获得通过网络访问的队列对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去
    for i in range(10):
	    n = random.randint(0, 10000)
	    print('Put TASK %d...' % n)
	    task.put(n)

    # 从result队列读取结果
    print('Try get results...')
    for i in range(10):
	    r = result.get(timeout=10)
	    print('Result: %s' % r)

    # 关闭
    manager.shutdown()
    print('master exit.')