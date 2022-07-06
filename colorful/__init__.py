#!/usr/bin/env python3
"""Color terminal text with ANSI Styles and Colors"""

__author__ = "Jason Rebuck"
__copyright__ = "2021-2022"
__version__ = "0.22"

# NOTE:
# reset = \33[0m
# color = \33[ + 3 + COLOR NUMBER + m
# bright = \33[ + 9 + COLOR NUMBER + m
# style = \33[ + STYLE NUMBER + m
# bg = \33[ + 4 + COLOR NUMBER + m

# COLORS
# black = 0
# red = 1
# green = 2
# yellow = 3
# blue = 4
# magenta = 5
# cyan = 6
# white = 7

# STYLES
# reset = 0
# bold = 1
# dim = 2
# italic = 3
# underline = 4
# blink = 5
# rapid blink = 6
# invert = 7
# hide = 8
# strike = 9

# 8-bit (256) colors
# 0-7 = standard
# 8-15 = bright
# 16-231 = 216 colors
# 232-255 = grayscale

# 24-bit colors
# R,G,B
# NOT SUPPORTED IN SOME TERMINALS

class Color:
    """Output Text With ANSI Color And Style"""

    def __init__(self, text="", space=" "):
        """Collect Text"""
        self.text = text
        self.space = space

    def _wrap(self, attr="", num=0, end="m", esc="\x1b["):
        """Wrap with ANSI codes"""
        self.text = f"{esc}{attr}{num}{end}{self.text}{esc}0{end}"
        return self

    # Output
    def __add__(self, obj):
        """Concat Text or Color Objs"""
        self.text = f"{self.text}{self.space}{obj}"
        return self

    def __repr__(self):
        """Return Text"""
        return self.text

    # Colors
    def black(self):
        """Color Black"""
        return self._wrap(3, 0)

    def red(self):
        """Color Red"""
        return self._wrap(3, 1)

    def green(self):
        """Color Green"""
        return self._wrap(3, 2)

    def yellow(self):
        """Color Yellow"""
        return self._wrap(3, 3)

    def blue(self):
        """Color Blue"""
        return self._wrap(3, 4)

    def magenta(self):
        """Color Magenta"""
        return self._wrap(3, 5)

    def cyan(self):
        """Color Cyan"""
        return self._wrap(3, 6)

    def white(self):
        """Color White"""
        return self._wrap(3, 7)

    # Bright Colors
    def bright_black(self):
        """Color Bright Black"""
        return self._wrap(9, 0)

    def bright_red(self):
        """Color Bright Red"""
        return self._wrap(9, 1)

    def bright_green(self):
        """Color Bright Green"""
        return self._wrap(9, 2)

    def bright_yellow(self):
        """Color Bright Yellow"""
        return self._wrap(9, 3)

    def bright_blue(self):
        """Color Bright Blue"""
        return self._wrap(9, 4)

    def bright_magenta(self):
        """Color Bright Magenta"""
        return self._wrap(9, 5)

    def bright_cyan(self):
        """Color Bright Cyan"""
        return self._wrap(9, 6)

    def bright_white(self):
        """Color Bright White"""
        return self._wrap(9, 7)

    # Background
    def on_black(self):
        """Background Black"""
        return self._wrap(4, 0)

    def on_red(self):
        """Background Red"""
        return self._wrap(4, 1)

    def on_green(self):
        """Background Green"""
        return self._wrap(4, 2)

    def on_yellow(self):
        """Background Yellow"""
        return self._wrap(4, 3)

    def on_blue(self):
        """Background Blue"""
        return self._wrap(4, 4)

    def on_magenta(self):
        """Background Magenta"""
        return self._wrap(4, 5)

    def on_cyan(self):
        """Background Cyan"""
        return self._wrap(4, 6)

    def on_white(self):
        """Background White"""
        return self._wrap(4, 7)

    # Styles
    def reset(self):
        """Style Reset"""
        return self._wrap(num=0)

    def bold(self):
        """Style Bold"""
        return self._wrap(num=1)

    def dim(self):
        """Style Dim"""
        return self._wrap(num=2)

    def italic(self):
        """Style Italic"""
        return self._wrap(num=3)

    def underline(self):
        """Style Underline"""
        return self._wrap(num=4)

    def blink(self):
        """Style blink"""
        return self._wrap(num=5)

    def invert(self):
        """Style Inverse"""
        return self._wrap(num=7)

    def hide(self):
        """Style Hidden"""
        return self._wrap(num=8)

    def strike(self):
        """Style Strike"""
        return self._wrap(num=9)

class Extended(Color):
    """Extended Color Modes"""

    def color(self, color=0):
        """Wrap with extended color (0-255)"""
        return self._wrap("38;5;", color)

    def on_color(self, color=0):
        """Wrap with extended bg color (0-255)"""
        return self._wrap("48;5;", color)

class RGB(Color):
    """RGB Color Modes"""

    def color(self, red=0, green=0, blue=0):
        """Wrap with 24-bit color (red,green,blue)"""
        return self._wrap("38;2;", f"{red};{green};{blue}")

    def on_color(self, red=0, green=0, blue=0):
        """Wrap with 24-bit bg color (red ,green, blue)"""
        return self._wrap("48;2;", f"{red};{green};{blue}")

if __name__ == "__main__":
    pass
