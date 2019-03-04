from Complex import *
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
