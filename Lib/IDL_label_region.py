#! /usr/bin/env python
import numpy
from scipy import ndimage

def label_region(data, all_neighbors=False, ULong=False):
    """
    Replicates the label_region function avaiable within IDL
    (Interactive Data Language, EXELISvis).
    Consecutively labels all regions/segments with a unique region
    index.

    :param data:
        A 2D NumPy array, ideally a bi-level array.

    :param all_neighbors:
        If set to True then all 8 neighbors of a pixel are used to
        determine connectivity. Default is False, only the 4 immediate
        neighbors of a pixel are used to determnine connectiviy.

    :param ULong:
        If set to True then the output array will be an 32 bit unsinged
        long integer. Default is False, and the output will be a 16 bit
        unsinged integer. Use this keyword if you expect > 65525 regions.

    :return:
        A 2D NumPy array either 16 or 32 bit unsigned integer, with
        each pixel containing its region/segment index. Zeros values
        are considered to be background.

    :notes:
        Only non-zero values are considered in the labelling process.
        Zero values are considered background data in the input data
        array, and ignored.

    :history:
        *  16/08/2014: Created

    :copyright:
        Copyright (c) 2014, Josh Sixsmith
        All rights reserved.

        Redistribution and use in source and binary forms, with or without
        modification, are permitted provided that the following conditions are met:

        1. Redistributions of source code must retain the above copyright notice, this
           list of conditions and the following disclaimer. 
        2. Redistributions in binary form must reproduce the above copyright notice,
           this list of conditions and the following disclaimer in the documentation
           and/or other materials provided with the distribution. 

        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
        ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
        WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
        DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
        ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
        (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
        LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
        ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
        (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
        SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

        The views and conclusions contained in the software and documentation are those
        of the authors and should not be interpreted as representing official policies, 
        either expressed or implied, of the FreeBSD Project.
    """

    if data.ndim != 2:
        raise Exception('Error. Array must be 2 dimensional.')

    if all_neighbors:
        kernel = numpy.array([[1,1,1],[1,1,1],[1,1,1]]).reshape(3,3)
    else:
        kernel = numpy.array([[0,1,0],[1,1,1],[0,1,0]]).reshape(3,3)

    if ULong:
        result = numpy.zeros(data.shape, dtype='UInt32')
    else:
        result = numpy.zeros(data.shape, dtype='UInt16')

    # We don't return the number of features
    nfeatures = ndimage.label(data, structure=kernel, output=result)

    return result

