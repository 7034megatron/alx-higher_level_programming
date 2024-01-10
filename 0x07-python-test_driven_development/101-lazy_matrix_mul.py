#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices using NumPy.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        np.ndarray: The result of the matrix multiplication.
    """
    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        raise ValueError("shapes {} and {} not aligned: {} (dim 1) != {} (dim 0)".format(
            np.shape(m_a), np.shape(m_b), np.shape(m_a)[1], np.shape(m_b)[0])) from e
    except Exception as e:
        raise type(e)("invalid type for matrix multiplication") from e
