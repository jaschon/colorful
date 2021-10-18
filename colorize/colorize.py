#!/usr/bin/env python3
"""Color terminal text with ANSI Styles and Colors"""

# NOTE:
# reset = \33[0m
# color = \33[ + 3 + COLOR NUMBER + m
# bright = \33[ + 9 + COLOR NUMBER + m
# style = \33[ + STYLE NUMBER + m
# bg = \33[ + 4 + COLOR NUMBER + m

__author__ = "Jason Rebuck"
__copyright__ = "2021"
__version__ = "0.18"

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
            }

    STYLES = {
            "reset" : 0,
            "bold" : 1,
            "dim" : 2,
            "italic" : 3,
            "underline" : 4,
            "blink" : 5,
            #"rapid" : 6, #rapid blink. not usually supported
            "invert" : 7,
            "hide" : 8, #hides output
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

    def _bright(self, color=""):
        """Wrap with bright color"""
        return self._wrap(9, self.COLORS.get(color, 0))

    def _bg(self, color=""):
        """Wrap with background color"""
        return self._wrap(4, self.COLORS.get(color, 0))

    def _style(self, style=""):
        """Wrap with style"""
        return self._wrap("", self.STYLES.get(style, 0))

    # 8-bit colors
    def color8(self, color=0):
        """Wrap with 8-bit color (0-255)"""
        #0-255
        return self._wrap("38;5;", color)

    def bg8(self, color=0):
        """Wrap with 8-bit bg color (0-255)"""
        #0-255
        return self._wrap("48;5;", color)

    # 24-bit colors
    def color24(self, r=0, g=0, b=0):
        """Wrap with 24-bit color (r,g,b)"""
        return self._wrap("38;2;", f"{r};{g};{b}")

    def bg24(self, color=0):
        """Wrap with 24-bit bg color (r,g,b)"""
        return self._wrap("48;2;", f"{r};{g};{b}")

    # Alignment
    # NOTE Not ANSI, but helpful.
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

    # Shortcut Colors
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

    # Shortcut Bright Colors
    def brblack(self):
        """Color Bright Black"""
        return self._bright("black")

    def brred(self):
        """Color Bright Red"""
        return self._bright("red")

    def brgreen(self):
        """Color Bright Green"""
        return self._bright("green")

    def bryellow(self):
        """Color Bright Yellow"""
        return self._bright("yellow")

    def brblue(self):
        """Color Bright Blue"""
        return self._bright("blue")

    def brmagenta(self):
        """Color Bright Magenta"""
        return self._bright("magenta")

    def brcyan(self):
        """Color Bright Cyan"""
        return self._bright("cyan")

    def brwhite(self):
        """Color Bright White"""
        return self._bright("white")

    # Shortcut Background
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
    def reset(self):
        """Style Reset"""
        return self._style("reset")

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

    def invert(self):
        """Style Inverse"""
        return self._style("invert")

    def hide(self):
        """Style Hidden"""
        return self._style("hide")

    def strike(self):
        """Style Strike"""
        #NOT USUALLY SUPPORTED!
        return self._style("strike")

    # Output
    def __add__(self, obj):
        """Concat Text or Color Objs"""
        self.text = f"{self.text} {obj}"
        return self

    def __repr__(self):
        """Return Text"""
        return self.text

if __name__ == "__main__":
    pass
