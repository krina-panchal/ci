import unittest
from test_func import is_string

# Create a test class
class TestFunction(unittest.TestCase):

    def test_string(self):
        self.assertTrue(is_string("Hello, World!"))
    
    def test_integer(self):
        self.assertFalse(is_string(42))
    
    def test_list(self):
        self.assertFalse(is_string([1, 2, 3]))
    
    def test_float(self):
        self.assertFalse(is_string(3.14))

if __name__ == '__main__':
    unittest.main()
