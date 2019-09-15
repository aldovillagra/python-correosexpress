#!/usr/bin/env python
# This file is part of asm. The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

import os
from setuptools import setup, find_packages

__version__ = '0.0.10'

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='correosexpress',
        version=__version__,
        author='Aldo A. Villagra B.',
        author_email='aldovillagra@gmail.com',
        url="http://www.linkedin.com/in/aldo-villagra-49546510/",
        description="Python API Correos express carrier",
        long_description=long_description,
        long_description_content_type="text/markdown",
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
