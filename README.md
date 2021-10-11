# colorize
* Simple python class to color, align and style terminal text. *

### FG Colors

- black()
- red()
- green()
- yellow()
- blue()
- magenta()
- cyan()
- white()

### Styles

- bold()
- dim()
- blink()
- inverse()

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


## Notes

- Use `print()` to output.
- Can chain multiple methods together.
- Can add objects and strings together.

---

## Simple Example

```
c = Color("This is some text")
c.bold() #set bold style
c.green() #set green text
print(c) #output
```

---

### Chain Example 1

```
c = Color("This is a chain example")
c.bold().green().bgmagenta().left(center) #green text, magenta background and align center (between 50 characters)
print(c) #output
```

## Chain Example 2

```
print(Color("This is some text").bold().yellow()) # Create, chain and output in one line.
```

---

## Object Adding Example 1

```
obj1 = Color("This is some text").yellow().inverse()
obj2 = Color("This is some more text").magenta().blink()
print(obj1+obj2)
```

## Object Adding Example 2

```
obj = Color("This is some text").yellow().inverse()
string = "This is some more text"
print(obj+string)
```





