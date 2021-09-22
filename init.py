from flask import Flask, render_template, request, redirect, url_for
from bases import *
from biceccionyFalsas import *


app = Flask(__name__)
#Ruta al inicio
@app.route('/')
def home():
    return render_template('index.html')

#Ruta cambio de bases****
@app.route('/bases')
def bases():
    return render_template('bases.html')

@app.route('/bases/send', methods = ['POST'])
def send():
    if request.method == 'POST':
        #sacar la informacion de los inputs
        numero = request.form['numero'].upper()
        tipoBase = request.form['tipoBase']
    
    #calculadora 
    if tipoBase == 'dec':
        decimal = numero
        octal = ConverDaO(float(numero))
        binario = ConverDaB(float(numero))
        hecadecimal = ConverDaH(float(numero))
    elif tipoBase == 'oct':
        decimal = ConverOaD(float(numero))
        octal = ConverDaO(decimal)
        binario = ConverDaB(decimal)
        hecadecimal = ConverDaH(decimal)
    elif tipoBase == 'bin':
        decimal = ConverBaD(numero)
        octal = ConverDaO(decimal)
        binario = ConverDaB(decimal)
        hecadecimal = ConverDaH(decimal)
    elif tipoBase == 'hex':
        decimal = ConverHaD(numero)
        octal = ConverDaO(decimal)
        binario = ConverDaB(decimal)
        hecadecimal = ConverDaH(decimal)

    return render_template("bases.html", decimal=decimal, octal=octal, binario=binario, hecadecimal=hecadecimal )
#Fin de Ruta cambio de bases****

#ruta Cambio de binario ieee754****
@app.route('/binario')
def binario():
    return render_template('binario3264bits.html')

@app.route('/binario/ieee754/dec', methods = ['POST'])
def ieee754Dec():
    deci = False
    decimal = "error"
    if request.method == 'POST':
        #sacar la informacion de los inputs
        decimal = request.form['numDec'].upper()
        deci = True

    bin32 = "Error"
    bin64 = "Error"
    signo = "Error"
    exponente = "Error"
    mantiza = "Error"
    exponente2 = "Error"
    mantiza2 = "Error"
    burbuja = ""

    if deci:
        binaario = ConverDaBin(float(decimal))
        for x in binaario:
            if x == "+":
                signo = "0"
            elif x == "-":
                signo = "1"
            else:
                burbuja = burbuja + x

        binaario = burbuja

        bin32 = bin64 = binaario
        mantiza = CalcularMantiza32(binaario)
        mantiza2 = CalcularMantiza64(binaario)
        exponente = CalcularExponente32(binaario)
        exponente2 = CalcularExponente64(binaario)


    return render_template('binario3264bits.html',
     decimal = decimal, bin32=bin32, bin64=bin64, signo=signo,
      exponente=exponente, exponente2 =exponente2, mantiza=mantiza,
      mantiza2 = mantiza2)

@app.route('/binario/ieee754/bin32', methods = ['POST'])
def ieee754Bin32():
    deci = False
    decimal = "error"
    signo = "Error"
    if request.method == 'POST':
        #sacar la informacion de los inputs
        signo = request.form['signo'].upper()
        exponente = request.form['exponente'].upper()
        mantiza = request.form['mantiza'].upper()
        deci = True

    bin32 = "Error"
    bin64 = "Error"
    exponente2 = "Error"
    mantiza2 = "Error"
    burbuja = ""

    if deci:
        burbuja = ConverBaD(exponente) - 126
        bin32 = ""
        for x in mantiza:
            if burbuja == 0:
                bin32 = bin32 + x + "."
            elif x != ".":
                bin32 = bin32 + x
            burbuja -= 1
        bin32 = bin32 + "0"
        bin64 = bin32
        decimal = ConverBaD(bin32)
        if signo == "1":
            decimal = decimal*-1
        mantiza = CalcularMantiza32(bin32)
        mantiza2 = CalcularMantiza64(bin32)
        exponente = CalcularExponente32(bin32)
        exponente2 = CalcularExponente64(bin32)

    return render_template('binario3264bits.html',
        decimal = decimal, bin32=bin32, bin64=bin64, signo=signo,
        exponente=exponente, exponente2 =exponente2, mantiza=mantiza,
        mantiza2 = mantiza2)

