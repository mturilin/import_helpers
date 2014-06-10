# !/usr/bin/env python
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


README = read('README.rst')

setup(
    name='import_helpers',
    version='0.1',
    author='mikhail turilin',
    author_email='mikhail@turilin.com',
    description='Easy importing helpers',
    license='MIT',
    url='https://github.com/mturilin/import_helpers',
    long_description=README,
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
    ],
    install_requires=[

    ],
)
