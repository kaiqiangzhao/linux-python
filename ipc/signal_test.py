# -*- coding: utf-8 -*-
# __author__ = kaiqiangzhao

import os
import signal
import time


def receive_alarm(signum, stack):
    print("pid={}, Alarm:{}".format(os.getpid(), time.ctime()))


def alarm_main():
    """
    信号通知是一个异步事件
    如果信号发送给一个正在睡眠的进程，那么要看该进程进入睡眠的优先级，如果进程睡眠在可被中断的优先级上，则唤醒进程；
    否则仅设置进程表中信号域相应的位，而不唤醒进程。
    进程检查是否收到信号的时机是：一个进程在即将从内核态返回到用户态时；或者，在一个进程要进入或离开一个适当的低调度优先级睡眠状态时。

    sleep的进程被唤醒
    1)已经过了seconds所指定的墙上时钟时间
    2)调用进程捕捉到一个信号并从信号处理程序返回
    """
    signal.signal(signal.SIGALRM, receive_alarm)  # 向信号注册函数
    signal.alarm(2)  # 2s后执行注册在SIGALRM的函数, 但不会阻塞当前进程

    print('pid={}, Before:{}'.format(os.getpid(), time.ctime()))
    # 进入一个低优先级的睡眠状态时, 也可以执行信号注册函数
    # alarm注册的函数执行完后，会发送终中断信号唤醒原进程, 原进程sleep被中断, 继续进行
    time.sleep(4)
    print('pid={}, After:{}'.format(os.getpid(), time.ctime()))

    # output
    # ('Before:', 'Fri Mar 13 14:23:46 2020')
    # ('Alarm :', 'Fri Mar 13 14:23:48 2020')
    # ('After :', 'Fri Mar 13 14:23:48 2020')


def do_exit(signum, stack):
    raise SystemExit("Exiting")


def exit_alarm():
    """
    Ctrl-C 忽略，kill -usr1 pid 可以结束进程
    """
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGUSR1, do_exit)

    print("pid={}".format(os.getpid()))
    signal.pause()


if __name__ == '__main__':
    # alarm_main()
    exit_alarm()