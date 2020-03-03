"""
虽然列表既灵活又简单， 但面对各类需求时， 我们可能会有更好的选择。

比如， 要存放1000 万个浮点数的话， 数组（array） 的效率要高得多， 因为数组在背后存的并不是float 对象， 而是数字的机器翻译，
也就是字节表述。

这一点就跟 C 语言中的数组一样。 再比如说， 如果需要频繁对序列做先进先出的操作， deque（双端队列） 的速度应该
会更快。

如果在你的代码里， 包含操作（比如检查一个元素是否出现在一个集合中） 的频率很高， 用 set（集合） 会更合适。

set 专为检查元素是否存在做过优化。 但是它并不是序列， 因为 set 是无序的。

只包含数字的列表， 那么 array.array 比 list 更高效


array.array同样有：
    .pop
    .insert
    .append
并且有以下方法用来读写文件：
    .frombytes
    .tofile



"""
from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))











