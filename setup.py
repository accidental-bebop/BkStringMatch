# --- Imports

import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


# --- Package requirements

INSTALL_REQUIREMENTS = [
    ]

TESTING_REQUIREMENTS = [
    'coverage',
    'pep8',
    'pylint',
    'pytest',
    'pytest-cov',
    'pytest-pep8',
    'pytest-pylint',
    'pytest-xdist',
    ]

DEV_REQUIREMENTS = TESTING_REQUIREMENTS + [
    ]


# --- pytest class

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


# --- Package information

# Package root directory
pkg_root_dir = os.path.dirname(os.path.normcase(__file__))

# Version
version_file = open(os.path.join(pkg_root_dir, 'VERSION'))
version = version_file.read().strip()

# Authors and author email
authors_file = open(os.path.join(pkg_root_dir, 'AUTHORS'))
author_lines = authors_file.readlines()
authors = ','.join([line.split('<')[0].strip() for line in author_lines])
first_author_split = author_lines[0].split('<')
if len(first_author_split) > 1:
    author_email = first_author_split[1].split('>')[0].strip()
else:
    author_email = ''


# --- Setup

setup(
    # Package information
    name='BkStringMatch',
    version=version,
    author=authors,
    author_email=author_email,
    description='BK Tree Nearest Neighbor Search Algorithm',
    long_description=open('README.markdown').read(),
    keywords='BkStringMatch',
    url='',

    # Package construction
    packages=find_packages(),
    scripts=[],

    # Package requirements
    install_requires=INSTALL_REQUIREMENTS,
    tests_require=TESTING_REQUIREMENTS,
    extras_require={
        'dev': DEV_REQUIREMENTS,
        'testing': TESTING_REQUIREMENTS,
    }
)
