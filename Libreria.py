from math import *

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


def main():
    c1 = (3,-1)
    c2 = (1,4)
    resultado = producto(c1,c2)
    mat = [[(6,-4),(7,3),(4.2,-8.1),(0,-3)],[(16,2.3),(0,-7),(6,0),(0,-4)]]
    mat1 = [(6,3),(0,0),(5,1),(4,0)]
    scalar = (3,2)
    print(impresion(resultado))
    print(sumaMatriz(mat))
    print(inverso(mat[0]))
    print(productoScalarMatriz(scalar,mat1))
    
main()
