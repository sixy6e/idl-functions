#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import subprocess
import fnmatch


def locate(pattern, root):
    matches = []
    for path, dirs, files in os.walk(os.path.abspath(root)):
        for filename in fnmatch.filter(files, pattern):
            matches.append(os.path.join(path, filename))
    return matches


if __name__ == '__main__':
    dir_list = os.listdir(os.getcwd())
    if 'build' not in dir_list:
        msg = ("The build directory was not found. Please build the "
               "idl_functions module first. Exiting...")
        sys.exit(msg)
    else:
        # Change to the build directory
        os.chdir('build')

        # Find the unittest script
        test_file1 = locate('unit_test_idl_histogram.py', os.getcwd())[0]
        test_file2 = locate('unit_test_idl_hist_equal.py', os.getcwd())[0]
        test_file3 = locate('unit_test_idl_array_indices.py', os.getcwd())[0]
        test_file4 = locate('unit_test_idl_bytscl.py', os.getcwd())[0]
        test_file5 = locate('unit_test_idl_region_grow.py', os.getcwd())[0]
        test_file6 = locate('unit_test_idl_randomu.py', os.getcwd())[0]

        # Get the directory path that contains the unittest script and change
        # to that directory
        dname = os.path.dirname(test_file1)
        os.chdir(dname)

        # Move up two directories from where unit_test_IDL_Hist.py was located
        os.chdir(os.pardir)
        os.chdir(os.pardir)

        # Now execute the unittest script from the command line
        print("Testing idl_histogram")
        subprocess.call(['python', test_file1])
        print("Testing idl_hist_equal")
        subprocess.call(['python', test_file2])
        print("Testing idl_array_indices")
        subprocess.call(['python', test_file3])
        print("Testing idl_bytscl")
        subprocess.call(['python', test_file4])
        print("Testing idl_region_grow")
        subprocess.call(['python', test_file5])
        print("Testing idl_randomu")
        subprocess.call(['python', test_file6])
