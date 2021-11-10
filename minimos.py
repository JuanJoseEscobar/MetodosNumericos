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
def minimosMin(x,y):
    x=[0,math.pi/4,math.pi/2,3*math.pi/4,math.pi]
    y=[1,0.604,0.397,0.238,0.106]


    c = polyfit(x,y,2)
    imprimir = 'Y =  {:.5f} X^2  +  {:.5f} X  +  {:.5f}'.format(c[0],c[1],c[2])

    xx = linspace(x[0],x[len(x)-1],50)
    yy = polyval(c,xx)
    plt.scatter(x, y);plt.xlabel('X');plt.ylabel('Y')
    plt.plot(xx,yy,'r')
    plt.show()
    return imprimir
