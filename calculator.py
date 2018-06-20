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


# Your code goes here
while True:

    user_input = input("> ").lower()

    if user_input == "q" or user_input == "quit":
        break

    tokens = user_input.split()
    operator = tokens[0]
    if operator not in operations:
        print("BAD USER!!!")
        continue
    try:
        for idx in range(1, len(tokens)):
            tokens[idx] = float(tokens[idx])
    except ValueError:
        print("USE NUMBERS!!!")
    else:
        nums = tokens[1:]
        print(operations[operator](nums))

    # print arithmetic.operations[operator]

    # if operator == "+":

    #     print(arithmetic.add(tokens[1], tokens[2]))

    # elif operator == "-":

    #     print(arithmetic.subtract(tokens[1], tokens[2]))

    # elif operator == "*":

    #     print(arithmetic.multiply(tokens[1], tokens[2]))

    # elif operator == "/":

    #     print(arithmetic.divide(tokens[1], tokens[2]))

    # elif operator == "square":

    #     print(arithmetic.square(tokens[1]))

    # elif operator == "cube":

    #     print(arithmetic.cube(tokens[1]))

    # elif operator == "pow":

    #     print(arithmetic.power(tokens[1], tokens[2]))

    # elif operator == "mod":

    #     print(arithmetic.mod(tokens[1], tokens[2]))

    # elif operator == "x+":

    #     print(arithmetic.add_mult(tokens[1], tokens[2], tokens[3]))

    # elif operator == "cubes+":

    #     print(arithmetic.add_cubes(tokens[1], tokens[2]))

    # else:

    #     print("please enter valid command")
