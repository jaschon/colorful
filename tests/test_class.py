#!/usr/bin/env python3
"""Unittest Color Class"""

import sys
import unittest
# sys.path.append("..")
from colorize.colorize import Color

class TestColor(unittest.TestCase):
    """Test Base Color"""

    tests = (
            ("black", "\33[30mthis is a test\33[0m"),
            ("red", "\33[31mthis is a test\33[0m"),
            ("green", "\33[32mthis is a test\33[0m"),
            ("yellow", "\33[33mthis is a test\33[0m"),
            ("blue", "\33[34mthis is a test\33[0m"),
            ("magenta", "\33[35mthis is a test\33[0m"),
            ("cyan", "\33[36mthis is a test\33[0m"),
            ("white", "\33[37mthis is a test\33[0m"),
            )

    def test_objs(self):
        """Loop through tuple and compare values"""
        for col in self.tests:
            obj = Color("this is a test")
            getattr(obj, col[0])()
            self.assertEqual(obj.text, col[1], col[1])
            self.assertEqual(obj, getattr(obj, col[0])())

class TestBackground(TestColor):
    """Test Background Color"""

    tests = (
            ("bgblack", "\33[40mthis is a test\33[0m"),
            ("bgred", "\33[41mthis is a test\33[0m"),
            ("bggreen", "\33[42mthis is a test\33[0m"),
            ("bgyellow", "\33[43mthis is a test\33[0m"),
            ("bgblue", "\33[44mthis is a test\33[0m"),
            ("bgmagenta", "\33[45mthis is a test\33[0m"),
            ("bgcyan", "\33[46mthis is a test\33[0m"),
            ("bgwhite", "\33[47mthis is a test\33[0m"),
            )

class TestStyle(TestColor):
    """Test Base Style"""

    tests = (
            ("bold", "\33[1mthis is a test\33[0m"),
            ("dim", "\33[2mthis is a test\33[0m"),
            ("italic", "\33[3mthis is a test\33[0m"),
            ("underline", "\33[4mthis is a test\33[0m"),
            ("blink", "\33[5mthis is a test\33[0m"),
            ("inverse", "\33[7mthis is a test\33[0m"),
            )

class TestAlign(TestColor):
    """Test Alignment"""

    tests = (
            ("left", "this is a test           "),
            ("right", "           this is a test"),
            ("center", "     this is a test      "),
            )

class TestChainColor(unittest.TestCase):
    """Test Chain Colors with Bold"""

    tests = (
            ("black", "\33[30m\33[1mthis is a test\33[0m\33[0m"),
            ("red", "\33[31m\33[1mthis is a test\33[0m\33[0m"),
            ("green", "\33[32m\33[1mthis is a test\33[0m\33[0m"),
            ("yellow", "\33[33m\33[1mthis is a test\33[0m\33[0m"),
            ("blue", "\33[34m\33[1mthis is a test\33[0m\33[0m"),
            ("magenta", "\33[35m\33[1mthis is a test\33[0m\33[0m"),
            ("cyan", "\33[36m\33[1mthis is a test\33[0m\33[0m"),
            ("white", "\33[37m\33[1mthis is a test\33[0m\33[0m"),
            )

    def test_objs(self):
        """Loop through tuple and compare values"""
        for col in self.tests:
            obj = Color("this is a test")
            obj.bold()
            getattr(obj, col[0])()
            self.assertEqual(obj.text, col[1])
            self.assertEqual(obj, getattr(obj, col[0])())

class TestChainStyle(TestChainColor):
    """Test Chain Styles with Bold"""

    tests = (
            ("bold", "\33[1m\33[1mthis is a test\33[0m\33[0m"),
            ("dim", "\33[2m\33[1mthis is a test\33[0m\33[0m"),
            ("italic", "\33[3m\33[1mthis is a test\33[0m\33[0m"),
            ("underline", "\33[4m\33[1mthis is a test\33[0m\33[0m"),
            ("blink", "\33[5m\33[1mthis is a test\33[0m\33[0m"),
            ("inverse", "\33[7m\33[1mthis is a test\33[0m\33[0m"),
            )

class TestChainBackground(TestChainColor):
    """Test Chain Background with Bold"""

    tests = (
            ("bgblack", "\33[40m\33[1mthis is a test\33[0m\33[0m"),
            ("bgred", "\33[41m\33[1mthis is a test\33[0m\33[0m"),
            ("bggreen", "\33[42m\33[1mthis is a test\33[0m\33[0m"),
            ("bgyellow", "\33[43m\33[1mthis is a test\33[0m\33[0m"),
            ("bgblue", "\33[44m\33[1mthis is a test\33[0m\33[0m"),
            ("bgmagenta", "\33[45m\33[1mthis is a test\33[0m\33[0m"),
            ("bgcyan", "\33[46m\33[1mthis is a test\33[0m\33[0m"),
            ("bgwhite", "\33[47m\33[1mthis is a test\33[0m\33[0m"),
            )

class TestAdd(unittest.TestCase):
    """Test Adding Method"""

    def test_add_class_basic(self):
        """Test Adding Classes (No Style)"""
        obj1 = Color("this is a test")
        obj2 = Color("another test")
        self.assertEqual("this is a test another test", str(obj1+obj2))

    def test_add_class_style(self):
        """Test Adding Classes (With Style)"""
        obj1 = Color("this is a test").bold()
        obj2 = Color("another test").blue()
        self.assertEqual("\33[1mthis is a test\33[0m \33[34manother test\33[0m", str(obj1+obj2))

    def test_add_str_basic(self):
        """Test Adding Classes (With Strings)"""
        obj1 = Color("this is a test")
        obj2 = "another test"
        self.assertEqual("this is a test another test", str(obj1+obj2))

    def test_add_str_style(self):
        """Test Adding Classes (With Styles and Strings)"""
        obj1 = Color("this is a test").bold()
        obj2 = "another test"
        self.assertEqual("\33[1mthis is a test\33[0m another test", str(obj1+obj2))


if __name__ == "__main__":
    unittest.main()
