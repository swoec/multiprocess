#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 20:14:32 2018

@author: alex
"""
#Unix/Linux下可使用fork()
#跨平台使用multiprocessing
#多进程数据通信Queue、Pipes
from multiprocessing import Process,Queue
import os,time,random

#写数据
def write(q):
    print('Process to write:%s'%os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue.'%value)
        q.put(value)
        time.sleep(random.random())

#读数据
def read(q):
    print('Process to read:%s'%os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.'%value)



if __name__ == '__main__':
    q = Queue()
    pw = Process(target = write,args=(q,))
    pr = Process(target = read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()