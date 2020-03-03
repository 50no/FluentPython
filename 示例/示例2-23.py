"""
虽然列表可以模拟队列，（利用.append和.pop(0)）

但是collections.deque是一个线程安全、 可以快速从两端添加或者删除元素的数据类型。

实例方法：
    rotate: >0正向循环
    append: 添加
    appendleft:
    extend: 按顺序添加一组
    extendleft:

"""
from collections import deque
dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(-4)
print(dq)
dq.append(100)
print(dq)
dq.appendleft(100)
print(dq)
dq.extend([11, 22, 33, 44])
print(dq)
dq.extendleft([11, 22, 33, 44])
print(dq)

