import unittest

from app.routes import min

class TestMin(unittest.TestCase):
    def test_with_min(self):
        data = [1, 2, 3, 4, 5]
        result = min(data)
        self.assertEqual(result, 1)
        
        
    