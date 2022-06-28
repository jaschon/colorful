#!/usr/bin/env python3

import os
from setuptools import setup
import colorful

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Colorful",
    version = colorful.__version__,
    author = colorful.__author__,
    description = (colorful.__doc__),
    keywords = "Color, ANSI",
    url = "https://github.com/jaschon/colorful",
    packages=['colorful'],
    long_description=read('README.md'),
    test_suite="tests",
)
