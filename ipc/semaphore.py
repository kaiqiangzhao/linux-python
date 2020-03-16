# -*- coding: utf-8 -*-
# __author__ = kaiqiangzhao
from multiprocessing.synchronize import Semaphore
from multiprocessing.process import Process
import time
import random

"""
信号量
"""


def work(sem, unum):
    sem.acquire()  # P 操作
    print("now user num={} start work".format(unum))
    time.sleep(random.randint(0, 3))
    sem.release()  # V 操作


def main():
    sem = Semaphore(value=2)  # value 表示资源数, 即规定同时多少个进程可以执行临界区的代码
    pls = []
    for unum in range(10):
        p = Process(target=work, args=(sem, unum))
        p.start()
        pls.append(p)

    for pt in pls:
        pt.join()


if __name__ == '__main__':
    main()