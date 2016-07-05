#!/usr/bin/python
# coding: utf-8

# multiprocessing.py

import os

print "Process (%s) start ..." % os.getpid()
pid = os.fork()

if pid == 0:
    print "I am child process ({}) and my parent is {}".format(
        os.getpid(), os.getppid()
    )
else:
    print "I {} just created a child process {}".format(
        os.getpid(), pid
    )
