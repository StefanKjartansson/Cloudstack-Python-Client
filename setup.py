#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='cloudstack',
    version='0.1',
    author='Stefan Kjartansson',
    author_email='esteban.supreme@gmail.com',
    url='http://www.greenqloud.com',
    description = 'Cloud.com Cloudstack API client',
    packages=find_packages(),
    install_requires=[
    ],
    include_package_data=True,
    classifiers=[
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
    'Topic :: Cloud Computing'
],)

