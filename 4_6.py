# generator # 產生器 
# from collections import abc

# x = ['a', 'b', 'c', 'd']
# e = enumerate(x)
# print(isinsrance(e, abc.Iterator))

# for i, name in enumerate(x):
#     print(i, neme)

# a = lambda x: x + 1
# print(a(1))

products = [
    ('aaa',1),
    ('bbb',2),
    ('ccc',3),

]

print(sorted(products, key=lambda x: x[1]))
