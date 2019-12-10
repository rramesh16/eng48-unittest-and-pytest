import unittest
from simple_calc import SimpleCalc

class CalcTest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)
        self.assertEqual(self.calc.add(6, 2), 8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        self.assertEqual(self.calc.subtract(6, 2), 4)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(6, 2), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertEqual(self.calc.divide(6, 2), 3)

