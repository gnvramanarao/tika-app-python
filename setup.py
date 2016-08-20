#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Tika App',
    version='0.3',
    description='Python client for Apache Tika App',
    author='Fedele Mantuano',
    author_email='mantuano.fedele@gmail.com',
    maintainer='Fedele Mantuano',
    maintainer_email='mantuano.fedele@gmail.com',
    url='https://github.com/fedelemantuano/tika-app-python',
    keywords=['tika', 'apache', 'toolkit'],
    requires=['simplejson'],
    license="Apache License, Version 2.0",
    packages=['tika_app'],
)
