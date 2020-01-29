"""
虽然列表既灵活又简单， 但面对各类需求时， 我们可能会有更好的选择。

比如， 要存放1000 万个浮点数的话， 数组（array） 的效率要高得多， 因为数组在背后存的并不是
float 对象， 而是数字的机器翻译， 也就是字节表述。

 这一点就跟 C 语言中的数组一样。 再比如说， 如果需要频繁对序列做先进先出的操作， deque（双端队列） 的速度应该
会更快。

如果在你的代码里， 包含操作（比如检查一个元素是否出现在一个集合中） 的频率很高， 用 set（集合） 会更合适。

set 专为检查元素是否存在做过优化。 但是它并不是序列， 因为 set 是无序的。
"""
import time
import functools
import random
import array

def timing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('{}耗时：'.format(func.__name__), str(end_time-start_time))
        return result
    return wrapper


@timing
def new_list():
    new_list = [random.random() for _ in range(10**8)]
    return new_list


@timing
def new_array():
    new_array = array.array('d', (random.random() for _ in range(10**8)))
    return new_array


new_list()
new_array()  # 然而这个更加耗时!!!
