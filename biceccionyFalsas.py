from sympy import *
import numpy as np
 
def funcion(x,ecua):
    return eval(ecua)


def biseccion(ecua,x_i,x_f, iteraciones=1000, error_r=0.001):
    #inicializar variablesclear

    solucion = None
    contador = 0
    error_calculado= 101
    
    # Evaluar si la raiz estÃ¡ en el intervalo o no

    if(funcion(x_i,ecua))*funcion(x_f,ecua) <= 0:
        # calcular solucion
        texto = ""
        while contador <= iteraciones and error_calculado >= error_r:
            contador +=1
            solucion=(x_i + x_f)/2
            error_calculado = abs((solucion - x_i)/solucion)*100
            #Redefinir el nuevo intervalo 

            if funcion(x_i,ecua) *funcion(solucion, ecua) >=0:
                x_i=solucion
            else:
                x_f=solucion
            print('El intervalo es: ',x_i,x_f)
            texto += 'El intervalo '+str(contador)+' es: [ a= {:.4f}'.format(x_i)+', b= {:.4f}'.format(x_f)+' ].\n'
        #Imprimir el resultado
        
        print ('la solucion aproximada es: {:.3f} '.format(solucion))
        print ('Encontrada en:  {:.0f}'.format(contador)+ 'iteraciones')
        print ('Con un error relativo de: {:.2f}'.format(error_calculado)+'%')
        x =['{:.7f} '.format(solucion),'{:.0f}'.format(contador)+ ' iteraciones','{}'.format(error_calculado)+'%', texto]
        return x
    else:
        x =['No existe solucion en ese intervalo','ERROR','ERROR','No se realizo ningún calculo']
        print('No existe solucion en ese intervalo') 
        return x


def falsap(ecua,x_i,x_f, iteraciones=1000, error_r=0.001):
    #inicializar variablesclear
    solucion = None
    contador = 0
    error_calculado= 101
    
    # Evaluar si la raiz estÃ¡ en el intervalo o no
    if(funcion(x_i,ecua))*funcion(x_f,ecua) <= 0:
        # calcular solucion
        texto = ""
        while contador <= iteraciones and error_calculado >= error_r:
            contador +=1
            solucion=x_f - ((funcion(x_f,ecua)*(x_f - x_i))/(funcion(x_f,ecua)-funcion(x_i,ecua)))
            error_calculado = abs((solucion - x_i)/solucion)*100
            #Redefinir el nuevo intervalo 
            if funcion(x_i,ecua) *funcion(solucion, ecua) >=0:
                x_i=solucion
            else:
                x_f=solucion
            print('El intervalo es: ',x_i,x_f)
            texto += 'El intervalo '+str(contador)+' es: [ a= '+str(x_i)+', b= '+str(x_f)+' ].\n'
        #Imprimir el resultado
        
        print ('la solucion aproximada es: {:.3f} '.format(solucion))
        print ('Encontrada en:  {:.0f}'.format(contador)+ 'iteraciones')
        x =['{} '.format(solucion),'{}'.format(contador)+ ' iteraciones','{}'.format(error_calculado)+'%',texto]
        return x
    else:
        x =['No existe solucion en ese intervalo','ERROR','ERROR','No se realizo ningún calculo']
        print('No existe solucion en ese intervalo') 
        return x


def newtonRas(ecua,p_0,n=1000, tol=0.001):
    texto = ""
    x=symbols('x')
    df = diff(funcion(x,ecua), x)
    """
    Método Newton Raphson
    :param f: Funcion a la que se le intenta encontrar una solucion para la ecuacion f(x)=0, previamente definida
    :param df: derivada de la función
    :param p_0: semilla (punto inicial)
    :param tol: toleracia, criterio de parada
    :param n: número máximo de iteraciones, criterio de parada
    :return: solución exacta o aproximada, si tiene.
    """
    print('ite {:<2}: p_{:<2}={:.7f}'.format(0,0,p_0))
    e_abs = 1
    i = 1
    while i <= n:
        
        if funcion(p_0,str(df)) == 0:  # división por cero
            print('Solución no encontrara - df(x)=0')
            return None
        
        p_1 = p_0 - (funcion(p_0,ecua))/(funcion(p_0,str(df)))  # fórmula método
        e_abs = abs(p_1-p_0)
        print('ite {:<2}: p_{:<2}={:.7f}, error absoluto={:.7f}'.format(i,i,p_1,e_abs))
        texto += ('ite {:<2}: p_{:<2}={:.7f}, error absoluto={:.7f} \n'.format(i,i,p_1,e_abs))
        
        if e_abs < tol: #criterio de parada
            print('Solución encotrada x={:.7f}, iteraciones: {}'.format(p_1,i))
            texTreturn = ['{:.7f}'.format(p_1),'{} iteraciones'.format(i),'{}'.format(e_abs)+'%',texto]
            return texTreturn
        
        p_0 = p_1
        i += 1
    print('Solución no encontrada, iteraciones agotadas: {}'.format(i-1))
    texTreturn = ['Solución no encontrada','iteraciones agotadas','S.N','Solución no encontrada']
    return texTreturn

def derivadaNumerica(ecua,x0):

    x=symbols('x')
    sol = diff(funcion(x,ecua), x)
    sol2 = diff(funcion(x,ecua), x,2)

    texTreturn = ['{}'.format(sol), '{}'.format(sol2),'{}'.format(sol.subs(x,x0))]

    return texTreturn

