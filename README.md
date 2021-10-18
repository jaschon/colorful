# colorize
__A simple python class to color, align and style terminal text.__



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
c.bold().green().bgmagenta().left(center) #green text, magenta background and align center (between 50 characters)
print(c) #output
```

### Chain Example 2

```
print(Color("This is some text").bold().yellow()) # Create, chain and output in one line.
```

---

### Add Example 1

```
obj1 = Color("This is some text").yellow().inverse()
obj2 = Color("This is some more text").magenta().blink()
print(obj1+obj2)
```

### Add Example 2

```
obj = Color("This is some text").yellow().inverse()
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
- normal()

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
- inverse()
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





