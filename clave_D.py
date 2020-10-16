import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*3 = 24
"""


# start-->
def multiplicar(numero1, numero2, numero3):
    result = numero1 * numero2 * numero3
    print(result)
    return result


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1000 al 2000
"""


# start-->
def sumaDivTresYCincoPlus():
    contador = 1000
    sumaDeNumeros = 0
    while contador <= 2000:
        contador += 1
        if (contador % 3 == 0) and (contador % 5 == 0):
            sumaDeNumeros += contador
        else:
            pass

    result = sumaDeNumeros
    print(result)
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area y el volumen de un ortoedro
longitud = 10 m
latitud = 6 m
altura = 5 m

area: A = 2(longitud · latitud + longitud · altura + latitud · altura)
volumen: V = longitud · latitud · altura
"""


# start-->
def definicionOrtoedro(Longitud, Latitud, Altura):
    area = obtenerArea(Longitud, Latitud, Altura)
    volumen = obtenerVolumen(Longitud, Latitud, Altura)
    result = {"area": area, "volumen": volumen}
    print(result)
    return result


def obtenerArea(Longitud, Latitud, Altura):
    area = 2 * ((Longitud * Latitud) + (Longitud * Altura) + (Latitud * Altura))
    return area


def obtenerVolumen(Longitud, Latitud, Altura):
    volumen = Longitud * Latitud * Altura
    return volumen


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Ortoedro:
    def definicionOrtoedro(Longitud, Latitud, Altura):
        area = obtenerArea(Longitud, Latitud, Altura)
        volumen = obtenerVolumen(Longitud, Latitud, Altura)
        result = {"area": area, "volumen": volumen}
        print(result)
        return result

    def obtenerArea(Longitud, Latitud, Altura):
        area = 2 * ((Longitud * Latitud) + (Longitud * Altura) + (Latitud * Altura))
        return area

    def obtenerVolumen(Longitud, Latitud, Altura):
        volumen = Longitud * Latitud * Altura
        return volumen


"""
***************************************************************
@@ ejercicio 5 @@ GG WP no pude hacerlo, me dieron ganas de llorar :c

VentaComputadoras
Computadora
    procesador
    ram
    tarjeta_grafica
    ssd
    costo
    conDescuento
    descuento
    conPlazo
    cuota
"""


class VentaComputadoras:
    def orden(self):
        pass

    def totalProcesadorIntel(self):
        return 0

    def totalRam16ConDescuento(self):
        return 0


class Computadora:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/Cosmonaut-afk/parcial-python"
