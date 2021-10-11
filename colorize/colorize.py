#!/usr/bin/env python3
"""Color terminal text with ANSI Styles and Colors"""

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
            "rapid" : 6, #not usually supported
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
    def color(self, color=""):
        """Wrap with color"""
        return self._wrap(3, self.COLORS.get(color, ""))

    def bright(self, color=""):
        """Wrap with bright color"""
        return self._wrap(9, self.COLORS.get(color, ""))

    def background(self, color=""):
        """Wrap with background color"""
        return self._wrap(4, self.COLORS.get(color, ""))

    def bgbright(self, color=""):
        """Wrap with bright background color"""
        return self._wrap(10, self.COLORS.get(color, ""))

    def style(self, style=""):
        """Wrap with style"""
        return self._wrap("", self.STYLES.get(style, ""))

    # Alignment
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
        return self.color("black")

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

    #Shortcut Background
    def bgblack(self):
        """Background Black"""
        return self.background("black")

    def bgred(self):
        """Background Red"""
        return self.background("red")

    def bggreen(self):
        """Background Green"""
        return self.background("green")

    def bgyellow(self):
        """Background Yellow"""
        return self.background("yellow")

    def bgblue(self):
        """Background Blue"""
        return self.background("blue")

    def bgmagenta(self):
        """Background Magenta"""
        return self.background("magenta")

    def bgcyan(self):
        """Background Cyan"""
        return self.background("cyan")

    def bgwhite(self):
        """Background White"""
        return self.background("white")

    # Shortcut Styles
    def bold(self):
        """Style Bold"""
        return self.style("bold")

    def dim(self):
        """Style Dim"""
        return self.style("dim")

    def blink(self):
        """Style blink"""
        return self.style("blink")

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

    # Output
    def get(self, *args, **kwargs):
        """Print Text"""
        print(self.text, *args, **kwargs)

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
