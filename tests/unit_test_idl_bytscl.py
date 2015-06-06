#!/usr/bin/env python

import sys
import os
import unittest
import numpy

# Need to temporarily append to the PYTHONPATH in order to import the 
# newly built bytscl function
sys.path.append(os.getcwd())
from idl_functions import bytscl


class IDL_bytscl_Tester(unittest.TestCase):

    """
    A unit testing procedure for the IDL BYTSCL function.
    """

    def setUp(self):
        self.array1 = numpy.random.randn(100,100)
        self.array2 = numpy.random.randint(0,256,(100,100))

    def test_output_range(self):
        """
        Test that the output array is [0,255].
        """
        byt = bytscl(self.array1)
        outside = (byt < 0) | (byt > 255)
        total = numpy.sum(outside)
        self.assertEqual(total, 0)

    def test_out_dtype(self):
        """
        Test that the output array is of type uint8.
        """
        byt = bytscl(self.array1)
        dtype = byt.dtype
        self.assertEqual(dtype, 'uint8')

    def test_top_keyword(self):
        """
        Test that the top keyword works as expected.
        """
        # Set top to 200
        byt = bytscl(self.array1, top=200)
        mx = numpy.max(byt)
        self.assertEqual(mx, 200)

    def test_maxv_keyword(self):
        """
        Test that the maxv keyword works as expected.
        """
        # Set maxv to 200
        byt = bytscl(self.array2, maxv=200)
        control = numpy.sum(self.array2 >= 200)
        total = numpy.sum(byt == 255)
        self.assertEqual(total, control)

    def test_minv_keyword(self):
        """
        Test that the minv keyword works as expected.
        """
        # Set minv to 200
        byt = bytscl(self.array2, minv=200)
        control = numpy.sum(self.array2 <= 200)
        total = numpy.sum(byt == 0)
        self.assertEqual(total, control)

    def test_nan_keyword(self):
        """
        Test that the nan keyword works as expected.
        """
        # If array has any nan's then the output will return all zeros
        array = self.array1.copy()
        array[0,0] = numpy.nan
        byt = bytscl(array, nan=True)
        total = numpy.sum(byt)
        self.assertTrue(total != 0)

    def test_datatype_error(self):
        """
        Test that an array of an unsupported datatype raises an error.
        """
        arr = numpy.zeros((10,10), dtype='complex')
        self.assertRaises(ValueError, bytscl, arr)

if __name__ == '__main__':
    unittest.main()
