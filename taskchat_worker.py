#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing.managers import BaseManager
import time

if __name__=='__main__':

    print('++++++++    欢迎来到一问一答系统   +++++++++++++++')
    BaseManager.register('get_queue')

    worker = BaseManager(address=('127.0.0.1', 5000), authkey=b'abc')
    worker.connect()

    accept_queue = worker.get_queue()
    first_msg = '不好意思来迟了，我是Worker!'
    accept_queue.put(first_msg)
    print('我：',first_msg)
    time.sleep(0.5)
    while True:
        accept_msg = accept_queue.get(True)
        print('Master：',accept_msg)
        me_msg = input('Worker：')
        accept_queue.put(me_msg)
        time.sleep(0.5)