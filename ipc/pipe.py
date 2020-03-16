# -*- coding: utf-8 -*-
# __author__ = kaiqiangzhao
from multiprocessing import Pipe
from multiprocessing.connection import Pipe

c1, c2 = Pipe(duplex=True)

c2.send("a")
# print c1.recv()