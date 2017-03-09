#!/usr/bin/env python

from __future__ import print_function
from __future__ import absolute_import
from numpy.random import RandomState
from numpy.random import mtrand


def randomu(seed, di=None, binomial=None, double=False, gamma=False,
            normal=False, poisson=False):
    """
    Replicates the randomu function avaiable within IDL
    (Interactive Data Language, EXELISvis).
    Returns an array of uniformly distributed random numbers of the
    specified dimensions.
    The randomu function returns one or more pseudo-random numbers
    with one or more of the following distributions:
    Uniform (default)
    Gaussian
    binomial
    gamma
    poisson

    :param seed:
        If seed is not of type mtrand.RandomState, then a new state is
        initialised. Othersise seed will be used to generate the random
        values.

    :param di:
        A list specifying the dimensions of the resulting array. If di
        is a scalar then randomu returns a scalar.
        Dimensions are D1, D2, D3...D8 (x,y,z,lambda...).
        The list will be inverted to suit Python's inverted dimensions
        i.e. (D3,D2,D1).

    :param binomial:
        Set this keyword to a list of length 2, [n,p], to generate
        random deviates from a binomial distribution. If an event
        occurs with probablility p, with n trials, then the number of
        times it occurs has a binomial distribution.

    :param double:
        If set to True, then randomu will return a double precision
        random numbers.

    :param gamma:
        Set this keyword to an integer order i > 0 to generate random
        deviates from a gamm distribution.

    :param Long:
        If set to True, then randomu will return integer uniform
        random deviates in the range [0...2^31-1], using the Mersenne
        Twister algorithm. All other keywords will be ignored.

    :param normal:
        If set to True, then random deviates will be generated from a
        normal distribution.

    :param poisson:
        Set this keyword to the mean number of events occurring during
        a unit of time. The poisson keword returns a random deviate
        drawn from a poisson distribution with that mean.

    :param ULong:
        If set to True, then randomu will return unsigned integer
        uniform deviates in the range [0..2^32-1], using the Mersenne
        Twister algorithm. All other keywords will be ignored.

    :return:
        A NumPy array of uniformly distributed random numbers of the
        specified dimensions.

    Example:
        >>> seed = None
        >>> x, sd = randomu(seed, [10,10])
        >>> x, sd = randomu(seed, [100,100], binomial=[10,0.5])
        >>> x, sd = randomu(seed, [100,100], gamma=2)
        >>> # 200x by 100y array of normally distributed values
        >>> x, sd = randomu(seed, [200,100], normal=True)
        >>> # 1000 deviates from a poisson distribution with a mean of 1.5
        >>> x, sd = randomu(seed, [1000], poisson=1.5)
        >>> # Return a scalar from a uniform distribution
        >>> x, sd = randomu(seed)

    :author:
        Josh Sixsmith, josh.sixsmith@gmail.com, joshua.sixsmith@ga.gov.au

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

    # Initialise the data type
    if double:
        dtype = 'float64'
    else:
        dtype = 'float32'

    # Check the seed
    # http://stackoverflow.com/questions/5836335/consistenly-create-same-random-numpy-array
    if type(seed) != mtrand.RandomState:
        seed = RandomState()

    if di is not None:
        if type(di) is not list:
            raise TypeError("Dimensions must be a list or None.")
        if len(di) > 8:
            raise ValueError("Error. More than 8 dimensions specified.")
        # Invert the dimensions list
        dims = di[::-1]
    else:
        dims = 1

    # Python has issues with overflow:
    # OverflowError: Python int too large to convert to C long
    # Occurs with Long and ULong
    #if Long:
    #    res = seed.random_integers(0, 2**31-1, dims)
    #    if di is None:
    #        res = res[0]
    #    return res, seed

    #if ULong:
    #    res = seed.random_integers(0, 2**32-1, dims)
    #    if di is None:
    #        res = res[0]
    #    return res, seed

    # Check for other keywords
    distributions = 0
    kwds = [binomial, gamma, normal, poisson]
    for kwd in kwds:
        if kwd:
            distributions += 1

    if distributions > 1:
        print("Conflicting keywords.")
        return

    if binomial:
        if len(binomial) != 2:
            msg = "Error. binomial must contain [n,p] trials & probability."
            raise ValueError(msg)

        n = binomial[0]
        p = binomial[1]

        res = seed.binomial(n, p, dims)

    elif gamma:
        res = seed.gamma(gamma, size=dims)

    elif normal:
        res = seed.normal(0, 1, dims)

    elif poisson:
        res = seed.poisson(poisson, dims)

    else:
        res = seed.uniform(size=dims)

    res = res.astype(dtype)

    if di is None:
        res = res[0]

    return res, seed
