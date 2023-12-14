#Andrea Diaz 18-10826
#Pregunta 6
#Las pruebas se ejecutan correctamente en las partes del programa que no tienen que ver con la funcion ASK

import unittest
import medioPrologForTest as mp

class TestMedioProlog(unittest.TestCase):
    def test_crearPredicado1(self):
        self.assertEqual(mp.crearPredicado("padre(miguel, gaby)"), True)
    def test_crearPredicado2(self):
        self.assertEqual(mp.crearPredicado("Padre(miguel, gaby, juan)"), False)
    def test_crearPredicado3(self):
        self.assertEqual(mp.crearPredicado("ancestro(X, Y) padre(X, Y)"), True)
    def test_crearPredicado4(self):
        self.assertEqual(mp.crearPredicado("ancestro(X, Y, Z) Padre(X, Y)"), False)
    def test_crearPredicado5(self):
        self.assertEqual(mp.crearPredicado("ancestro(X, Y) Padre(X, Y)"), False)
    def test_bucarHecho1(self):
        self.assertEqual(mp.buscarHecho(["padre","juan","jose"]), True)
    def test_bucarHecho2(self):
        self.assertEqual(mp.buscarHecho(["padre","juan","pedro"]), False)
    def test_bucarHecho4(self):
        self.assertEqual(mp.buscarHecho(["padre","juan","X"]), [["X","jose"]])

if __name__ == '__main__':
    unittest.main()