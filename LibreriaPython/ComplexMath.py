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
def sumaMatrices(mat1,mat2):
    res = [[] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1[i])):
            res[i].append(mat1[i][j] + mat2[i][j])
    return res
def restaVectores(mat1,mat2):
    res = []
    for i in range(len(mat1)):
        res.append(mat1[i] - mat2[i])
    return res
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
def productoMatricesComplejas(mat1,mat2):
    res=[[] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1[i])):
            c = (0,0)
            for k in range(len(mat2)):
                c = suma(c,producto(mat1[i][k],mat2[k][j]))
            res[i].append(c)
    return res
def productoMatrices(mat1,mat2):
    res=[[] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2)):
            c = 0
            for k in range(len(mat2)):
                c += (mat1[i][k])*(mat2[k][j])
            res[i].append(c)
    return res
def productoMatrizVectorComplejos(mat1,vec):
    res=[]
    for i in range(len(mat1)):
        c = (0,0)
        for j in range(len(vec)):
            mul = producto(mat1[i][j],vec[j])
            c = suma(c,mul)
        res.append(c)
    return res
def productoMatrizVector(mat1,vec):
    res=[]
    for i in range(len(mat1)):
        c = 0
        for j in range(len(vec)):
            c += mat1[i][j] * vec[j]
        res.append(c)
    return res
def productoVectorVectorComplejos(vec1,vec2):
    res=[]
    for i in range(len(vec1)):
        c = (0,0)
        for j in range(len(vec1)):
            mul = producto(vec1[i],vec2[j])
            c = suma(c,mul)
        res.append(c)
    return res
def productoInterno(mat1,mat2):
    trans = transpuesta(mat1)
    res = productoMatrices(trans,mat2)
    return res
def productoInternoVectoresComplejos(mat1,mat2):
    r = productoMatrices(mat1,mat2)
    res = []
    for i in r:
        res.append((i[0],i[1]))
    return res
def normComplex(mat):
    res = 0
    for i in range(len(mat)):
        res += mat[i][0]**2
        res += mat[i][1]**2
    res = res **0.5
    return res
def normVector(mat):
    res = 0
    for i in range(len(mat)):
        res += mat[i]**2
    res = res **0.5
    return res
def normVectorComplejo(mat):
    res = 0
    for i in range(len(mat)):
        res += mat[i][0]**2
        res += mat[i][1]**2
    res = res **0.5
    return res
def distanciaVectores(mat1,mat2):
    a = restaVectores(mat1,mat2)
    res = normVector(a)
    return res
def matrizHermitiana(mat):
    trans = transpuesta(mat)
    res = conjugadoMatriz(trans)
    return res==mat
def matrizUnitaria(mat):
    trans = transpuesta(mat)
    res1 = conjugadoMatriz(trans)
    res = productoMatricesComplejas(mat,res1)
    return res
def productoTensor(mat1,mat2):
    for x in range(2,len(mat2)**2):
        if len(mat2) % x == 0:
            aux = x
            break
    res = [[] for _ in range(len(mat1)*len(mat2))]
    for i in range(len(mat1)):
        for l in range(len(mat1[i])):
            a = mat1[i][l]
            con = i * aux
            for j in range(len(mat2)):
                for k in range(len(mat2[j])):
                    res[con].append(producto(a,mat2[j][k]))
                con+=1
    return res
