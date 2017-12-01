#!/usr/bin/python
#coding: utf-8
#(c) 2017 4Geeks Technologies, Inc.

from setuptools import setup, find_packages

setup(name='gpayments',
      version='0.1',
      description='Client for 4Geeks Payments',
      url='https://github.com/4GeeksDev/gpayments-python',
	  download_url='https://github.com/4GeeksDev/gpayments-python/tarball/master',
      author='4Geeks Technologies, Inc',
      author_email='hello@4geeks.io',
      license='MIT',
      packages=find_packages(),
	  keywords='4geeks payments',
      zip_safe=False)