def metodo_secante(ecua, p_0, p_1, n=50, tol=10**-4):
    texto = ""
    """
    Método Newton Raphson
    :param f: Funcion a la que se le intenta encontrar una solucion para la ecuacion f(x)=0, previamente definida
    :param p_0: semilla (punto inicial)
    :param p_1: semilla (punto inicial)
    :param tol: toleracia, criterio de parada
    :param n: número máximo de iteraciones, criterio de parada
    :return: solución exacta o aproximada, si tiene.
    """
    e_abs = abs(p_1 - p_0)
    
    print('ite {:<2}: punto {:<2}={:.7f}'.format(0,0,p_0))
    print('ite {:<2}: punto {:<2}={:.7f}, e_abs={:.7f}'.format(1,1,p_1,e_abs))
    texto += ('iteración {:<2}: punto {:<2}= {:.7f}, e_abs = {:.7f} \n'.format(1,1,p_1,e_abs))
    
    i = 2
    while i <= n:
        if funcion(p_1,ecua) == funcion(p_0,ecua): #división por cero
            print('Solución no encontrada (error en los valores iniciales)')
            texTreturn = ['solucion no encontrada','solucion no encontrada','solucion no encontrada','solucion no encontrada']
            return texTreturn
        
        p_2 = p_0 - (funcion(p_0,ecua)*(p_1 - p_0))/(funcion(p_1,ecua) - funcion(p_0,ecua))  # fórmula método secante
        e_abs = abs(p_2 - p_1)
        print('iteración {:<2}: punto {:<2} = {:.7f}, e_abs = {:.7f}'.format(i,i,p_2,e_abs))
        texto += ('iteración {:<2}: punto {} = {:.7f}, e_abs = {:.7f} \n'.format(i,i,p_2,e_abs))
        
        if e_abs < tol:  # criterio de parada
            print('Solución encontrada x= {:.7f}, iteraciones: {}'. format(p_2,i))
            texTreturn = ['{:.7f}'.format(p_2),'{} iteraciones'.format(i),'{}'.format(e_abs)+'%',texto]
            return texTreturn
        p_0 = p_1
        p_1 = p_2
        i += 1
    print('Solución no encontrada, iteraciones agotadas: {}'.format(i-1))
    texTreturn = ['Solución no encontrada','iteraciones agotadas','S.N','Solución no encontrada']
    return texTreturn


def calculoPolynomio(P):
    texTreunr = "[ "
    burbuja = np.roots(P)
    cont = 0
    tam = len(burbuja)
    for n in burbuja:
        if (tam-1) > cont:
            texTreunr += str(n) +', '
        else:
            texTreunr += str(n)+ ' '
        cont+=1

    texTreunr += '].'
    return texTreunr


def integracionRIZ(ecua, pA, pB, n):
    x = ''
    suma = 0.0
    Dx = (pB-pA)/float(n)
    for i in range(n):
        altura = funcion(pA,ecua)
        Area = Dx * altura
        suma = suma + Area
        pA = pA +Dx

    x = '{}'.format(suma)

    return x

def integracionRDE(ecua, pA, pB, n):
    x = ''
    suma = 0.0
    Dx = (pB-pA)/float(n)
    for i in range(n):
        altura = funcion(pA + Dx,ecua)
        Area = Dx * altura
        suma = suma + Area
        pA = pA +Dx

    x = '{}'.format(suma)

    return x

def integracionRMID(ecua, pA, pB, n):
    x = ''
    suma = 0.0
    Dx = (pB-pA)/float(n)
    for i in range(n):
        altura = funcion(pA+(Dx)/2,ecua)
        Area = Dx * altura
        suma = suma + Area
        pA = pA +Dx

    x = '{}'.format(suma)

    return x




def integracionRectangular(ecua, pA, pB, n):
    iz = integracionRIZ(ecua, pA, pB, n)
    de = integracionRDE(ecua, pA, pB, n)
    mid = integracionRMID(ecua, pA, pB, n)

    x = [iz,de, mid]
    return x


def integracionTrapecios(ecua, pA, pB, n):
    xy=['','']
    suma = 0.0
    Dx = (pB - pA)/float(n)
    auxpA = pA
    for i in range(n):
        Area = ((funcion(pA,ecua) + funcion(pA+Dx,ecua)) * Dx / 2)
        suma = suma + Area
        pA = pA + Dx

    x = symbols("x")
    value = integrate((funcion(x,ecua)), (x,auxpA,pB)).evalf()
    xy=['{}'.format(suma),'{}%'.format(abs(value - suma)/value * 100)]

    return xy

def intSimpson13(ecua, pA, pB, n):
    xy=['Error','Error']
    suma = 0.0
    auxpA = pA
    auxpB = pB
    Dx = (pB - pA) / float(n)
    for i in range(n):
        pB = pA + Dx
        m = (pA + pB) / 2
        Area = (pB - pA) / 6 * (funcion(pA, ecua) + 4 * funcion(m, ecua) + funcion(pB, ecua))
        suma = suma + Area
        pA = pB
    x = symbols("x")
    value = integrate((funcion(x,ecua)), (x,auxpA,auxpB)).evalf()
    xy=['{}'.format(suma),'{}%'.format(abs(value - suma)/value * 100)]
    return xy

def intSimpson38(ecua, pA, pB, n):
    xy=['Error','Error']
    suma = 0.0
    auxpA = pA
    auxpB = pB
    Dx = (pB - pA) / float(n)
    for i in range(n):
        pB = pA + Dx
        m1 = (2 * pA + pB) / 3
        m2 = (pA + 2 * pB) / 3
        Area = (pB - pA) / 8 * (funcion(pA, ecua) + 3 * funcion(m1, ecua) + 3 * funcion(m2, ecua) + funcion(pB, ecua))
        suma = suma + Area
        pA = pB
    x = symbols("x")
    value = integrate((funcion(x,ecua)), (x,auxpA,auxpB)).evalf()
    xy=['{}'.format(suma),'{}%'.format(abs(value - suma)/value * 100)]
    return xy