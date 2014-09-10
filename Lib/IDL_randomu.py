#!/usr/bin/env python

from numpy.random import RandomState
from numpy.random import mtrand

def randomu(seed, di=None, Binomial=None, Double=False, Gamma=False,
            Long=False, Normal=False, Poisson=False, ULong=False):
    """
    Replicates the randomu function avaiable within IDL
    (Interactive Data Language, EXELISvis).
    Returns an array of uniformly distributed random numbers of the
    specified dimensions.
    The randomu function returns one or more pseudo-random numbers
    with one or more of the following distributions:
    Uniform (default)
    Gaussian
    Binomial
    Gamma
    Poisson

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

    :param Binomial:
        Set this keyword to a list of length 2, [n,p], to generate
        random deviates from a binomial distribution. If an event
        occurs with probablility p, with n trials, then the number of
        times it occurs has a binomial distribution.

    :param Double:
        If set to True, then randomu will return a double precision
        random numbers.

    :param Gamma:
        Set this keyword to an integer order i > 0 to generate random
        deviates from a gamm distribution.

    :param Long:
        If set to True, then randomu will return integer uniform
        random deviates in the range [0...2^31-1], using the Mersenne
        Twister algorithm. All other keywords will be ignored.

    :param Normal:
        If set to True, then random deviates will be generated from a
        normal distribution.

    :param Poisson:
        Set this keyword to the mean number of events occurring during
        a unit of time. The Poisson keword returns a random deviate
        drawn from a Poisson distribution with that mean.

    :param ULong:
        If set to True, then randomu will return unsigned integer
        uniform deviates in the range [0..2^32-1], using the Mersenne
        Twister algorithm. All other keywords will be ignored.
    """

    # Initialise the data type
    if Double:
        dtype = 'float64'
    elif Long:
        dtype = 'int32'
    elif ULong:
        dtype = 'uint32'
    else:
        dtype = 'float32'

    # Check the seed
    # http://stackoverflow.com/questions/5836335/consistenly-create-same-random-numpy-array
    if type(seed) != mtrand.RandomState:
        seed = RandomState()

    if di is not None:
        if type(di) is not list:
            print "Dimensions must be a list."
        if len(di) > 8:
            print "Can't be more than 8 dimensions."
        # Invert the dimensions list
        dims = di[::-1]
    else:
        dims = 1

    # Check for other keywords
    distributions = 0
    kwds = [Binomial,Gamma,Normal,Poisson]
    for kwd in kwds:
        if kwd:
            distributions += 1

    if distributions > 1:
        print "Conflicting keywords."
        return

    if Binomial:
        if len(Binomial) != 2:
            print "Binomial must contain [n,p] trials & probability."

        n = Binomial[0]
        p = Binomial[1]

        res = seed.binomial(n, p, dims)

    elif Gamma:
        res = seed.gamma(Gamma, size=dims)

    elif Normal:
        res = seed.normal(0, 1, dims)

    elif Poisson:
        res = seed.poisson(Poisson, dims)

    else:
        res = seed.uniform(size=dims)

    res = res.astype(dtype)

    if di is None:
        res = res[0]

    return res, seed

