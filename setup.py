#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup for bibutils."""
from __future__ import unicode_literals

from setuptools import setup

name = str('bibutils')

dependencies = [
    'sarge',
]

setup(
    name=name,
    version='0.0.1',
    description='bibutils wrapper.',
    keywords='bib xml copac end isi med ris mods',
    author='John Vandenberg',
    author_email='jayvdb@gmail.com',
    url='https://github.com/jayvdb/bibutils',
    license='MIT',
    packages=[name],
    install_requires=dependencies,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
