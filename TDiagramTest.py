import unittest
from TDiagramForTest import *

class TestTDiagram(unittest.TestCase):
    def test_ejecutable1(self):
        self.assertEqual(ejecutar('holamundo'), True)
    def test_ejecutable2(self):
        self.assertEqual(ejecutar('Buddy'), True)
    def test_ejecutable3(self):
        self.assertEqual(ejecutar('Main'), True)
    def test_ejecutable4(self):
        self.assertEqual(ejecutar('Fin'), False)
    def test_ejecutable5(self):
        self.assertEqual(ejecutar('C'), False)


if __name__ == '__main__':
    unittest.main()
