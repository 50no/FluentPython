tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
print(id(tuple1))
print(id(tuple2))
tuple1 += tuple2
print(id(tuple1))