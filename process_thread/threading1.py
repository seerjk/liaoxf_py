#!/usr/bin/python
# coding: utf-8

import time, threading


def loop():
    """
    新线程执行的代码
    :return:
    """
    print "thread %s is running..." % threading.current_thread().name
    n = 0
    while n < 5:
        n = n +1
        print "thread %s >>> %s" %(threading.current_thread().name, n)
        time.sleep(1)

    print "thread %s ended." % threading.current_thread().name


if __name__ == "__main__":
    print "thread %s is running..." % threading.current_thread().name
    # t = threading.Thread(target=loop, name="LoopThread")
    t = threading.Thread(target=loop)
    t.start()
    t.join()
    print 'thread %s ended.' % threading.current_thread().name

