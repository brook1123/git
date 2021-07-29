#closure 閉包

def f():
    x = 1
    def qqq():
        print('aaaaa')
    class Barman:
        def __int__(self):
            print('iiii'):

    def inner():
        print(x)
        qqq()
        b = Barman()
    return inner

y = f()
#print(y)
y()





