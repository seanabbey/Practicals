def main():
    MIN = 1
    MAX = 45
    AMOUNT = 6
    quickpicks = int(input("How many quick picks do you wish to generate? "))
    numbers = []
    import random
    for i in range(quickpicks):
        for i in range(AMOUNT):
            num = random.randint(MIN, MAX)
            while num in numbers:
                num = random.randint(MIN, MAX)
            numbers.append(num)
        numbers.sort()
        print(numbers)
        numbers = []
main()