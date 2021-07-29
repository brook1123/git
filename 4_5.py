# generator # 產生器 

def g():
    while True:
        yield 1

print(next(g()))
print(next(g()))
print(next(g()))


def my_range(n):
    i = 0
    while i < n:
        print(f'我現在準備要生產{i}了')
        yield i
        i += 1

for i in my_range(5):
    print(i)


# generator expression
x = [0, 1, 2, 3, 4]
# print([i*i for i in x])
# print((i*i for i in x))
it = (i*i for i in x)
print(next(it))
print(next(it))

it1 = (i*i for i in x)
it2 = (i+2 for i in it1)
print(next(it2))
print(next(it2))
print(next(it2))
