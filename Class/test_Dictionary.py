import unittest

class MyDictionary():
    def __init__(self):
        self.dict = {}
    def add(self, k, v):
        self.dict[k] = v
    def get(self, k):
        return self.dict.get(k)

class TestMyDictionary(unittest.TestCase):
    def setUp(self):
        self.myDictionary = MyDictionary()
    def test_add(self):
        self.myDictionary.add('00001', "Alice")
        self.assertEqual(self.myDictionary.get("00001"), "Alice")
    def test_getNonExistingKey(self):
        result = self.myDictionary.get("00002")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()