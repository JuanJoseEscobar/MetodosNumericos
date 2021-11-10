from math import pi
import math
from os import linesep
import matplotlib
import numpy as np
from numpy.core.function_base import linspace
from numpy.lib.polynomial import polyfit, polyval
from numpy.linalg import inv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


""" x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
y = [432,439,442,444,446,447,449,451,453,458,463,466,468,470,472,477,479,491,516,516,521,524,526,533,541,548,555,560,563,564] """

x=[1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000]
y=[1650,1750,1860,2070,2300,2560,3040,3710,4450,5280,6070]


plt.scatter(x, y);plt.xlabel('X');plt.ylabel('Y')
plt.show()

c = polyfit(x,y,1)
""" print('y =  {:.5f} X^2  +  {:.5f} X  +  {:.5f}'.format(c[0],c[1],c[2])) """
print('y =  {:.5f} X  {:.5f} '.format(c[0],c[1]))


xx = linspace(x[0],x[len(x)-1],100)
yy = polyval(c,xx)
plt.scatter(x, y);plt.xlabel('X');plt.ylabel('Y')
plt.plot(xx,yy,'c')
plt.show()
