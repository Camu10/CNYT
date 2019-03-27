import unittest
import Complex

class Pruebas(unittest.TestCase):

    def test_suma(self):
        c1 = (3,-1)
        c2 = (1,4)
        resultado = Complex.suma(c1,c2)
        self.assertEqual(resultado,(4,3))
        
    def test_producto(self):
        c1 = (3,-1)
        c2 = (1,4)
        resultado = Complex.producto(c1,c2)
        self.assertEqual(resultado,(7,11))
        
    def test_suma_vector(self):
        mat1 = [(6,-4),(7,3),(4.2,-8.1),(0,-3)]
        mat2 = [(16,2.3),(0,-7),(6,0),(0,-4)]
        resultado = Complex.sumaVectores(mat1,mat2)
        self.assertEqual(resultado,[(22, -1.7000000000000002), (7, -4), (10.2, -8.1), (0, -7)])
    
    def test_inverso_vector(self):
        mat = [(6,-4),(7,3),(4.2,-8.1),(0,-3)]
        resultado = Complex.inversoVector(mat)
        self.assertEqual(resultado,[(-6, 4), (-7, -3), (-4.2, 8.1), (0, 3)])

    def test_producto_scalar(self):
        mat1 = [(6,3),(0,0),(5,1),(4,0)]
        scalar = (3,2)
        resultado = Complex.productoScalarMatriz(scalar,mat1)
        self.assertEqual(resultado,[(12, 21), (0, 0), (13, 13), (12, 8)])

    def test_conjugado_transpuesta(self):
        mat = [[(6,-3),(2,12),(0,-19)],[(0,0),(5,2.1),(17,0)],[(1,0),(2,5),(3,-4.5)]]
        resultado = Complex.conjugadoMatriz(Complex.transpuesta(mat))
        self.assertEqual(resultado,[[(6, 3), (0, 0), (1, 0)], [(2, -12), (5, -2.1), (2, -5)], [(0, 19), (17, 0), (3, 4.5)]])

    def test_producto_matrices(self):
        mat1=[[(3,2),(0,0),(5,-6)],[(1,0),(4,2),(0,1)],[(4,-1),(0,0),(4,0)]]
        mat2=[[(5,0),(2,-1),(6,-4)],[(0,0),(4,5),(2,0)],[(7,-4),(2,7),(0,0)]]
        resultado = Complex.productoMatricesComplejas(mat1,mat2)
        self.assertEqual(resultado,[[(26, -52), (60, 24), (26, 0)], [(9, 7), (1, 29), (14, 0)], [(48, -21), (15, 22), (20, -22)]])

    def test_producto_interno(self):
        mat1 = [[1,2],[0,1]]
        mat2 = [[0,-1],[-1,0]]
        mat3 = [[2,1],[1,3]]
        resultado = Complex.productoInterno(Complex.sumaMatrices(mat1,mat2),mat3)
        self.assertEqual(resultado,[[1,-2],[3,4]])

    def test_norm(self):
        mat = [(4,3),(6,-4),(12,-7),(0,13)]
        resultado = Complex.normComplex(mat)
        self.assertEqual(resultado,20.952326839756964)

    def test_norm_vector(self):
        mat1 = [3,1,2]
        mat2 = [2,2,-1]
        resultado = Complex.distanciaVectores(mat1,mat2)
        self.assertEqual(resultado,3.3166247903554)

    def test_hermitiana_matriz(self):
        mat = [[(5,0),(4,5),(6,-16)],[(4,-5),(13,0),(7,0)],[(6,16),(7,0),(-2.1,0)]]
        resultado = Complex.matrizHermitiana(mat)
        self.assertTrue(resultado)

    def test_unitaria_matriz(self):
        mat = [[(1,1),(1,-1)],[(1,-1),(1,1)]]
        resultado = Complex.matrizUnitaria(mat)
        self.assertEqual(resultado,[[(4,0),(0,0)],[(0,0),(4,0)]])

    def test_producto_tensorial(self):
        mat1 = [[(3,2),(5,-1),(0,2)],[(0,0),(12,0),(6,-3)],[(2,0),(4,4),(9,3)]]
        mat2 = [[(1,0),(3,4),(5,-7)],[(10,2),(6,0),(2,5)],[(0,0),(1,0),(2,9)]]
        resultado = Complex.productoTensor(mat1,mat2)
        self.assertEqual(resultado,[[(3, 2), (1, 18), (29, -11), (5, -1), (19, 17), (18, -40), (0, 2), (-8, 6), (14, 10)], [(26, 26), (18, 12), (-4, 19), (52, 0), (30, -6), (15, 23), (-4, 20), (0, 12), (-10, 4)], [(0, 0), (3, 2), (-12, 31), (0, 0), (5, -1), (19, 43), (0, 0), (0, 2), (-18, 4)], [(0, 0), (0, 0), (0, 0), (12, 0), (36, 48), (60, -84), (6, -3), (30, 15), (9, -57)], [(0, 0), (0, 0), (0, 0), (120, 24), (72, 0), (24, 60), (66, -18), (36, -18), (27, 24)], [(0, 0), (0, 0), (0, 0), (0, 0), (12, 0), (24, 108), (0, 0), (6, -3), (39, 48)], [(2, 0), (6, 8), (10, -14), (4, 4), (-4, 28), (48, -8), (9, 3), (15, 45), (66, -48)], [(20, 4), (12, 0), (4, 10), (32, 48), (24, 24), (-12, 28), (84, 48), (54, 18), (3, 51)], [(0, 0), (2, 0), (4, 18), (0, 0), (4, 4), (-28, 44), (0, 0), (9, 3), (-9, 87)]])

    def test_canicas(self):
        mat = [[(0,0),(0,0),(0,0),(0,0),(0,0),(1,0)],[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(1,9),(0,0),(0,0),(0,0),(1,45)],[(0,0),(0,0),(0,0),(1,5),(0,0),(0,0)],[(0,0),(0,0),(1,1),(0,0),(0,0),(0,0)],[(1,10),(0,0),(0,0),(0,0),(1,8),(0,0)]]
        estado = [(6,2),(2,3),(1,1),(5,1),(3,4),(10,1)]
        resultado = Complex.canicas(mat,estado,1)
        self.assertEqual(resultado,[(10, 1), (0, 0), (-60, 472), (0, 26), (0, 2), (-43, 90)])

    def test_rendijas(self):
        mat = [[0,0,0,0,0,0,0,0],[0.5,0,0,0,0,0,0,0],[0.5,0,0,0,0,0,0,0],[0,0.33,0,1,0,0,0,0],[0,0.33,0,0,1,0,0,0],[0,0.33,0.33,0,0,1,0,0],[0,0,0.33,0,0,0,1,0],[0,0,0.33,0,0,0,0,1]]
        estado = [1,0,0,0,0,0,0,0]
        resultado = Complex.rendijas(2,mat,estado,1)
        self.assertEqual(resultado,[0.0, 0.0, 0.0, 0.165, 0.165, 0.33, 0.165, 0.165])

    def test_rendijas_complejas(self):
        mat = [[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0.5,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0.5,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(0.33,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(0.33,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],[(0,0),(0.33,0),(0.33,0),(0,0),(0,0),(1,0),(0,0),(0,0)],[(0,0),(0,0),(0.33,0),(0,0),(0,0),(0,0),(1,0),(0,0)],[(0,0),(0,0),(0.33,0),(0,0),(0,0),(0,0),(0,0),(1,0)]]
        estado = [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        resultado = Complex.rendijasComplejos(2,mat,estado)
        self.assertEqual(resultado,[(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.165, 0.0), (0.165, 0.0), (0.33, 0.0), (0.165, 0.0), (0.165, 0.0)])

    def test_particula(self):
        points = [(-3,-1),(0,-2),(0,1),(2,0)]
        resultado = Complex.particula(points,1)
        self.assertEqual(resultado,0.05263157894736841)

    def test_particula_ket_doble(self):
        vec1 = [(1,0),(0,1)]
        vec2 = [(0,1),(-1,0)]
        resultado = Complex.paticulaDobleKet(vec1,vec2)
        self.assertEqual(resultado,[(0,-1),(-1,0)])
    def test_observable_ket_media(self):
        mat = [[(1,0),(0,-1)],[(0,1),(2,0)]]
        vec = [(0.7071067811865476,0),(0,0.7071067811865476)]
        resultado = Complex.observableKet(mat,vec)
        self.assertEqual(resultado,(2.5000000000000004, 0.0))
    def test_observable_ket_varianza(self):
        mat = [[(1,0),(0,-1)],[(0,1),(2,0)]]
        vec = [(0.7071067811865476,0),(0,0.7071067811865476)]
        resultado = Complex.observableKetVarianza(mat,vec)
        self.assertEqual(resultado,0.25)
if __name__ == '__main__':
    unittest.main()
