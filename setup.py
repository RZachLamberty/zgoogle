#!/usr/bin/env python
from setuptools import setup

setup(
    name='zgoogle',
    version='1.0.0',
    description='google api wrappers',
    include_package_data=True,
    author='Zach Lamberty',
    author_email='r.zach.lamberty@gmail.com',
    url='https://github.com/RZachLamberty/',
    packages=['zgoogle'],
    install_requires=[
        'pyyaml',
        'googlemaps'
    ]
)
