#!/usr/bin/env python3

__author__ = "Jason Rebuck"
__copyright__ = "2021"
__version__ = "0.10"

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
            "gray": 8,
            "normal": 9
            }

    STYLE = {
            "reset" : 0,
            "bold" : 1,
            "dim" : 2,
            "italic" : 3,
            "underline" : 4,
            "blink" : 5,
            "slow" : 5,
            "rapid" : 6,
            "inverse" : 7,
            "hide" : 8,
            "strike" : 9,
            }

    def __init__(self, text=""):
        """Collect Text"""
        self.text = text

    def _wrap(self, attr="", num=0):
        """Wrap with ANSI codes"""
        self.text = f"\033[{attr}{num}m{self.text}\033[0m"
        return self

    # Basic
    def color(self, color=""):
        """Wrap with color"""
        return self._wrap(attr=3, num=self.COLORS.get(color, "black"))

    def background(self, color=""):
        """Wrap with background color"""
        return self._wrap(attr=4, num=self.COLORS.get(color, "white"))

    def style(self, style=""):
        """Wrap with background color"""
        return self._wrap(attr="", num=self.STYLE.get(style, "reset"))

    # Alignment
    def left(self, amt=10):
        """Left align"""
        self.text = f"{self.text:<{amt}}"
        return self

    def right(self, amt=10):
        """Left align"""
        self.text = f"{self.text:>{amt}}"
        return self

    def center(self, amt=10):
        """Left align"""
        self.text = f"{self.text:^{amt}}"
        return self

    #Shortcut Colors
    def red(self):
        """Color Red"""
        return self.color("red")

    def green(self):
        """Color Green"""
        return self.color("green")

    def yellow(self):
        """Color Yellow"""
        return self.color("yellow")

    def blue(self):
        """Color Blue"""
        return self.color("blue")

    def magenta(self):
        """Color Magenta"""
        return self.color("magenta")

    def cyan(self):
        """Color Cyan"""
        return self.color("cyan")

    def white(self):
        """Color White"""
        return self.color("white")

    # Shortcut Styles
    def bold(self):
        """Style Bold"""
        return self.style("bold")

    def dim(self):
        """Style Dim"""
        return self.style("dim")

    def italic(self):
        """Style Italic"""
        return self.style("italic")

    def underline(self):
        """Style Underline"""
        return self.style("underline")

    def inverse(self):
        """Style Inverse"""
        return self.style("inverse")

    def strike(self):
        """Style Strike"""
        return self.style("strike")

    def __repr__(self):
        """Return Text"""
        return self.text

if __name__ == "__main__":
    pass




