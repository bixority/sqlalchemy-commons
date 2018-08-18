#!/usr/bin/env python
import os.path
from setuptools import setup


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))

    return [line for line in lineiter if line and not line.startswith('#')]


install_reqs = parse_requirements('requirements.txt')

current_file_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(current_file_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sqlalchemy_commons',
    version='0.0.2',
    python_requires='~=3.7',
    packages=[
        'sqlalchemy_commons',
    ],
    # setup_requires=['pytest-runner'],
    # tests_require=['pytest'],
    package_dir={'': 'src'},
    url='https://github.com/bixority/sqlalchemy-commons',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    keywords='sqlalchemy orm common models',
    install_requires=install_reqs,
    author='Oleg Korsak',
    author_email='kamikaze.is.waiting.you@gmail.com',
    description='SQLAlchemy common models',
    test_suite='tests'
)
