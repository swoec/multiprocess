#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 20:16:02 2018

@author: alex
"""

import time,threading

#线程代码
def loop():
    print('thread %s is running..'%threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' %(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.'%threading.current_thread().name)

print('thread %s is running.'%threading.current_thread().name)
t = threading.Thread(target = loop,name = 'LoopThread')
t.start()
t.join()
print('thread %s ended.'%threading.current_thread().name)