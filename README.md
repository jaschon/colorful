# colorize
__Color terminal text with ANSI Styles and Colors.__

## Install

```
python setup.py install
python setup.py test
```

## Import

```
from colorize import Color
...
```


### Simple Example 1

```
c = Color("This is some text")
c.bold() #set bold style
c.green() #set green text
print(c) #output
```

### Simple Example 2

```
print(Color("This is some text").green()) # Create and output in one line.
```

### Simple Example 3 (8-bit Color)

```
print(Color("This is some text").color8(32)) # Create and output 8-bit color in one line.
```

---

### Chain Example 1

```
c = Color("This is a chain example")
c.bold().green().bgmagenta() #green text, magenta background
print(c) #output
```

### Chain Example 2

```
print(Color("This is some text").bold().yellow()) # Create, chain and output in one line.
```

---

### Add Example 1

```
obj1 = Color("This is some text").yellow().invert()
obj2 = Color("This is some more text").magenta().blink()
print(obj1+obj2)
```

### Add Example 2

```
obj = Color("This is some text").yellow().invert()
string = "This is some more text"
combo = obj + string
print(combo)
```

---

### FG Colors

- black()
- red()
- green()
- yellow()
- blue()
- magenta()
- cyan()
- white()

### Bright FG Colors

- brblack()
- brred()
- brgreen()
- bryellow()
- brblue()
- brmagenta()
- brcyan()
- brwhite()

### Styles

- reset()
- bold()
- dim()
- blink()
- italic()
- underline()
- invert()
- hide()
- strike() __--NOT SUPPORTED IN SOME TERMINALS--__

### BG Colors

- bgblack()
- bgred()
- bggreen()
- bgyellow()
- bgblue()
- bgmagenta()
- bgcyan()
- bgwhite()

---

### 8-Bit Colors 

#### (1-7 = Standard, 8-15 = Bright, 16-231 = 216 Palette, 232-255 = Grayscale)

- color8(_0-255_)
- bg8(_0-255_)

---


### 24-Bit Colors 

#### (__NOT SUPPORTED IN SOME TERMINALS__)

- color24(_r_, _g_, _b_)
- bg24(_r_, _g_, _b_)


