# -*- coding: utf-8 -*-

# Learn more: https://github.com/PabRod/toypy

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='toypy',
    version='0.1.0',
    description='Toy package',
    long_description=readme,
    author='Pablo Rodríguez-Sánchez',
    author_email='pablo.rodriguez.sanchez@gmail.com',
    url='https://github.com/PabRod/toypy',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
