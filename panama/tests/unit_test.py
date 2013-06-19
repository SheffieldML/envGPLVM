# Copyright (c) 2012, GPy authors (see AUTHORS.txt).
# Licensed under the BSD 3-clause license (see LICENSE.txt)

import unittest
import numpy as np

class FullTest(unittest.TestCase):
    def model_test(self):
        import panama
        Y = np.random.randn(100, 200)
        S = np.random.randn(100, 400)
        conf = panama.core.ConfounderGPLVM(Y, S, population_structure=None, num_factors=5)
