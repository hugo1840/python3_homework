#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import queue,time
from multiprocessing.managers import BaseManager

q = queue.Queue()

def send_message(msg):
    q.put(msg)

def get_queue():
    return q


if __name__=='__main__':

    print('++++++++    欢迎来到一问一答系统   +++++++++++++++')
    BaseManager.register('get_queue', callable=get_queue)

    master = BaseManager(address=('127.0.0.1', 5000), authkey=b'abc')
    master.start()

    accept_queue = master.get_queue()

    while True:
        accept_msg = accept_queue.get(True)
        print('Worker：',accept_msg)
        me_msg = input('Master：')
        accept_queue.put(me_msg)
        time.sleep(0.5)