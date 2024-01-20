# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    arr = np.ones((len(x), 1))
    for darage in range(1, degree+1):
        arr = np.c_[arr, np.power(x, darage)]
    return arr
