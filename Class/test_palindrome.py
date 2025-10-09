import unittest

def isPalindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertFalse(isPalindrome("Hello"))
        self.assertTrue(isPalindrome("Racecar"))
        self.assertTrue(isPalindrome(""))
        self.assertTrue(isPalindrome("Able was I ere I saw Elba"))


if __name__ == "__main__":
    unittest.main()