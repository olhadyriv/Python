num_1: int = int(input("Enter the 1st number: "))

while num_1 == 10 or num_1 == 20:
    num_1: int = int(input("Enter the 1st number: "))
if num_1 < 5 or num_1 > 1000:
    print("Incorrect value.")
elif num_1 == 666:
    print("You are on the highway to hell")
else:
    num_2: int = int(input("Enter the 2nd number: "))

    while num_2 == 10 or num_2 == 20:
        num_2: int = int(input("Enter the 2nd number: "))
    if num_2 < 5 or num_2 > 1000:
        print("Incorrect value.")
    elif num_2 == 666:
        print("You are on the highway to hell")

    symbol = input("Enter the character +, -, *, /: ")

    if symbol == "+":
        print(f"Result is {num_1 + num_2}")
    elif symbol == "-":
        print(f"char is {num_1 - num_2}")
    elif symbol == "*":
        print(f"Result is {num_1 * num_2}")
    elif symbol == "/" or num_2 != 0:
        print(f"Result is {num_1 / num_2}")
    while num_1 + num_2 or num_1 - num_2 or num_1 * num_2 or num_1 / num_2 == 666:
        print("The end")
        break
