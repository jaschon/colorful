#!/usr/bin/env python3
"""Color terminal text with ANSI Escape Styles and Colors"""

# NOTE:
# reset = \33[0m
# color = \33[ + 3 + COLOR NUMBER + m
# style = \33[ + STYLE NUMBER + m
# bg = \33[ + 4 + COLOR NUMBER + m

# - Can make "bright" colors with attr of 9 instead of 3
# but this seems to be similar to bold() in most terminals.
# - Some styles don't seem to work in the terminals I've tried
# so I didn't make methods for them.

__author__ = "Jason Rebuck"
__copyright__ = "2021"
__version__ = "0.15"

class Color:
    """Output Text With Color And Style"""

    COLORS = {
            "black" : 0,
            "red" : 1,
            "green": 2,
            "yellow": 3,
            "blue" : 4,
            "magenta" : 5,
            "cyan": 6,
            "white": 7,
            "normal": 9
            }

    STYLES = {
            "reset" : 0,
            "bold" : 1,
            "dim" : 2,
            "italic" : 3, #not usually supported
            "underline" : 4,
            "blink" : 5,
            "rapid" : 6, #rapid blink. not usually supported
            "inverse" : 7,
            "hide" : 8, #not usually supported
            "strike" : 9, #not usually supported
            }

    def __init__(self, text=""):
        """Collect Text"""
        self.text = text

    def _wrap(self, attr="", num=0):
        """Wrap with ANSI codes"""
        self.text = f"\033[{attr}{num}m{self.text}\033[0m"
        return self

    # Basic
    def _color(self, color=""):
        """Wrap with color"""
        return self._wrap(3, self.COLORS.get(color, 0))

    def _bg(self, color=""):
        """Wrap with background color"""
        return self._wrap(4, self.COLORS.get(color, 0))

    def _style(self, style=""):
        """Wrap with style"""
        return self._wrap("", self.STYLES.get(style, 0))

    # Alignment
    #NOTE Not ANSI, but helpful.
    def left(self, amt=25):
        """Left align"""
        self.text = f"{self.text:<{amt}}"
        return self

    def right(self, amt=25):
        """Left align"""
        self.text = f"{self.text:>{amt}}"
        return self

    def center(self, amt=25):
        """Left align"""
        self.text = f"{self.text:^{amt}}"
        return self

    #Shortcut Colors
    def black(self):
        """Color Black"""
        return self._color("black")

    def red(self):
        """Color Red"""
        return self._color("red")

    def green(self):
        """Color Green"""
        return self._color("green")

    def yellow(self):
        """Color Yellow"""
        return self._color("yellow")

    def blue(self):
        """Color Blue"""
        return self._color("blue")

    def magenta(self):
        """Color Magenta"""
        return self._color("magenta")

    def cyan(self):
        """Color Cyan"""
        return self._color("cyan")

    def white(self):
        """Color White"""
        return self._color("white")

    #Shortcut Background
    def bgblack(self):
        """Background Black"""
        return self._bg("black")

    def bgred(self):
        """Background Red"""
        return self._bg("red")

    def bggreen(self):
        """Background Green"""
        return self._bg("green")

    def bgyellow(self):
        """Background Yellow"""
        return self._bg("yellow")

    def bgblue(self):
        """Background Blue"""
        return self._bg("blue")

    def bgmagenta(self):
        """Background Magenta"""
        return self._bg("magenta")

    def bgcyan(self):
        """Background Cyan"""
        return self._bg("cyan")

    def bgwhite(self):
        """Background White"""
        return self._bg("white")

    # Shortcut Styles
    def bold(self):
        """Style Bold"""
        return self._style("bold")

    def dim(self):
        """Style Dim"""
        return self._style("dim")

    def blink(self):
        """Style blink"""
        return self._style("blink")

    def italic(self):
        """Style Italic"""
        return self._style("italic")

    def underline(self):
        """Style Underline"""
        return self._style("underline")

    def inverse(self):
        """Style Inverse"""
        return self._style("inverse")

    # Output
    def __add__(self, obj):
        """Concat Text or Color Objs"""
        if isinstance(obj, Color):
            self.text = self.text + " " + obj.text
        elif isinstance(obj, str):
            self.text = self.text + " " + obj
        return self

    def __repr__(self):
        """Return Text"""
        return self.text

if __name__ == "__main__":
    pass
