# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mimemiko',
    version='0.0.1',
    packages=['mimemiko', ],
    url='https://github.com/ndrwpvlv/mimemiko',
    license='',
    author='Andrei S. Pavlov',
    author_email='ndrw.pvlv@gmail.com',
    description='mime type recognition package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
