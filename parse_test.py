import unittest
import parse

class Test_TestRippleRegion(unittest.TestCase):
    def test_add(self):
        x = parse.add(2,3)
        self.assertEqual(x,5,"adding")

    
