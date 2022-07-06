#!/usr/bin/env python3
"""Test Color Output"""

import unittest
from colorful import Color

COLORS = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
STYLES = ["reset", "bold", "dim", "italic", "underline", "blink", "invert", "hide", "strike"]

class TestOutputColor(unittest.TestCase):
    """Test Output Base Color"""

    title = "Color"
    check = COLORS
    method = ""
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

class TestOutputStyle(TestOutputColor):
    """Test Output Style"""

    title = "Style"
    check = STYLES
    method = ""
    method_add = ""

class TestOutputBG(TestOutputColor):
    """Test Output BG"""

    title = "Backgrounds"
    check = COLORS
    method = ""
    method_add = "on_"

class TestOutputBright(TestOutputColor):
    """Test Output Bright"""

    title = "Bright"
    check = COLORS
    method = ""
    method_add = "bright_"

if __name__ == "__main__":
    unittest.main()
