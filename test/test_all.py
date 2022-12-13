import unittest
from calculator.Calculcator import Calculator


class TestCalculator(unittest.TestCase):

    def test_substract(self):
        """
        Test substract on int 4-2=2
        :return:
        """
        self.assertEqual(Calculator().substract(4, 2), 2)

    def test_add(self):
        """
        Tests add on int 4+2=6
        :return:
        """
        self.assertEqual(Calculator().add(4, 2), 6)


if __name__ == '__main__':
    unittest.main()
