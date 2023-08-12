import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from matplotlib import *
from mpl_toolkits import mplot3d
f=plt.figure()
f.set_figwidth(10)
f.set_figheight(10)
t=linspace(0,360,1000)
x_mercury= 0.387*cos(t)+0.1
y_mercury=0.387*sin(t)
x_venus=0.723*cos(t)
y_venus=0.723*sin(t)
x_earth=cos(t)
y_earth=sin(t)
x_mars=1.523*cos(t) + 0.15
y_mars=1.523*sin(t)
plt.xlabel("x/AU")
plt.ylabel("y/AU") 
plt.title("Eliptical Orbits of the 4 Inner Planets")
plt.plot(x_mercury,y_mercury, label="Mercury")
plt.plot(x_venus,y_venus, label="Venus")
plt.plot(x_earth,y_earth, label="Earth")
plt.plot(x_mars,y_mars, label="Mars")
plt.scatter(0,0, s=2500, color='yellow')
plt.legend(fontsize="small")
plt.grid()
plt.show()

