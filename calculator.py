"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

import arithmetic

operations = {
    "+": arithmetic.add,
    "-": arithmetic.subtract,
    "*": arithmetic.multiply,
    "/": arithmetic.divide,
    "square": arithmetic.square,
    "cube": arithmetic.cube,
    "pow": arithmetic.power,
    "mod": arithmetic.mod,
    "%": arithmetic.mod,
    "x+": arithmetic.add_mult,
    "cubes+": arithmetic.add_cubes
    }

quit_list = ["q", "quit"]


def calculate(math_string):
    """ Takes a single string and performs the math function specified at the 
    beginning on all following numbers. Returns a string with calculation or 
    user error info.
    """

    tokens = math_string.split()
    operator = tokens[0]
    if operator not in operations:
        return "INVALID INPUT!!!"
    try:
        for idx in range(1, len(tokens)):
            tokens[idx] = float(tokens[idx])
    except ValueError:
        return "USE NUMBERS!!!"
    else:
        nums = tokens[1:]
        return "{:.2f}".format(operations[operator](nums))


while True:

    print("Please choose an option, or type q to quit.")
    print()
    print("1. User input prefix calculator")
    print("2. Prefix calculate from text")

    user_input = input("> ").lower()

    if user_input in quit_list:
        break
    elif user_input == "1":
        print("You have chosen the user calculator")
        while True:
            math_string = input("> ").lower()
            if math_string in quit_list:
                break
            print(calculate(math_string))
    elif user_input == "2":
        file = open("math-to-do.txt")
        for line in file:
            line = line.rstrip()
            print(calculate(line))

        file.close()
    else:
        print("That was not a valid option")
