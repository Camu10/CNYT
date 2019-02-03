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
        resultado = Complex.productoMatrices(mat1,mat2)
        self.assertEqual(resultado,[[(26, -52), (60, 24), (26, 0)], [(9, 7), (1, 29), (14, 0)], [(48, -21), (15, 22), (20, -22)]])

if __name__ == '__main__':
    unittest.main()
