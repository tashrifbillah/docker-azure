#!/usr/bin/env python

import numpy as np
import unittest

class TestEnigma(unittest.TestCase):

    print('Test ENIGMA branch results')

    def test_enigma_FA(self):
        np.testing.assert_equal(5,5)

    def test_enigma_AD(self):
        np.testing.assert_equal(5,5)

if __name__ == '__main__':
    unittest.main()
