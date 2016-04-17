#!/usr/bin/env python

import numpy
from idl_functions import histogram
from idl_functions import bytscl


def linear_percent(cumulative_histogram, percent, minv, binsize):
    """
    Image contrast enhancement.

    Given a cumulative histogram, upper and lower DN values are
    computed and returned.

    :param cumulative_histogram:
        A 1D numpy array. Must the cumulative sum of a histogram.

    :param perecent:
        A value in the range of 0-100.

    :param minv:
        The minumum value to be used in the determining the stretch.

    :param binsize:
        The binsize used in constructing the histogram of which the
        cumulative histogram was then derived.

    :return:
        Two scalars, maxdn and mindn, corresponding to the maximum
        and minimum values of the original array to be used in the
        contrast stretch.

    :author:
        Josh Sixsmith; joshua.sixsmith@ga.gov.au; josh.sixsmith@gmail.com

    :history:
       *  2013/10/24: Created

    """
    ch = cumulative_histogram
    if len(ch.shape) != 1:
        raise ValueError('Only 1D arrays are supported.')

    # Calculate upper and lower values
    low = (percent / 100.)
    high = (1 - (percent / 100.))

    # number of elements
    n = ch[-1]

    x1 = numpy.searchsorted(ch, n * low)
    while ch[x1] == ch[x1 + 1]:
        x1 = x1 + 1

    x2 = numpy.searchsorted(ch, n * high)
    while ch[x2] == ch[x2 - 1]:
        x2 = x2 - 1

    mindn = x1 * binsize + minv
    maxdn = x2 * binsize + minv

    return maxdn, mindn


def hist_equal(array, binsize=None, maxv=None, minv=None, omax=None, omin=None,
               percent=None, top=None, histogram_only=False):
    """
    Image contrast enhancement.
    Replicates the hist_equal function available within IDL
    (Interactive Data Language, EXELISvis).
    Converts an array to a histogram equalised byte array.

    :param array:
        A numpy array of any type.

    :param binsize:
        The binsize to be used in constructing the histogram.
        The default is 1 for arrays with a datatype of byte (uint8).
        Arrays of other datatypes the binsize is computed as
        (maxv - minv) / 5000. (floating point).

    :param maxv:
        The maximum data value to be considered in the contrast stretch.
        The default is 255 for arrays with a datatype of byte (uint8).
        Otherwise the maximum data value of array is used.

    :param minv:
        The minimum data value to be considered in the contrast stretch.
        The default is 0 for arrays with a datatype of byte (uint8).
        Otherwise the minimum data value of array is used.

    :param omax:
        (Optional) A string name used to refer to the dictionary key
        that will contain the maximum value used in generating the
        histogram.

    :param omin:
        (Optional) A string name used to refer to the dictionary key
        that will contain the minimum value used in generating the
        histogram.

    :param percent:
        A scalar between the values 0 and 100 that will be used to
        stretch the array histogram.

    :param top:
        The maximum value of the scaled result. Default is 255.
        The mimimum value of the scaled result is always 0.

    :param histogram_only:
        Type Bool. Default is false. If set to True, then a numpy
        array of type int32 will be returned that contains the
        cumulative sum of the histogram.

    :return:
        Varies. If histogram_only is set to True, then the cumulative
        sum of the histogram will be returned. Additional optional
        returns omax and and omin. Otherwise a byte scaled version of
        array is returned. Additional optional returns omax and and omin.

    Example:

        >>> # 100x100 array of samples from N(3, 6.25)
        >>> a = 2.5 * numpy.random.randn(100,100) + 3
        >>> scl_a = hist_equal(a)
        >>> scl_pct_a = hist_equal(a, percent=2)

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
    if (array.dtype == 'uint8'):
        maxv = 255
        minv = 0

    if (maxv is None):
       maxv = numpy.amax(array)

    if (minv is None):
       minv = numpy.amin(array)

    if (top is None):
       top = 255

    if (binsize is None):
        if (array.dtype == 'uint8'):
            binsize = 1
        else:
            binsize = (maxv - minv) / 5000.

    # Retrieve the dimensions of the array
    dims = array.shape

    h = histogram(array, binsize=binsize, maxv=maxv, minv=minv,
                  omax='omax', omin='omin')

    # Need to check for omin and omax so they can be returned
    return_extra = False
    if ((omin is not None) | (omax is not None)):
        return_extra = True
        d = {}
        if (omin is not None):
            d[omin] = h['omin']
        if (omax is not None):
            d[omax] = h['omax']

    # Zeroing the first element of the histogram
    hist = h['histogram']
    hist[0] = 0

    cumu_hist = numpy.cumsum(hist, dtype='float')

    if (histogram_only):
        cumu_hist = cumu_hist.astype('int32')
        # Need to check for omin and omax so they can be returned
        if return_extra:
            return cumu_hist, d
        else:
            return cumu_hist

    # Evaluate a linear percent stretch
    if (percent is not None):
        if (percent <= 0) or (percent >= 100):
            raise ValueError('Percent must be between 0 and 100')

        maxdn, mindn = linear_percent(cumu_hist, percent=percent, minv=minv,
                                      binsize=binsize)
        scl = bytscl(array, maxv=maxdn, minv=mindn, top=top)
        if return_extra:
            return scl, d
        else:
            return scl

    scl_lookup = bytscl(cumu_hist, top=top)

    # apply the scl_lookup in order to retrieve the new scaled value
    if (type(array) == 'uint8'):
        # We know the binsize for byte data, i.e. 1
        # Clip the lower bounds
        arr = array.clip(min=minv)
        scl = (scl_lookup[arr.ravel() - minv]).reshape(dims)
    else:
        # We need to divide by the binsize in order to the bin position
        # Clip the lower bounds
        arr = array.clip(min=minv)
        arr = numpy.floor((arr - minv) / binsize).astype('int')
        scl = (scl_lookup[arr.ravel()]).reshape(dims)

    if return_extra:
        return scl, d
    else:
        return scl
