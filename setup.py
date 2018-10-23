from __future__ import absolute_import
from __future__ import print_function
import sys

# we should build this module in three steps:
# Unix/Linux:
# 1. python setup.py build --fcompiler=gnu95
# 2. python test.py
# If all tests have passed, then it is ok to install.
# 3. python setup.py install

# Windows
# 1. python setup.py build --fcompiler=gnu95 --compiler=mingw32
# 2. python test.py
# If all tests have passed, then it is ok to install.
# 3. python setup.py install

# Use distutils setup rather than setuptools setup as we need to compile Fortran
# code using F2PY
from numpy.distutils.core import setup, Extension
from numpy.distutils import fcompiler

avail_fcompilers = fcompiler.available_fcompilers_for_platform()
if ('gnu95' not in avail_fcompilers):
    raise RuntimeError("gnu95 required to install idl-functions")
 
## setup the python module
setup(name="idl_functions", # name of the package to import later
      version='0.5.4',
      author='Josh Sixsmith',
      author_email='josh.sixsmith@gmail.com, joshua.sixsmith@ga.gov.au',
      url='https://github.com/sixy6e/idl-functions',
      ext_modules = [
                     Extension('_idl_histogram', ['lib/idl_histogram.f90']),
                     Extension('idl_functions.tests.unit_test_idl_hist',
                               ['tests/unit_test_idl_hist.f90'])
                    ],
      
     ## Install these to their own directory
     package_dir = {'idl_functions':'lib', 'idl_functions/tests':'tests'},
     packages = ["idl_functions", 'idl_functions/tests'],
)
