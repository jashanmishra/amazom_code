import unittest
from program import divide

class TestMathFunctions(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(10, 0), "Cannot divide by zero!")

if __name__ == "__main__":
    unittest.main()