import unittest
from slugify import slugify

class TestSlugify(unittest.TestCase):
    def test_helloWold(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_punctuation(self):
        self.assertEqual(slugify("Ball State University!"), "ball-state-university")

    def test_multipleSpaces(self):
        self.assertEqual(slugify("     This   is   a    test"), "this-is-a-test")

    def test_empty(self):
        self.assertEqual(slugify(""), "")

    def test_specialCharacters(self):
        self.assertEqual(slugify("@#%^"), "")


if __name__ == "__main__":
    unittest.main()