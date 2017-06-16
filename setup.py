#!/usr/bin/env python
# This file is part of asm. The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

import os
from setuptools import setup, find_packages

__version__ = '0.0.1'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='correosexpress',
        version=__version__,
        author='comunitea',
        author_email='info@comunitea.com',
        url="http://comunitea.com/",
        description="Python API Correos express carrier",
        long_description=read('README'),
        download_url="https://github.com/Comunitea/python-correosexpress",
        packages=find_packages(),
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU Affero General Public License v3',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ],
        install_requires=[],
        license='GPL-3',
        extras_require={
        },
    )
