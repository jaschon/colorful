# colorful
__Color terminal text with ANSI Styles and Colors.__

## Install

```
python setup.py install
python setup.py test
```

## Import

```
from colorful import Color
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

---

### Chain Example 1

```
c = Color("This is a chain example")
c.bold().green().on_magenta() #green text, magenta background
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

- bright\_black()
- bright\_red()
- bright\_green()
- bright\_yellow()
- bright\_blue()
- bright\_magenta()
- bright\_cyan()
- bright\_white()

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

- on\_black()
- on\_red()
- on\_green()
- on\_yellow()
- on\_blue()
- on\_magenta()
- on\_cyan()
- on\_white()
