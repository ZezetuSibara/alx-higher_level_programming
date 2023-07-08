#!/usr/bin/python3
"""
   The 101-lazy_matrix_mul Module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
        The multiplies 2 matrices

        Args:
            m_a: the first matrix in 2D List)
            m_b: the second matrix in 2D List)

        Returns:
            the product of the matrices
    """
    return np.matmul(m_a, m_b)
