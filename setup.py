#!/usr/bin/env python3

import os
from setuptools import setup
from colorize import colorize

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Colorizer",
    version = colorize.__version__,
    author = colorize.__author__,
    description = (colorize.__doc__),
    keywords = "Color, ANSI",
    url = "https://github.com/jaschon/colorize",
    packages=['colorize', 'tests'],
    long_description=read('README.md'),
)
