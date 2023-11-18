import unittest
from unittest.mock import patch
from PrePostFixForTest import *


class TestPrePostFix(unittest.TestCase):
    def test_eval(self):
        self.assertEqual(eval('PRE','+ * + 3 4 5 7'), 42)
    def test_eval2(self):
        self.assertEqual(eval('POST','8 3 - 8 4 4 + * +'), 69)
    def test_eval3(self):
        self.assertEqual(mostrar('PRE','+ * + 3 4 5 7'),'( 3 + 4 ) * 5 + 7')
    def test_eval4(self):
        self.assertEqual(mostrar('POST','8 3 - 8 4 4 + * +'),'8 - 3 + 8 * ( 4 + 4 )')
    def test_eval5(self):
        self.assertEqual(eval('PRE','* 3 2 + * 4 5'), 54)
    def test_eval6(self):
        self.assertEqual(mostrar('PRE','* 3 2 + * 4 5'), '3 * 2 + 4 * 5')

if __name__ == '__main__':
    unittest.main()