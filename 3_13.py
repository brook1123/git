# @staticmethod
# @classmethod

class Batman:
    @staticmethod
    def f():
        print('aaaaaa')

    @staticmethod
    def calc_avg(x):
        return sum(x)/ len(x)

    @classmethod
    def fff(cls):
        cls().f()
        


# Batman.f()
Batman.fff()
#x = [1,2,3]
# print(Batman.calc_avg(x))








