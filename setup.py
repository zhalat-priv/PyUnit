# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import find_packages
import os

long_description = """\
PyUnit_skeleton. Your quick start with PyUnit tests.
"""

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, 'requirements.txt')) as f:
    required = f.read().splitlines()

setup(
    name='PyUnit_skeleton',
    version='1.0.0',
    python_requires='>=3.6.0',
    description='Base test skeleton for your PyUnit test',
    long_description=long_description,
    license='open soruce',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,

    install_requires=required,
)