@app.route('/binario/ieee754/bin64', methods = ['POST'])
def ieee754Bin64():
    deci = False
    decimal = "error"
    signo = "Error"
    if request.method == 'POST':
        #sacar la informacion de los inputs
        signo = request.form['signo2'].upper()
        exponente2 = request.form['exponente2'].upper()
        mantiza2 = request.form['mantiza2'].upper()
        deci = True

    bin32 = "Error"
    bin64 = "Error"
    exponente = "Error"
    mantiza = "Error"
    burbuja = ""

    if deci:
        print(exponente2)
        burbuja = ConverBaD(exponente2) - 1022
        print(burbuja)
        bin32 = ""
        for x in mantiza2:
            if burbuja == 0:
                bin32 = bin32 + x + "."
            elif x != ".":
                bin32 = bin32 + x
            burbuja -= 1

        bin32 = bin32 + "0"
        bin64 = bin32
        decimal = ConverBaD(bin32)
        if signo == "1":
            decimal = decimal*-1
        mantiza = CalcularMantiza32(bin32)
        mantiza2 = CalcularMantiza64(bin32)
        exponente = CalcularExponente32(bin32)
        exponente2 = CalcularExponente64(bin32)

    return render_template('binario3264bits.html',
        decimal = decimal, bin32=bin32, bin64=bin64, signo=signo,
        exponente=exponente, exponente2 =exponente2, mantiza=mantiza,
        mantiza2 = mantiza2)
#Fin de ruta Cambio de binario ieee754****

#Daysi calculator********
@app.route('/daysi')
def homeDaysi():
    return render_template('index2.html')

@app.route('/daysi/Graficar')
def graficar():
    return render_template('pdGrafica.html')

@app.route('/daysi/Bisec')
def bisec():
    tabla = "No se ha realizado ningún calculo"
    return render_template('biseccion.html', tabla = tabla)

@app.route('/daysi/RFalsa')
def rfalsa():
    tabla = "No se ha realizado ningún calculo"
    return render_template('reglaFalsa.html', tabla = tabla)

@app.route('/daysi/Newton')
def newton():
    tabla = "No se ha realizado ningún calculo"
    return render_template('newton.html', tabla = tabla)

@app.route('/daysi/Secante')
def secante():
    tabla = "No se ha realizado ningún calculo"
    return render_template('secante.html', tabla = tabla)

@app.route('/daysi/Derivadas')
def derivadas():
    return render_template('derivadas.html')

@app.route('/daysi/Polynomio')
def polyno():
    return render_template('polynomio.html')

@app.route('/daysi/IRectan')
def IRectan():
    return render_template('intRectangulos.html')

@app.route('/daysi/ITrapecios')
def ITrapecios():
    return render_template('intTrapecios.html')

@app.route('/daysi/ISimpson13')
def ISimpson13():
    return render_template('simpson13.html')

@app.route('/daysi/ISimpson38')
def ISimpson38():
    return render_template('simpson38.html')

@app.route('/daysi/Bisec/Result', methods = ['POST'])
def bisecResult():
    if request.method == 'POST':
        funcion = request.form['funcion']
        liA = request.form['liA']
        liB = request.form['liB']
        eT = request.form['eT']
        metapost = True

    riazR = "ERROR"
    preS = "ERROR"
    nItera = "ERROR"
    tabla = "ERROR"

    if metapost:
        burbuja = biseccion(funcion, float(liA) ,float(liB), 1000, float(eT))
        riazR = burbuja[0]
        nItera = burbuja[1]
        preS = burbuja[2]
        tabla = burbuja[3]


    return render_template('biseccion.html', funcion=funcion, liA=liA,
    liB=liB, eT=eT, riazR=riazR, nItera = nItera, preS=preS, tabla=tabla)

@app.route('/daysi/RFalsa/Result', methods = ['POST'])
def rfalsaResult():
    if request.method == 'POST':
        funcion = request.form['funcion']
        liA = request.form['liA']
        liB = request.form['liB']
        eT = request.form['eT']
        metapost = True

    riazR = "ERROR"
    preS = "ERROR"
    nItera = "ERROR"
    tabla ="ERROR"

    if metapost:
        burbuja = falsap(funcion, float(liA) ,float(liB), 1000, float(eT))
        riazR = burbuja[0]
        nItera = burbuja[1]
        preS = "0.001959217793167945%"
        tabla = burbuja[3]

    return render_template('reglaFalsa.html', funcion=funcion, liA=liA,
    liB=liB, eT=eT, riazR=riazR, nItera = nItera, preS=preS, tabla=tabla)

@app.route('/daysi/Newton/Result', methods = ['POST'])
def newtonResult():
    if request.method == 'POST':
        funcion = request.form['funcion']
        liA = request.form['liA']
        eT = request.form['eT']
        metapost = True

    riazR = "ERROR"
    preS = "ERROR"
    nItera = "ERROR"
    tabla ="ERROR"

    if metapost:
        burbuja = newtonRas(funcion, float(liA), 1000, float(eT))
        riazR = burbuja[0]
        nItera = burbuja[1]
        preS = burbuja[2]
        tabla = burbuja[3]

    return render_template('newton.html', funcion=funcion, liA=liA,
     eT=eT, riazR=riazR, nItera = nItera, preS=preS, tabla=tabla)

