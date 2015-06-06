#!/usr/bin/env python

import numpy


def bytscl(array, maxv=None, minv=None, top=255, nan=False):
    """
    Replicates the bytscl function available within IDL
    (Interactive Data Language, EXELISvis).
    Scales all values of array in the range
    (minv <= value <= maxv) to (0 <= scl_value <= top).

    :param array:
        A numpy array of any type.

    :param maxv:
        The maximum data value to be considered.
        Otherwise the maximum data value of array is used.

    :param minv:
        The minimum data value to be considered.
        Otherwise the minimum data value of array is used.

    :param top:
        The maximum value of the scaled result. Default is 255.
        The mimimum value of the scaled result is always 0.

    :param nan:
        type Bool. If set to True, then NaN values will be ignored.

    :return:
        A numpy array of type byte (uint8) with the same dimensions
        as the input array.

    Example:

        >>> a = numpy.random.randn(100,100)
        >>> scl_a = bytscl(a)

    :author:
        Josh Sixsmith; josh.sixsmith@gmail.com; joshua.sixsmith@ga.gov.au

    :history:
       *  2013/10/24: Created

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

    if (maxv == None):
        if (nan):
            maxv = numpy.nanmax(array)
        else:
            maxv = numpy.amax(array)

    if (minv == None):
        if (nan):
            minv = numpy.nanmin(array)
        else:
            minv = numpy.amin(array)

    if (top > 255):
        top = 255

    scl = array.copy()
    scl[scl >= maxv] = top
    scl[scl <= minv] = 0

    int_types = ['int', 'int8', 'int16', 'int32', 'int64', 'uint8', 'uint16',
                 'uint32', 'uint64']
    flt_types = ['float', 'float16', 'float32', 'float64']

    if (array.dtype in int_types):
        rscl = numpy.floor(((top + 1.) * (scl - minv) - 1.) / (maxv - minv))
    elif (array.dtype in flt_types):
        rscl = numpy.floor((top + 0.9999) * (scl - minv) / (maxv - minv))
    else:
        msg = ("Error! Unknown datatype. "
               "Supported datatypes are: "
               "int8, uint8, int16, uint16, int32, uint32, int64, uint64, "
               "float32, float64.")
        raise ValueError(msg)

    # Check and account for any overflow that might occur during
    # datatype conversion
    rscl[rscl >= top] = Top
    rscl[rscl < 0] = 0
    scl = rscl.astype('uint8')

    return scl
