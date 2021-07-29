
# 繼承
from dunder import Product

class Drink(Product):
    def __init__(self,name,price,volume):
        super().__init__(name, price)
        #self.name = name
        #self.price = price
        self.volume =volume
    

d = Drink('珍珠奶茶',80,600)
print(type(d))
print(isinstance(d ,Drink))