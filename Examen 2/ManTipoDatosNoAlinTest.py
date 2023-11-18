import unittest
from unittest.mock import patch
from ManTipoDatosNoAlinForTest import *

class TestManTipoDatos(unittest.TestCase):
    def test_uni(self):
        self.assertEqual(describir('uni'), (4,0))
    def test_int(self):
        self.assertEqual(describir('int'), (4,0))
    def test_struct(self):
        self.assertEqual(describir('meta2'), (5,0))
    def test_struct2(self):
        self.assertEqual(describir('meta'), (18,0))
    def test_inexistente(self):
        self.assertEqual(describir('inexistente'), (0,0))

if __name__ == '__main__':
    unittest.main()