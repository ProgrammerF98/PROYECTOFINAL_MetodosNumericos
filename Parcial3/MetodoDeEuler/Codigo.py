# Metodo de Euler
# y' - e^x = 0 y(0) = 1 y(5) = ?
# dy/dx = e^x
import math
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return math.sin(x) + math.log(y) #aquí poner derivada

def euler(y0, x, h, f):
    y = []
    y.append(y0)
    for i in range(1, len(x)):
        y.append(y[i-1] + h*f(x[i-1], y[i-1])) #formula de euler
    return y

n = 20 #despejar n
a = 0.13 #valor inicial
b = 0.14 #valor de incognita
h = abs(a-b)/(n-1)
x = np.linspace(a,b,n)
y = euler(1,x,h,f)

plt.plot(x,y,'g')
#plt.plot(x,[math.exp(xi) for xi in x], 'b')
plt.grid()
