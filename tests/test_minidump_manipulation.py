#! /usr/bin/env python

import os
__dir__ = os.path.dirname(__file__)

from test_all import run_tests, assertion, hashlib, open_read
from elfesteem.minidump_init import Minidump

def test_MD_windows(assertion):
    md = open_read(__dir__+'/binary_input/windows.dmp')
    assertion('82a09a9d801bddd1dc94dfb9ba6eddf0',
              hashlib.md5(md).hexdigest(),
              'Reading windows.dmp')
    e = Minidump(md)
    d = e.dump().encode('latin1')
    assertion('48cae6cc782305b611f6e8b82049b9a0',
              hashlib.md5(d).hexdigest(),
              'Displaying the content of windows.dmp')

def test_MD_i386(assertion):
    md = open_read(__dir__+'/binary_input/minidump-i386.dmp')
    assertion('0f2ee1a0a2e6351e64929197c07679e6',
              hashlib.md5(md).hexdigest(),
              'Reading minidump-i386.dmp')
    e = Minidump(md)
    d = e.dump().encode('latin1')
    assertion('c89c01352e515874b00d998b1ad06998',
              hashlib.md5(d).hexdigest(),
              'Displaying the content of minidump-i386.dmp')

def test_MD_x86_64(assertion):
    md = open_read(__dir__+'/binary_input/minidump-x86_64.dmp')
    assertion('ecde7af61615e05ffcde1f064c1a22f8',
              hashlib.md5(md).hexdigest(),
              'Reading minidump-x86_64.dmp')
    e = Minidump(md)
    d = e.dump().encode('latin1')
    assertion('4357695a7e265aca04bb2809485b8634',
              hashlib.md5(d).hexdigest(),
              'Displaying the content of minidump-x86_64.dmp')

def run_test(assertion):
    for name, value in dict(globals()).items():
        if name.startswith('test_'):
            value(assertion)

if __name__ == "__main__":
    run_tests(run_test)
