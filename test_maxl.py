import unittest
from main import maxl

class MyTestCase(unittest.TestCase):
    def test_max(self):
        self.assertEqual(maxl([2,6,9,3],0,2),9)
