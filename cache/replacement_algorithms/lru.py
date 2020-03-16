# -*- coding: utf-8 -*-

from collections import OrderedDict


class LRUDict(OrderedDict):
    """
    LRU: 页面置换算法, redis key 淘汰算法
    LRU 需要维护一个链表, 链表末尾是最久没有被使用过的数据, 当某个数据被访问后, 需要将其移动到链表头

    这里使用有序字典假装链表, 只不过是将最久未用的放在了字典的开头，最新被访问的放在了末尾。
    """

    def __init__(self, capacity):
        """
        Args:
            capacity: 容量
        """
        super(LRUDict, self).__init__()
        self.capacity = capacity
        self.items = OrderedDict()

    def __setitem__(self, key, value):
        """
        超出最大容量, 删除最久未使用的, 位于orderdict头部m, 添加新元素
        """
        old_value = self.items.get(key)
        if old_value is not None:
            self.items.pop(key)
            self.items[key] = value
        elif len(self.items) < self.capacity:
            self.items[key] = value
        else:
            self.items.popitem(last=False)
            self.items[key] = value

    def __getitem__(self, key):
        """
        每次获取，将其删除后重添加
        """
        value = self.items.get(key)
        if value is not None:
            self.items.pop(key)
            self.items[key] = value
        return value
    
    def get(self, key, d=None):
        """
        每次获取，将其删除后重添加
        """
        value = self.items.get(key, d)
        if value is not None:
            self.items.pop(key)
            self.items[key] = value
        return value

    def __repr__(self):
        return repr(self.items)


if __name__ == '__main__':

    lrud = LRUDict(10)

    for i in range(15):
        lrud[i] = i

    lrud.get(10)
    print lrud