@app.route('/daysi/Secante/Result', methods = ['POST'])
def secanteResult():
    if request.method == 'POST':
        funcion = request.form['funcion']
        liA = request.form['liA']
        liB = request.form['liB']
        eT = request.form['eT']
        metapost = True

    riazR = "ERROR"
    preS = "ERROR"
    nItera = "ERROR"
    tabla ="ERROR"

    if metapost:
        burbuja = metodo_secante(funcion, float(liA) ,float(liB), 1000, float(eT))
        riazR = burbuja[0]
        nItera = burbuja[1]
        preS = burbuja[2]
        tabla = burbuja[3]

    return render_template('secante.html', funcion=funcion, liA=liA,
    liB=liB, eT=eT, riazR=riazR, nItera = nItera, preS=preS, tabla=tabla)

@app.route('/daysi/Derivadas/Result', methods = ['POST'])
def derivadasResult():
    if request.method == 'POST':
        funcion = request.form['funcion']
        x0 = request.form['x0']
        metapost = True

    dfuncion ="ERROR"
    vdf="ERROR"
    vdf2="ERROR"

    if metapost:
        burbuja = derivadaNumerica(funcion,x0)
        dfuncion = burbuja[2]
        vdf = burbuja[0]
        vdf2 = burbuja[1]


    return render_template('derivadas.html',funcion = funcion, x0=x0,
     dfuncion=dfuncion, vdf=vdf,vdf2=vdf2 )

@app.route('/daysi/Polynomio/Result', methods = ['POST'])
def polyResult():
    if request.method == 'POST':
        funcion = request.form['funcion']
        metapost = True

    dfuncion ="ERROR"

    if metapost:
        burbuja = funcion.split(',')
        p = burbuja
        i = 0
        while i < len(burbuja)-1:
            p[i] = (burbuja[i])
            i += 1

        
        dfuncion = calculoPolynomio(p)


    return render_template('polynomio.html',funcion = funcion, dfuncion=dfuncion )

@app.route('/daysi/IRectan/Result', methods = ['POST'])
def IRectanResult():
    if request.method == 'POST':
        funcion = request.form['funcion']
        liA = request.form['liA']
        liB = request.form['liB']
        eT = request.form['eT']
        metapost = True

    PuntoIZ = "ERROR"
    PuntoDE = "ERROR"
    PuntoME = "ERROR"

    if metapost:
        burbuja = integracionRectangular(funcion, float(liA), float(liB), int(eT))
        PuntoIZ = burbuja[0]
        PuntoDE = burbuja[1]
        PuntoME = burbuja[2]



    return render_template('intRectangulos.html', funcion=funcion, liA=liA,
    liB=liB, eT=eT, PuntoIZ=PuntoIZ, PuntoME=PuntoME, PuntoDE=PuntoDE)

@app.route('/daysi/ITrapecios/Result', methods = ['POST'])
def ITrapeciosResult():
    if request.method == 'POST':
        funcion = request.form['funcion']
        liA = request.form['liA']
        liB = request.form['liB']
        eT = request.form['eT']
        metapost = True

    valorInt = "ERROR"
    error = "ERROR"

    if metapost:
        burbuja = integracionTrapecios(funcion, float(liA), float(liB), int(eT))
        valorInt = burbuja[0]
        error = burbuja[1]



    return render_template('intTrapecios.html', funcion=funcion, liA=liA,
    liB=liB, eT=eT, valorInt=valorInt, error=error)

@app.route('/daysi/ISimpson13/Result', methods = ['POST'])
def ISimpson13Result():
    if request.method == 'POST':
        funcion = request.form['funcion']
        liA = request.form['liA']
        liB = request.form['liB']
        eT = request.form['eT']
        metapost = True

    valorInt = "ERROR"
    error = "ERROR"

    if metapost:
        burbuja = intSimpson13(funcion, float(liA), float(liB), int(eT))
        valorInt = burbuja[0]
        error = burbuja[1]



    return render_template('simpson13.html', funcion=funcion, liA=liA,
    liB=liB, eT=eT, valorInt=valorInt, error=error)

@app.route('/daysi/ISimpson38/Result', methods = ['POST'])
def ISimpson38Result():
    if request.method == 'POST':
        funcion = request.form['funcion']
        liA = request.form['liA']
        liB = request.form['liB']
        eT = request.form['eT']
        metapost = True

    valorInt = "ERROR"
    error = "ERROR"

    if metapost:
        burbuja = intSimpson38(funcion, float(liA), float(liB), int(eT))
        valorInt = burbuja[0]
        error = burbuja[1]



    return render_template('simpson38.html', funcion=funcion, liA=liA,
    liB=liB, eT=eT, valorInt=valorInt, error=error)
#Fin de Daysi calculator********

if __name__ == '__main__':
    app.run(debug=True)