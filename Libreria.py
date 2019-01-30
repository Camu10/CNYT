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

def sumaMatriz(mat):
    res = []
    for i in range(len(mat[0])):
        res.append((mat[0][i][0]+mat[1][i][0],mat[0][i][1]+mat[1][i][1]))
    return res
    
def inverso(mat):
    res = []
    for i in range(len(mat)):
        res.append((-mat[i][0],-mat[i][1]))
    return res
def productoScalarMatriz(scalar,matriz):
    res = []
    for i in matriz:
        res.append(producto(scalar,i))
    return res    
    
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
