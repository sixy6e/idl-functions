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

# TODO Need to incorporate a complete fail and exit if the gnu95 compiler
# is not found.
avail_fcompilers = fcompiler.available_fcompilers_for_platform()
if ('gnu95' not in avail_fcompilers):
    print('gnu95 compiler not found')
 
extra_compile_args=['--fcompiler=gnu95']
    
## setup the python module
setup(name="idl_functions", # name of the package to import later
      version='0.5.2',
      author='Josh Sixsmith',
      author_email='josh.sixsmith@gmail.com, joshua.sixsmith@ga.gov.au',
      # Build fortran wrappers, uses f2py
      #ext_modules = [Extension('_idl_histogram', ['Src/IDL_Histogram.f90'],
      #                          files,
      #                         libraries=[],
      #                         library_dirs=[],
      #  		       include_dirs=['Src'],
      #                         extra_compile_args=extra_compile_args,
      #                         ),
      ext_modules = [
                     Extension('_idl_histogram',['Src/idl_histogram.f90']),
                     Extension('idl_functions.tests.unit_test_idl_hist',
                               ['tests/unit_test_idl_hist.f90'])
                    ],
      
     ## Install these to their own directory
     package_dir = {'idl_functions':'Lib', 'idl_functions/tests':'tests'},
     packages = ["idl_functions", 'idl_functions/tests'],
     test_suite = ['idl_functions.tests.unit_test_idl_histogram',
                   'idl_functions.tests.unit_test_idl_hist_equal',
                   'idl_functions.tests.unit_test_idl_array_indices',
                   'idl_functions.tests.unit_test_idl_bytscl',
                   'idl_functions.tests.unit_test_idl_region_grow',
                   'idl_functions.tests.unit_test_idl_randomu'])
