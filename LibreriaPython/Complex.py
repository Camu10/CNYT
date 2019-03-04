from math import *
from ComplexMath import *
from Simuladores import *

def modulo(c):
    return sqrt((c[0]**2)+(c[1]**2))

def conjugado(c):
    return (c[0],-c[1])

def fase(c):
    return atan((c[1]/c[0]))

def impresion(c):
    aux = c[1]
    if c[1] == 0:
        return str(c[0])
    if c[1] > 0:
        aux = " + " + str(c[1])
        if c[1] == 1:
            return str(c[0])+ " + i"
        return str(c[0])+ " + " +str(c[1]) +"i"
    elif c[1]==-1:
        return str(c[0])+ " - i"
    return str(c[0])+" - "+ str(abs(c[1])) +"i"
