"""
_fields: 类属性
_make: 类方法
_asdict()： 实例方法
"""
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
# print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
# print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ':', value)






