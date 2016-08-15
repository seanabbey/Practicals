def main():
    lower = 33
    upper = 127

    get_number(lower, upper)


def get_number(lower, upper):
    uinput = int(input("Enter a number 33-127 "))
    while uinput < lower or uinput > upper:
        print("Please enter a valid Number ")
        uinput = int(input("Enter a number 33-127 "))
    print("{} {}".format(uinput, chr(uinput)))


main()
