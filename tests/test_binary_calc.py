import unittest
from binary_calc import BinaryCalculator  # Ensure this matches your file name

class TestBinaryCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = BinaryCalculator()
    
    def test_binary_to_decimal(self):
        self.assertEqual(self.calc.binary_to_decimal("101"), 5)
        self.assertEqual(self.calc.binary_to_decimal("1101"), 13)
        self.assertEqual(self.calc.binary_to_decimal("0"), 0)
    
    def test_decimal_to_binary(self):
        self.assertEqual(self.calc.decimal_to_binary(5), "101")
        self.assertEqual(self.calc.decimal_to_binary(13), "1101")
        self.assertEqual(self.calc.decimal_to_binary(0), "0")
    
    def test_is_valid_binary(self):
        self.assertTrue(self.calc.is_valid_binary("101"))
        self.assertFalse(self.calc.is_valid_binary("102"))
        self.assertTrue(self.calc.is_valid_binary("110011"))
    
    def test_bitwise_operations(self):
        self.assertEqual(self.calc.bitwise_operations(5, 3, "&"), "0001")
        self.assertEqual(self.calc.bitwise_operations(5, 3, "|"), "0111")
        self.assertEqual(self.calc.bitwise_operations(5, 3, "^"), "0110")
        self.assertEqual(self.calc.bitwise_operations(5, 3, "%"), "0001")
        self.assertEqual(self.calc.bitwise_operations(2, 3, "**"), "1000")
    
    def test_unary_not_operation(self):
        self.assertEqual(self.calc.calculate("~101"), "010")
    
    def test_factorial(self):
        self.assertEqual(self.calc.calculate("101", "fact"), 120)
        with self.assertRaises(ValueError):
            self.calc.calculate("-101", "fact")
    
    def test_logarithm(self):
        self.assertEqual(self.calc.calculate("1000", "log"), 3.0)
        with self.assertRaises(ValueError):
            self.calc.calculate("0", "log")
    
    def test_trigonometric_functions(self):
        self.assertEqual(self.calc.calculate("110", "sin"), 0.105)
        self.assertEqual(self.calc.calculate("110", "cos"), 0.995)
        self.assertEqual(self.calc.calculate("110", "tan"), 0.106)
    
    def test_bitwise_shift_operations(self):
        self.assertEqual(self.calc.calculate("101", "<<", "2"), "10100")
        self.assertEqual(self.calc.calculate("101", ">>", "1"), "10")
    
    def test_invalid_operations(self):
        with self.assertRaises(ValueError):
            self.calc.calculate("101", "invalid")
        with self.assertRaises(ValueError):
            self.calc.calculate("101", "&", "XYZ")

if __name__ == "__main__":
    unittest.main()