
#scope範圍 
#LEGB查找 先找自己
#低對高不能寫入 可以讀取

x = 1
def f():
    
    global x
    x = 10
 #   print(x)

f()
#print(x)


def ff():
    x = 1
    def fff():
        nonlocal x
        x = 10
    fff()
    print(x)


ff()
