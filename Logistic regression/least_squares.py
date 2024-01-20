# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares solution."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # least squares: TODO
    term1 = tx.T.dot(tx)
    term2 = tx.T.dot(y)
    optimal_weights = np.linalg.inv(term1).dot(term2)
    mse = compute_mse(y, tx, optimal_weights)
    return optimal_weights 

    
def calculate_mse(e):
    return 1/2*np.mean(e**2)

def compute_mse(y, tx, w):
    """Calculate the loss.

    You can calculate the loss using mse or mae.
    """
    e = y - tx.dot(w)
    return calculate_mse(e)
   