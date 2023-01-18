#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='tap-netsuite',
    version='1.5.19',
    description='Singer.io tap for extracting data from the NetSuite SOAP',
    author='hotglue',
    url='https://hotglue.xyz/',
    classifiers=['Programming Language :: Python :: 3 :: Only'],
    py_modules=['tap_netsuite'],
    install_requires=[
        'netsuitesdk @ git+https://github.com/hotgluexyz/netsuite-sdk-py.git@2.7.5#egg=netsuitesdk', # USING THE HOTGLUE VERSION
        'requests==2.21.0',
        'singer-python==5.3.1',
        'xmltodict==0.11.0',
        'jsonpath-ng==1.4.3',
        'jsonschema==2.6.0',
        'pytz==2018.4'
    ],
    entry_points='''
        [console_scripts]
        tap-netsuite=tap_netsuite:main
    ''',
    packages=find_packages(exclude=['tests']),
    package_data={
        'tap_netsuite.netsuite': ['schemas/*.json']
    },
    include_package_data=True,
)
