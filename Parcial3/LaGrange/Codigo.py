from sympy import *

import matplotlib.pyplot as plt
import numpy as np

x = [67, 52, 56, 66, 65, 80]
y = [481, 292, 357, 396, 345, 469]

pL = ''
for k in range(len(y)):
    pL += str(y[k]) + '*'
    Lxk = 1
    for i in range (len(x)):
        if (i == k):
            continue
        pL += '(x - %f)*'%(x[i])
        Lxk *= (x[k] - x[i])
    pL = pL[:-1]
    pL += '/%f+'%(Lxk)
pL = pL[:-1]

expr = sympify(pL)
#expr = expand(expr)
print(expand(expr))
plt.plot(x,y,'go')

x2 = np.linspace(52,80,100) #Valor inicial 52, valor final 80 y cuántos puntos
x = symbols('x')
y2 = [expr.subs(x, xi) for xi in x2]
plt.plot(x2,y2)
plt.grid()
