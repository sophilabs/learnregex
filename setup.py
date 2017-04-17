#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
]

test_requirements = [
]

setup(
    name='learnregex',
    version='0.2.2',
    description='A pyschool story for learning regular expressions.',
    long_description=readme + '\n\n' + history,
    author='Sophilabs',
    author_email='hi@sophilabs.co',
    url='https://github.com/sophilabs/learnregex',
    packages=[
        'learnregex',
    ],
    package_dir={'learnregex': 'learnregex'},
    entry_points={
        'console_scripts': [
            'learnregex=learnregex.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license='MIT license',
    zip_safe=False,
    keywords='learnregex',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
