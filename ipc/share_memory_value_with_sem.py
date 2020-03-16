# -*- coding: utf-8 -*-
# __author__ = kaiqiangzhao

import os
import time
from multiprocessing.process import Process
from multiprocessing.synchronize import Semaphore
from multiprocessing.sharedctypes import RawArray, Array, RawValue, Value

import mmap

# 模拟有信号量加锁对共享内存进行读写
# 定义共享内存
# 创建进程
# 读写共享内存


def write(shm, sem):
    print("pid={}, start write, num={}".format(os.getpid(), shm.value))
    for i in range(10):
        sem.acquire()  # P 操作
        shm.value += 1
        time.sleep(0.1)
        sem.release()  # V 操作
    print("pid={}, end write, num={}".format(os.getpid(), shm.value))


def read(shm):
    print("pid={}, start read, num={}".format(os.getpid(), shm.value))
    for i in range(10):
        print("pid={}, end read, num={}".format(os.getpid(), shm.value))
        time.sleep(0.1)


def main():
    """
    typecode_to_type = {
        'c': ctypes.c_char,
        'b': ctypes.c_byte, 'B': ctypes.c_ubyte,
        'h': ctypes.c_short, 'H': ctypes.c_ushort,
        'i': ctypes.c_int, 'I': ctypes.c_uint,
        'l': ctypes.c_long, 'L': ctypes.c_ulong,
        'f': ctypes.c_float, 'd': ctypes.c_double
    }
    一般共享内存需要通过信号量加锁
    """

    sem = Semaphore(value=1)  # 信号量, 一次只能一个写进程执行写操作, 如果不加锁, 最后的结果可能会不等于20

    shm = Value('i', 0, lock=True)  # typecode_to_type, num, lock是互斥锁
    pw1 = Process(target=write, args=(shm, sem))  # 写进程1
    pw2 = Process(target=write, args=(shm, sem))  # 写进程2
    pr = Process(target=read, args=(shm, ))  # 读进程

    print("father pid={}, start run, num={}".format(os.getpid(), shm.value))

    pw1.start()
    pw2.start()
    pr.start()

    pw1.join()
    pw2.join()
    pr.join()

    print("father pid={}, end run, num={}".format(os.getpid(), shm.value))


if __name__ == '__main__':
    main()