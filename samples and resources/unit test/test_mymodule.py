import unittest
from mymodule import square,double
class TestMyModule(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2),4)
        self.assertEqual(square(3),9)
        self.assertEqual(square(9),81)
        self.assertEqual(square(10),100)

    def test_double(self):
        self.assertEqual(double(0),0)

if __name__ == '__main__':
    unittest.main()