# colorize
__Color terminal text with ANSI Styles and Colors.__

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
print(Color("This is some text").color8(32)) # Create and output in one line.
```

---

### Chain Example 1

```
c = Color("This is a chain example")
c.bold().green().bgmagenta().center(50) #green text, magenta background and align center (between 50 characters)
print(c) #output
```

### Chain Example 2

```
print(Color("This is some text").bold().yellow()) # Create, chain and output in one line.
```

---

### Add Example 1

```
obj1 = Color("This is some text").yellow().invert)
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

### Alignment

- left(_NUM_)
- center(_NUM_)
- right(_NUM_)

### 8-Bit Colors

- color8(_0-255_)
- bg8(_0-255_)

