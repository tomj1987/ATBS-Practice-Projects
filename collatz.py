def collatz(number):
    while number != 1:
        print(number)
        if number % 2 == 0:
            number = int(number // 2)
        else:
            number = int(3 * number + 1)
    else:
        print(number)
        print("Done")
try:
    res = int(input("Please enter a number:"))
    collatz(res)
except ValueError:
    print("Please enter an integer.")
