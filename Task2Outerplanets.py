import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from matplotlib.pyplot import *
f=plt.figure()
f.set_figwidth(10)
f.set_figheight(10)
t=linspace(0,360,1000)
x_jupiter=5.20*cos(t)+0.1
y_jupiter=5.20*sin(t)
x_saturn=9.58*cos(t)
y_saturn=9.58*sin(t)
x_uranus=19.29*cos(t)
y_uranus=19.29*sin(t)
x_neptune=30.25*cos(t)+ 0.15
y_neptune=30.25*sin(t)
plt.xlabel("x/AU")
plt.ylabel("y/AU")
plt.title("Eliptical Orbits of the 4 Outer Planets")
plot(x_jupiter,y_jupiter, label="Jupiter")
plot(x_saturn,y_saturn, label="Saturn")
plot(x_uranus,y_uranus, label="Uranus")
plot(x_neptune,y_neptune, label="Neptune")
plt.scatter(0,0, s=1500, color='yellow')
plt.legend(fontsize="small")
plt.grid()
show()
