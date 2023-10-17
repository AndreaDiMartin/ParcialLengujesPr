#Andrea Diaz 18-10826 
#Pregunta 4 Test
#Modulo para realizar tests unitarios para el modulo threeDimensionalVectors.py 
#Retorna OK para todos los tests.

import unittest
import math
from threeDimensionalVectors import *

a = vector(1,2,3)
b = vector(5,6,7)
c = vector(10,20,35) 

class TestThreeDimensionalVectors(unittest.TestCase):
    def test_sumaEntreVectores(self):
        self.assertEqual((a+b).v, vector(6, 8, 10).v)
    def test_sumaVectorConEscalar(self):
        self.assertEqual((c+5).v, vector(15,25,40).v)
    def test_restaEntreVectores(self):
        self.assertEqual((a - b).v, vector(-4,-4,-4).v)
    def test_restaVectorConEscalar(self):
        self.assertEqual((vector(-7,0,5) - 5).v, vector(-12,-5,0).v)
    def test_productoPunto(self):
        self.assertEqual(vector(1,2,3) % vector(5,6,7), 38)
    def test_productoCruz(self):
        self.assertEqual((vector(1,2,3) * vector(5,6,7)).v, vector(-4,8,-4).v)
    def test_norma(self):
        self.assertEqual(~vector(3,4,5), math.sqrt(50))
    def test_productoEscalar(self):
        self.assertEqual((vector(1,2,3) * 5).v, vector(5,10,15).v)
    def test_extraTest1(self):
        self.assertEqual((vector(1,2,3) * vector(2, 3, 9) + vector(-1,-2,-3)).v, vector(8,-5,-4).v)
    def test_extraTest2(self):
        self.assertEqual(((vector(1,2,3) + vector(1,2,3))*(vector(2, 3, 9)- vector(-1,-5,-10))).v, vector(28, -20, 4).v)
    def test_extraTest3(self):
        self.assertEqual(vector(100,250, 369) % (vector(27,96,-50)*vector(154,55,1)), -6554481)
    def test_extraTest4(self):
        self.assertEqual((vector(1,2,3)*10.6 + ~vector(5,6,7)).v, vector(10.6 + math.sqrt(110),21.2+math.sqrt(110),31.8+math.sqrt(110)).v)
    def test_extraTest5(self):
        self.assertEqual(((vector(1,2,3) + vector(1,2,3))*(vector(2, 3, 9) % vector(-1,-5,-10))).v, vector(-214,-428,-642).v)

if __name__ == '__main__':
    unittest.main()