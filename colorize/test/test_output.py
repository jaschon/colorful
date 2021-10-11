#!/usr/bin/env python3
"""Test Color Output"""

import sys
sys.path.append("..")
from colorize import Color

def colors():
    """Test Color Output"""
    print(Color("1. None (black)"))
    print(Color("2. Black Text").black())
    print(Color("3. Red Text").red())
    print(Color("4. Green Text").green())
    print(Color("5. Blue Text").blue())
    print(Color("6. Yellow Text").yellow())
    print(Color("7. Magenta Text").magenta())
    print(Color("8. Cyan Text").cyan())
    print(Color("9. White Text").white())

def styles():
    """Test Style Output"""
    print(Color("10. Bold Style").bold())
    print(Color("11. Dim Style").dim())
    print(Color("12. Underline Style").underline())
    print(Color("13. Blink Style").blink())
    print(Color("14. Inverse Style").inverse())

def backgrounds():
    """Test Background Output"""
    print(Color("15. Black BG").bgblack())
    print(Color("16.Red BG").bgred())
    print(Color("17. Green BG").bggreen())
    print(Color("18. Blue BG").bgblue())
    print(Color("19. Yellow BG").bgyellow())
    print(Color("20. Magenta BG").bgmagenta())
    print(Color("21. Cyan BG").bgcyan())
    print(Color("22. White BG").bgwhite())

def align():
    """Test Alignment"""
    print(Color("23. Left Align").bold().left(50))
    print(Color("24. Right Align").red().bold().right(50))
    print(Color("25. Center Align").green().dim().center(50))

def chain():
    """Test Method Chaining"""
    print(Color("26. bold, cyan, bg black, blink").center(50).cyan().bold().bgblack().blink())
    print(Color("27. dim black yellow bg, underline").bgyellow().black().dim().underline())

def add():
    """Test Method Adding"""
    obj1 = Color("28. First Object Added To").bold().cyan().bgmagenta()
    obj2 = Color("Second Object").dim().green()
    obj3 = "Third String"
    print(obj1+obj2+obj3)


    obj = Color("This is an object").blue()
    string = "More Stuff"
    combo = obj + string
    print(combo)

if __name__ == "__main__":
    print()
    colors()
    styles()
    backgrounds()
    align()
    chain()
    add()
    print()
