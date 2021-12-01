"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
# Replace this with your code

while True:
    input_string = input("> ")
    tokens = input_string.split(' ')
    if tokens[0] == "q":
        print("Thanks, see ya later!")
        break
    else:
        if tokens[0] == "+":
            answer = add(float(tokens[1]), float(tokens[2]))
            print(answer)
        if tokens[0] == "-":
            answer = subtract(float(tokens[1]), float(tokens[2]))
            print(answer)
        if tokens[0] == "*":
            answer = multiply(float(tokens[1]), float(tokens[2]))
            print(answer)
        if tokens[0] == "/":
            answer = divide(float(tokens[1]), float(tokens[2]))
            print(answer)
        if tokens[0] == "square":
            answer = square(float(tokens[1]))
            print(answer)
        if tokens[0] == "cube":
            answer = cube(float(tokens[1]))
            print(answer)
        if tokens[0] == "pow":
            answer = power(float(tokens[1]), float(tokens[2]))
            print(answer)
        if tokens[0] == "mod":
            answer = mod(float(tokens[1]), float(tokens[2]))
            print(answer)
