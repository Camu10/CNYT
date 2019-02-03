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
def sumaVectores(mat1,mat2):
    res = []
    for i in range(len(mat1)):
        res.append((mat1[i][0]+mat2[i][0],mat1[i][1]+mat2[i][1]))
    return res
    
def inversoVector(mat):
    res = []
    for i in range(len(mat)):
        res.append((-mat[i][0],-mat[i][1]))
    return res
def productoScalarMatriz(scalar,matriz):
    res = []
    for i in matriz:
        res.append(producto(scalar,i))
    return res
def transpuesta(mat):
    res=[[] for _ in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            res[j].append(mat[i][j])
    return res
def conjugadoMatriz(mat):
    res=[[] for _ in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            res[i].append((mat[i][j][0],-mat[i][j][1]))
    return res
def productoMatrices(mat1,mat2):
    res=[[] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1[i])):
            c = (0,0)
            for k in range(len(mat2)):
                c = suma(c,producto(mat1[i][k],mat2[k][j]))
            res[i].append(c)
    return res
