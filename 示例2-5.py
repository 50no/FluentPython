"""用生成式表达式初始化元组和数组"""

example = 'abcdefghijklmnopqrstuvwxyz'

print(tuple(i for i in example)) 

import array
print(array.array('I', (ord(i) for i in example)))