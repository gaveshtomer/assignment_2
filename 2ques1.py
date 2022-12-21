a = "Python is a case sensitive language."
# QUESTION 1 --- Part (a)
b = len(a)
print(b)

# QUESTION 1 --- Part(b)
x = a[::-1]
print(x)

# QUESTION 1 --- Part(c)
y = a[10:26]
print(y)

# QUESTION 1 --- Part(d)
print(a.find("a"))

# QUESTION 2 --- Part(e)
s = a.split()
for i in s :
    print(i,end= '')
