#test/my_mod_test.py

import unittest

from my_ray_lambda_ds12.my_mod import enlarge

class TestStringMethods(unittest.TestCase):

    def test_enlarge(unittest.TestCase):
        self.assertEqual(enlarge(5, 500))

if __name__ == '__main__':
    unittest.main()
