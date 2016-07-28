#!/usr/bin/env python
from setuptools import setup,find_packages

setup(
    name="fum-po",
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'pyyaml',
        'couchdb',
    ],
    entry_points='''
        [console_scripts]
        dream=fum_po.dreamcatcher:cli
    ''',
)
