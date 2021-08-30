
#convertir Decimal a Binario*
def ConverDaB(burbuja):
    negativo = ""
    if burbuja<0:
        burbuja = burbuja*(-1)
        negativo = "-"

    bFracion = ""
    fracion = burbuja
    fracion = fracion - int(burbuja)
    cont = 0
    while True:
        fracion = fracion * 2
        
        if fracion >= 1:
            bFracion += "1"
            fracion = fracion - 1
        else:
            bFracion += "0"
        
        cont += 1
        if cont >=50 or fracion == 0:
            break
    
    binario = str(bin(int(burbuja))[2:])
    binario = negativo + binario + "." + bFracion
    
    return binario



#convertir Decimal a octal*
def ConverDaO(burbuja):
    negativo = ""
    if burbuja<0:
        burbuja = burbuja*(-1)
        negativo = "-"
    octal = ""

    bFracion = ""
    fracion = burbuja
    fracion = fracion - int(burbuja)
    burbuja = int(burbuja)
    cont = 0
    while True:
        fracion = fracion * 8
        
        if fracion >= 1 and fracion < 2:
            bFracion += "1"
            fracion = fracion - 1
        elif fracion >= 2 and fracion < 3:
            bFracion += "2"
            fracion = fracion - 2
        elif fracion >= 3 and fracion < 4:
            bFracion += "3"
            fracion = fracion - 3
        elif fracion >= 4 and fracion < 5:
            bFracion += "4"
            fracion = fracion - 4
        elif fracion >= 5 and fracion < 6:
            bFracion += "5"
            fracion = fracion - 5
        elif fracion >= 6 and fracion < 7:
            bFracion += "6"
            fracion = fracion - 6
        elif fracion >= 7 :
            bFracion += "7"
            fracion = fracion - 7
        elif fracion <= 0:
            bFracion += "0"
        
        cont += 1
        if cont >=50 or fracion == 0:
            break

    while True:

        octal = str(burbuja%8) + octal
        burbuja = burbuja//8

        if burbuja <8:
            octal = str(burbuja) + octal
            break

    octal = negativo + octal + "." + bFracion
    return octal

#convertir Decimal a hexadecimal*
def ConverDaH(burbuja):
    negativo = ""
    if burbuja<0:
        burbuja = burbuja*(-1)
        negativo = "-"
    nb = ""
    hexa = ""

    bFracion = ""
    fracion = burbuja
    fracion = fracion - int(burbuja)
    burbuja = int(burbuja)
    cont = 0
    while True:
        fracion = fracion * 16
        
        if fracion >= 1 and fracion < 2:
            bFracion += "1"
            fracion = fracion - 1
        elif fracion >= 2 and fracion < 3:
            bFracion += "2"
            fracion = fracion - 2
        elif fracion >= 3 and fracion < 4:
            bFracion += "3"
            fracion = fracion - 3
        elif fracion >= 4 and fracion < 5:
            bFracion += "4"
            fracion = fracion - 4
        elif fracion >= 5 and fracion < 6:
            bFracion += "5"
            fracion = fracion - 5
        elif fracion >= 6 and fracion < 7:
            bFracion += "6"
            fracion = fracion - 6
        elif fracion >= 7 and fracion < 8:
            bFracion += "7"
            fracion = fracion - 7
        if fracion >= 8 and fracion < 9:
            bFracion += "8"
            fracion = fracion - 8
        elif fracion >= 9 and fracion < 10:
            bFracion += "9"
            fracion = fracion - 9
        elif fracion >= 10 and fracion < 11:
            bFracion += "A"
            fracion = fracion - 10
        elif fracion >= 11 and fracion < 12:
            bFracion += "B"
            fracion = fracion - 11
        elif fracion >= 12 and fracion < 13:
            bFracion += "C"
            fracion = fracion - 12
        elif fracion >= 13 and fracion < 14:
            bFracion += "D"
            fracion = fracion - 13
        elif fracion >= 14 and fracion < 15:
            bFracion += "E"
            fracion = fracion - 14
        elif fracion >= 15:
            bFracion += "F"
            fracion = fracion - 15
        elif fracion <= 0:
            bFracion += "0"
        
        cont += 1
        if cont >=50 or fracion == 0:
            break


    while True:

        if burbuja%16 == 0:
            nb = "0"
        if burbuja%16 == 1:
            nb = "1"
        if burbuja%16 == 2:
            nb = "2"
        if burbuja%16 == 3:
            nb = "3"
        if burbuja%16 == 4:
            nb = "4"
        if burbuja%16 == 5:
            nb = "5"
        if burbuja%16 == 6:
            nb = "6"
        if burbuja%16 == 7:
            nb = "7"
        if burbuja%16 == 8:
            nb = "8"
        if burbuja%16 == 9:
            nb = "9"
        elif burbuja%16 == 10:
            nb = "A"
        elif burbuja%16 == 11:
            nb = "B"
        elif burbuja%16 == 12:
            nb = "C"
        elif burbuja%16 == 13:
            nb = "D"
        elif burbuja%16 == 14:
            nb = "E"
        elif burbuja%16 == 15:
            nb = "F"

        hexa = nb + hexa
        burbuja = burbuja//16

        if burbuja == 0:
            del nb
            break

    hexa = negativo + hexa + "." + bFracion
    return hexa

