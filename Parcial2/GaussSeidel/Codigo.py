# 4x1 + x2 - x3 = 0
# 2x1 + 5x2 + 2x3 = 3
# x1 ´2x2 + 4x3 = 11

def getX1(x2,x3,x4):
    return (3 + 2*x2 - x3 - 2*x4)/7

def getX2(x1,x3,x4):
    return (-2 - 2*x1 - 3*x3 - x4)/8

def getX3(x1,x4):
    return (5 + x1 - 2*x4)/5

def getX4(x2,x3):
    return (4 - 2*x2 + x3)/4

x1 = 0
x2 = 0
x3 = 0
x4 = 0
E = 0.001
for i in range(100):
    x1i = getX1(x2,x3,x4)
    x2i = getX2(x1i,x3,x4)
    x3i = getX3(x1i,x4)
    x4i = getX4(x2i,x3i)
    Ex1 = abs(x1-x1i)
    Ex2 = abs(x2 - x2i)
    Ex3 = abs(x3 - x3i)
    Ex4 = abs(x4 - x4i)
    x1 = x1i
    x2 = x2i
    x3 = x3i
    x4 = x4i
    if Ex1 < E and Ex2 < E and Ex3 < E and Ex4 < E:
        break
print("La solución es:",x1,x2,x3,x4)
