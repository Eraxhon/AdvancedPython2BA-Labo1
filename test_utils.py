# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(0),1)
        with self.assertRaises(ValueError):
            return -fact(-n)
        pass
    
    def test_roots(self):
 #       self.assertEqual(utils.fact(1,-2,1),-1)
        self.assertEqual(type(utils.roots(1,2,3)),type(1,2,3))
        pass
    
    def test_integrate(self):
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
