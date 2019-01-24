from math import *
def suma(c1,c2):
    return (c1[0] + c2[0] , c1[1]+c2[1])

def resta(c1,c2):
    return (c1[0] - c2[0] , c1[1] - c2[1])
    
def producto(c1,c2):
    return (c1[0]*c2[0]- c1[1]*c2[1] , c1[0]*c2[1] + c2[0]*c1[1])

def division(c1,c2):
    divisor = (c1[1]**2) + (c2[1]**2)
    dividendo1 = c1[0]*c1[1] + c2[0]*c2[1]
    dividendo2 = c1[1]*c2[0] - c1[0]*c2[1]
    return (dividendo1/divisor,dividendo2/divisor)

def modulo(c):
    return sqrt((c[0]**2)+(c[1]**2))

def conjugado(c):
    return (c[0],-c[1])

def cartesiano_polar(c):
    angulo = atan((c[1]/c[0]))
    p = sqrt((c[0]**2)+(c[1]**2))
    return (p,angulo)

def polar_cartesiano(c):
    x = c[0]*cos(c[1])
    y = c[0]*sin(c[1])
    return (x,y)

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

def main():
    c1 = (3,-1)
    c2 = (1,4)
    resultado = producto(c1,c2)
    print(impresion(resultado))
main()
