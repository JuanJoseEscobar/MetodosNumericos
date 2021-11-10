from types import TracebackType
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

def SUMA(A,B):
    if len(A) != len(B):
        print("el tamaño de a es:"+len(A))
        return "Error. Las matrices deben ser iguales"
    else:
        return A+B

def RESTA(A,B):
    if len(A) != len(B):
        return "Error. Las matrices deben ser iguales"
    else:
        return A-B

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
        texto = ['ERROR. Revise las matrices o sus operaciones, puede que esten mal digitadas o los tamaños no concuerden. Porfavor consulte a su profesor.','{}'.format(5),'{}'.format(5), "d"]
        return texto
    except LinAlgError:
        print("Oops!  That was no valid number.  Try again...")
        texto = ['Su matriz es singular.','{}'.format(5),'{}'.format(5), "d"]
        return texto
    except NameError:
        print("Oops!  That was no valid number.  Try again...")
        texto = ['Error. No se reconoce lo digitado.','{}'.format(5),'{}'.format(5), "d"]
        return texto
    except TypeError:
        print("Oops!  That was no valid number.  Try again...")
        texto = ['Error. No se reconoce lo digitado.','{}'.format(5),'{}'.format(5), "d"]
        return texto
