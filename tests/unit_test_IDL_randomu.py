#!/usr/bin/env python
import sys
import unittest
import numpy

# Need to temporarily append to the PYTHONPATH in order to import the 
# newly built randomu function
sys.path.append(os.getcwd())
from IDL_functions import randomu

class IDL_randomu_Tester(unittest.TestCase):
    """
    A unit testing procedure for the IDL Randomu function.
    """

    def test_scalar(self):
        """
        Test that a single scalar gets returned.
        """
        seed = None

        x, seed = randomu(seed)

        self.AsserTrue(numpy.isscalar(x))

    def test_dimension_columns(self):
        """
        Test that the output column dimensions are the same.
        """

        arr = numpy.arange(120).reshape((10,12))

        in_rows,in_cols = arr.shape

        in_dims = (in_cols,in_rows)

        seed = None

        x, seed = randomu(sd, in_dims)

        out_rows,out_cols = x.shape

        self.assertEqual(in_cols, out_cols)

    def test_dimension_rows(self):
        """
        Test that the output row dimensions are the same.
        """

        arr = numpy.arange(120).reshape((10,12))

        in_rows,in_cols = arr.shape

        in_dims = (in_cols,in_rows)

        seed = None

        x, seed = randomu(sd, in_dims)

        out_rows,out_cols = x.shape

        self.assertEqual(in_rows, out_rows)

    def test_dimensions_nonlist(self):
        """
        Test that inputing a non-list type dimensions keyword raises
        a type error.
        """

        seed = None

        dims = (10,20)

        self.assertRaises(TypeError, randomu, seed, dims)

    def test_too_many_dimensions(self):
        """
        Test that a list describing > 8 dimensions raises a value error.
        """

        seed = None

        dims = [1,2,3,4,5,6,7,8,9]

        self.assertRaises(ValueError, randomu, seed, dims)

    def test_binomial_input(self):
        """
        Test that the a list != 2 for Binomial distribution raises a
        value error.
        """

        seed = None
        kwds = {'seed': seed, 'Binomial': [0,1,2]}

        self.assertRaises(ValueError, randomu, **kwds)

