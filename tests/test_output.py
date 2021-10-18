#!/usr/bin/env python3
"""Test Color Output"""

import unittest
from colorize.colorize import Color

class TestOutputColor(unittest.TestCase):
    """Test Output Base Color"""

    title = "Color"
    check = Color.COLORS
    method = "_color"
    method_add = ""

    def setUp(self):
        print()
        print(Color(self.title).bold().underline())

    def tearDown(self):
        print()

    def test_loop(self):
        """Loop through colors and print"""
        for index, itm in enumerate(self.check):
            obj = Color(f"{index+1}.) {itm}")
            if self.method:
                print(getattr(obj, self.method)(itm))
            else:
                if hasattr(obj, self.method_add+itm):
                    print(getattr(obj, self.method_add+itm)())
                else:
                    print(f"X.) *Skipping* ({self.method_add}{itm} method not found)")


class TestOutputColorWrap(TestOutputColor):
    """Test Output Base Color Wrapper"""

    title = "Color Wrap"
    check = Color.COLORS
    method = ""
    method_add = ""


class TestOutputStyle(TestOutputColor):
    """Test Output Style"""

    title = "Style"
    check = Color.STYLES
    method = "_style"
    method_add = ""


class TestOutputStyleWrapper(TestOutputColor):
    """Test Output Style Wrapper"""

    title = "Style Wrapper"
    check = Color.STYLES
    method = ""
    method_add = ""


class TestOutputBG(TestOutputColor):
    """Test Output BG"""

    title = "Backgrounds"
    check = Color.COLORS
    method = "_bg"
    method_add = ""


class TestOutputBGWrapper(TestOutputColor):
    """Test Output BG Wrapper"""

    title = "BG Wrapper"
    check = Color.COLORS
    method = ""
    method_add = "bg"


class TestOutputBright(TestOutputColor):
    """Test Output Bright"""

    title = "Bright"
    check = Color.COLORS
    method = "_bright"
    method_add = ""

class TestOutputBrightWrapper(TestOutputColor):
    """Test Output Bright Wrapper"""

    title = "Bright Wrapper"
    check = Color.COLORS
    method = ""
    method_add = "br"

class TestOutputAdd(TestOutputColor):
    """Test Output Class Adding"""

    title = "Class Adding"
    check = ()
    method = ""
    method_add = ""

    def test_loop(self):
        """Loop through colors and print"""
        for index, color in enumerate(Color.COLORS):
            obj1 = Color(f"{index+1}.)").bold()._bg(color)
            obj2 = Color(f"{color}")._color(color)
            num = 12345
            string = "String"
            print(obj1+obj2+num+string)


if __name__ == "__main__":
    unittest.main()
