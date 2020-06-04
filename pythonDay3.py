#more python today :)
#mostly string practice

a = 'Python is neat'
b = 'and so are you :)'
g = 21
txt = 'I am {} years old'
newLine = 'I heard you can place a new line with a \ and an n \n hopefully its true.'

print(a[0])
print(a[1:6])
print(len(a))
print(a.lower())
print(a.upper())
# should return p, ython, length of original string, and lower/upper case versions.
x = 'neat' in a
print(x)
#should return t/f if neat is in the string
c = a + " " + b
print(c)
#format can allow a number to be placed in a string like so
print(txt.format(g))
print(newLine)
