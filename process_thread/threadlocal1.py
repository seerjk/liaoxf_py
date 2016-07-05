#!/usr/bin/python
# coding:utf-8

import threading


# 创建全局ThreadLocal对象
local_school = threading.local()


def process_student():
    print "hello, %s (in %s)" % (local_school.student, threading.current_thread().name)


def process_thread(name):
    # 绑定ThreadLocal的student
    # print type(local_school)
    local_school.student = name
    process_student()

if __name__ == "__main__":
    print "threading.local type is {}".format(type(local_school))
    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-Bob')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

