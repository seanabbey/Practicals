lower = int(input("What is the lower? "))
upper = int(input("What is the upper? "))

while lower < 33 or upper > 127:
    lower = int(input("What is the lower? Must be 33 or above. "))
    upper = int(input("What is the upper? Must be 127 or lower. "))
for i in range(lower, upper + 1):
    print("{} {}".format(i, chr(i)))