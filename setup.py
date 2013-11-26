# -*- coding: utf-8 -*-
"""
    task.py
    ~~~~~~~~
    
    :copyright: (c) 2013 by Abhinav Singh.
    :license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages
import task

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Topic :: Communications',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

install_requires = open('requirements.txt', 'rb').read().strip().split()

setup(
    name                = 'task.py',
    version             = task.__version__,
    description         = task.__description__,
    long_description    = open('README.md').read().strip(),
    author              = task.__author__,
    author_email        = task.__author_email__,
    url                 = task.__homepage__,
    license             = task.__license__,
    packages            = find_packages(),
    install_requires    = install_requires,
    classifiers         = classifiers
)
