
# abstract class 抽象類別
#import abc # abstract base class
from abc import ABCMeta, abstractmethod
class Product(metaclass=ABCMeta):
    @abstractmethod
    def hi(self):
        pass

    @abstractmethod
    def hi2(self):
        pass

class Drink(Product):
    def hi(self):
        print('hhii')
    def hi2(self):
        print('hhii222')


#p = Product()
d = Drink()

