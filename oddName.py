"""Sean"""

name = str(input("What is your name? "))
while len(name) < 1:
    name = str(input("What is your name? "))
else:
    print(name[1:len(name):2])
