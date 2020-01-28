"""
生成器表达式会在每次 for 循环运行时才
生成一个组合。 如果要计算两个各有 1000 个元素的列表的笛卡儿积， 生成器表达式就可
以帮忙省掉运行 for 循环的开销， 即一个含有 100 万个元素的列表
"""
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('{} {}'.format(color, size) for color in colors for size in sizes):  # 这里
    print(tshirt)