#decorator 裝飾器 降低重複性 避免動到別人FUNC
import time

def print_func(func):
    def inner():
        print('running',func.__name__)
        func()
    return inner
    
def  time_func(func):
    def inner():
        start =time.time()
        func()
        end =time.time()
        print('elapsed',end - start,'seconds')
    return inner


@time_func
@print_func
def test():
    print('hi')

def test2():
    print('ni hao')

test()
#print('加工中')
#test = print_func(test)
#test2 = time_func(test2)
#test()
#test2()








