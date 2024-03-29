#!/usr/bin/python
# coding: utf-8

from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print "Run task %s (%s)..." % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print "Task %s runs %0.2f seconds." % (name, (end - start))


if __name__ == "__main__":
    print 'Parent process %s.' % os.getpid()
    # p = Pool()
    p = Pool(3)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocess done...'

    # 调用join()之前必须先调用close()
    # 调用close()之后就不能继续添加新的Process
    p.close()

    # 等待所有子进程执行完毕
    p.join()

    print 'All subprocess done.'
