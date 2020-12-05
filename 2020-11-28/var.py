###变量
x = 10 #x is of type int
x = "Bill" # x is now of type str
x = 'Bill'
# is the same as
x = "Bill"
print(x)

x, y, z = "Orange", "Bannana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print("Phone is " + x)

x = "Python is "
y = "awesome"
z = x + y
print(z)

x = 5
y = 10
print(x + y)

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

x = "awesome"

def  myfunc():
    x = "fantastic"
    print("Phthon is " + x)

myfunc()

print("Phthon is " + x)

def myfunc():
    global x
    x = "fantastic"
myfunc()

print("Phthon is " + x)
