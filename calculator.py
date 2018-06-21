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
        print("{:.2f}".format(operations[operator](nums)))
