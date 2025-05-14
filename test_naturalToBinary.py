import unittest
from naturalToBinary import natural_to_binary

class TestNaturalToBinary(unittest.TestCase):

    # Poprawność konwersji liczb
    def test_binary_of_1(self):
        self.assertEqual(natural_to_binary(1), '1')

    def test_binary_of_10(self):
        self.assertEqual(natural_to_binary(10), '1010')

    def test_binary_of_100(self):
        self.assertEqual(natural_to_binary(100), '1100100')

    # Zakres
    def test_value_below_range(self):
        with self.assertRaises(ValueError):
            natural_to_binary(0)

    def test_value_above_range(self):
        with self.assertRaises(ValueError):
            natural_to_binary(101)

    # Sprawdzenie, czy liczba jest naturalna (brak części dziesiętnej)
    def test_float_input(self):
        with self.assertRaises(TypeError):
            natural_to_binary(10.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            natural_to_binary("10")

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            natural_to_binary(-5)

if __name__ == '__main__':
    unittest.main()