# @property

# encapsilation 封裝
# OOP
# private
# public
# _x

# class Batman:
#     def __init__(self, hp):
#         self._hp =hp
#         #self._attack

#     def get_hp(self):
#         ruturn self._hp

#     def set_hp(self):
#         self._hp = hp
#         if hp >100:
#             self._hp = 100
#         elif hp < 0:
#             self._hp = 0


# b1 = Batman(100)
# b2 = Batman(50)
# b1.set_hp(b1.get_hp()+b2.get_hp())





class Batman:
    def __init__(self, hp):
        self._hp =hp

    @property
    def hp(self):
        print('23232')
        return self._hp
    
    @hp.setter
    def hp(self, hp):
        self._hp = hp
        if hp >100:
            self._hp = 100
        elif hp < 0:
            self._hp = 0
            

b1 = Batman(100)
b2 = Batman(50)
b1.hp = b1.hp + b2.hp

