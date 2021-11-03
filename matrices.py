import numpy as np
from numpy.linalg.linalg import LinAlgError, solve
from scipy import linalg

def SOL(A,B):
    return linalg.solve(A,B)

def DET(A):
    return '{:.5f}'.format(np.linalg.det(A))

def INV(A):
    return A**-1

def T(A):
    return np.transpose(A)

def funcion(A,B,ecua):
    return eval(ecua)

def operacionM(am,bm,f):
    """ A = np.matrix(am)
    B = np.matrix(bm)

    R = funcion(A,B,f)
    texto = ['{}'.format(R),'{}'.format(5),'{}'.format(5), "d"]
    return texto """
    try:
        A = np.matrix(am)
        B = np.matrix(bm)

        R = funcion(A,B,f)
        texto = ['{}'.format(R),'{}'.format(5),'{}'.format(5), "d"]
        return texto
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        texto = ['ERROR. Revise las matrices o sus operaciones, puede que esten mal digitadas o los tamaños no concuerden. porfavor consulte a su profesor.','{}'.format(5),'{}'.format(5), "d"]
        return texto
    except LinAlgError:
        print("Oops!  That was no valid number.  Try again...")
        texto = ['Su matriz es singular ó esta errada','{}'.format(5),'{}'.format(5), "d"]
        return texto
