from Complex import *
import math
def canicas(inicial,estado,clicks):
    for i in range(clicks):
        estado = productoMatrizVectorComplejos(inicial,estado)
    return estado

def rendijas(num,inicial,estado,clicks):
    for i in range(num):
        inicial = productoMatrices(inicial,inicial)
    for i in range(clicks):
        estado = productoMatrizVector(inicial,estado)
    return estado

def rendijasComplejos(num,inicial,estado,clicks):
    for i in range(num):
        inicial = productoMatricesComplejas(inicial,inicial)
    for i in range(clicks):
        estado = productoMatrizVectorComplejos(inicial,estado)
    return estado
def particula(points,pos):
    norm = normVectorComplejo(points)
    probablidad = math.pow(pos,2)/math.pow(norm,2)
    return probablidad
def paticulaDobleKet(ket1,ket2):
    aux = []
    for i in range(len(ket2)):
        aux.append((ket2[i][0],-ket2[i][1]))
    res = productoInternoVectoresComplejos(aux,ket1)
    return res
