#pass by value    整數或字串 [0] ,0
#pass by reference 清單[0,1] ,1
#pass by object reference 
def f(y):
    y.append(1)

x = [0]
f(x)
print(x)

def ff(y):
    y += 1

x = 0
ff(x)
print(x)