#!/usr/bin/env python2

# This file is part of Local Scraperlibs.

import warnings
import os
from distutils.core import setup

def has_external_dependency(name):
    'Check that a non-Python dependency is installed.'
    for directory in os.environ['PATH'].split(':'):
        if os.path.exists(os.path.join(directory, name)):
            return True
    return False

if not has_external_dependency('wget'):
    warnings.warn(
        'wget not found: attach() and swimport() will not work.')

if not has_external_dependency('pdftohtml'):
    warnings.warn(
        'Local Scraperlibs requires pdftohtml, but pdftoxml was not found\n'
        'in the PATH. You probably need to install it.'
    )

# requires = open('requirements.txt').read().split('\n')[:-1]
requires = ['dumptruck==0.1.0']

setup(name='scraperwiki_local',
    author='Thomas Levine',
    author_email='thomas@scraperwiki.com',
    description='Local version of scraperwiki scraperlibs',
    url='https://github.com/tlevine/scraperwiki_local',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: SQL',
        'Topic :: Database :: Front-Ends',
    ],
    packages=['scraperwiki', 'scraperwiki.geo'],

    version = '0.1.0',
    license='GPL',
    install_requires = requires,
   )
