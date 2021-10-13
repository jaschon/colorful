#!/usr/bin/env python3

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Colorizer",
    version = "0.15",
    author = "Jason Rebuck",
    description = ("A simple python class to color, align and style terminal text."),
    keywords = "Color, ANSI",
    url = "https://github.com/jaschon/colorize",
    packages=['colorize', 'tests'],
    long_description=read('README.md'),
    classifiers=[],
)
