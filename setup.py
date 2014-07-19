#!/usr/bin/env python

from setuptools import setup

setup(name='hadoopio',
      version='0.2',
      description='Python Hadoop I/O Utilities',
      license="Apache Software License 2.0 (ASF)",
      author='Matteo Bertozzi',
      author_email='theo.bertozzi@gmail.com',
      url='http://hadoopio.apache.org',
      packages=["hadoopio", 'hadoopio.util', 'hadoopio.io', 'hadoopio.io.compress',
                "hadoopio.pydoop"],
      extras_require = {
        'pydoop': ['pydoop>=0.9.1']
        }
     )

