#Se probara con la posicion del que se va a liberar y la que se va a reservar, el rearrange con los espacios unificados

import unittest
from unittest.mock import patch
from BuddyForTest import *

class TestBuddy(unittest.TestCase):
    def test_reservar(self):
        self.assertEqual(reservar('A',32), 0)
    def test_reservar2(self):
        self.assertEqual(reservar('B',64), 0)
    def test_reservar3(self):
        self.assertEqual(reservar('B',10000), -1)
    def test_rearrange(self):
        self.assertEqual(rearrange(), 3)
    def test_liberar(self):
        self.assertEqual(liberar('A'), 0)
    def test_liberar2(self):
        self.assertEqual(liberar('B'), 0)
    def test_liberar3(self):
        self.assertEqual(liberar('F'), 1)


if __name__ == '__main__':
    unittest.main()

