# choosing operation
a = input("Please choose operations available: addition, subtraction, multiplication or division: " )

# choosing numbers
x = input("Choose the first number: " )
y = input("Choose the second number: " )

# addition
if a == "addition":
    try:
        x = int(x)
        y = int(y)
        print(x, "+", y, " is", x + y)
    except:
        print("You have inputted strings instead of integers, please restart this program.")

# subtraction
if a == "subtraction":
    try:
        x = int(x)
        y = int(y)
        print(x, "-", y, " is", x - y)
    except:
        print("You have inputted strings instead of integers, please restart this program.")


# multiplication
if a == "multiplication":
    try:
        x = int(x)
        y = int(y)
        print(x, "*", y, " is", x * y)
    except:
        print("You have inputted strings instead of integers, please restart this program.")


# division
if a == "division":
    try:
        x = int(x)
        y = int(y)
        print(x, "/", y, " is", x / y)
    except:
        print("You have inputted strings instead of integers, please restart this program.")

k = input("Press ENTER to close the program. MADE BY IMSERIOUSS")