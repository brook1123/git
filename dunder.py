
# _  沒有用的
# _name 私人的
# name_  二次使用加_
# __name  用在class 避免撞名 系統會重新命名
# __name__ dunder methods/ magic methods


class Product:
    def __init__(self, name, price):
        self.name =name #property
        self.price = price #property

    def __str__(self):
        #return self.name + ' '+str(self.price)
        return f'{self.name} ${self.price}'
    
    def __repr__(self):
        return f'<Product({self.name},{self.price})>'

    def __add__(self,other):
        if isinstance(other,str):
            self.name += other
        if isinstance(other,Product):
            return [self,other]

    def __mul__(self,other):
        re = []
        if isinstance(other, int):
            for i in range(other):
                re.append(self)
        return re

p1 = Product('珍珠奶茶',60) 
p2 = Product('義大利麵',222) 
#p = Product('珍珠奶茶',60) 
#p + '白玉'
#print(p1+p2)
#print(p)
#print(repr(p))
print(p1*1)


