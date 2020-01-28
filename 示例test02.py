"""
insort
果然这玩意只能用在可变序列上
"""
import bisect
my_tuple = [3, 4, 6, 37, 23, 17, 65]
new_tuple = [1, 2, 3, 4, 5, 6]
for i in new_tuple:
    bisect.insort(my_tuple, i)
    print('{:2d} ->  '.format(i), my_tuple)