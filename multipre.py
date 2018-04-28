#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 11:59:04 2018

@author: alex
"""

import multiprocessing
import os

def run_proc(name):
    print('Child process {0} {1} Running '.format(name, os.getpid()))

if __name__ == '__main__':
    print('Parent process {0} is Running'.format(os.getpid()))
    for i in range(5):
        p = multiprocessing.Process(target=run_proc, args=(str(i),))
        print('process start')
        p.start()
    p.join()
    print('Process close')