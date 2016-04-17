#!/usr/bin/env python

from __future__ import print_function
import numpy
import datetime
import _idl_histogram


def histogram(data, binsize=None, maxv=None, minv=None, nbins=None, omax=None,
              omin=None, reverse_indices=None, locations=None, input_arr=None,
              nan=False):
    """
    Replicates the histogram function avaiable within IDL
    (Interactive Data Language, EXELISvis).

    :param data:
        A 1-Dimensional array to calculate the histogram for.

    :param binsize:
        (Optional) The binsize (Default is 1) to be used for creating the
        histogram.

    :param maxv:
        (Optional) The maximum value to be used in creating the histogram.
        If not specified the array will be searched for max.

    :param minv:
        (Optional) The minimum value to be used in creating the histogram.
        If not specified the array will be searched for min.

    :param nbins:
        (Optional) The number of bins to be used for creating the histogram.
        If set binsize is calculated as ((max - min) / (nbins - 1)), and the
        max value will be adjusted to (nbins*binsize + min).

    :param omax:
        (Optional) A string name used to refer to the dictionary key
        that will contain the maximum value used in generating the histogram.

    :param omin:
        (Optional) A string name used to refer to the dictionary key
        that will contain the minimum value used in generating the histogram.

    :param reverse_indices:
        (Optional) A string name used to refer to the
        dictionary key that will contain the reverse indices of the histogram.

    :param locations:
        (Optional) A string name used to refer to the dictionary
        key that will contain the starting locations of each bin.

    :param input_arr:
        (Optional) Used to specify an input array that will be added to the
        result of the histogram. Useful for tiling mechanisms that only handle
        portions of an array at a time. The input array must be 1-Dimensional
        and contain at least as many elements as are required to construct
        the histogram.

    :param nan:
        If set to True (Default is False) then nan values will be
        accounted for and treated as missing data.

    :return:
        A dictionary containing the histogram and other optional components.
        The dictionary key name for the histogram is 'histogram'.

    Example:

        >>> h = histogram(data, minv=0, omin='omin', omax='omax', reverse_indices='ri')
        >>> hist = h['histogram']
        >>> ri = h['ri']
        >>> loc = loc['ri']
        >>> data_at_ith_bin_indices = data[ri[ri[i]:ri[i+1]]]

    :author:
        Josh Sixsmith; josh.sixsmith@gmail.com; joshua.sixsmith@ga.gov.au

    :history:
       * 04/02/2013: Created
       *  05/04/2013: Added nan keyword
       *  05/06/2013: Now checks for max value of 256 and datatype of 'uint8'
       *  12/06/2013: Added input_arr keyword

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
    def hist_int(data, n, minv, maxv, binsize, nbins, max_bin, ri):
        # increase the size by one. When specifying a min and max, it shouldn't
        # be included in the histogram. Stuff not to be included gets dumped
        # into the 1st position then removed prior to returning to the user.

        nbins_ = nbins + 1
        hist = numpy.zeros(nbins_, dtype='uint32')

        _idl_histogram.idl_histogram.histogram_int(data, hist, n, nbins_, minv,
                                                   maxv, max_bin, binsize)

        if ri:
            return hist
        else:
            return hist[1:]

    def hist_long(data, n, minv, maxv, binsize, nbins, max_bin, ri):
        # increase the size by one. When specifying a min and max, it shouldn't
        # be included in the histogram. Stuff not to be included gets dumped
        # into the 1st position then removed prior to returning to the user.

        nbins_ = nbins + 1
        hist = numpy.zeros(nbins_, dtype='uint32')

        _idl_histogram.idl_histogram.histogram_long(data, hist, n, nbins_,
                                                    minv, maxv, max_bin,
                                                    binsize)

        if ri:
            return hist
        else:
            return hist[1:]

    def hist_dlong(data, n, minv, maxv, binsize, nbins, max_bin, ri):
        # increase the size by one. When specifying a min and max, it shouldn't
        # be included in the histogram. Stuff not to be included gets dumped
        # into the 1st position then removed prior to returning to the user.

        nbins_ = nbins + 1
        hist = numpy.zeros(nbins_, dtype='uint32')

        _idl_histogram.idl_histogram.histogram_dlong(data, hist, n, nbins_,
                                                     minv, maxv, max_bin,
                                                     binsize)

        if ri:
            return hist
        else:
            return hist[1:]

    def hist_float(data, n, minv, maxv, binsize, nbins, max_bin, ri):
        # increase the size by one. When specifying a min and max, it shouldn't
        # be included in the histogram. Stuff not to be included gets dumped
        # into the 1st position then removed prior to returning to the user.

        nbins_ = nbins + 1
        hist = numpy.zeros(nbins_, dtype='uint32')

        _idl_histogram.idl_histogram.histogram_float(data, hist, n, nbins_,
                                                     minv, maxv, max_bin,
                                                     binsize)

        if ri:
            return hist
        else:
            return hist[1:]

    def hist_dfloat(data, n, minv, maxv, binsize, nbins, max_bin, ri):
        # increase the size by one. When specifying a min and max, it shouldn't
        # be included in the histogram. Stuff not to be included gets dumped
        # into the 1st position then removed prior to returning to the user.

        nbins_ = nbins + 1
        hist = numpy.zeros(nbins_, dtype='uint32')

        _idl_histogram.idl_histogram.histogram_dfloat(data, hist, n, nbins_,
                                                      minv, maxv, max_bin,
                                                      binsize)

        if ri:
            return hist
        else:
            return hist[1:]

    def ri_int(data, hist, nbins, n, ri_sz, minv, maxv, max_bin, binsize):
        # increase the size by one. When specifying a min and max, it shouldn't
        # be included in the reverse indices. Stuff not to be included gets
        # dumped into the 1st position then removed prior to returning to the
        # user.

        nbins_ = nbins + 1
        ri = numpy.zeros(ri_sz, dtype='uint32')

        _idl_histogram.idl_histogram.reverse_indices_int(data, hist, ri,
                                                         nbins_, n, ri_sz,
                                                         minv, maxv, max_bin,
                                                         binsize)

        return (hist[1:], ri[1:])

    def ri_long(data, hist, nbins, n, ri_sz, minv, maxv, max_bin, binsize):
        # increase the size by one. When specifying a min and max, it shouldn't
        # be included in the reverse indices. Stuff not to be included gets
        # dumped into the 1st position then removed prior to returning to the
        # user.

        nbins_ = nbins + 1
        ri = numpy.zeros(ri_sz, dtype='uint32')

        _idl_histogram.idl_histogram.reverse_indices_long(data, hist, ri,
                                                          nbins_, n, ri_sz,
                                                          minv, maxv, max_bin,
                                                          binsize)

        return (hist[1:], ri[1:])

    def ri_dlong(data, hist, nbins, n, ri_sz, minv, maxv, max_bin, binsize):
        # increase the size by one. When specifying a min and max, it shouldn't
        # be included in the reverse indices. Stuff not to be included gets
        # dumped into the 1st position then removed prior to returning to the
        # user.

        nbins_ = nbins + 1
        ri = numpy.zeros(ri_sz, dtype='uint32')

        _idl_histogram.idl_histogram.reverse_indices_dlong(data, hist, ri,
                                                           nbins_, n, ri_sz,
                                                           minv, maxv, max_bin,
                                                           binsize)

        return (hist[1:], ri[1:])

    def ri_float(data, hist, nbins, n, ri_sz, minv, maxv, max_bin, binsize):
        # increase the size by one. When specifying a min and max, it shouldn't
        # be included in the reverse indices. Stuff not to be included gets
        # dumped into the 1st position then removed prior to returning to the
        # user.

        nbins_ = nbins + 1
        ri = numpy.zeros(ri_sz, dtype='uint32')

        _idl_histogram.idl_histogram.reverse_indices_float(data, hist, ri,
                                                           nbins_, n, ri_sz,
                                                           minv, maxv, max_bin,
                                                           binsize)

        return (hist[1:], ri[1:])

    def ri_dfloat(data, hist, nbins, n, ri_sz, minv, maxv, max_bin, binsize):
        # increase the size by one. When specifying a min and max, it shouldn't
        # be included in the reverse indices. Stuff not to be included gets
        # dumped into the 1st position then removed prior to returning to the
        # user.

        nbins_ = nbins + 1
        ri = numpy.zeros(ri_sz, dtype='uint32')

        _idl_histogram.idl_histogram.reverse_indices_dfloat(data, hist, ri,
                                                            nbins_, n, ri_sz,
                                                            minv, maxv,
                                                            max_bin, binsize)

        return (hist[1:], ri[1:])


    def datatype(val):
        instr = str(val)
        return {'int8': '1',
                'uint8': '1',
                'int16': '2',
                'uint16': '12',
                'int32': '3',
                'uint32': '13',
                'int64': '13',
                'uint64': '15',
                'int': '13',
                'float32': '4',
                'float64': '5'}.get(instr, 'Error')

    def data_convert(val, b):
        instr = str(val)
        return {'int8': numpy.int8(b),
                'uint8': numpy.uint8(b),
                'int16': numpy.int16(b),
                'uint16': numpy.uint16(b),
                'int32': numpy.int32(b),
                'uint32': numpy.uint32(b),
                'int64': numpy.int64(b),
                'uint64': numpy.uint64(b),
                'int': numpy.int64(b),
                'float32': numpy.float32(b),
                'float64': numpy.float64(b)}.get(instr, 'Error')


    dtype = datatype(data.dtype.name)
    if (dtype == 'Error'):
        msg = ("Error. Incompatable Data Type. Compatable Data Types Include: "
               "int8, uint8, int16, uint16, int32, uint32, int64, uint64, "
               "float32, float64")
        raise TypeError(msg)

    if len(data.shape) != 1:
        data = data.ravel()

    if ((maxv is not None) & (binsize is not None) & (nbins is not None)):
        msg = ("Error. Conflicting Keywords. maxv cannot be set when both "
               "binsize and nbins are set.")
        raise Exception(msg)

    if ((input_arr is not None) & (reverse_indices is not None)):
        msg = ("Error. Conflicting Keywords. Both input_arr and "
               "reverse_indices cannot be set at the same time.")
        raise Exception(msg)

    if (maxv is None):
        if nan:
            maxv = numpy.nanmax(data)
        else:
            maxv = numpy.max(data)

    if (minv is None):
        if nan:
            minv = numpy.nanmin(data)
        else:
            minv = numpy.min(data)

    minv = data_convert(data.dtype.name, minv)
    maxv = data_convert(data.dtype.name, maxv)

    if (binsize is None) & (nbins is None):
        binsize = 1
        nbins = (maxv - minv) + 1
    elif (binsize is None):
        # TODO: monitor binsize calcs for Python3
        # The binsize might get calculated incorrectly if True divide
        # is used for integer datasets
        binsize = (maxv - minv) / (nbins - 1)
        maxv = nbins * binsize + minv
    elif (binsize is not None) & (nbins is None):
        nbins = numpy.floor((maxv - minv) / binsize) + 1
    else:
        maxv = nbins * binsize + minv

    binsize = data_convert(data.dtype.name, binsize)
    minv = data_convert(data.dtype.name, minv)

    # If nbins is set to 256 and the array datatype is uint8, then the max
    # value will be adjusted to 256, however due to datatype conversions, the
    # max value of 256 will change to 0
    # This fix conforms with IDL.
    if ((maxv == 256) & (data.dtype.name == 'uint8')):
        maxv = 255
    maxv = data_convert(data.dtype.name, maxv)

    #probably also need to pass in a max binvalue into the fortran code
    # the max bin value is non-inclusive, but also check that the data
    #values are <= the max value
    # eg max value = 1.0, but max bin = 1.08, therefore a value of 1.04
    # will not be included
    max_bin = nbins * binsize + minv

    if (binsize == 0):
        raise ValueError("Error. Binsize = 0, histogram can't be computed.")

    # Probably unessessary to include the max and max_bin equality warning
    #if (max == max_bin):
    #    msg = ("!!!!!Warning!!!!! \n"
    #           "maxv is equal to the last bin's right edge, "
    #           "maximum value will not be included in the histogram.")
    #    print msg

    if (input_arr is None):
        # Check that input_arr is 1-Dimensional
        if (len(input_arr.shape) != 1):
            print("input_arr will be flattened to 1D.")
            input_arr = input_arr.ravel()

        # Check that input is at least nbins in length
        if (input_arr.shape[0] < nbins):
            print('Number of elements of input_arr: ', input_arr.shape[0])
            print('minimum number of elemets required: ', nbins)
            msg = "Error. Input array does not have enough elements."
            raise ValueError(msg)

    n = numpy.size(data)

    # Some unsigned data types will be promoted as Fortran doesn't handle
    # unsigned data types.
    get_hist = {'int8': hist_int,
                'uint8': hist_int,
                'int16': hist_int,
                'uint16': hist_long,
                'int32': hist_long,
                'uint32': hist_dlong,
                'int64': hist_dlong,
                'uint64': hist_dlong,
                'int': hist_dlong,
                'float32': hist_float,
                'float64': hist_dfloat}

    ri = False

    if (reverse_indices is not None):
        ri = True
        hist = get_hist[data.dtype.name](data, n, minv, maxv, binsize, nbins,
                                         max_bin, ri)
        cum_sum = numpy.sum(hist[1:])
        ri_sz = nbins + cum_sum + 1 + 1

        get_ri = {'int8': ri_int,
                  'uint8': ri_int,
                  'int16': ri_int,
                  'uint16': ri_long,
                  'int32': ri_long,
                  'uint32': ri_dlong,
                  'int64': ri_dlong,
                  'uint64': ri_dlong,
                  'int': ri_dlong,
                  'float32': ri_float,
                  'float64': ri_dfloat}

        hri = get_ri[data.dtype.name](data, hist, nbins, n, ri_sz, minv, maxv,
                                      max_bin, binsize)

        results = {'histogram': hri[0]}
        results[reverse_indices] = hri[1]
    else:
        hist = get_hist[data.dtype.name](data, n, minv, maxv, binsize, nbins,
                                         max_bin, ri)
        if (input_arr is not None):
            # Now to add the input array to the histogram.
            # The result will take the shape of the larger of the two arrays.
            if (input_arr.shape[0] == hist.shape[0]):
               hist += input_arr
               results = {'histogram': hist}
            else:
               temp = numpy.zeros(input_arr.shape, dtype='uint32')
               temp[0:hist.shape[0]] = hist
               temp += input_arr
               results = {'histogram': temp}
        else:
            results = {'histogram': hist}

    if (omax is not None):
        results[omax] = maxv

    if (omin is not None):
        results[omin] = minv

    if (locations is not None):
        loc = numpy.zeros(nbins, dtype=data.dtype.name)
        for i in numpy.arange(nbins):
            loc[i] = minv + i * binsize

        results[locations] = loc

    return results
