# -*- coding: utf-8 -*-
# __author__ = kaiqiangzhao

import os
import time
from multiprocessing.process import Process
from multiprocessing.synchronize import Semaphore
from multiprocessing.sharedctypes import RawArray, Array, RawValue, Value

import mmap

# 模拟lock=False, 对共享内存进行读写
# 定义共享内存
# 创建进程
# 读写共享内存


def write(shm):
    uls = u"北京你好"
    print(u"pid={}, start write, num={}".format(os.getpid(), "".join(shm)))
    with shm.get_lock():
        for i in range(4):
            shm[i] = uls[i]
            time.sleep(0.1)
    print(u"pid={}, end write, num={}".format(os.getpid(), "".join(shm)))


def read(shm):
    print(u"pid={}, start read, num={}".format(os.getpid(), "".join(shm)))
    for i in range(4):
        print(u"pid={}, end read, num={}".format(os.getpid(), "".join(shm)))
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

    shm = Array('u', 4, lock=True)  # typecode_to_type, num, lock是递归锁
    pw1 = Process(target=write, args=(shm, ))  # 写进程1
    pw2 = Process(target=write, args=(shm, ))  # 写进程2
    pr = Process(target=read, args=(shm, ))  # 读进程

    print(u"father pid={}, start run, num={}".format(os.getpid(), "".join(shm)))

    pw1.start()
    pw2.start()
    pr.start()

    pw1.join()
    pw2.join()
    pr.join()

    print(u"father pid={}, end run, num={}".format(os.getpid(), "".join(shm)))


if __name__ == '__main__':
    main()