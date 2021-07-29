
# _  沒有用的
# _name 私人的
# name_  二次使用加_
# __name  用在class 避免撞名 系統會重新命名
# __name__ dunder methods/ magic methods

for _ in range(10):
    print( _, 'hi')

class Qwe:
    def public_function():
        print('asdasd')

    def _private_function():
        print('asdasd')

q =Qwe()
q._private_function()

class Person:
    def __init_(self):
        self.x =1
        self._y =1
        self.__z=1

p = Person()
print(p.x)
print(p._y)
print(dir(p))
#print(p.__z)

