# -*- coding: utf-8 -*-
# __author__ = kaiqiangzhao

import os

"""
execve 执行程序函数

int execve(const char *filename, char *const argv[], char *const envp[]); 
args:
    *filename: 二进制可执行文件或脚本
    argv: 执行程序的参数，类似python中的args
    envp: 键值对参数，类似python中的kwargs
    
一个进程一旦调用exec类函数，它本身就"死亡"了，系统把代码段替换成新的程序的代码，废弃原有的数据段和堆栈段，
并为新程序分配新的数据段与堆栈段，唯一留下的，就是进程号，
也就是说，对系统而言，还是同一个进程，不过已经是另一个程序了。

fork 后子进程的代码段和数据段仍然和父进程相同
execve 后子进程的代码段和数据段会被覆盖
"""

command = "echo 'hello execve!' > text.txt"
os.system(command)
