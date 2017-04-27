#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    name='learnregex',
    version='0.4.11',
    description='A pyschool story for learning regular expressions.',
    long_description=readme + '\n\n' + history,
    author='Sophilabs',
    author_email='hi@sophilabs.co',
    url='https://github.com/sophilabs/learnregex',
    packages=['learnregex'],
    entry_points={
        'console_scripts': [
            'learnregex=learnregex:Story.begin'
        ]
    },
    include_package_data=True,
    install_requires=[
        'story>=1.2.2'
    ],
    python_requires='!=2, !=3.0.*, !=3.1.*, !=3.2.*, <4',
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
    tests_require=[]
)