#Convertir binario a decimal*
def ConverBaD(burbuja):
    decimal = 0.0
    frac = False
    bfracion = ""
    for n in burbuja:
        if n ==".":
            frac = True

    if frac:
        x = burbuja.split(".")
        bfracion = x[1]
        burbuja = x[0]

    burbuja2 = ""
    cont2 = 0
    negativo = ""
    for n in burbuja:
        if cont2 == 0 and n == "-":
            negativo = "-"
        else:
            burbuja2 = burbuja2 + n
        
        cont2 += 1

    burbuja = burbuja2

    cont = len(burbuja)
    for n in burbuja:
        cont-=1
        decimal += (2**cont)*int(n)

    if frac:
        for n in bfracion:
            cont -= 1
            decimal += (2**cont)*int(n)
    
    if negativo == "-":
        decimal = decimal*(-1)

    return decimal

#Convertir Octal a Decimal*
def ConverOaD(burbuja):
    decimal = 0
    negativo = False
    if burbuja < 0:
        negativo = True
        burbuja = burbuja*(-1)

    burbuja = str(burbuja)

    frac = False
    bfracion = ""
    for n in burbuja:
        if n ==".":
            frac = True

    if frac:
        x = burbuja.split(".")
        bfracion = x[1]
        burbuja = x[0]


    cont = len(burbuja)
    for n in burbuja:
        cont-=1
        decimal += (8**cont)*int(n)

    if frac:
        for n in str(bfracion):
            cont-=1
            decimal += (8**cont)*int(n)

    
    if negativo:
        decimal = decimal * (-1)

    return decimal

#Convertir Hexa a Decimal*
def ConverHaD(burbuja):
    decimal = 0
    nb = 0

    frac = False
    bfracion = ""
    for n in burbuja:
        if n ==".":
            frac = True

    if frac:
        x = burbuja.split(".")
        bfracion = x[1]
        burbuja = x[0]

    burbuja2 = ""
    negativo = False
    for n in burbuja:
        if n == "-":
            negativo = True
        else:
            burbuja2 = burbuja2 + n
 

    burbuja = burbuja2

    cont = len(burbuja)
    for n in burbuja:
        cont-=1

        if n == '0':
            nb = 0
        elif n== '1':
            nb = 1
        elif n== '2':
            nb = 2
        elif n== '3':
            nb = 3
        elif n== '4':
            nb = 4
        elif n== '5':
            nb = 5
        elif n== '6':
            nb = 6
        elif n== '7':
            nb = 7
        elif n== '8':
            nb = 8
        elif n== '9':
            nb = 9
        elif n== 'A':
            nb = 10
        elif n== 'B':
            nb = 11
        elif n== 'C':
            nb = 12
        elif n== 'D':
            nb = 13
        elif n== 'E':
            nb = 14
        elif n== 'F':
            nb = 15

        decimal += (16**cont)*int(nb)

    if frac:
        for n in bfracion:
            cont-=1

            if n == '0':
                nb = 0
            elif n== '1':
                nb = 1
            elif n== '2':
                nb = 2
            elif n== '3':
                nb = 3
            elif n== '4':
                nb = 4
            elif n== '5':
                nb = 5
            elif n== '6':
                nb = 6
            elif n== '7':
                nb = 7
            elif n== '8':
                nb = 8
            elif n== '9':
                nb = 9
            elif n== 'A':
                nb = 10
            elif n== 'B':
                nb = 11
            elif n== 'C':
                nb = 12
            elif n== 'D':
                nb = 13
            elif n== 'E':
                nb = 14
            elif n== 'F':
                nb = 15

            decimal += (16**cont)*int(nb)


    if negativo:
        decimal = decimal* (-1)

    return decimal

#conv

def ConverDaBin(burbuja):
    negativo = "+"
    if burbuja<0:
        burbuja = burbuja*(-1)
        negativo = "-"

    bFracion = ""
    fracion = burbuja
    fracion = fracion - int(burbuja)
    cont = 0
    while True:
        fracion = fracion * 2
        
        if fracion >= 1:
            bFracion += "1"
            fracion = fracion - 1
        else:
            bFracion += "0"
        
        cont += 1
        if cont >=50 or fracion == 0:
            break
    
    binario = str(bin(int(burbuja))[2:])
    binario = negativo + binario + "." + bFracion
    
    return binario

def CalcularMantiza32(burbuja):
    mantiza = ""
    ini = True
    for n in burbuja:
        if ini:
            mantiza = n + "."
            ini = False
        else:
            if n != ".":
                mantiza = mantiza + n

    fmantiza = ""
    long = len(mantiza)
    cont = 0
    
    if long > 25:
        for n in mantiza:
            fmantiza = fmantiza + n
            cont += 1
            if cont == 25:
                break
    elif long < 25:
        while True:
            fmantiza = fmantiza + "0"
            long += 1
            if long == 25:
                fmantiza = mantiza + fmantiza
                break
    else:
        fmantiza = mantiza
    
    return fmantiza

def CalcularMantiza64(burbuja):
    mantiza = ""
    ini = True
    for n in burbuja:
        if ini:
            mantiza = n + "."
            ini = False
        else:
            if n != ".":
                mantiza = mantiza + n

    fmantiza = ""
    long = len(mantiza)
    cont = 0
    
    if long > 54:
        for n in mantiza:
            fmantiza = fmantiza + n
            cont += 1
            if cont == 25:
                break
    elif long < 54:
        while True:
            fmantiza = fmantiza + "0"
            long += 1
            if long == 54:
                fmantiza = mantiza + fmantiza
                break
    else:
        fmantiza = mantiza
    
    return fmantiza

def CalcularExponente32(burbuja):
    entero = burbuja.split(".")
    long=len(entero[0])-1

    long = long + 127
    flong = ConverDaB(float(long))

    fflong = flong.split(".")
    return fflong[0]


def CalcularExponente64(burbuja):
    entero = burbuja.split(".")
    long=len(entero[0])-1

    long = long + 1023
    flong = ConverDaB(float(long))

    fflong = flong.split(".")
    return fflong[0]




