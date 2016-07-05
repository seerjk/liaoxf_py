#!/usr/bin/python
# coding: utf-8

from multiprocessing import Process
import os
import time


def run_proc(name):
    """
    子进程要执行的代码
    :param name:
    :return:
    """
    print "Run child process %s (%s)" % (name, os.getpid())
    print "I am (%s). My parent process is %s." % (os.getpid(), os.getppid())
    time.sleep(5)


if __name__ == "__main__":
    print "Parent process %s." % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'

