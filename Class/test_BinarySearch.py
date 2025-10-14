import unittest
from binarySearch import BinarySearch

class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        numbers = [2, 5, 10, 20, 100]
        target = 5
        result = BinarySearch(numbers, target)
        self.assertTrue(result)
    
    def test_NotFound(self):
        numbers = list(range(1, 2000, 5))
        target = 7
        result = BinarySearch(numbers, target)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()