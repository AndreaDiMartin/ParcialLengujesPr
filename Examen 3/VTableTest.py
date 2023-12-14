#Andrea Diaz 18-10826
#Pregunta 4
#Todas las pruebas aqui presentada se realizaron sin fallos

import unittest
from VtableForTest import *

class TestVtable(unittest.TestCase):
    def test_crearClase1(self):
        self.assertEqual(crearClase("D","C",["f","h"]), True)
    def test_crearClase2(self):
        self.assertEqual(crearClase("D","C",["f","h"]), False)
    def test_crearClase3(self):
        self.assertEqual(crearClase("E","E",["f","h"]), False)
    def test_crearClase4(self):
        self.assertEqual(crearClase("F","superclase",["f","f"]), False)
    def test_crearClase5(self):
        self.assertEqual(crearClase("C","S",["f","h"]), False)
    def test_describir1(self):
        self.assertEqual(describir("A"), [("A","f"),("A","g")])
    def test_describir2(self):
        self.assertEqual(describir("B"), [("B","f"),("B","h"),("A","g")])
    def test_describir3(self):
        self.assertEqual(describir("C"), [("C","f"),("C","h"),("C","g")])

if __name__ == '__main__':
    unittest.main()
